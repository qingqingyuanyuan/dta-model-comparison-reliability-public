Final document table transcriptions (UTF-8 CSV). Row/table ordering follows the DOCX; the supplementary contains multi-panel tables, so file index is NOT the S-table number. These exports are not independent recomputations. S22 uses sample SD (ddof=1); the original per-seed results and mean scores are unchanged. S17 errors are on the raw scale. S13 Delta=A-B. S18 reports paired mean and sample SD, not bootstrap intervals.
S11 export mapping:
Revised-Supplementary-table-11.csv contains the regime-pair summary correlations.
Revised-Supplementary-table-12.csv contains the seedwise regime-pair correlations for both replacement sets: mean-pooling and max_len=1000 (12 data rows).
The physical CSV table indices are not the supplementary table numbers.
S11 Part 2 calculation protocol:
The table reports seedwise cross-regime Kendall rank correlations for two replacement model sets: mean-pooling and max_len=1000.
For each replacement set, only ConcatFusion is replaced by the corresponding sensitivity variant. The other four models remain unchanged.
Model rankings are based on record-level C-index within each dataset, evaluation regime, and model seed.
For each seed, the rankings of five models are compared between two evaluation regimes. There are 10 possible pairwise model comparisons. Kendall tau is calculated using the original table convention:
tau = (C - D) / 10
where C and D denote the numbers of concordant and discordant model pairs, respectively.
The seed order is 42, 123, and 2026.
Part 2 contains 12 data rows: two replacement sets, two datasets (KIBA and Davis), and three regime-pair comparisons per dataset.
The original five-model seedwise correlations are not included in Part 2.
These CSVs are document-table transcriptions; inclusion here does not imply independent recomputation from raw record-level predictions.
