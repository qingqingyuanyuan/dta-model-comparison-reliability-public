# Controlled Multi-Regime Evaluation for Drug–Target Affinity Prediction

Reproducibility materials accompanying **Model Rankings in Drug–Target Affinity Prediction Vary Across Evaluation Regimes: A Controlled Multi-Seed Study of Model-Comparison Reliability**.

## Current Repository Revision — v1.1.2

Version v1.1.2 corrects the public export of Supplementary Table S11 Part 2, including the seedwise Kendall rank correlations for two replacement model sets.

This is a correction to the existing reproducibility distribution. It does not represent additional experiments, new model training, or independent experimental replication.

The manuscript evidence remains **282 runs**, organized into the following distinct layers:

| Evidence layer | Runs | Scope |
|---|---:|---|
| Original campaign | 126 | KIBA/Davis primary comparisons and prespecified sensitivity/efficiency runs |
| Capacity controls | 36 | Original splits; widened DeepDTA-style/GraphDTA-GCN-style baselines; matched AdamW protocol |
| Second KIBA split | 30 | Five configurations × two cold-start regimes × three model seeds |
| GPCR extension | 30 | One human GPCR Ki cohort/split; within-cohort cold-drug/cold-target retraining |
| Protease extension | 60 | Two splits of one human protease Ki cohort; within-cohort retraining |

Historical 36-run Adam exploration is auxiliary and **excluded** from the 282-run total.

## Supplementary Table S11 — Part 2 Correction

Version v1.1.2 corrects the seedwise regime-pair Kendall rank-correlation export.

The corrected file is:

`revisions/v1.1.0/final_table_exports/Revised-Supplementary-table-12.csv`

The corrected export contains **12 data rows**:

- Mean-pooling replacement set: 6 rows.
- max_len=1000 replacement set: 6 rows.

Each replacement set contains three regime-pair comparisons for KIBA and three for Davis.

### Calculation protocol

- Only ConcatFusion is replaced by the corresponding replacement variant.
- The other four models remain unchanged.
- Model rankings are based on record-level C-index.
- Each seed is evaluated separately.
- Five models produce ten pairwise model comparisons.
- Kendall tau follows the original convention:

  `tau = (C - D) / 10`

  where C and D denote the numbers of concordant and discordant model pairs, respectively.

- Seed order: 42, 123, and 2026.

The previous six-row export contained seedwise correlations for the original five-model set, rather than the required two replacement model sets.

The correction changes the public table export and its documentation. The underlying 282-run evidence, training protocols, run-level results, and prediction data remain unchanged.

These CSVs are document-table transcriptions; their inclusion does not imply independent recomputation from raw record-level predictions.

## Scientific Scope and Limitations

Paired model seeds are 42, 123 and 2026. Warm evaluation belongs to KIBA/Davis; external extensions cover cold-drug and full-sequence-defined cold-target evaluation.

The original KIBA mean-ordering reversal was conditional on training, model set and split. Cross-regime mean-ranking Kendall tau is −0.60 for GPCR and +0.40/+0.20 for the two protease splits.

Two non-kinase classes do not establish proteome-wide generality. GPCR cold-target contains only seven independent test sequences. Protease splits share two test sequences and 163 cold-drug entities; they are not two independent external cohorts.

External capacities are unequal, so these runs cannot isolate causal superiority of fusion mechanisms. This is retraining within cohorts, not zero-shot transfer of kinase-trained weights.

The study does not establish universal model-ranking reversal, prospective discovery performance, or zero-shot cross-family transfer.

## Find the Reproducibility Materials

- [Revision guide](revisions/v1.1.0/README.md): scope, reconstruction, checks and known gaps.
- [External metrics](revisions/v1.1.0/results/): 90-run recomputed metrics, summaries, partitions and rank correlations.
- [Final table exports](revisions/v1.1.0/final_table_exports/): corrected document tables; source labels/structures are projected out.
- [Preparation and evaluation code](revisions/v1.1.0/code/external_90/): readable external campaign entry points; complete modules/configurations are in the payload.
- [Payload index](revisions/v1.1.0/payload_index.json): checksummed ZIP parts containing the original-126 prediction projections, 36 AdamW controls, 30 second-split results, external-90 results, code, metadata and frozen integer membership.
- [Payload ZIP parts](revisions/v1.1.0/payload_parts/): 69 independently checksummed archive parts, numbered `part-001.zip` through `part-069.zip`.

### S11 Export Mapping

- `Revised-Supplementary-table-11.csv` contains the regime-pair summary correlations.
- `Revised-Supplementary-table-12.csv` contains the seedwise regime-pair correlations for both replacement sets: mean-pooling and max_len=1000.

The physical CSV table indices are not the supplementary table numbers. The supplementary contains multi-panel tables, so file index is not the S-table number.

The S11 Part 2 CSV is a document-table transcription, not an independently recomputed result from raw record-level predictions.

## Unpacking and Reproducibility

For exact historical v1.1.0 reconstruction, run:

```bash
python scripts/unpack_revision_v110.py --output ../dta_v110_materials
```

For the corrected v1.1.2 distribution, run:

```bash
python scripts/unpack_revision_v112.py --output ../dta_v112_materials
```

The original 69 ZIP parts and v1.1.0 payload index remain unchanged. The v1.1.2 unpacking script validates the historical payload and overlays the corrected 12-row S11 Part 2 CSV into the extracted output.

Both scripts validate the original archive checksums and do not load weights, execute archived code or run training.

No third-party source structures, sequences or affinity labels are redistributed. Reconstruct labels and features from independently acquired upstream versions and exact membership records and hashes, as explained in the payload provenance documentation.

Weights and large execution logs are omitted from the lightweight public payload.

Complete original-126 weights, logs, record predictions and original bootstrap random-number-generator states were not retained.

Historical checkpoint and prediction receipts refer to the original files, not the derived public projections.

Inherited bootstrap summaries are distinguished from independently recomputed metrics. File verification does not reconstruct historical test access or prove training determinism.


## Final Statistical Corrections

- **S17:** Errors use raw affinity units; MSE uses squared raw affinity units.
- **S13:** The contrast is defined as `Delta = C-index(A) - C-index(B)`. A positive value favors model A.
- **S18:** Reports the mean and sample standard deviation of three paired differences; bootstrap contrasts are reported separately.
- **S22:** Uses sample standard deviation (`ddof=1`). Original per-seed scores and means remain unchanged.

## Authors and Citation

**Haobo Kui; Xinyuan Cui**, in that order.

**Corresponding author:** Haobo Kui  
School of Chemistry and Chemical Engineering, Harbin Normal University  
Email: 2993272783@qq.com

**Co-author:** Xinyuan Cui  
School of Physics and Electronic Engineering, Harbin Normal University

No equal-contribution designation is asserted in the current metadata.

Citation metadata for this distribution is provided in [CITATION.cff](CITATION.cff).

### Archival References

Previously published research archives remain available:

- **v1.0.0:** https://doi.org/10.5281/zenodo.22860429
- **v1.0.1:** https://doi.org/10.5281/zenodo.24051010
- **v1.1.1:** https://doi.org/10.5281/zenodo.24247403

The v1.1.1 Zenodo record is a historical archive and does not contain the v1.1.2 S11 Part 2 correction.

The v1.1.2 version-specific Zenodo record is now published:

- **v1.1.2:** https://doi.org/10.5281/zenodo.24279260

The v1.1.1 Zenodo record remains available as a historical archive and does not contain the v1.1.2 S11 Part 2 correction.

**Concept DOI (all versions):** https://doi.org/10.5281/zenodo.24247402

Use the version-specific DOI to cite v1.1.2. The Concept DOI resolves to the latest version and can be used to cite the complete version history.
## License Scope

Previously published v1.0.0/v1.0.1 material retains its original **CC BY 4.0** grant.

New additions under `revisions/v1.1.0/` are distributed under **CC BY-NC 4.0**, as specified in [LICENSE_SCOPE.md](LICENSE_SCOPE.md). Third-party data and dependencies remain subject to their respective licenses.

See [LICENSE_SCOPE.md](LICENSE_SCOPE.md) and [LICENSE-NEW-ADDITIONS.txt](LICENSE-NEW-ADDITIONS.txt) for further details.

Peer-review correspondence, cover letters and private submission documents are not public release assets.

## Repository and Release Information

**Repository:** https://github.com/qingqingyuanyuan/dta-model-comparison-reliability-public

**Current repository revision:** v1.1.2

**Evidence scope:** 282 runs

**Revision payload:** `revisions/v1.1.0/`

**Payload archive parts:** 69

Version v1.1.2 corrects the S11 Part 2 public table export and associated documentation. It does not claim new experiments or independent experimental replication.
