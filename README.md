# Malaria Cell Detection

Computer vision research-reproduction project for classifying segmented red
blood cells as parasitized or uninfected using the NIH/NLM Malaria Cell Images
dataset.

## Team

| Member | Responsibility |
|---|---|
| Manasa | Dataset preparation and PyTorch data pipeline |
| Shanker | DANet model implementation and training |
| Vivekananda | Repository structure, base-paper revision, final evaluation, and documentation |

## Base paper

The original Milestone 1 submission selected Rajaraman et al. (2018) and a
ResNet50 feature-extraction baseline. Following evaluator feedback, the team
changed the reproduction target to:

> A. Ali et al., "DANet: A lightweight dilated attention network for malaria
> parasite detection," *Scientific Reports*, vol. 15, 36689, 2025.

- Paper: <https://doi.org/10.1038/s41598-025-20402-1>
- Official implementation: <https://github.com/asfakali/DANet>
- Selected baseline: DANet-S with LogSoftMax

The reason for this change and the updated reproducibility checklist are
recorded in [Base Paper Revision After Milestone 1](docs/base_paper_revision_after_m1.md).

## Dataset

The project uses the public NIH/NLM Malaria Cell Images dataset:

- 27,558 segmented RGB cell images
- 13,779 parasitized images
- 13,779 uninfected images
- Binary classification task

Dataset page: <https://lhncbc.nlm.nih.gov/LHC-research/LHC-projects/image-processing/malaria-datasheet.html>

The dataset is downloaded separately and is not stored in this repository.

## Repository structure

```text
malaria-cell-detection/
|-- README.md
|-- CONTRIBUTING.md
|-- CONTRIBUTIONS.md
|-- docs/
|   `-- base_paper_revision_after_m1.md
|-- milestone1/
|   |-- milestone1.pdf
|   `-- malaria_literature_review.pdf
|-- milestone2/
|   |-- README.md
|   |-- data_preparation/
|   |   |-- malaria_data_preparation_pipeline.ipynb
|   |   `-- artifacts/
|   |-- model_training/
|   |   |-- malaria_danet_training_evaluator_ready.ipynb
|   |   `-- artifacts/
|   `-- model_evaluation/
|       |-- malaria_danet_final_evaluation_evaluator_ready.ipynb
|       `-- artifacts/
`-- src/
    |-- README.md
    `-- danet.py
```

The Milestone 2 directory separates dataset preparation, model training, and
final evaluation. Each workflow contains an evaluator-ready notebook and its
supporting reproducibility artifacts.

## Reproduced results

The selected Epoch 67 checkpoint was evaluated once on the reserved test split
of 5,512 images.

| Metric | Result |
|---|---:|
| Test loss | 0.110878 |
| Accuracy | 96.34% |
| Precision | 96.88% |
| Recall or sensitivity | 95.75% |
| Specificity | 96.92% |
| F1-score | 96.31% |
| ROC-AUC | 0.9919 |
| Average precision | 0.9926 |

The base paper reports 97.95% accuracy for DANet-S with LogSoftMax. The
reproduction is 1.61 percentage points lower. Detailed results, figures, error
analysis, and the comparison table are available in
[Milestone 2 model evaluation](milestone2/model_evaluation/).

The selected model checkpoint is stored externally because model checkpoints
are excluded from the repository. Its SHA-256 checksum is recorded in the
evaluation configuration and training summary.

## Milestone status

| Milestone | Status |
|---|---|
| Milestone 1: literature review and initial paper selection | Completed |
| Base-paper revision after evaluator feedback | Documented |
| Milestone 2: dataset preparation, model training, and evaluation | Completed |
| Milestone 3: hypothesis, prediction, and introduction | Not started |

## Contribution workflow

All contributors must work from an issue, use the branch naming convention,
write meaningful commit messages, and request review before integration. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the complete conventions.

## Project constraints

- Do not commit the image dataset or dataset archives.
- Do not commit credentials, access tokens, or environment files.
- Do not commit large model checkpoints directly.
- Report sensitivity or recall and AUC in addition to accuracy.
- Clearly document patient overlap and other evaluation limitations.
- Do not make clinical claims from the experimental results.

## Evaluation limitation

The project follows the base paper's stratified image-level split. Images from
the same mapped patient may occur across training, validation, and test sets.
This overlap can make the reported image-level performance more optimistic than
a patient-independent evaluation. The results are experimental and do not
establish clinical validity.
