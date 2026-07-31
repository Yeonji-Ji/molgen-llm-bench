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
│       └── user.md            # user prompt sent to each model
├── runs/
│   └── {tool}/v1/
│       └── raw_smiles.py      # SMILES extracted from that model's response
├── eval/
│   ├── score_candidates.py    # shared scoring script
│   ├── data_list.txt          # experimental reference SMILES
│   └── data_list_candidates.png
└── results/
    ├── candidate_scores_v1.xlsx   # all models combined into one workbook
    └── {tool}/v1/
        ├── candidate_scores.csv   # scored candidates for that model
        └── candidates.png
```

`{tool}` is one of `claude`, `gemini`, `chatgpt`, `claudescience`.

- `prompt_id` (currently `v1`) ties a prompt version to the runs/results it produced.
- `tool` is one of `claude`, `gemini`, `chatgpt`, `claudescience`.

## Models

| tool | model | naming |
|---|---|---|
| Claude | Opus5 | `claude_01..10` |
| Gemini | 3.1Pro (extended) | `gemini_01..10` |
| ChatGPT | GPT5.6Sol | `chatgpt_01..10` |
| Claude Science | Opus5 — chemistry-research-focused session | descriptive (`CyMe4-BTPhen`, ...) |

## Reference data

`eval/data_list.txt` — the 9 experimental (Source=Experimental) BTBP/BTPhen
extractants included in the prompt's evaluation table. `eval/data_list_candidates.png`
renders them. All `max_sim_exp`/`min_sim_exp`/`dup_of_exp` scoring columns are
computed against this set (no separate experimental dataset exists in this repo).

## Running the scorer

```
eval/score_candidates.py
```

reads `runs/{tool}/v1/raw_smiles.py` for each tool, scores every SMILES, and
writes `results/{tool}/v1/candidate_scores.csv` + `candidates.png`. Requires
`rdkit` (with the `SA_Score` contrib module) and `pandas`.

To add a new prompt version: create `prompts/v2/`, add `runs/{tool}/v2/raw_smiles.py`
per tool, and change `PROMPT_ID` in `eval/score_candidates.py`.

## Score columns

canonical SMILES, formula, MW, MolLogP, TPSA, HBD, aromatic-N count,
triazine substructure count, rotatable bonds, synthetic accessibility
(`SA_score`), Tanimoto similarity to the experimental set (max/min),
whether it duplicates an experimental compound, max internal similarity
within the same model's batch, and pass/fail flags for the two design
criteria used in the prompt (`0.25 <= sim_exp <= 0.85`, `logP > 3`).
