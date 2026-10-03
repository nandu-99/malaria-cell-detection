# Milestone 2

Milestone 2 contains the complete DANet-S reproduction workflow. The work is
divided into three evaluator-ready components so that dataset preparation,
training, and final evaluation can be reviewed independently.

## Components

| Component | Contributor | Main notebook | Supporting artifacts |
|---|---|---|---|
| Dataset preparation | Manasa | [Data preparation pipeline](data_preparation/malaria_data_preparation_pipeline.ipynb) | [Data artifacts](data_preparation/artifacts/) |
| DANet-S training | Shanker | [Training workflow](model_training/malaria_danet_training_evaluator_ready.ipynb) | [Training artifacts](model_training/artifacts/) |
| Final test evaluation | Vivekananda | [Evaluation workflow](model_evaluation/malaria_danet_final_evaluation_evaluator_ready.ipynb) | [Evaluation artifacts](model_evaluation/artifacts/) |

## Shared protocol

- Dataset: NIH/NLM Malaria Cell Images
- Total images: 27,558
- Split: 70% training, 10% validation, and 20% test
- Input size: 224 x 224
- Selected model: DANet-S with LogSoftMax
- Selected checkpoint: Epoch 67 by lowest validation loss
- Final test images: 5,512
- Final test accuracy: 96.34%
- Final test F1-score: 96.31%
- Final test ROC-AUC: 0.9919

The test split was reserved during model development and used only for the final
evaluation. The manifest follows an image-level split, so mapped patient
identifiers overlap across dataset partitions. See the
[evaluation summary](model_evaluation/artifacts/danet_evaluation_summary.md)
for interpretation and limitations.

## Repository policy

The image dataset, dataset archive, credentials, temporary files, and model
checkpoints are excluded. Small configurations, manifests, histories, tables,
summaries, and figures are retained for reproducibility. Contribution ownership
and issue references are recorded in [CONTRIBUTIONS.md](../CONTRIBUTIONS.md).
