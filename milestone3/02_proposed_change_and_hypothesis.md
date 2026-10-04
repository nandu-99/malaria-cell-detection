# Proposed Change and Hypothesis

**Contributor:** Shanker

## Primary Change

We will add mild ColorJitter to the training steps.

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

Adding mild ColorJitter during training will help DANet-S work better when stain strength and microscope lighting change. The model will see more colour conditions while the cell structure and class label stay the same.

## Reasoning

The baseline changes image orientation through rotation and flips. These steps do not represent colour or lighting differences.

ColorJitter makes small changes to brightness, contrast, saturation, and hue. This may stop the model from depending too much on one colour pattern. It may help the model focus more on parasite structure and cell appearance.

The changes are kept small. Strong colour changes could make unrealistic blood-smear images and hide useful parasite features.

## Single-Variable Rule

Only the training augmentation will change. The model, loss function, optimizer, scheduler, split manifest, and test method will stay the same.

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

We must submit this hypothesis and its predicted values before adding ColorJitter or running the new experiment.
