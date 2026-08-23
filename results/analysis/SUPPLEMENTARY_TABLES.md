# Supplementary Tables

## Table 1. Study design: molecules generated per cell

|   design |   ChatGPT |   Claude |   Claude Science |   Gemini |
|---------:|----------:|---------:|-----------------:|---------:|
|        1 |        50 |       50 |               50 |       50 |
|        2 |        50 |       50 |               50 |       50 |
|        3 |        50 |       50 |               50 |       50 |
|        4 |        50 |       50 |               50 |       50 |

## Table 2. Variance decomposition (eta-squared) over model x design

| descriptor   |   eta2_model |   eta2_design |   eta2_interaction |   eta2_residual |
|:-------------|-------------:|--------------:|-------------------:|----------------:|
| MW           |        0.169 |         0.099 |              0.038 |           0.695 |
| MolLogP      |        0.182 |         0.031 |              0.05  |           0.736 |
| TPSA         |        0.004 |         0.481 |              0.01  |           0.505 |
| HBD          |        0.016 |         0.05  |              0.057 |           0.877 |
| arom_N       |        0.007 |         0.694 |              0.007 |           0.292 |
| rot_bonds    |        0.11  |         0.232 |              0.046 |           0.612 |
| SA_score     |        0.134 |         0.071 |              0.012 |           0.783 |
| rings        |        0.093 |         0.415 |              0.014 |           0.478 |
| sim_ref295   |        0.093 |         0.074 |              0.042 |           0.792 |

## Table 3. Molecular descriptors by model

|            | Unnamed: 1   |   ChatGPT |   Claude |   Claude Science |   Gemini |
|:-----------|:-------------|----------:|---------:|-----------------:|---------:|
| MW         | mean         |    486.43 |   569.36 |           586.28 |   585.95 |
| MW         | std          |     86.51 |    95.15 |            87.35 |    98.05 |
| MolLogP    | mean         |      6.62 |     8.61 |             8.79 |     9.12 |
| MolLogP    | std          |      1.58 |     2.14 |             1.88 |     2.57 |
| TPSA       | mean         |     79.78 |    80.75 |            82.86 |    83    |
| TPSA       | std          |     22    |    19.64 |            20.72 |    23.11 |
| HBD        | mean         |      0.14 |     0.09 |             0.05 |     0.02 |
| HBD        | std          |      0.48 |     0.36 |             0.3  |     0.25 |
| arom_N     | mean         |      4.86 |     5.24 |             5.5  |     5.1  |
| arom_N     | std          |      2.8  |     2.62 |             2.6  |     2.98 |
| nN         | mean         |      5.6  |     5.98 |             6.21 |     5.87 |
| nN         | std          |      2.07 |     1.84 |             1.87 |     2.08 |
| nO         | mean         |      0.93 |     0.82 |             0.73 |     0.99 |
| nO         | std          |      1.04 |     0.95 |             0.84 |     1.29 |
| rings      | mean         |      2.97 |     3.94 |             4.57 |     3.24 |
| rings      | std          |      1.63 |     1.83 |             2.48 |     1.77 |
| arom_rings | mean         |      2.8  |     3.4  |             3.56 |     2.92 |
| arom_rings | std          |      1.36 |     1.41 |             1.34 |     1.28 |
| rot_bonds  | mean         |     12.84 |    14.76 |            13.2  |    19.41 |
| rot_bonds  | std          |      5.12 |     8.12 |             7.54 |     8.61 |
| SA_score   | mean         |      2.98 |     3.34 |             3.55 |     3.08 |
| SA_score   | std          |      0.46 |     0.6  |             0.62 |     0.58 |

## Table 4. Molecular descriptors by design

|            | Unnamed: 1   |      1 |      2 |      3 |      4 |
|:-----------|:-------------|-------:|-------:|-------:|-------:|
| MW         | mean         | 531.41 | 549.75 | 536.43 | 610.43 |
| MW         | std          |  96.04 | 101.67 |  99.37 |  84.88 |
| MolLogP    | mean         |   7.71 |   8.62 |   8.1  |   8.7  |
| MolLogP    | std          |   2.16 |   2.31 |   2.38 |   2.16 |
| TPSA       | mean         |  87.84 |  65.42 |  70.28 | 102.86 |
| TPSA       | std          |  15.23 |  14.64 |  21.49 |   6.91 |
| HBD        | mean         |   0.22 |   0.02 |   0.06 |   0.02 |
| HBD        | std          |   0.59 |   0.12 |   0.33 |   0.17 |
| arom_N     | mean         |   6.96 |   2.65 |   3.18 |   7.92 |
| arom_N     | std          |   1.14 |   1.66 |   2.26 |   0.41 |
| nN         | mean         |   7    |   4.16 |   4.57 |   7.92 |
| nN         | std          |   1.02 |   1.31 |   1.63 |   0.42 |
| nO         | mean         |   0.07 |   1.68 |   1.63 |   0.08 |
| nO         | std          |   0.31 |   0.75 |   0.99 |   0.47 |
| rings      | mean         |   4.41 |   2.4  |   2.43 |   5.48 |
| rings      | std          |   1.58 |   1.3  |   1.24 |   2.03 |
| arom_rings | mean         |   3.84 |   2.25 |   2.31 |   4.29 |
| arom_rings | std          |   1.06 |   1.14 |   1.11 |   0.84 |
| rot_bonds  | mean         |  11.42 |  19.05 |  18.66 |  11.09 |
| rot_bonds  | std          |   6.59 |   6.8  |   6.48 |   7.79 |
| SA_score   | mean         |   3.29 |   3.16 |   3.03 |   3.46 |
| SA_score   | std          |   0.55 |   0.6  |   0.62 |   0.59 |

## Table 5. Descriptor means by design x model

|             | MW      | MW.1   | MW.2           | MW.3   | MolLogP   | MolLogP.1   | MolLogP.2      | MolLogP.3   | SA_score   | SA_score.1   | SA_score.2     | SA_score.3   | arom_N   | arom_N.1   | arom_N.2       | arom_N.3   |
|:------------|:--------|:-------|:---------------|:-------|:----------|:------------|:---------------|:------------|:-----------|:-------------|:---------------|:-------------|:---------|:-----------|:---------------|:-----------|
| model_label | ChatGPT | Claude | Claude Science | Gemini | ChatGPT   | Claude      | Claude Science | Gemini      | ChatGPT    | Claude       | Claude Science | Gemini       | ChatGPT  | Claude     | Claude Science | Gemini     |
| design      | nan     | nan    | nan            | nan    | nan       | nan         | nan            | nan         | nan        | nan          | nan            | nan          | nan      | nan        | nan            | nan        |
| 1           | 446.75  | 542.1  | 561.57         | 575.24 | 5.86      | 7.98        | 8.22           | 8.76        | 3.05       | 3.38         | 3.49           | 3.24         | 6.64     | 6.72       | 7.2            | 7.26       |
| 2           | 449.17  | 555.93 | 583.92         | 610.0  | 6.38      | 8.62        | 9.16           | 10.31       | 2.84       | 3.2          | 3.53           | 3.06         | 2.08     | 2.96       | 3.36           | 2.2        |
| 3           | 477.55  | 577.24 | 559.88         | 531.03 | 6.35      | 9.39        | 8.68           | 7.99        | 2.78       | 3.19         | 3.3            | 2.83         | 2.8      | 3.42       | 3.42           | 3.06       |
| 4           | 572.24  | 602.18 | 639.77         | 627.55 | 7.89      | 8.43        | 9.09           | 9.41        | 3.24       | 3.58         | 3.86           | 3.17         | 7.9      | 7.84       | 8.04           | 7.88       |

## Table 6. Unique molecules and Murcko scaffolds

| group              |   n |   unique_molecules |   unique_murcko_scaffolds |   mean_scaffolds_per_run |
|:-------------------|----:|-------------------:|--------------------------:|-------------------------:|
| Design 1           | 200 |                163 |                        90 |                     8.1  |
| Design 2           | 200 |                163 |                        55 |                     7.35 |
| Design 3           | 200 |                148 |                        52 |                     7.55 |
| Design 4           | 200 |                128 |                        43 |                     5.9  |
| ChatGPT            | 200 |                188 |                        74 |                     5.45 |
| Claude             | 200 |                147 |                        67 |                     8.95 |
| Claude Science     | 200 |                153 |                        82 |                     9.3  |
| Gemini             | 200 |                119 |                        43 |                     5.2  |
| All generated      | 800 |                528 |                       187 |                   nan    |
| Experimental table | 295 |                295 |                        69 |                   nan    |

## Table 7. Run-to-run reproducibility

|                       |   unique_molecules_of_50 |   unique_scaffolds_of_50 |   jaccard_molecules |   jaccard_scaffolds |   CV_MW_pct |   CV_logP_pct |
|:----------------------|-------------------------:|-------------------------:|--------------------:|--------------------:|------------:|--------------:|
| (1, 'ChatGPT')        |                       49 |                       31 |               0.005 |               0.093 |         3.7 |           6   |
| (1, 'Claude')         |                       44 |                       32 |               0.033 |               0.163 |         0.9 |           4.2 |
| (1, 'Claude Science') |                       47 |                       36 |               0.016 |               0.099 |         8.5 |           9.4 |
| (1, 'Gemini')         |                       34 |                       14 |               0.147 |               0.344 |         7.6 |          13.1 |
| (2, 'ChatGPT')        |                       48 |                       12 |               0.011 |               0.341 |         2.8 |          13.5 |
| (2, 'Claude')         |                       46 |                       24 |               0.027 |               0.254 |        10.1 |          14.8 |
| (2, 'Claude Science') |                       39 |                       30 |               0.088 |               0.205 |         2.2 |           5.8 |
| (2, 'Gemini')         |                       41 |                       20 |               0.077 |               0.244 |         2.4 |           4.9 |
| (3, 'ChatGPT')        |                       49 |                       24 |               0.005 |               0.107 |        15.3 |          12.2 |
| (3, 'Claude')         |                       39 |                       22 |               0.077 |               0.327 |         6.7 |          10.7 |
| (3, 'Claude Science') |                       40 |                       20 |               0.073 |               0.391 |         5   |           4.5 |
| (3, 'Gemini')         |                       39 |                       12 |               0.068 |               0.414 |         3.3 |           7.3 |
| (4, 'ChatGPT')        |                       43 |                       12 |               0.055 |               0.218 |         2.7 |           6.5 |
| (4, 'Claude')         |                       39 |                       17 |               0.071 |               0.424 |         4.5 |          10.1 |
| (4, 'Claude Science') |                       41 |                       21 |               0.06  |               0.269 |         2.9 |           5.6 |
| (4, 'Gemini')         |                       31 |                       11 |               0.222 |               0.264 |         4.9 |          10.3 |

## Table 8. Ligand-core prevalence by design

| core                             |   exp295_n |   exp295_pct |   D1_n |   D1_pct |   D2_n |   D2_pct |   D3_n |   D3_pct |   D4_n |   D4_pct |   gen800_n |   gen800_pct |
|:---------------------------------|-----------:|-------------:|-------:|---------:|-------:|---------:|-------:|---------:|-------:|---------:|-----------:|-------------:|
| BTP                              |          3 |          1   |     58 |     29   |      3 |      1.5 |     11 |      5.5 |      9 |      4.5 |         81 |         10.1 |
| BTBP                             |          8 |          2.7 |     26 |     13   |      0 |      0   |      6 |      3   |    148 |     74   |        180 |         22.5 |
| BTPhen                           |          1 |          0.3 |     21 |     10.5 |      0 |      0   |      4 |      2   |     31 |     15.5 |         56 |          7   |
| bis-triazolyl-pyridine           |          1 |          0.3 |      5 |      2.5 |      3 |      1.5 |      7 |      3.5 |      0 |      0   |         15 |          1.9 |
| bis-benzimidazolyl-pyridine      |          0 |          0   |      7 |      3.5 |      0 |      0   |      3 |      1.5 |      0 |      0   |         10 |          1.2 |
| bipyridine (any)                 |         16 |          5.4 |     49 |     24.5 |     38 |     19   |     31 |     15.5 |    152 |     76   |        270 |         33.8 |
| phenanthroline (any)             |         31 |         10.5 |     35 |     17.5 |     40 |     20   |     31 |     15.5 |     31 |     15.5 |        137 |         17.1 |
| picolinamide (mono)              |         36 |         12.2 |      4 |      2   |    149 |     74.5 |    119 |     59.5 |      0 |      0   |        272 |         34   |
| DPA (pyridine-2,6-diamide)       |          7 |          2.4 |      0 |      0   |     22 |     11   |     30 |     15   |      0 |      0   |         52 |          6.5 |
| PDA (phenanthroline-2,9-diamide) |         12 |          4.1 |      2 |      1   |     24 |     12   |     20 |     10   |      0 |      0   |         46 |          5.8 |
| DGA (diglycolamide)              |         85 |         28.8 |      0 |      0   |      2 |      1   |      5 |      2.5 |      0 |      0   |          7 |          0.9 |
| malonamide                       |         44 |         14.9 |      0 |      0   |      0 |      0   |      2 |      1   |      0 |      0   |          2 |          0.2 |
| CMPO                             |         14 |          4.7 |      0 |      0   |      0 |      0   |      0 |      0   |      0 |      0   |          0 |          0   |
| phosphoryl P=O (any)             |         37 |         12.5 |      0 |      0   |     14 |      7   |      1 |      0.5 |      0 |      0   |         15 |          1.9 |

## Table 9. Ligand-core prevalence by model

| core                             |   ChatGPT_n |   ChatGPT_pct |   Claude_n |   Claude_pct |   Claude Science_n |   Claude Science_pct |   Gemini_n |   Gemini_pct |
|:---------------------------------|------------:|--------------:|-----------:|-------------:|-------------------:|---------------------:|-----------:|-------------:|
| BTP                              |          21 |          10.5 |         10 |          5   |                 14 |                  7   |         36 |         18   |
| BTBP                             |          44 |          22   |         36 |         18   |                 39 |                 19.5 |         61 |         30.5 |
| BTPhen                           |           0 |           0   |         24 |         12   |                 27 |                 13.5 |          5 |          2.5 |
| bis-triazolyl-pyridine           |           0 |           0   |          4 |          2   |                  8 |                  4   |          3 |          1.5 |
| bis-benzimidazolyl-pyridine      |           0 |           0   |          5 |          2.5 |                  4 |                  2   |          1 |          0.5 |
| bipyridine (any)                 |          66 |          33   |         64 |         32   |                 60 |                 30   |         80 |         40   |
| phenanthroline (any)             |           2 |           1   |         54 |         27   |                 59 |                 29.5 |         22 |         11   |
| picolinamide (mono)              |          50 |          25   |         82 |         41   |                 79 |                 39.5 |         61 |         30.5 |
| DPA (pyridine-2,6-diamide)       |          14 |           7   |         12 |          6   |                  9 |                  4.5 |         17 |          8.5 |
| PDA (phenanthroline-2,9-diamide) |           2 |           1   |         16 |          8   |                 13 |                  6.5 |         15 |          7.5 |
| DGA (diglycolamide)              |           0 |           0   |          3 |          1.5 |                  0 |                  0   |          4 |          2   |
| malonamide                       |           0 |           0   |          0 |          0   |                  1 |                  0.5 |          1 |          0.5 |
| CMPO                             |           0 |           0   |          0 |          0   |                  0 |                  0   |          0 |          0   |
| phosphoryl P=O (any)             |          12 |           6   |          1 |          0.5 |                  2 |                  1   |          0 |          0   |

## Table 10. PubChem-confirmed compounds, counts per cell

| design             |   ChatGPT |   Claude |   Claude Science |   Gemini |   design_total_of_200 |
|:-------------------|----------:|---------:|-----------------:|---------:|----------------------:|
| 1                  |         7 |       11 |                6 |       29 |                    53 |
| 2                  |         7 |        0 |                0 |        4 |                    11 |
| 3                  |         1 |       10 |                7 |       17 |                    35 |
| 4                  |         4 |       10 |                6 |       17 |                    37 |
| model_total_of_200 |        19 |       31 |               19 |       67 |                   136 |

## Table 11. PubChem-confirmed compounds, by number of occurrences

| pubchem_compound_title                                                                                                                                                    |   pubchem_cid |   occurrences |   n_models | models                          | designs   | in_prompt_table   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------:|--------------:|-----------:|:--------------------------------|:----------|:------------------|
| 3-[6-[6-(5,6-Dihexyl-1,2,4-triazin-3-yl)-2-pyridinyl]-2-pyridinyl]-5,6-dihexyl-1,2,4-triazine                                                                             |   1.35022e+08 |            11 |          2 | ChatGPT, Gemini                 | 1, 3, 4   | False             |
| 2,6-Bis(5,6-diisobutyl-1,2,4-triazine-3-yl)pyridine                                                                                                                       |   1.66585e+07 |             9 |          2 | ChatGPT, Gemini                 | 1, 3      | False             |
| 5,6-Dibutyl-3-[6-[6-(5,6-dibutyl-1,2,4-triazin-3-yl)-2-pyridinyl]-2-pyridinyl]-1,2,4-triazine                                                                             |   8.62436e+07 |             7 |          2 | ChatGPT, Gemini                 | 1, 3, 4   | False             |
| 2,6-Bis(5,6-dihexyl-1,2,4-triazine-3-yl)pyridine                                                                                                                          |   6.8624e+07  |             6 |          1 | Gemini                          | 1, 3, 4   | False             |
| 1-Octyl-2-[6-(1-octylbenzimidazol-2-yl)-2-pyridinyl]benzimidazole                                                                                                         |   1.53357e+07 |             6 |          2 | Claude, Claude Science          | 1, 3      | False             |
| 2,9-Bis(5,6-dipentyl-1,2,4-triazin-3-yl)-1,10-phenanthroline                                                                                                              |   1.02315e+08 |             5 |          3 | Claude, Claude Science, Gemini  | 1, 4      | False             |
| 2,6-Bis[1-(2-ethylhexyl)-1h-1,2,3-triazol-4-yl]pyridine                                                                                                                   |   1.34821e+08 |             5 |          2 | Claude, Claude Science          | 1, 3      | False             |
| 5,6-Dicyclohexyl-3-[6-(5,6-dicyclohexyl-1,2,4-triazin-3-yl)-2-pyridinyl]-1,2,4-triazine                                                                                   |   8.58771e+07 |             5 |          2 | ChatGPT, Gemini                 | 1, 4      | False             |
| 2,9-Bis(5,5,8,8-tetramethyl-6,7-dihydro-1,2,4-benzotriazin-3-yl)-1,10-phenanthroline                                                                                      |   1.0178e+08  |             4 |          2 | Claude, Claude Science          | 4         | True              |
| 2-N,2-N,6-N,6-N-tetrahexylpyridine-2,6-dicarboxamide                                                                                                                      |   4.09425e+06 |             4 |          3 | ChatGPT, Claude Science, Gemini | 2, 3      | False             |
| 3-[6-[6-(5,6-Dioctyl-1,2,4-triazin-3-yl)-2-pyridinyl]-2-pyridinyl]-5,6-dioctyl-1,2,4-triazine                                                                             |   1.41463e+08 |             4 |          1 | Gemini                          | 1, 4      | False             |
| 2-N,2-N,9-N,9-N-tetraoctyl-1,10-phenanthroline-2,9-dicarboxamide                                                                                                          |   1.02115e+08 |             4 |          2 | Claude, Gemini                  | 2, 3      | True              |
| 2,9-Bis(5,6-dibutyl-1,2,4-triazin-3-yl)-1,10-phenanthroline                                                                                                               |   1.02315e+08 |             4 |          2 | Claude, Claude Science          | 1, 3, 4   | False             |
| 2,6-Bis(1-octyl-1h-1,2,3-triazol-4-yl)pyridine                                                                                                                            |   1.025e+08   |             4 |          2 | Claude, Gemini                  | 1, 3      | False             |
| 2,9-Bis(8,11,11-trimethyl-3,4,6-triazatricyclo[6.2.1.02,7]undeca-2(7),3,5-trien-5-yl)-1,10-phenanthroline                                                                 |   1.02315e+08 |             4 |          2 | Claude, Claude Science          | 1, 4      | False             |
| 2-[1-(2-Ethylhexyl)triazol-4-yl]-6-[6-[1-(2-ethylhexyl)triazol-4-yl]-2-pyridinyl]pyridine                                                                                 |   1.32541e+08 |             3 |          2 | Claude, Claude Science          | 1         | False             |
| 3-[6-(5,6-Dioctyl-1,2,4-triazin-3-yl)-2-pyridinyl]-5,6-dioctyl-1,2,4-triazine                                                                                             |   1.0123e+08  |             3 |          1 | Gemini                          | 1, 4      | False             |
| N6,N6,N6',N6'-Tetraoctyl-[2,2'-bipyridine]-6,6'-dicarboxamide                                                                                                             |   1.68434e+08 |             3 |          2 | Claude Science, Gemini          | 2, 3      | False             |
| 2-(1-Hexyltriazol-4-yl)-6-[6-(1-hexyltriazol-4-yl)-2-pyridinyl]pyridine                                                                                                   |   1.02522e+08 |             2 |          2 | Claude, Gemini                  | 1         | False             |
| N,N,N',N'-tetra-n-hexyl-3-oxa-pentanediamide                                                                                                                              |   8.57869e+07 |             2 |          1 | Gemini                          | 3         | True              |
| N,N,N',N'-tetrabutyl-2,6-pyridinedicarboxamide                                                                                                                            |   3.71592e+06 |             2 |          1 | ChatGPT                         | 2, 3      | False             |
| N,N-dibutyl-6-[6-(dibutylcarbamoyl)-2-pyridinyl]pyridine-2-carboxamide                                                                                                    |   1.01896e+08 |             2 |          2 | ChatGPT, Gemini                 | 2, 3      | False             |
| N,N,N',N'-tetrabutyl-1,10-phenanthroline-2,9-dicarboxamide                                                                                                                |   1.32427e+08 |             2 |          1 | Gemini                          | 3         | True              |
| 2-[2-(dioctylamino)-2-oxoethyl]sulfanyl-N,N-dioctylacetamide                                                                                                              |   1.01869e+08 |             2 |          1 | Gemini                          | 2, 3      | False             |
| 3-[6-(5,6-Diheptyl-1,2,4-triazin-3-yl)-2-pyridinyl]-5,6-diheptyl-1,2,4-triazine                                                                                           |   6.86255e+07 |             2 |          1 | Gemini                          | 1         | False             |
| 2-N,6-N-dioctyl-2-N,6-N-diphenylpyridine-2,6-dicarboxamide                                                                                                                |   1.0259e+08  |             2 |          2 | Claude, Claude Science          | 3         | False             |
| 2,6-Bis(5,6-diphenyl-1,2,4-triazin-3-YL)pyridine                                                                                                                          |   6.41443e+06 |             1 |          1 | ChatGPT                         | 1         | False             |
| 2-N,2-N,9-N,9-N-tetra(propan-2-yl)-1,10-phenanthroline-2,9-dicarboxamide                                                                                                  |   1.53531e+08 |             1 |          1 | ChatGPT                         | 2         | False             |
| 2,9-Bis[5,6-bis(4-methylphenyl)-1,2,4-triazin-3-yl]-1,10-phenanthroline                                                                                                   |   1.39229e+08 |             1 |          1 | Claude                          | 1         | False             |
| 2,6-bis(5-butyl-1H-1,2,4-triazol-3-yl)pyridine                                                                                                                            |   1.54143e+07 |             1 |          1 | ChatGPT                         | 1         | False             |
| 2,6-Bis(3,5-ditert-butylpyrazol-1-yl)pyridine                                                                                                                             |   8.62379e+07 |             1 |          1 | Gemini                          | 1         | False             |
| 2,2'-(Methylimino)bis(N,N-di-n-octylacetamide)                                                                                                                            |   7.15513e+07 |             1 |          1 | Claude Science                  | 3         | True              |
| 2,4,6-Tris(5-hexyl-2-pyridinyl)-1,3,5-triazine                                                                                                                            |   5.82507e+07 |             1 |          1 | Gemini                          | 1         | False             |
| 2,4,6-Tris(5-tert-butyl-2-pyridinyl)-1,3,5-triazine                                                                                                                       |   5.82507e+07 |             1 |          1 | Gemini                          | 1         | False             |
| 1-Hexyl-2-[6-(1-hexylbenzimidazol-2-yl)-2-pyridinyl]benzimidazole                                                                                                         |   1.78638e+07 |             1 |          1 | Claude Science                  | 3         | False             |
| 2,6-Bis(5-t-butyl-1h-pyrazole-3-yl)pyridine                                                                                                                               |   1.01497e+08 |             1 |          1 | Claude                          | 1         | False             |
| 2,6-Bis(dihexylphosphorylmethyl)pyridine                                                                                                                                  |   1.55204e+07 |             1 |          1 | ChatGPT                         | 2         | False             |
| 2,6-bis(5-butyl-1H-pyrazol-3-yl)pyridine                                                                                                                                  |   1.29859e+08 |             1 |          1 | ChatGPT                         | 1         | False             |
| 2-[hexyl-[2-[methyl(octyl)amino]-2-oxoethyl]amino]-N-methyl-N-octylacetamide                                                                                              |   1.0203e+08  |             1 |          1 | ChatGPT                         | 2         | False             |
| 3-[6-[5,6-Bis(4-tert-butylphenyl)-1,2,4-triazin-3-yl]-2-pyridinyl]-5,6-bis(4-tert-butylphenyl)-1,2,4-triazine                                                             |   1.35022e+08 |             1 |          1 | Claude                          | 1         | False             |
| 3-[6-[5,6-Di(nonyl)-1,2,4-triazin-3-yl]-2-pyridinyl]-5,6-di(nonyl)-1,2,4-triazine                                                                                         |   1.01569e+08 |             1 |          1 | Gemini                          | 1         | False             |
| 3-[4-Tert-butyl-6-[4-tert-butyl-6-(5,5,8,8-tetramethyl-6,7-dihydro-1,2,4-benzotriazin-3-yl)-2-pyridinyl]-2-pyridinyl]-5,5,8,8-tetramethyl-6,7-dihydro-1,2,4-benzotriazine |   5.73819e+07 |             1 |          1 | Claude                          | 4         | True              |
| 3-[4-Chloro-6-(5,6-dipropyl-1,2,4-triazin-3-yl)-2-pyridinyl]-5,6-dipropyl-1,2,4-triazine                                                                                  |   1.02417e+08 |             1 |          1 | ChatGPT                         | 1         | False             |
| 2-N,6-N-bis(2-ethylhexyl)pyridine-2,6-dicarboxamide                                                                                                                       |   5.21006e+06 |             1 |          1 | Gemini                          | 3         | False             |
| 2-N,2-N,9-N,9-N-tetraethyl-1,10-phenanthroline-2,9-dicarboxamide                                                                                                          |   1.01893e+08 |             1 |          1 | ChatGPT                         | 2         | False             |
| 2-[2-[bis(2-methylpropyl)amino]-2-oxoethyl]sulfanyl-N,N-bis(2-methylpropyl)acetamide                                                                                      |   1.02483e+08 |             1 |          1 | Gemini                          | 3         | False             |
| 3-[6-[6-(5,6-Diphenyl-1,2,4-triazin-3-yl)-2-pyridinyl]-2-pyridinyl]-5,6-diphenyl-1,2,4-triazine                                                                           |   6.74264e+07 |             1 |          1 | ChatGPT                         | 4         | False             |
| 5,5,9,9-tetramethyl-3-[6-[6-(5,5,9,9-tetramethyl-7,8-dihydro-6H-cyclohepta[e][1,2,4]triazin-3-yl)-2-pyridinyl]-2-pyridinyl]-7,8-dihydro-6H-cyclohepta[e][1,2,4]triazine   |   5.73819e+07 |             1 |          1 | Claude                          | 4         | False             |
| 5,5,8,8-Tetramethyl-3-[4-methyl-6-[4-methyl-6-(5,5,8,8-tetramethyl-6,7-dihydro-1,2,4-benzotriazin-3-yl)-2-pyridinyl]-2-pyridinyl]-6,7-dihydro-1,2,4-benzotriazine         |   5.73819e+07 |             1 |          1 | Claude                          | 4         | True              |
| 4,7-Diphenyl-2,9-bis(5,5,8,8-tetramethyl-6,7-dihydro-1,2,4-benzotriazin-3-yl)-1,10-phenanthroline                                                                         |   1.32529e+08 |             1 |          1 | Claude Science                  | 4         | False             |
| 3-[6-[6-[5,6-Di(nonyl)-1,2,4-triazin-3-yl]-2-pyridinyl]-2-pyridinyl]-5,6-di(nonyl)-1,2,4-triazine                                                                         |   1.32916e+08 |             1 |          1 | Gemini                          | 4         | False             |
| 3-[6-[6-[5,6-Bis(3-methylbutyl)-1,2,4-triazin-3-yl]-2-pyridinyl]-2-pyridinyl]-5,6-bis(3-methylbutyl)-1,2,4-triazine                                                       |   1.41349e+08 |             1 |          1 | Gemini                          | 1         | False             |
| 3-[6-[6-[5,6-Bis(4-methylpentyl)-1,2,4-triazin-3-yl]-2-pyridinyl]-2-pyridinyl]-5,6-bis(4-methylpentyl)-1,2,4-triazine                                                     |   1.41349e+08 |             1 |          1 | Gemini                          | 4         | False             |
| 6,6'-Bis(5,6-dipentyl-[1,2,4]triazine-3-yl)-[2,2']bipyridine                                                                                                              |   8.62391e+07 |             1 |          1 | Gemini                          | 4         | True              |
| 5-Tert-butyl-2,9-bis(5,5,8,8-tetramethyl-6,7-dihydro-1,2,4-benzotriazin-3-yl)-1,10-phenanthroline                                                                         |   1.41709e+08 |             1 |          1 | Claude Science                  | 4         | False             |

## Table 12. Mean maximum Tanimoto similarity under three reference sets

|   design |   reference_used_in_source_csv |   sim_vs_295 |   sim_vs_9 |   sim_vs_286 |   source_csv_max_sim_exp |
|---------:|-------------------------------:|-------------:|-----------:|-------------:|-------------------------:|
|        1 |                            295 |        0.558 |      0.523 |        0.471 |                    0.558 |
|        2 |                            295 |        0.548 |      0.357 |        0.536 |                    0.548 |
|        3 |                              9 |        0.574 |      0.385 |        0.547 |                    0.385 |
|        4 |                              9 |        0.658 |      0.621 |        0.563 |                    0.621 |

## Table 13. D2 versus D3 similarity under each reference set

| reference_set                    |   D2_mean |   D3_mean |   mann_whitney_p |
|:---------------------------------|----------:|----------:|-----------------:|
| 295 molecules (all experimental) |     0.548 |     0.574 |            0.332 |
| 9 molecules (positive subset)    |     0.357 |     0.385 |            0.143 |
| 286 molecules (295 minus 9)      |     0.536 |     0.547 |            0.974 |

## Table 14. Specification violations per cell

|                       |   n |   sim_above_0.85 |   sim_below_0.25 |   logP_le_3 |   design_focus_compliance_pct |
|:----------------------|----:|-----------------:|-----------------:|------------:|------------------------------:|
| (1, 'ChatGPT')        |  50 |                0 |                0 |           0 |                           100 |
| (1, 'Claude')         |  50 |                0 |                0 |           0 |                           100 |
| (1, 'Claude Science') |  50 |                0 |                0 |           0 |                           100 |
| (1, 'Gemini')         |  50 |               15 |                0 |           0 |                           100 |
| (2, 'ChatGPT')        |  50 |                0 |                0 |           0 |                            84 |
| (2, 'Claude')         |  50 |                0 |                0 |           0 |                            98 |
| (2, 'Claude Science') |  50 |                0 |                0 |           0 |                            96 |
| (2, 'Gemini')         |  50 |                3 |                0 |           0 |                            94 |
| (3, 'ChatGPT')        |  50 |                0 |                0 |           0 |                           100 |
| (3, 'Claude')         |  50 |                4 |                0 |           0 |                            76 |
| (3, 'Claude Science') |  50 |                1 |                0 |           0 |                            86 |
| (3, 'Gemini')         |  50 |               13 |                0 |           1 |                            66 |
| (4, 'ChatGPT')        |  50 |                5 |                0 |           0 |                            94 |
| (4, 'Claude')         |  50 |                6 |                0 |           0 |                            90 |
| (4, 'Claude Science') |  50 |                3 |                0 |           0 |                            96 |
| (4, 'Gemini')         |  50 |               19 |                0 |           2 |                            88 |

## Table 15. Exact matches to the 295-molecule experimental table

| design      |   ChatGPT |   Claude |   Claude Science |   Gemini |   design_total |
|:------------|----------:|---------:|-----------------:|---------:|---------------:|
| 1           |         0 |        0 |                0 |        0 |              0 |
| 2           |         0 |        0 |                0 |        1 |              1 |
| 3           |         0 |        3 |                1 |        4 |              8 |
| 4           |         0 |        5 |                1 |        1 |              7 |
| model_total |         0 |        8 |                2 |        6 |             16 |

## Table 16. Property distributions, generated set versus experimental library

| descriptor   |   exp_mean |   exp_sd |   exp_p5 |   exp_p95 |   gen_mean |   gen_sd |   gen_p5 |   gen_p95 |   sd_ratio_gen_over_exp |
|:-------------|-----------:|---------:|---------:|----------:|-----------:|---------:|---------:|----------:|------------------------:|
| MW           |     549.04 |   338.23 |   266.32 |    838.24 |     557.01 |   100.61 |   402.4  |    715.2  |                    0.3  |
| MolLogP      |       7.19 |     4.54 |     2.05 |     14.27 |       8.28 |     2.29 |     5.02 |     12.53 |                    0.5  |
| TPSA         |      73.84 |    48.54 |    31.57 |    127.97 |      81.6  |    21.41 |    48.5  |    103.1  |                    0.44 |
| rot_bonds    |      20.17 |    14.79 |     2    |     43.3  |      15.06 |     7.9  |     3    |     30    |                    0.53 |

## Table 17. SMARTS patterns used for core assignment

| Core | SMARTS |
|---|---|
| BTP | `c1cc(-c2nccnn2)nc(-c3nccnn3)c1` |
| BTBP | `c1ccc(-c2nccnn2)nc1-c3cccc(-c4nccnn4)n3` |
| BTPhen | `c1cc(-c2nccnn2)nc3c1ccc4ccc(-c5nccnn5)nc34` |
| bis-triazolyl-pyridine | `c1cc(-c2cn([#6])nn2)nc(-c3cn([#6])nn3)c1` |
| bis-benzimidazolyl-pyridine | `c1cc(-c2nc3ccccc3n2)nc(-c4nc5ccccc5n4)c1` |
| bipyridine (any) | `c1ccnc(c1)-c2ccccn2` |
| phenanthroline (any) | `c1cc2ccc3cccnc3c2nc1` |
| picolinamide (mono) | `O=C([NX3])c1ccccn1` |
| DPA (pyridine-2,6-diamide) | `O=C([NX3])c1cccc(C(=O)[NX3])n1` |
| PDA (phenanthroline-2,9-diamide) | `O=C([NX3])c1ccc2ccc3ccc(C(=O)[NX3])nc3c2n1` |
| DGA (diglycolamide) | `O=C([NX3])COCC(=O)[NX3]` |
| malonamide | `O=C([NX3])CC(=O)[NX3]` |
| CMPO | `O=P(*)(*)CC(=O)[NX3]` |
| phosphoryl P=O (any) | `[PX4]=O` |
