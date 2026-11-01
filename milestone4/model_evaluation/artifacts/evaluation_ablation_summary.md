# Milestone 4: Evaluation and Ablation

## Evaluation setup
- Model: DANet-S with mild training-only ColorJitter
- Selected checkpoint: epoch 62, by validation loss
- Test images: 5,512
- Split, image contents, and labels verified against the baseline
- Test preprocessing: resize and tensor conversion only
- Inference: float32, no mixed precision
- Positive class: Parasitized

## Modified-model test results
- Loss: 0.093517
- Accuracy: 96.83%
- Precision: 96.77%
- Recall: 96.88%
- Specificity: 96.77%
- F1-score: 96.83%
- ROC-AUC: 0.994025
- Average precision: 0.994644
- False negatives: 86
- False positives: 89

## Comparison with the reproduced baseline
- Accuracy change: +0.4898 percentage points
- Recall change: +1.1248 percentage points
- F1-score change: +0.5130 percentage points
- False negatives decreased from 117 to 86.
- False positives increased from 85 to 89.
- Total errors decreased from 202 to 175.
- Precision and specificity decreased slightly.

## M3 predictions and success criteria
All three recorded success criteria were met on this fixed test split.
Accuracy and F1-score were within their predicted ranges.
Recall exceeded its predicted range, and ROC-AUC exceeded its predicted minimum.
The precision decrease was within the anticipated 0.5 percentage-point allowance.

## Paired outcomes
- Both models correct: 5258
- Baseline wrong, modified model correct: 79
- Baseline correct, modified model wrong: 52
- Both models wrong: 123

## Interpretation and limitations
The modified run achieved better accuracy, recall, F1-score, ROC-AUC, and
average precision on the same held-out images. These observations meet the
operational M3 success criteria.

The baseline switched to full precision after epoch 24; this experiment switched after epoch 22 due to non-finite loss. Training schedules therefore differ, so performance differences cannot be attributed solely to ColorJitter.
This is therefore a baseline-versus-modified-run comparison with a training
schedule confound, rather than an isolated estimate of the ColorJitter effect.

The image-level split retains patient overlap across partitions.
Results cover one seed and one split; statistical significance and
generalization to other laboratories have not been established.
No explicit lighting/stain-shift robustness test was performed.
The displayed examples are descriptive and do not establish error causes.
These experimental results do not establish clinical validity.

## Checkpoint
- Filename: danet_s_colorjitter_best.pth
- SHA-256: ee7bc1fd413439343fda5a3b8dddad5f0a6bdbe98981488da2c1eb56775f30b3
