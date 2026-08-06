"""Score SMILES lists from runs/{tool}/v1/design{N}/raw_smiles.py into the
candidate_scores.csv column format, and render a 2D grid PNG per tool/design.

Reference list for max/min_similarity_exp differs by design:
  design1, design2 -> eval/data_list_all.json
  design3, design4 -> eval/data_list.txt
"""
import json
import runpy

import pandas as pd
from rdkit import Chem, RDLogger
from rdkit.Chem import AllChem, Descriptors, Draw, rdMolDescriptors
from rdkit import DataStructs
from rdkit.Chem import RDConfig
import sys, os
sys.path.append(os.path.join(RDConfig.RDContribDir, "SA_Score"))
import sascorer

RDLogger.DisableLog("rdApp.*")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FP_RADIUS, FP_BITS = 2, 2048

PROMPT_ID = "v1"
DESIGNS = [1, 2, 3, 4]
DESIGN_REF = {
    1: "data_list_all.json",
    2: "data_list_all.json",
    3: "data_list.txt",
    4: "data_list.txt",
}
MODEL_VARS = {
    "claude": "SMILES_claude",
    "gemini": "SMILES_gemini",
    "chatgpt": "SMILES_chatGPT",
    "claudescience": "SMILES_claudescience",
}
NAME_VARS = {"claudescience": "NAMES_claudescience"}


def load_exp_reference(filename):
    exp_records = json.load(open(os.path.join(ROOT, "eval", filename)))
    exp_mols = [Chem.MolFromSmiles(r["SMILES"]) for r in exp_records]
    exp_fps = [AllChem.GetMorganFingerprintAsBitVect(m, FP_RADIUS, FP_BITS) for m in exp_mols if m]
    exp_canon = {Chem.MolToSmiles(m) for m in exp_mols if m}
    return exp_fps, exp_canon


REF_CACHE = {fname: load_exp_reference(fname) for fname in set(DESIGN_REF.values())}


def ring_n_counts(mol):
    """(n_pyridine_rings, n_triazine_rings): aromatic 6-rings by N count (1 or 3)."""
    n_pyr = n_tz = 0
    for ring in mol.GetRingInfo().AtomRings():
        if len(ring) != 6:
            continue
        atoms = [mol.GetAtomWithIdx(i) for i in ring]
        if not all(a.GetIsAromatic() for a in atoms):
            continue
        n_count = sum(a.GetAtomicNum() == 7 for a in atoms)
        if n_count == 1:
            n_pyr += 1
        elif n_count == 3:
            n_tz += 1
    return n_pyr, n_tz


def score_one(smiles, fps_so_far, exp_fps, exp_canon):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    canonical = Chem.MolToSmiles(mol)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, FP_RADIUS, FP_BITS)

    sims_exp = DataStructs.BulkTanimotoSimilarity(fp, exp_fps) if exp_fps else [0.0]
    max_sim_exp, min_sim_exp = max(sims_exp), min(sims_exp)
    max_sim_internal = max(
        DataStructs.BulkTanimotoSimilarity(fp, fps_so_far), default=0.0
    )

    logp = Descriptors.MolLogP(mol)
    n_pyridine_rings, n_triazine_rings = ring_n_counts(mol)

    row = {
        "canonical_smiles": canonical,
        "formula": rdMolDescriptors.CalcMolFormula(mol),
        "MW": round(Descriptors.MolWt(mol), 1),
        "MolLogP": round(logp, 2),
        "TPSA": round(Descriptors.TPSA(mol), 1),
        "HBD": Descriptors.NumHDonors(mol),
        "arom_N": sum(a.GetIsAromatic() and a.GetAtomicNum() == 7 for a in mol.GetAtoms()),
        "rot_bonds": Descriptors.NumRotatableBonds(mol),
        "SA_score": round(sascorer.calculateScore(mol), 2),
        "max_sim_exp": round(max_sim_exp, 3),
        "min_sim_exp": round(min_sim_exp, 3),
        "dup_of_exp": canonical in exp_canon,
        "max_sim_internal": round(max_sim_internal, 3),
        "crit_sim_exp_0.25_0.85": 0.25 <= max_sim_exp <= 0.85,
        "crit_logP_gt3": logp > 3,
        "n_triazine_rings": n_triazine_rings,
        "n_pyridine_rings": n_pyridine_rings,
    }
    return row, fp


for design in DESIGNS:
    ref_file = DESIGN_REF[design]
    exp_fps, exp_canon = REF_CACHE[ref_file]

    for model, var in MODEL_VARS.items():
        run_path = os.path.join(ROOT, "runs", model, PROMPT_ID, f"design{design}", "raw_smiles.py")
        if not os.path.exists(run_path):
            continue
        mod = runpy.run_path(run_path)
        smiles_list = mod[var]
        names = mod.get(NAME_VARS.get(model, ""))

        rows, mols_for_png, legends, fps_so_far = [], [], [], []
        for i, smi in enumerate(smiles_list, start=1):
            result = score_one(smi, fps_so_far, exp_fps, exp_canon)
            if result is None:
                print(f"[{model} design{design}] skip invalid SMILES #{i}: {smi}")
                continue
            row, fp = result
            name = names[i - 1] if names else f"{model}_d{design}_{i:02d}"
            rows.append({"name": name, **row})
            fps_so_far.append(fp)

            mol = Chem.MolFromSmiles(row["canonical_smiles"])
            mols_for_png.append(mol)
            legends.append(
                f'{name}\n{row["formula"]}  MW {row["MW"]}  cLogP {row["MolLogP"]}'
            )

        df = pd.DataFrame(rows)
        out_dir = os.path.join(ROOT, "results", model, PROMPT_ID, f"design{design}")
        os.makedirs(out_dir, exist_ok=True)
        csv_path = os.path.join(out_dir, "candidate_scores.csv")
        png_path = os.path.join(out_dir, "candidates.png")
        df.to_csv(csv_path, index=False)

        img = Draw.MolsToGridImage(
            mols_for_png, molsPerRow=3, subImgSize=(400, 400), legends=legends
        )
        img.save(png_path)
        print(f"{model} design{design}: {len(rows)}/{len(smiles_list)} scored -> {csv_path}, {png_path}")
