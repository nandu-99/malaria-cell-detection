# Malaria Cell Detection

Computer vision research-reproduction project for classifying segmented red
blood cells as parasitized or uninfected using the NIH/NLM Malaria Cell Images
dataset.

## Team

| Member | Responsibility |
|---|---|
| Manasa | Dataset preparation and PyTorch data pipeline |
| Shanker | DANet model implementation and training |
| Vivekananda | Repository structure, base-paper revision, and contribution documentation |

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
|   `-- README.md
`-- src/
    `-- README.md
```

Each member will add their assigned implementation, notebooks, and artifacts
through their own issue, branch, commits, and pull request. Manasa will add the
Member 1 dataset preparation work separately.

## Milestone status

| Milestone | Status |
|---|---|
| Milestone 1: literature review and initial paper selection | Completed |
| Base-paper revision after evaluator feedback | Documented |
| Milestone 2: dataset preparation, model training, and evaluation | In progress |
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
