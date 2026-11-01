# Milestone 4: DANet-S ColorJitter Training

## Experiment
DANet-S trained from scratch with the mild ColorJitter settings recorded in M3.
The baseline split manifest, label mapping, and evaluation preprocessing were preserved.

## Training
- Completed epochs: 75
- Training images: 19,290
- Validation images: 2,756
- Trainable parameters: 2,310,842
- Batch size: 64
- Random seed: 42
- Optimizer: RMSprop
- Loss: NLLLoss
- Scheduler: OneCycleLR
- Retained epoch time: 287.5 minutes
- Timing excludes the failed attempt and runtime setup.

## Recovery and continuation
Epochs 1-22 used mixed precision with maximum learning rate 0.001.
Epoch 23 encountered non-finite training loss and was discarded.
The saved epoch 22 state was restored, and epochs 23-75 used full precision
with a fresh RMSprop optimizer and 53-epoch OneCycleLR schedule,
with maximum learning rate 0.0005.

After a GPU usage interruption, training resumed from the completed epoch 68
checkpoint with model, optimizer, scheduler, scaler, and random states restored.
The retained history contains exactly epochs 1-75.

## Selected checkpoint
- Selection rule: lowest validation loss
- Selected epoch: 62
- Validation loss: 0.08110992
- Validation accuracy: 0.97206096
- Model file: danet_s_colorjitter_best.pth
- Model size: 8.90 MB
- SHA-256: ee7bc1fd413439343fda5a3b8dddad5f0a6bdbe98981488da2c1eb56775f30b3

## Final epoch
- Training loss: 0.057206
- Training accuracy: 0.979212
- Validation loss: 0.084753
- Validation accuracy: 0.970610

## Limitations and evaluation boundary
The baseline switched to full precision after epoch 24; this experiment switched after epoch 22 due to non-finite loss. Training schedules therefore differ, so performance differences cannot be attributed solely to ColorJitter.
The image-level split retains patient overlap across partitions.
The environment record describes the resumed runtime only.
No test evaluation was performed in this notebook.
Test metrics and the baseline comparison belong to the evaluation notebook.
Keep model checkpoints in Drive; do not commit them to the repository.
