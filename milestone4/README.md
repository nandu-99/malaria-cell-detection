# Milestone 4

Milestone 4 implements and evaluates the mild ColorJitter experiment proposed
in Milestone 3. Data preparation, the 75-epoch modified-model training run,
and final test evaluation with the baseline comparison are complete. The
comparison includes a training-schedule difference, documented below.

## Data preparation — Manasa

- [Executed notebook](data_preparation/malaria_m4_data_preparation.ipynb)
- [Data configuration](data_preparation/artifacts/data_config.json)
- [Split manifest](data_preparation/artifacts/split_manifest.csv)
- [Preparation summary](data_preparation/artifacts/data_preparation_summary.md)
- [Environment versions](data_preparation/artifacts/environment.json)
- [Augmentation comparison](data_preparation/artifacts/figures/colorjitter_comparison.png)
- [Artifact checksums](data_preparation/artifacts/data_artifact_manifest.json)

The notebook contains 21 executed code cells without saved errors. All 27,558
image hashes match the baseline manifest. The saved split manifest is identical
to the Milestone 2 manifest. ColorJitter is applied only to training images;
validation and test preprocessing remain resize and tensor conversion.

## Colab and repository layout

The notebook reads the baseline artifacts from
`/content/drive/MyDrive/malaria_danet/` and writes its outputs to
`milestone4/data_preparation/` within that Drive folder. The repository stores
these exported outputs in `data_preparation/artifacts/`, with the comparison
image in `artifacts/figures/`, following the Milestone 2 layout. Artifact
manifest filenames are relative to the repository's `artifacts/` directory.

The summary was recovered from its saved notebook output because it was absent
from the uploaded files. Its bytes match the original recorded SHA-256 checksum.
The executed notebook is preserved unchanged.

## Model training — Shanker

- [Training notebook](model_training/malaria_m4_danet_training.ipynb)
- [Final configuration](model_training/artifacts/danet_colorjitter_config_final.json)
- [75-epoch history](model_training/artifacts/danet_colorjitter_history.csv)
- [Training summary](model_training/artifacts/danet_colorjitter_training_summary.md)
- [Resumed runtime environment](model_training/artifacts/training_environment.json)
- [Artifact checksums](model_training/artifacts/training_artifact_manifest.json)
- [Accuracy curves](model_training/artifacts/figures/training_validation_accuracy.png)
- [Loss curves](model_training/artifacts/figures/training_validation_loss.png)
- [Learning-rate schedule](model_training/artifacts/figures/learning_rate_schedule.png)

The selected checkpoint is epoch 62, with validation loss 0.08110992 and
validation accuracy 97.21%. The model checkpoint remains in Drive; its
SHA-256 is recorded in the final configuration. Training recovered from
non-finite loss in epoch 23 by restoring epoch 22 and switching to full
precision, then resumed after a runtime interruption at completed epoch 68.
The retained history contains all 75 epochs.

The notebook is organized as an evaluator copy with numbered sections.
Successful result outputs and all three embedded charts are preserved.
Obsolete recovery commands and error traces were removed; historical epoch
and recovery logs are retained as labeled transcripts. The retained training
invocation is disabled by default. Original execution counts are preserved
because the record spans two runtime sessions. Recovery and the schedule
limitation remain documented. Inspect the saved results without rerunning
training; setup and artifact cells require the original Drive files.

All seven exported training artifacts, including the loss curve, match the
sizes and SHA-256 checksums recorded in the training artifact manifest.

## Evaluation and comparison — Vivekananda

- [Executed evaluation notebook](model_evaluation/malaria_m4_evaluation_ablation.ipynb)
- [Test metrics](model_evaluation/artifacts/test_metrics.json)
- [Test predictions](model_evaluation/artifacts/test_predictions.csv)
- [Baseline comparison](model_evaluation/artifacts/baseline_colorjitter_comparison.csv)
- [M3 success criteria](model_evaluation/artifacts/hypothesis_assessment.json)
- [M3 prediction comparison](model_evaluation/artifacts/m3_prediction_comparison.csv)
- [Paired outcomes](model_evaluation/artifacts/paired_prediction_outcomes.csv)
- [Evaluation summary](model_evaluation/artifacts/evaluation_ablation_summary.md)
- [Evaluation settings](model_evaluation/artifacts/evaluation_config.json)
- [Artifact checksums](model_evaluation/artifacts/evaluation_artifact_manifest.json)
- [Comparison figures and examples](model_evaluation/artifacts/figures/)

| Metric | M2 baseline | M4 modified run |
|---|---:|---:|
| Test accuracy | 96.34% | 96.83% |
| Precision | 96.88% | 96.77% |
| Recall | 95.75% | 96.88% |
| Specificity | 96.92% | 96.77% |
| F1-score | 96.31% | 96.83% |
| ROC-AUC | 0.991887 | 0.994025 |
| False negatives | 117 | 86 |
| False positives | 85 | 89 |

All three operational M3 success criteria were met. Recall exceeded its
predicted range. The modified model corrected 79 baseline errors and introduced
52 errors on images the baseline classified correctly, reducing total errors
from 202 to 175. This is one seed on one fixed split; no explicit lighting or
stain-shift robustness experiment was performed.

The evaluation notebook has 39 executed code cells without saved errors. Its
code, outputs, figures, execution counts, and metadata are preserved; only a
title and section headings were added and the final empty cell removed.
All 16 evaluation artifact sizes and checksums were verified. Reported
classification metrics, ROC-AUC, average precision, and the confusion matrix
were independently recomputed from saved predictions. Baseline input hashes
match the M2 repository artifacts, and test paths and labels match the shared
manifest.

The missing uploaded `prediction_examples.csv` was recovered using the saved
prediction rows and sampling seed 42. Its bytes match the original manifest
checksum. Evaluation artifacts are stored under `model_evaluation/artifacts/`,
with images in `artifacts/figures/`, matching the other milestone components.

## Experiment protocol and interpretation

Use the M4 configuration and unchanged split manifest. Reconstruct the training
transform with the recorded ColorJitter parameters and use evaluation
preprocessing for validation and test data. Reset seeds and recreate loaders
before training because the preparation notebook inspected one training batch.

Record the training schedule and any differences from the recovered M2 training
run when interpreting the baseline comparison. The image-level split retains
patient overlap; this experiment does not establish clinical validity.

M2 switched to full precision after epoch 24, whereas M4 switched after epoch
22. This difference limits attribution of performance changes solely to
ColorJitter. The selected epoch 62 checkpoint was evaluated on the fixed test
split; the training notebook separately reports validation results. The
comparison meets the recorded success criteria but does not isolate the
augmentation effect from the schedule difference. Milestone 5 failure
analysis, final IEEE-format paper, and defence remain separate work.
