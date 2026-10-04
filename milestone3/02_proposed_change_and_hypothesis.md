# Proposed Change and Hypothesis

**Contributor:** Shanker

## Primary Change

The proposed change is to add mild ColorJitter augmentation to the training pipeline.

The baseline training pipeline uses:

- Resize to 224 x 224
- Random rotation within 15 degrees
- Horizontal flip with probability 0.2
- Vertical flip with probability 0.2
- Tensor conversion

The modified pipeline will add:

```python
transforms.ColorJitter(
    brightness=0.2,
    contrast=0.2,
    saturation=0.1,
    hue=0.02,
)
```

ColorJitter will be applied only to training images. Validation and test images will not use ColorJitter.

## Formal Hypothesis

Adding mild ColorJitter augmentation during training will improve DANet-S generalization to realistic changes in stain intensity and microscope illumination. The model will see a wider range of colour conditions while keeping the cell structure and class label unchanged.

## Reasoning

The baseline already changes image orientation through rotation and flips. These operations do not represent colour or illumination differences.

ColorJitter changes brightness, contrast, saturation, and hue within small limits. This may reduce dependence on one narrow colour pattern and encourage the model to focus on parasite structure and cell appearance.

The augmentation values are intentionally mild. Strong colour changes could create unrealistic blood-smear images and damage useful parasite features.

## Single-Variable Rule

Only the training augmentation will change. The experiment will not change the model architecture, loss function, optimizer, scheduler, split manifest, or evaluation method.

This makes the comparison clear:

| Configuration | Training augmentation |
|---|---|
| Baseline | Rotation and flips |
| Modified | Rotation, flips, and ColorJitter |

## Settings That Remain Fixed

- Model: DANet-S with two LogSoftMax outputs
- Input size: 224 x 224
- Split manifest: unchanged
- Random seed: 42
- Batch size: 64
- Optimizer: RMSprop
- Loss: NLLLoss
- Scheduler: OneCycleLR
- Maximum epochs: 75
- Checkpoint rule: lowest validation loss
- Test evaluation method: unchanged

## Condition Before Implementation

This hypothesis and its numerical predictions must be submitted before ColorJitter is added to the training code or any modified experiment is run.
