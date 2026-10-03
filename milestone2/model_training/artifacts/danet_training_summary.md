# DANet-S Training Summary

## Model and data

- Model: DANet-S
- Classes: Parasitized and Uninfected
- Input size: 224 x 224
- Training images: 19,290
- Validation images: 2,756
- Test images reserved for later evaluation: 5,512
- Trainable parameters: 2,310,842
- Random seed: 42

## Training configuration

- Optimizer: RMSprop
- Loss: Negative log-likelihood loss
- Scheduler: OneCycleLR
- Batch size: 64
- Completed epochs: 75
- Checkpoint criterion: Lowest validation loss
- Approximate retained training time: 155.0 minutes

## Training recovery

Training initially used mixed precision. Numerical instability occurred during the initial continuation, so the safe Epoch 24 checkpoint was restored. Training resumed from Epoch 25 in full precision with RMSprop reinitialized and a maximum learning rate of 0.0005. The final history contains the retained Epochs 1 through 24 followed by the stable full-precision Epochs 25 through 75.

## Selected checkpoint

- Selected epoch: 67
- Validation loss: 0.095962
- Validation accuracy: 0.966255
- Model file: danet_s_best_final.pth
- Model size: 8.90 MB
- SHA-256: `d08ff52e3c0682fadf0b23b631b916305405e1c9693e2f581dec26b5ba4f0aa1`

## Additional validation result

- Highest validation accuracy: 0.968070
- Highest-accuracy epoch: 72

## Final epoch

- Training loss: 0.083671
- Training accuracy: 0.969155
- Validation loss: 0.097548
- Validation accuracy: 0.967344

## Implementation note

The official public DANet-S implementation hardcodes more than two classifier outputs even though the malaria dataset is binary. This implementation uses two LogSoftMax outputs matching the saved class mapping.

## Evaluation boundary

The test split was not used during model development, training, checkpoint selection, or this validation summary. Final test evaluation is reserved for the evaluation stage.

The manifest uses an image-level split. Images from the same mapped patient may occur across training, validation, and test sets, which must be stated when interpreting the final results.
