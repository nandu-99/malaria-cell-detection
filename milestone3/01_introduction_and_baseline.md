# Introduction and Baseline

**Contributor:** Manasa

## Problem

Malaria parasites infect red blood cells. Trained experts often check stained blood-smear images under a microscope. This work takes time and needs careful attention. A computer vision model can support research by classifying cells as parasitized or uninfected.

This project studies image classification on one public dataset. It does not make clinical claims.

## Dataset

We use the NIH/NLM Malaria Cell Images dataset. It contains 27,558 segmented RGB cell images:

- 13,779 parasitized images
- 13,779 uninfected images

The saved manifest uses the same split ratios as the base paper:

- Training: 19,290 images, or 70%
- Validation: 2,756 images, or 10%
- Test: 5,512 images, or 20%

Images are resized to 224 x 224 pixels. Training images use rotation and horizontal and vertical flips. Evaluation images use only resizing and tensor conversion.

## Base Paper and Model

Our base paper is *DANet: A Lightweight Dilated Attention Network for Malaria Parasite Detection* by Ali et al. We use DANet-S with LogSoftMax output.

DANet-S uses dilated attention blocks to learn small parasite features and wider cell patterns. Our binary model has 2,310,842 trainable parameters.

## Reproduced Baseline

We trained the model for 75 epochs. We selected the Epoch 67 checkpoint because it had the lowest validation loss.

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

The model made 117 false-negative errors and 85 false-positive errors on the test set. The base paper reports 97.95% accuracy. Our result is 1.61 percentage points lower.

## Motivation for the Proposed Change

Blood-smear images can differ in brightness, contrast, stain strength, and colour. The current training steps rotate and flip images, but they do not add colour changes.

We propose adding mild ColorJitter during training. It may help the model learn useful features when stain strength and microscope lighting change.

## References

1. Ali, A., Pal, R., Dey, I., et al. *DANet: A lightweight dilated attention network for malaria parasite detection*. Scientific Reports, 2025. <https://doi.org/10.1038/s41598-025-20402-1>
2. NIH/NLM Malaria Cell Images dataset. <https://lhncbc.nlm.nih.gov/LHC-research/LHC-projects/image-processing/malaria-datasheet.html>
