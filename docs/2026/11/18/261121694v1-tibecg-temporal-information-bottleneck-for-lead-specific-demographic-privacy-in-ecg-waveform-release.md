# TIBECG: Temporal Information Bottleneck for Lead-Specific Demographic Privacy in ECG Waveform Release

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Tsai-Min Chen, Jun Seita
- 机构：Academia Sinica, RIKEN
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21694v1) · [PDF](https://arxiv.org/pdf/2611.21694v1)

## TLDR
TIBECG is a lead-specific architectural temporal information bottleneck that releases ECG waveforms with high diagnostic utility for a frozen cloud classifier while reducing age and sex leakage better than conventional transformations, though privacy protection and operating-point selection vary by lead.

## Abstract
Transmitting an electrocardiogram (ECG) waveform can expose demographic information beyond an intended diagnostic task. We evaluate TIBECG, an architectural temporal information bottleneck, on individual leads extracted from hospital twelve-lead recordings. A 2,302,337-parameter processor varies its latent length while retaining the same nine-score consistency objective, without age or sex labels in protector fitting. Across 6,386 recordings, ten folds, 12 leads and 21 lengths, retrospective selections retained at least 95% of each lead's clean macro-F1. Their weaker age/sex interval gain exceeded the best eligible conventional transformation on all leads, by a median 22.08 percentage points. The implemented sampling-rate comparison shows that direct downsampling usually suppresses demographic inference more strongly but at a larger loss of diagnostic utility, whereas TIBECG favors utility preservation. Selection stability also varies by lead. Lower latent Kullback-Leibler (KL) divergence does not reliably rank residual sex leakage at a fixed length. These findings support lead-specific evaluation of waveform processing, not validated consumer deployment or expert-readable reconstruction. When the waveform-input diagnostic classifier is hosted as part of a proprietary cloud service rather than deployed on the device, waveform transmission is required to obtain its scores.
