# Final Report and Failure Analysis

This directory contains the final IEEE-format paper, methods documentation,
and prediction failure analysis for the DANet-S baseline and ColorJitter
experiment.

## IEEE paper

[Read the final IEEE-format paper](paper/malaria_danet_colorjitter_ieee.pdf).

The four-page paper covers the problem, related work, reproduced baseline,
recorded hypothesis, ColorJitter settings, actual training and recovery,
evaluation, failure analysis, and limitations. It includes a workflow diagram,
comparison tables, ROC and precision–recall curves, confusion matrices,
metric changes, and sampled failure images.

The compiled PDF is included in this repository. LaTeX source files and
presentation materials are not included in this checkout.

## Methods and reproducibility

[Methods and reproducibility](methods_and_reproducibility.md) describes the
dataset split, preprocessing, DANet-S architecture, augmentation, training
settings, checkpoint selection, recovery, and evaluation procedure.

The baseline and modified runs share the image split and network architecture,
but their numerical recovery schedules differ. The baseline switched to full
precision after epoch 24; the modified run switched after epoch 22. The report
therefore compares two completed runs without isolating the ColorJitter effect.

## Failure analysis

The analysis aligns saved baseline and modified-model predictions on the same
5,512 test images. It checks labels against the shared manifest and reuses
existing predictions, with no model inference or retraining.

| Outcome | Images |
|---|---:|
| Both models correct | 5,258 |
| Baseline error corrected by the modified model | 79 |
| New error in the modified model | 52 |
| Both models wrong | 123 |

Total errors decreased from 202 to 175. The changes by true class explain
both the gain in recall and the small decrease in precision:

| Error group | Uninfected | Parasitized | Total |
|---|---:|---:|---:|
| Corrected baseline error | 27 | 52 | 79 |
| New modified-model error | 31 | 21 | 52 |
| Shared error | 58 | 65 | 123 |

False negatives fell from 117 to 86 because 52 were corrected and 21 new
ones appeared. False positives rose from 85 to 89 because 27 were corrected
and 31 new ones appeared.

### Visual review and prediction scores

The visual review contains 18 examples: three images per true class from
each of the corrected, new-error, and shared-error groups, sampled with seed
42. Observations include purple regions, uneven colour, and irregular outlines.
Similar features occur across outcome groups, so these observations do not
establish why the models made particular decisions or whether labels are wrong.

The baseline made 80 errors with predicted-class probability at least 0.90;
the modified model made 59. These counts describe scores on errors and do not
establish calibration or certainty.

### Notebook and supporting files

| File | Purpose |
|---|---|
| [Executed notebook](failure_analysis/malaria_m5_failure_analysis.ipynb) | Paired comparison, sampling, plots, and saved outputs |
| [Failure-analysis write-up](failure_analysis/artifacts/failure_analysis.md) | Findings and interpretation |
| [Paired predictions](failure_analysis/artifacts/paired_predictions.csv) | Aligned per-image results from both models |
| [Outcome counts](failure_analysis/artifacts/outcome_counts.csv) | Confusion-matrix counts for each model |
| [Paired errors by class](failure_analysis/artifacts/paired_errors_by_class.csv) | Corrected, new, and shared errors by true class |
| [Visual review](failure_analysis/artifacts/visual_review_examples.csv) | Sample identifiers and per-image observations |
| [Visual pattern groups](failure_analysis/artifacts/visual_pattern_groups.csv) | Descriptive groups across sampled images |
| [Error-score summary](failure_analysis/artifacts/error_confidence_summary.csv) | Scores and high-score counts on incorrect predictions |
| [Analysis settings](failure_analysis/artifacts/failure_analysis_config.json) | Input hashes, sampling method, and analysis scope |
| [Environment record](failure_analysis/artifacts/analysis_environment.json) | Software versions used for analysis |
| [Figures](failure_analysis/artifacts/figures/) | Paired error chart, example panels, and score distributions |
| [Artifact manifest](failure_analysis/artifacts/failure_analysis_artifact_manifest.json) | Recorded file sizes and SHA-256 checksums |

## Reviewing or repeating the analysis

Start with the paper and failure-analysis write-up. The notebook contains
saved outputs so that the analysis can be reviewed without rerunning it.

For execution in Colab, provide the baseline predictions, modified-model
predictions, shared split manifest, and cell images. The notebook reads from
the Drive project `MyDrive/malaria_danet/`: baseline inputs are under
`baseline_evaluation/`, modified predictions under
`milestone4/model_evaluation/`, and the manifest under
`milestone4/data_preparation/`. Adjust paths if your Drive layout differs.

The notebook verifies test-image contents before visual review. It exports
to `milestone5/failure_analysis/` in Drive; this repository stores the outputs
under `failure_analysis/artifacts/`. Artifact-manifest paths are relative to
that directory. The image dataset is not included in Git.

## Interpretation and future work

The modified run improves accuracy, recall, and F1-score on the fixed test
split while introducing some new mistakes. Its 96.83% accuracy and 96.88%
recall should be read alongside the training-schedule difference, patient
overlap across partitions, and use of one dataset, split, and seed.

The 18-image review is descriptive and lacks expert annotation. External
validation, explicit colour-shift testing, statistical significance, and
clinical validity have not been established.

Future work includes matched training schedules, multiple seeds,
patient-independent splits, predefined colour shifts, external datasets,
and expert review of ambiguous examples. These are proposed studies rather
than completed experiments.
