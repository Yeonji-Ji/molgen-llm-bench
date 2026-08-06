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
│   └── {tool}/v1/design{N}/
│       └── raw_smiles.py      # SMILES extracted from that model's response
├── eval/
│   ├── score_candidates.py    # shared scoring script
│   ├── data_list.txt          # experimental reference SMILES (design3, design4)
│   ├── data_list_all.json     # experimental reference SMILES (design1, design2)
│   ├── data_list_candidates.png
│   └── data_list_all_candidates.png
└── results/
    ├── candidate_scores_v1.xlsx   # combined workbook: `combined` + one sheet per design
    └── {tool}/v1/design{N}/
        ├── candidate_scores.csv   # scored candidates for that model/design
        └── candidates.png
```

- `prompt_id` (currently `v1`) ties a prompt version to the runs/results it produced.
- `tool` is one of `claude`, `gemini`, `chatgpt`, `claudescience`.
- `design{N}` (`design1`..`design4`) is one of four design-focus variants run under the
  same `v1` prompt (see [Designs](#designs)). `design4` is the original/baseline design.

## Models

| tool | model | naming |
|---|---|---|
| Claude | Opus5 | `claude_01..10` (`claude_d{N}_01..10` for design1-3, no curated names) |
| Gemini | 3.1Pro (extended) | `gemini_01..10` (`gemini_d{N}_01..10` for design1-3) |
| ChatGPT | GPT5.6Sol | `chatgpt_01..10` (`chatgpt_d{N}_01..10` for design1-3) |
| Claude Science | Opus5 — chemistry-research-focused session | descriptive (`CyMe4-BTPhen`, ...) for design4 only; `claudescience_d{N}_01..10` for design1-3 |

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

for each design (1-4) and each tool, reads `runs/{tool}/v1/design{N}/raw_smiles.py`,
scores every SMILES against that design's reference set, and writes
`results/{tool}/v1/design{N}/candidate_scores.csv` + `candidates.png`. Requires
`rdkit` (with the `SA_Score` contrib module) and `pandas`.

To add a new prompt version: create `prompts/v2/`, add `runs/{tool}/v2/design{N}/raw_smiles.py`
per tool/design, and change `PROMPT_ID` in `eval/score_candidates.py`.

`results/candidate_scores_v1.xlsx` combines all `candidate_scores.csv` files into one
workbook: a `combined` sheet (all designs × all tools) plus one `design{N}` sheet per
design (all tools for that design).

## Score columns

canonical SMILES, formula, MW, MolLogP, TPSA, HBD, aromatic-N count,
rotatable bonds, synthetic accessibility (`SA_score`), Tanimoto similarity to the
experimental reference set (max/min), whether it duplicates an experimental compound,
max internal similarity within the same model/design batch, count of triazine and
pyridine aromatic 6-rings (`n_triazine_rings`, `n_pyridine_rings`), and pass/fail flags
for the two design criteria used in the prompt (`0.25 <= sim_exp <= 0.85`, `logP > 3`).
