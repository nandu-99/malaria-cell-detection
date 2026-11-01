# Milestone 4: Data Preparation Summary

## Experiment
DANet-S with mild ColorJitter added only to training images.

## Dataset verification
- Images checked: 27,558
- Missing images: 0
- SHA-256 mismatches against baseline: 0
- Split manifest: exact copy of the baseline manifest
- Class mapping: Uninfected = 0, Parasitized = 1

## Shared settings
- Training images: 19,290
- Validation images: 2,756
- Reserved test images: 5,512
- Input size: (224, 224)
- Batch size: 64
- Data-loader workers: 0
- Random seed: 42

## Training augmentation
Resize, rotation within 15 degrees, horizontal flip (0.2),
vertical flip (0.2), ColorJitter, and tensor conversion.

ColorJitter: brightness=0.2, contrast=0.2, saturation=0.1, hue=0.02.

## Evaluation preprocessing
Resize and tensor conversion only. No ColorJitter.

## Training handoff
Reconstruct transforms using the saved configuration, including ColorJitter.
Reset random seeds and recreate data loaders before training:
the batch check has advanced the current random states.

## Limitations
The baseline image-level split retains patient overlap across partitions.
This notebook verifies data preparation; it does not establish improvement.
