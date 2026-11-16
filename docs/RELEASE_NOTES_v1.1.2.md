# v1.1.2 — Correction to Supplementary Table S11 Part 2

## Overview

Version v1.1.2 corrects the public export of Supplementary Table S11 Part 2. No additional experiments or model training were performed. The evidence scope remains 282 runs.

## Correction

`revisions/v1.1.0/final_table_exports/Revised-Supplementary-table-12.csv` contains the corrected 12 seedwise Kendall rank-correlation rows for two replacement model sets:

- Mean-pooling replacement: 6 rows.
- max_len=1000 replacement: 6 rows.

Only ConcatFusion is replaced in each model set; the other four models remain unchanged.

Rankings are based on record-level C-index. Kendall tau is calculated separately for seeds 42, 123 and 2026 using the five-model convention:

τ = (C − D) / 10.

The previous six-row export contained seedwise correlations for the original five-model set rather than the required replacement model sets.

## Reproducibility

The original 282-run evidence set, training protocols, run-level results and underlying prediction data remain unchanged.

The 69 original ZIP parts and `payload_index.json` under `revisions/v1.1.0/` are retained unchanged as the historical v1.1.0 payload.

The historical ZIP payload intentionally retains its original six-row S11 Part 2 CSV. This historical copy is not represented as the corrected v1.1.2 export.

## v1.1.2 Unpacking and S11 Overlay

The new script `scripts/unpack_revision_v112.py` provides the corrected v1.1.2 reconstruction procedure.

It:

1. Verifies all 69 original ZIP parts against the existing v1.1.0 payload index.
2. Checks ZIP CRCs, member counts, duplicate paths and unsafe paths.
3. Extracts the historical payload and verifies the original `PUBLIC_SOURCE_MAPPING.json` hashes.
4. Replaces the extracted historical six-row S11 Part 2 CSV with the corrected 12-row public CSV.
5. Verifies the resulting S11 header, row count and file contents.

The corrected file is written to:

`external_90/final_table_exports/Revised-Supplementary-table-12.csv`

The original ZIP parts, historical payload index and v1.1.0 unpacking script are not modified.

For exact historical reconstruction, use `scripts/unpack_revision_v110.py`. For the corrected v1.1.2 distribution, use `scripts/unpack_revision_v112.py`.

## Archiving

Version v1.1.2 supersedes v1.1.1 for the corrected S11 Part 2 table export and its documented reconstruction procedure. The earlier release remains available as a historical record.
The v1.1.2 archive is published on Zenodo:

- Version-specific DOI: https://doi.org/10.5281/zenodo.24279260
- Concept DOI (all versions): https://doi.org/10.5281/zenodo.24247402

Use the version-specific DOI to cite this exact v1.1.2 release. The Concept DOI resolves to the latest version of the record.