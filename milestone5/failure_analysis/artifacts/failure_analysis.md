# Milestone 5: Prediction Failure Analysis

## Scope
This analysis compares saved M2 baseline and M4 modified-model predictions
on the same 5,512 test images. Paths and labels were aligned, and all test
image hashes matched the shared manifest. No inference or retraining was performed.

## Error changes
The baseline made 202 errors; the modified model made 175.
The modified model corrected 79 baseline errors but introduced 52 new errors.
Both models misclassified 123 images.

| Error group | Uninfected | Parasitized | Total |
|---|---:|---:|---:|
| Corrected baseline errors | 27 | 52 | 79 |
| New modified-model errors | 31 | 21 | 52 |
| Shared errors | 58 | 65 | 123 |

False negatives decreased from 117 to 86: 52 were corrected and 21 new
false negatives appeared. False positives increased from 85 to 89:
27 were corrected and 31 new false positives appeared.

The aggregate improvement therefore does not mean every prediction improved.

## Visual review
We randomly sampled three images per true class from each of the corrected,
new-error, and shared-error groups, using seed 42: 18 images in total.

Observed patterns included localized purple spots or edge regions, diffuse
or uneven coloration, irregular outlines, and less apparent internal features
in the sampled shared false negatives at the displayed scale.

Similar visual features occurred across different outcome groups. These
observations do not establish which features the models used, why an error
occurred, or whether a dataset label is incorrect. Pattern groups overlap and
do not estimate prevalence across the full error set.

Per-image observations and identifiers are saved in visual_review_examples.csv.
The descriptive groups are saved in visual_pattern_groups.csv.

## Prediction scores on errors
Using a descriptive predicted-class probability threshold of 0.90:
- Baseline: 34 false positives and 46 false negatives scored at least 0.90.
- Modified model: 23 false positives and 36 false negatives scored at least 0.90.

Both models can assign high scores to incorrect predictions. These counts
do not establish calibration or clinical certainty.

## Limitations
- M2 switched to full precision after epoch 24; M4 switched after epoch 22.
  The training-schedule difference limits attribution solely to ColorJitter.
- The image-level split retains patient overlap across partitions.
- Results cover one dataset, one split, and one seed.
- Only 18 stratified random examples were visually reviewed.
- Visual observations lack expert annotation and causal validation.
- No explicit stain-shift, lighting-shift, or external-dataset test was performed.
- Statistical significance and clinical validity have not been established.

## Implications and future work
The modified run reduced missed infected cells on this fixed split, while
introducing additional false positives and retaining shared failures.
Future work should compare models under matched training schedules and
multiple seeds, use patient-independent evaluation, test predefined colour
shifts, and obtain expert review of ambiguous examples.

These are proposed follow-up studies, not completed experiments.
