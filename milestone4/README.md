# Milestone 4

Milestone 4 implements and evaluates the mild ColorJitter experiment proposed
in Milestone 3. Data preparation and the 75-epoch modified-model training run
are complete. Final test evaluation and the baseline comparison are pending.

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

## Experiment protocol and evaluation handoff

Use the M4 configuration and unchanged split manifest. Reconstruct the training
transform with the recorded ColorJitter parameters and use evaluation
preprocessing for validation and test data. Reset seeds and recreate loaders
before training because the preparation notebook inspected one training batch.

Record the training schedule and any differences from the recovered M2 training
run when interpreting the baseline comparison. The image-level split retains
patient overlap; this experiment does not establish clinical validity.

M2 switched to full precision after epoch 24, whereas M4 switched after epoch
22. This difference limits attribution of performance changes solely to
ColorJitter. Evaluate the selected epoch 62 checkpoint on the fixed test split
in the evaluation notebook; the training notebook reports validation results.
