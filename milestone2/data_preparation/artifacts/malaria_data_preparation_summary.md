# Dataset Preparation Summary

- Dataset: NIH/NLM Malaria Cell Images
- Task: Binary classification of parasitized and uninfected cells
- Total images: 27,558
- Parasitized images: 13,779
- Uninfected images: 13,779
- Unreadable images: 0
- Exact duplicate groups: 0
- Original image sizes: variable
- Model input size: 224 × 224 RGB
- Pixel scaling: [0, 255] to [0, 1]
- Label mapping: Uninfected = 0, Parasitized = 1
- Split: 70% train, 10% validation, 20% test
- Training images: 19,290
- Validation images: 2,756
- Test images: 5,512
- Split seed: 42
- Batch size: 64
- Training augmentation: rotation ±15°, horizontal flip p=0.20,
  vertical flip p=0.20
- Validation/test augmentation: none
- Official patient identifiers found: 201

## Important limitation

The paper-matched split is performed at image level. All 201 patient
identifiers occur in the training, validation, and test subsets. This creates
patient overlap and may produce optimistic evaluation results. The split is
retained for faithful reproduction of the selected DANet paper and must be
reported as a limitation.
