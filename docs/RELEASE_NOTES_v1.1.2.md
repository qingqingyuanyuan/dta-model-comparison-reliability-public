# v1.1.2 — Correction to Supplementary Table S11 Part 2

## Overview

Version v1.1.2 corrects the public export of Supplementary Table S11 Part 2. No additional experiments or model training were performed. The evidence scope remains 282 runs.

## Correction

`revisions/v1.1.0/final_table_exports/Revised-Supplementary-table-12.csv` now contains the 12 seedwise Kendall rank-correlation rows for the two replacement model sets:

- Mean-pooling replacement: 6 rows.
- max_len=1000 replacement: 6 rows.

Only ConcatFusion is replaced in each model set; the other four models remain unchanged.

Rankings are based on record-level C-index. Kendall tau is calculated separately for seeds 42, 123 and 2026 using the five-model convention:

τ = (C − D) / 10.

The previous six-row export contained seedwise correlations for the original five-model set rather than the required replacement model sets.

## Reproducibility

The original 282-run evidence set, training protocols, run-level results and underlying prediction data remain unchanged.

The existing revision payload is retained under `revisions/v1.1.0/` for reproducibility and compatibility.

## Archiving

Version v1.1.2 supersedes v1.1.1 for the corrected S11 Part 2 table export. The earlier release remains available as a historical record.

A version-specific Zenodo DOI will be added after the new archive has been published and verified.
