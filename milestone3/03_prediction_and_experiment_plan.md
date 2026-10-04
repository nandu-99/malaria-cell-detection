# Prediction and Experiment Plan

**Contributor:** Vivekananda

## Baseline Evidence

| Metric | Baseline value |
|---|---:|
| Accuracy | 96.34% |
| Precision | 96.88% |
| Recall or sensitivity | 95.75% |
| Specificity | 96.92% |
| F1-score | 96.31% |
| ROC-AUC | 0.9919 |
| False negatives | 117 |
| False positives | 85 |

Recall is lower than specificity, and the model makes more false negatives than false positives. We expect the proposed change to improve performance under colour changes without changing the model.

## Predictions

| Metric | Baseline | Predicted result | Expected change |
|---|---:|---:|---:|
| Accuracy | 96.34% | 96.54% to 97.14% | +0.2 to +0.8 percentage points |
| Recall | 95.75% | 96.05% to 96.75% | +0.3 to +1.0 percentage point |
| F1-score | 96.31% | 96.51% to 97.11% | +0.2 to +0.8 percentage points |
| ROC-AUC | 0.9919 | 0.9919 or higher | Stable or slightly higher |

Precision may decrease by up to 0.5 percentage points if the colour changes cause more uninfected cells to be predicted as parasitized.

## Controlled Experiment

Two configurations will be compared:

1. Baseline DANet-S with rotation and flips.
2. Modified DANet-S with the same pipeline plus mild ColorJitter.

Both versions will use the same split manifest, seed, model, optimizer, loss, scheduler, batch size, epoch limit, and checkpoint rule.

## Experiment Sequence

1. Submit this hypothesis and prediction before coding.
2. Add ColorJitter only to the training transform.
3. Train the modified model using the same settings.
4. Select the checkpoint with the lowest validation loss.
5. Compare validation curves and checkpoint metrics.
6. Evaluate the final modified checkpoint once on the fixed test split.
7. Compare the modified results with the saved baseline.

## Evaluation Metrics

The comparison will report:

- Test loss
- Accuracy
- Precision
- Recall or sensitivity
- Specificity
- F1-score
- ROC-AUC
- Average precision
- Confusion matrix
- False negatives and false positives

## Success Criteria

Recall is the main success metric because the baseline has more false negatives than false positives.

The result supports the hypothesis if:

- Recall increases by at least 0.3 percentage points.
- F1-score does not decrease.
- Accuracy remains within 0.5 percentage points of the baseline or improves.

The result does not support the hypothesis if recall does not improve or if precision, F1-score, or accuracy falls too much.

## Limitations

- The dataset uses an image-level split.
- Images from the same mapped patient can occur in training, validation, and test sets.
- The study uses one public dataset and one fixed split.
- The result may not generalize to other laboratories, microscopes, staining methods, or populations.
- The experiment does not establish clinical validity.
- No clinical claims will be made.

## Expected Milestone 4 Output

Milestone 4 will report the new results and compare them with these predictions. The prediction may be wrong. We will explain why the actual result matched or differed from it.
