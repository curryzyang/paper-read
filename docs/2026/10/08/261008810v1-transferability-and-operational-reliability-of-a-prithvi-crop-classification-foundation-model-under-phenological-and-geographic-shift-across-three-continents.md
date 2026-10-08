# Transferability and operational reliability of a Prithvi crop classification foundation model under phenological and geographic shift across three continents

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Venkatesh Kolluru, Rajat Shinde, Abdelhak Marouane, Caden Helbling, Deepak Shah, Othneil Drew, Srinivas Kolluru, Iksha Gurung, Manil Maskey, Rahul Ramachandran
- 机构：University of Alabama in Huntsville, Space and Earth Science Data Analysis, NASA Marshall Space Flight Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08810v1) · [PDF](https://arxiv.org/pdf/2610.08810v1)

## TLDR
A fine-tuned Prithvi crop classification foundation model transfers usefully across continents only when observation windows match local crop phenology, since geographic/phenological misalignment causes large accuracy drops and confidently mislabeled pixels that can be partly recovered by coarsening classes or adjusting the temporal window.

## Abstract
Fine-tuned geospatial foundation models (GeoFMs) pretrained on large satellite archives have been shown to improve crop classification accuracy and geographic transferability. However, their operational performance beyond the training distribution remains poorly characterized. We evaluated the out-of-distribution performance of a widely adopted GeoFM [Prithvi-EO-2.0] across 37 events in 12 countries on three continents and validated against regional reference products. Results indicated that the mean overall accuracy (OA) declined from 0.65 in the United States to 0.40 in Europe. Beyond accuracy metrics, we assessed five key aspects of model performance: whether model confidence indicates signal failure, sensitivity to observation windows, the effect of coarsening class schemes, and robustness to both band loss and cloud- and shadow-contamination. Accuracy collapsed when the observation window misaligned with local crop phenology, while deterministic confidence remained high. Expected calibration error increased for seven of eight paired events, and 12-51% of each affected scene was confidently mislabeled at near-zero precision. Monte Carlo dropout entropy registered the shift in all eight, indicating that much of the apparent cross-continent decline reflected phenological misalignment rather than spatial transfer. Two adjustments recovered accuracy without retraining. Consolidating 13 classes into 10, based on the model's dominant confusions, raised the mean OA by 8.4 percentage points. Compressing the window toward near-real-time use preserved accuracy across a 45- to 90-day plateau, peaking near 75 days, though arms tighter than 30 days fell about 0.11 below that plateau. Fine-tuned crop GeoFMs therefore transfer usefully only where observation windows match local growing seasons. We translate these findings into operational guidance for the reliable deployment of the released model.
