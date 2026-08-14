# molgen-llm-bench

Benchmark comparing four LLM setups — Claude-Opus5, Claude Science (Opus5),
Gemini-3.1Pro, and ChatGPT-GPT5.6Sol — on generating novel lanthanide/actinide
extractant molecules (SMILES) for Am(III)/Eu(III) solvent extraction, scored
against a shared cheminformatics rubric.

The prompt (`prompts/v1/`) is adapted from Zhang et al., "Augmenting Large
Language Models for Automated Discovery of F-Element Extractants," *JACS*
148(5), 5520–5532 (2026).

## Layout

```
molgen-llm-bench/
├── prompts/
│   └── v1/
│       ├── system.md          # system prompt sent to each model
│       ├── user.md            # user prompt sent to each model
│       └── design.txt         # design_focus text for design1..4
├── runs/
│   └── {tool}/v1/design{N}/run{K}/
│       └── raw_smiles.py      # SMILES (+ names, for claudescience) extracted from that run's response
├── eval/
│   ├── score_candidates.py    # shared scoring script (regenerates run1 only, see below)
│   ├── data_list.txt          # experimental reference SMILES (design3, design4)
│   ├── data_list_all.json     # experimental reference SMILES (design1, design2)
│   ├── data_list_candidates.png
│   └── data_list_all_candidates.png
└── results/
    ├── candidate_scores_v1.xlsx     # run1-only combined workbook: `combined` + one sheet per design
    ├── {tool}/v1/design{N}/run{K}/
    │   ├── candidates.csv           # scored candidates for that model/design/run
    │   └── images/grid.png          # 2D structure grid for that model/design/run
    └── analysis/
        ├── all_candidates_long.csv      # all 800 scored molecules (4 design × 4 model × 5 run × 10)
        ├── run_means.csv                 # 80 rows: mean of the 10 molecules per (design, model, run)
        └── design_model_stats.csv        # 16 rows: mean/sd(ddof=1)/sem of the 5 run-means per (design, model)
```

- `prompt_id` (currently `v1`) ties a prompt version to the runs/results it produced. `v1` is the
  paper-reproduction experiment — Design 1-4 × 4 models × 5 runs (`run1`..`run5`). New prompts not
  from the paper start at `v2`.
- `tool` is one of `claude`, `gemini`, `chatgpt`, `claudescience`.
- `design{N}` (`design1`..`design4`) is one of four design-focus variants run under the
  same `v1` prompt (see [Designs](#designs)). `design4` is the original/baseline design.
- `run{K}` (`run1`..`run5`) is one of five repeated generations under the same design/tool/prompt.
  `run1` was scored first and lives in `candidate_scores_v1.xlsx`; `run2`-`run5` were parsed from
  raw model output (originally `runs/raw/`, deleted after parsing — SMILES/names are fully preserved
  in `runs/{tool}/v1/design{N}/run{K}/raw_smiles.py`, but per-candidate metrics Claude Science computed
  itself in its own run2-5 CSVs, e.g. its own logP/similarity numbers, were not kept — see
  `results/{tool}/v1/design{N}/run{K}/candidates.csv` for our own scoring instead).

## Models

| tool | model | naming |
|---|---|---|
| Claude | Opus5 | `claude_d{N}_r{K}_01..10` (no curated names) |
| Gemini | 3.1Pro (extended) | `gemini_d{N}_r{K}_01..10` |
| ChatGPT | GPT5.6Sol | `chatgpt_d{N}_r{K}_01..10` |
| Claude Science | Opus5 — chemistry-research-focused session | descriptive (`CyMe4-BTPhen`, ...) for run2-5, since its raw output includes names; `claudescience_d{N}_01..10` for run1 (no names in the original run1 source) |

(`run1` names for claude/gemini/chatgpt use the shorter `{tool}_d{N}_01..10` form, no `_r1`, kept
from before the run-folder restructure.)

## Designs

Four design-focus variants, same `v1` system/user prompt, defined in `prompts/v1/design.txt`:

| design | focus |
|---|---|
| design1 | binding ligands with 4 to 8 nitrogen atoms |
| design2 | tri-/tetra-dentate binding ligands with a mix of nitrogen and oxygen donor groups |
| design3 | tri-/tetra-dentate binding ligands with a mix of nitrogen and oxygen donor groups |
| design4 | binding ligands structurally similar to bis-triazinyl bipyridines (BTBPs) — original/baseline design |

## Reference data

Similarity/dup scoring (`max_sim_exp`, `min_sim_exp`, `dup_of_exp`) is computed against
a different experimental reference set per design:

- **design1, design2** — `eval/data_list_all.json` (full experimental candidate pool,
  rendered in `eval/data_list_all_candidates.png`)
- **design3, design4** — `eval/data_list.txt` (the 9 experimental, Source=Experimental
  BTBP/BTPhen extractants from the prompt's evaluation table, rendered in
  `eval/data_list_candidates.png`)

## Running the scorer

```
eval/score_candidates.py
```

for each design (1-4) and each tool, reads `runs/{tool}/v1/design{N}/run1/raw_smiles.py`,
scores every SMILES against that design's reference set, and writes
`results/{tool}/v1/design{N}/run1/candidates.csv` + `run1/images/grid.png`. Requires
`rdkit` (with the `SA_Score` contrib module) and `pandas`. It only (re)generates `run1` —
`run2`-`run5` were one-off parses of `runs/raw/` (ast-literal SMILES lists for
claude/gemini/chatgpt, CSVs with varying columns for claudescience) scored the same way via
`score_candidates.score_list`/`make_grid_png`, not re-run by this script.

To add a new prompt version: create `prompts/v2/`, add `runs/{tool}/v2/design{N}/run1/raw_smiles.py`
per tool/design, and change `PROMPT_ID` in `eval/score_candidates.py`.

`results/candidate_scores_v1.xlsx` combines all `run1` candidate CSVs into one
workbook: a `combined` sheet (all designs × all tools) plus one `design{N}` sheet per
design (all tools for that design). It does **not** include run2-5 — for the full 5-run
picture use `results/analysis/` (see [Layout](#layout)).

## Score columns

canonical SMILES, formula, MW, MolLogP, TPSA, HBD, aromatic-N count,
rotatable bonds, synthetic accessibility (`SA_score`), Tanimoto similarity to the
experimental reference set (max/min), whether it duplicates an experimental compound,
max internal similarity within the same model/design batch, count of triazine and
pyridine aromatic 6-rings (`n_triazine_rings`, `n_pyridine_rings`), and pass/fail flags
for the two design criteria used in the prompt (`0.25 <= sim_exp <= 0.85`, `logP > 3`).
