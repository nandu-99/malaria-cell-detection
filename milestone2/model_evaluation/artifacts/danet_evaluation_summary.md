# DANet-S Final Test Evaluation

## Evaluation setup

- Dataset: NIH/NLM Malaria Cell Images
- Selected model: DANet-S with LogSoftMax
- Selected checkpoint epoch: 67
- Test images: 5,512
- Uninfected test images: 2,756
- Parasitized test images: 2,756
- Input size: 224 x 224
- Trainable parameters: 2,310,842
- Test split usage: Final evaluation only

## Reproduced test results

- Test loss: 0.110878
- Accuracy: 0.963353 (96.34%)
- Precision: 0.968796 (96.88%)
- Recall or sensitivity: 0.957547 (95.75%)
- Specificity: 0.969158 (96.92%)
- F1-score: 0.963139 (96.31%)
- ROC-AUC: 0.991887
- Average precision: 0.992615

## Confusion matrix

- True negatives: 2,671
- False positives: 85
- False negatives: 117
- True positives: 2,639
- Total incorrect predictions: 202

## Base-paper comparison

The base paper reports 97.95% accuracy, 97.76% precision,
98.07% sensitivity, 97.87% specificity, and 97.86% F1-score
for DANet-S with LogSoftMax.

The reproduction achieved 96.34% accuracy and 96.31% F1-score.
Its accuracy is 1.61
percentage points below the paper, and its F1-score is
1.55 percentage points
below the paper.

Base paper:
https://doi.org/10.1038/s41598-025-20402-1

## Interpretation

The reproduced model maintains balanced performance across both
classes. Specificity is slightly higher than sensitivity, and the
confusion matrix contains more false negatives than false positives.
The ROC-AUC and average precision indicate strong discrimination on
this fixed test split.

Some incorrect examples have high predicted confidence. Therefore,
the output confidence should not be interpreted as calibrated
clinical certainty.

## Limitations

- The manifest follows the base paper's stratified image-level split.
- Images associated with the same mapped patient identifier occur
  across training, validation, and test splits.
- Patient overlap can make image-level results more optimistic than
  results from a patient-independent evaluation.
- The comparison uses one fixed split and does not reproduce the
  paper's complete cross-validation analysis.
- Differences from the paper may result from random split membership,
  implementation details, numerical precision, and the recovered
  training schedule.
- These experimental results do not establish clinical validity and
  must not be used for diagnosis.

## Evaluation boundary

The test split was not used for training or checkpoint selection.
The Epoch 67 checkpoint was selected using
validation loss before this final test evaluation.
