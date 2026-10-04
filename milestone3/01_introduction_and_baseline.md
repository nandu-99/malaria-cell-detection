# Introduction and Baseline

**Contributor:** Manasa

## Problem

Malaria is caused by parasites that infect red blood cells. Microscopy is commonly used to inspect blood-smear images, but manual inspection takes time and depends on trained experts. An automated image classifier can support research by separating parasitized cells from uninfected cells.

This project does not make clinical claims. It studies image classification performance on one public dataset.

## Dataset

The project uses the NIH/NLM Malaria Cell Images dataset. It contains 27,558 segmented RGB cell images:

- 13,779 parasitized images
- 13,779 uninfected images

The saved manifest uses the same split ratios as the base paper:

- Training: 19,290 images, or 70%
- Validation: 2,756 images, or 10%
- Test: 5,512 images, or 20%

Images are resized to 224 x 224 pixels. Training images use rotation and horizontal and vertical flips. Evaluation images use only resizing and tensor conversion.

## Base Paper and Model

The selected base paper is *DANet: A Lightweight Dilated Attention Network for Malaria Parasite Detection* by Ali et al. The selected model is DANet-S with LogSoftMax output.

DANet-S uses dilated attention blocks to capture features at different spatial scales. The reproduced binary model has 2,310,842 trainable parameters.

## Reproduced Baseline

The model was trained for 75 epochs. The checkpoint with the lowest validation loss was selected at Epoch 67.

| Metric | Reproduced result |
|---|---:|
| Test loss | 0.110878 |
| Accuracy | 96.34% |
| Precision | 96.88% |
| Recall or sensitivity | 95.75% |
| Specificity | 96.92% |
| F1-score | 96.31% |
| ROC-AUC | 0.9919 |
| Average precision | 0.9926 |

The test set produced 117 false negatives and 85 false positives. The base paper reports 97.95% accuracy. The reproduction is 1.61 percentage points lower.

## Motivation for the Proposed Change

Blood-smear images can differ in brightness, contrast, stain intensity, and colour. The current training pipeline uses geometric augmentation but does not add colour variation.

The proposed change is mild ColorJitter augmentation during training. This change may help the model learn features that remain useful when staining and illumination vary.

## References

1. Ali, A., Pal, R., Dey, I., et al. *DANet: A lightweight dilated attention network for malaria parasite detection*. Scientific Reports, 2025. <https://doi.org/10.1038/s41598-025-20402-1>
2. NIH/NLM Malaria Cell Images dataset. <https://lhncbc.nlm.nih.gov/LHC-research/LHC-projects/image-processing/malaria-datasheet.html>
