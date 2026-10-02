# Base Paper Revision After Milestone 1

## Revision status

The base paper was changed after the Milestone 1 evaluation. The evaluator recommended selecting a more recent method that goes beyond a basic convolutional neural network while remaining practical with the available computing resources.

## Original selection

- **Paper:** Rajaraman et al., *Pre-trained convolutional neural networks as feature extractors toward improved malaria parasite detection in thin blood smear images*
- **Year:** 2018
- **Primary approach:** Transfer learning with pretrained convolutional neural networks, including ResNet-50

This paper supported the initial literature review and Milestone 1 presentation. It is retained in the repository as part of the project history.

## Revised selection

- **Paper:** Ali et al., *DANet: A lightweight dilated attention network for malaria parasite detection*
- **Year:** 2025
- **Publication:** Scientific Reports
- **DOI:** https://doi.org/10.1038/s41598-025-20402-1
- **Official implementation:** https://github.com/asfakali/DANet
- **Selected model:** DANet-S with LogSoftMax output

DANet-S was selected because it is recent, lightweight, and more technically substantial than a basic convolutional network. Its architecture combines depthwise separable convolution, asymmetric convolution, and attention while keeping the implementation and training requirements manageable.

## Comparison of the selections

| Criterion | Original paper | Revised paper |
|---|---|---|
| Publication year | 2018 | 2025 |
| Main method | Transfer learning with pretrained CNNs | Purpose-built lightweight DANet architecture |
| Project baseline | ResNet-50 | DANet-S with LogSoftMax |
| Architectural focus | Feature extraction and fine-tuning | Depthwise separable convolution, asymmetric convolution, and attention |
| Reason for revision | Initial literature review choice | Updated in response to Milestone 1 feedback |

## Reproduction protocol

The project will use the following shared protocol so that all member contributions remain compatible:

| Setting | Project choice |
|---|---|
| Dataset | NIH malaria cell images |
| Total images | 27,558 |
| Classes | Parasitized and Uninfected |
| Input size | 224 x 224 pixels |
| Data split | 70% training, 10% validation, 20% testing |
| Batch size | 64 |
| Training augmentation | Random rotation up to 15 degrees, horizontal flip with probability 0.20, vertical flip with probability 0.20 |
| Evaluation preprocessing | Resize and tensor conversion only |
| Model | DANet-S with LogSoftMax output |
| Optimizer | RMSprop |
| Loss | Negative log-likelihood loss |
| Scheduler | OneCycleLR |
| Maximum epochs | 75 |
| Reproducibility seed | 42 |
| Main metrics | Accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC |

The saved split manifest is the common source for assigning images to the training, validation, and test sets. All members should use this manifest when working with the dataset.

## Reproducibility checklist

- Record the package versions and hardware used for each completed experiment.
- Use the shared split manifest and label mapping.
- Set the shared random seed before data loading and model training.
- Save the best checkpoint based on validation performance.
- Report final metrics only on the held-out test split.
- Add experiment artifacts through the branch and pull request of the member who produced them.
- Do not add the image dataset or large model checkpoints to the repository.

## Known ambiguities and limitations

The paper and its official implementation contain different learning-rate references. The article text reports 0.001, a configuration table reports 0.01, and repository examples use 0.001. The project will begin with 0.001 and record any justified changes in the reproduction report.

The current manifest uses a stratified image-level split. Since cells from the same patient may appear in more than one split, reported results may be optimistic compared with a patient-level split. This limitation must be stated when presenting the evaluation.

The official mapping used during dataset preparation identifies 201 patients overall and 151 patients with parasitized images. Some common descriptions of the dataset report 200 patients overall and 150 infected patients. The project will report the values obtained from the downloaded mapping files and preserve those files as the source of record.

The study uses a single public dataset. Performance on images from other laboratories, microscopes, staining processes, or populations is therefore not established. The results are for academic evaluation and do not support clinical deployment claims.

## Effect on later milestones

- **Milestone 2:** Prepare the reproducible data pipeline, implement DANet-S, train the model, and record experiments using the shared protocol.
- **Milestone 3:** Evaluate the selected model, analyse errors, compare reproduced results with the paper, document limitations, and prepare the final presentation and report.
