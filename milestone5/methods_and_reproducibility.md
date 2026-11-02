# Methods and Reproducibility

## Data and preprocessing

We classify single red blood cell images as Uninfected (0) or Parasitized (1).
The NIH/NLM dataset contains 27,558 RGB images, with 13,779 in each class.
Both experiments use the same saved image-level split:

| Split | Images |
|---|---:|
| Training | 19,290 |
| Validation | 2,756 |
| Test | 5,512 |

Images are resized to 224 × 224 pixels and converted to tensors with values
from 0 to 1. Baseline training uses random rotation within 15 degrees and
horizontal and vertical flips, each with probability 0.2. Validation and test
images use only resizing and tensor conversion.

## Model and proposed change

We reproduce DANet-S with LogSoftMax from the selected DANet paper by Ali et al.
The model has nine dilated attention blocks. Convolutions with dilation rates
1, 2, and 3 collect features over different areas. Pooling and channel attention
combine and weight these features. The classifier has two outputs and the
model has 2,310,842 trainable parameters.

Our proposed change adds mild ColorJitter after rotation and flips, before
tensor conversion. Its settings are brightness 0.2, contrast 0.2, saturation
0.1, and hue 0.02. It is applied only during training. The architecture and
data split stay the same. The aim is to test whether small colour changes
during training help classification; explicit stain or lighting robustness
was not tested.

## Training and recovery

Both models were trained for 75 epochs. Shared settings are seed 42, batch
size 64, RMSprop, NLLLoss, and OneCycleLR. The M4 model was trained from scratch.
The checkpoint with the lowest validation loss was selected.

| Run | First phase | Full-precision phase | Selected epoch |
|---|---|---|---:|
| M2 baseline | Epochs 1–24, mixed precision, maximum LR 0.001 | Epochs 25–75, maximum LR 0.0005 | 67 |
| M4 modified | Epochs 1–22, mixed precision, maximum LR 0.001 | Epochs 23–75, maximum LR 0.0005 | 62 |

Both runs needed recovery from numerical instability. In M4, epoch 23 produced
a non-finite loss. That incomplete epoch was discarded and epoch 22 was restored.
A fresh RMSprop optimizer and a 53-epoch OneCycleLR schedule were then used
in full precision. After a runtime interruption, M4 resumed from completed
epoch 68 with the saved model, optimizer, scheduler, scaler, and random states.

The recovery schedules differ. We therefore cannot attribute every performance
change solely to ColorJitter.

## Evaluation and reproducibility

Checkpoint selection used validation data. The selected models were evaluated
on the same test images, using float32 inference and no test augmentation.
The class with the larger output was predicted. Parasitized is the positive
class. We report loss, accuracy, precision, recall, specificity, F1-score,
ROC-AUC, average precision, and error counts.

To review or repeat the work, use the saved split and label mapping, recorded
settings, model code, and notebook workflow. Check image and model SHA-256
hashes before evaluation. Training histories, predictions, figures, and
environment records are saved; model checkpoints remain in Drive. The M4
training environment record covers the resumed runtime only. Seeds help
reproducibility but do not guarantee identical results across environments.

Cells from the same mapped patient occur across splits. Together with one
dataset, one split, and one seed, this limits generalization. The results do
not establish clinical validity.

## Supporting files

- [Model code](../src/danet.py)
- [M4 data settings](../milestone4/data_preparation/artifacts/data_config.json)
- [M2 training settings](../milestone2/model_training/artifacts/danet_training_config_final.json)
- [M4 training settings](../milestone4/model_training/artifacts/danet_colorjitter_config_final.json)
- [Evaluation settings](../milestone4/model_evaluation/artifacts/evaluation_config.json)
