# Milestone 5

Milestone 5 combines failure analysis, the final IEEE-format paper, and the
defence. The failure-analysis files are prepared for review under issue #22.
The methods and reproducibility section is also prepared for review under issue
#23. The assembled IEEE paper and final defence materials (#24) remain pending.

## Methods and reproducibility — Shanker (#23)

- [Methods and reproducibility](methods_and_reproducibility.md)

This document explains the model, data pipeline, proposed change, training,
recovery, and evaluation in simple English. It is source material for the
methods section of the final IEEE paper, not a replacement for the paper.

## Evaluation deliverables

The stated M5 requirements are failure analysis, an IEEE-format paper, and
the defence. The final paper and presentation will use the methods section,
failure-analysis write-up, tables, and figures. The notebook, prediction CSVs,
configuration, environment record, and checksum manifest provide supporting
evidence in the repository; they are not additional standalone submission
requirements in the milestone list. Defence rehearsal notes are omitted.

## Failure analysis — Manasa (#22)

- [Analysis notebook](failure_analysis/malaria_m5_failure_analysis.ipynb)
- [Failure-analysis write-up](failure_analysis/artifacts/failure_analysis.md)
- [Paired predictions](failure_analysis/artifacts/paired_predictions.csv)
- [Outcome counts](failure_analysis/artifacts/outcome_counts.csv)
- [Paired errors by class](failure_analysis/artifacts/paired_errors_by_class.csv)
- [Visual review and observations](failure_analysis/artifacts/visual_review_examples.csv)
- [Descriptive pattern groups](failure_analysis/artifacts/visual_pattern_groups.csv)
- [Error score summary](failure_analysis/artifacts/error_confidence_summary.csv)
- [Analysis configuration](failure_analysis/artifacts/failure_analysis_config.json)
- [Environment record](failure_analysis/artifacts/analysis_environment.json)
- [Figures](failure_analysis/artifacts/figures/)
- [Artifact checksums](failure_analysis/artifacts/failure_analysis_artifact_manifest.json)

## Findings

The modified run corrected 79 baseline errors and introduced 52 new errors;
123 images were wrong in both runs. Total errors decreased from 202 to 175.
False negatives fell from 117 to 86, while false positives rose from 85 to 89.

| Paired error group | Uninfected | Parasitized | Total |
|---|---:|---:|---:|
| Corrected baseline error | 27 | 52 | 79 |
| New modified-model error | 31 | 21 | 52 |
| Both wrong | 58 | 65 | 123 |

The visual review includes three images per class from each paired-error
group, sampled with seed 42 (18 images). Observations and overlapping pattern
groups describe only those examples and do not establish error causes or
prevalence. The modified model made 59 errors with predicted-class probability
at least 0.90, compared with 80 for the baseline. These scores do not establish
calibrated certainty.

## Verification and layout

All 14 exported artifact sizes and SHA-256 checksums were verified. Input
prediction and split-manifest hashes match the M2/M4 repository artifacts.
Error counts, paired outcomes, high-score counts, and sample selection were
independently checked against the saved predictions. The Colab outputs report
zero image-hash mismatches for the 5,512 test images; images are not stored here.

The notebook has 25 retained executed code cells without saved errors. Their
code and outputs are unchanged. A title and section headings were added;
one identical repeated chart cell and the final empty cell were removed.
Original execution counts were preserved, so the removed duplicate leaves a
gap. No model inference or training was rerun during repository preparation.

Colab reads from the Drive project `malaria_danet/`: baseline inputs are in
`baseline_evaluation/`, M4 predictions in `milestone4/model_evaluation/`, and
the split manifest in `milestone4/data_preparation/`. The notebook exports to
`milestone5/failure_analysis/` in Drive. In this repository, exports are under
`failure_analysis/artifacts/`, with images in `artifacts/figures/`, matching
the previous milestone structure. Manifest filenames are relative to
`artifacts/`.

## Paper and defence handoff

Use the failure-analysis write-up, numerical tables, and figures as evidence
for the final paper and defence. Preserve the distinction between observed
visual features and causal explanations. M2 switched to full precision after
epoch 24 and M4 after epoch 22, which limits attribution solely to ColorJitter.
Patient overlap, one split and seed, the small visual-review sample, and the
absence of external or explicit colour-shift testing remain limitations.
The failure analysis does not establish clinical validity.
