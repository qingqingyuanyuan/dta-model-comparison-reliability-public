# Controlled Multi-Regime Evaluation for Drug–Target Affinity Prediction

Reproducibility materials accompanying **Model Rankings in Drug–Target Affinity Prediction Vary Across Evaluation Regimes: A Controlled Multi-Seed Study of Model-Comparison Reliability**.

## Current distribution — v1.1.1

This v1.1.1 distribution updates the repository packaging and release metadata for the existing 282-run evidence set. It does not represent an additional experimental campaign.

The current manuscript evidence comprises **282 runs**, kept in distinct layers:

| Evidence layer | Runs | Scope |
|---|---:|---|
| Original campaign | 126 | KIBA/Davis primary comparisons and prespecified sensitivity/efficiency runs |
| Capacity controls | 36 | Original splits; widened DeepDTA-style/GraphDTA-GCN-style baselines; matched AdamW protocol |
| Second KIBA split | 30 | Five configurations × two cold-start regimes × three model seeds |
| GPCR extension | 30 | One human GPCR Ki cohort/split; within-cohort cold-drug/cold-target retraining |
| Protease extension | 60 | Two splits of one human protease Ki cohort; within-cohort retraining |

Historical 36-run Adam exploration is auxiliary and **excluded** from the 282-run total.

Paired model seeds are 42, 123 and 2026. Warm evaluation belongs to KIBA/Davis; external extensions cover cold-drug and full-sequence-defined cold-target evaluation.

The original KIBA mean-ordering reversal was conditional on training, model set and split. Cross-regime mean-ranking Kendall tau is −0.60 for GPCR and +0.40/+0.20 for the two protease splits.

Two non-kinase classes do not establish proteome-wide generality. GPCR cold-target contains only seven independent test sequences. Protease splits share two test sequences and 163 cold-drug entities; they are not two independent external cohorts.

External capacities are unequal, so these runs cannot isolate causal superiority of fusion mechanisms. This is retraining within cohorts, not zero-shot transfer of kinase-trained weights.

## Find the reproducibility materials

- [Revision guide](revisions/v1.1.0/README.md): scope, reconstruction, checks and known gaps.
- [External metrics](revisions/v1.1.0/results/): 90-run recomputed metrics, summaries, partitions and rank correlations.
- [Final table exports](revisions/v1.1.0/final_table_exports/): corrected document tables; source labels/structures are projected out.
- [Preparation and evaluation code](revisions/v1.1.0/code/external_90/): readable external campaign entry points; complete modules/configurations are in the payload.
- [Payload index](revisions/v1.1.0/payload_index.json): checksummed ZIP parts containing the original-126 prediction projections, 36 AdamW controls, 30 second-split results, external-90 results, code, metadata and frozen integer membership.
- [Payload ZIP parts](revisions/v1.1.0/payload_parts/): 69 independently checksummed archive parts, numbered `part-001.zip` through `part-069.zip`.

Existing `src`, `configs`, `data`, `results`, `case_study`, `audit` and `environment` directories retain the earlier published snapshot. Their historical 126-run scope must not be mistaken for the expanded 282-run evidence set.

## Unpacking and reproducibility

To reconstruct the revision materials, run the following command from the repository root:

```bash
python scripts/unpack_revision_v110.py --output ../dta_v110_materials
```

All ZIP parts unpack into one output directory.

The script checks hashes, rejects unsafe paths and does not load weights, execute archived code or run training.

No third-party source structures, sequences or affinity labels are redistributed. Reconstruct labels and features from independently acquired upstream versions and exact membership records and hashes, as explained in the payload provenance documentation.

Weights and large execution logs are omitted from the lightweight public payload.

Complete original-126 weights, logs, record predictions and original bootstrap random-number-generator states were not retained.

Historical checkpoint and prediction receipts refer to the original files, not the derived public projections.

Inherited bootstrap summaries are distinguished from independently recomputed metrics. File verification does not reconstruct historical test access or prove training determinism.

## Final statistical corrections

- **S17:** Errors use raw affinity units; MSE uses squared raw affinity units.
- **S13:** The contrast is defined as `Delta = C-index(A) - C-index(B)`. A positive value favors model A.
- **S18:** Reports the mean and sample standard deviation of three paired differences; bootstrap contrasts are reported separately.
- **S22:** Uses sample standard deviation (`ddof=1`). Original per-seed scores and means remain unchanged.

## Authors and citation

**Haobo Kui; Xinyuan Cui**, in that order.

**Corresponding author:** Haobo Kui  
School of Chemistry and Chemical Engineering, Harbin Normal University  
Email: 2993272783@qq.com

**Co-author:** Xinyuan Cui  
School of Physics and Electronic Engineering, Harbin Normal University

No equal-contribution designation is asserted in the current metadata.

Citation metadata for this distribution is provided in [CITATION.cff](CITATION.cff).

### Archival references

Previously published research archives remain available, including:

- **v1.0.0:** https://doi.org/10.5281/zenodo.22860429
- **v1.0.1:** https://doi.org/10.5281/zenodo.24051010

A version-specific DOI for v1.1.1 will be added after its Zenodo record has been published and verified.

Publishing a GitHub release does not itself establish that Zenodo has ingested the release materials. Earlier archival records remain independent of this repository update.

## License scope

Previously published v1.0.0/v1.0.1 material retains its original **CC BY 4.0** grant.

New revision additions retain the supplied public candidate's **CC BY-NC 4.0** terms. Third-party data and dependencies remain subject to their respective licenses.

See [LICENSE_SCOPE.md](LICENSE_SCOPE.md) and [LICENSE-NEW-ADDITIONS.txt](LICENSE-NEW-ADDITIONS.txt) for further details.

Peer-review correspondence, cover letters and private submission documents are not public release assets.

## Repository and release information

**Repository:** https://github.com/qingqingyuanyuan/dta-model-comparison-reliability-public

**Planned release:** v1.1.1

**Planned release date:** 2026-11-15

**Evidence scope:** 282 runs

**Revision payload:** `revisions/v1.1.0/`

**Payload archive parts:** 69

The v1.1.1 release is a repository distribution and metadata update for the existing evidence package. It does not claim new experiments or independent experimental replication.
