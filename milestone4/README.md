# Milestone 4

Milestone 4 implements and evaluates the mild ColorJitter experiment proposed
in Milestone 3. Data preparation is complete. Modified-model training and
final evaluation with the baseline comparison are still pending.

## Data preparation — Manasa

- [Executed notebook](data_preparation/malaria_m4_data_preparation.ipynb)
- [Data configuration](data_preparation/artifacts/data_config.json)
- [Split manifest](data_preparation/artifacts/split_manifest.csv)
- [Preparation summary](data_preparation/artifacts/data_preparation_summary.md)
- [Environment versions](data_preparation/artifacts/environment.json)
- [Augmentation comparison](data_preparation/artifacts/figures/colorjitter_comparison.png)
- [Artifact checksums](data_preparation/artifacts/data_artifact_manifest.json)

The notebook contains 21 executed code cells without saved errors. All 27,558
image hashes match the baseline manifest. The saved split manifest is identical
to the Milestone 2 manifest. ColorJitter is applied only to training images;
validation and test preprocessing remain resize and tensor conversion.

## Colab and repository layout

The notebook reads the baseline artifacts from
`/content/drive/MyDrive/malaria_danet/` and writes its outputs to
`milestone4/data_preparation/` within that Drive folder. The repository stores
these exported outputs in `data_preparation/artifacts/`, with the comparison
image in `artifacts/figures/`, following the Milestone 2 layout. Artifact
manifest filenames are relative to the repository's `artifacts/` directory.

The summary was recovered from its saved notebook output because it was absent
from the uploaded files. Its bytes match the original recorded SHA-256 checksum.
The executed notebook is preserved unchanged.

## Training handoff

Use the M4 configuration and unchanged split manifest. Reconstruct the training
transform with the recorded ColorJitter parameters and use evaluation
preprocessing for validation and test data. Reset seeds and recreate loaders
before training because the preparation notebook inspected one training batch.

Record the training schedule and any differences from the recovered M2 training
run when interpreting the baseline comparison. The image-level split retains
patient overlap; this experiment does not establish clinical validity.
