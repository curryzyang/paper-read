# Interaction-Gated Time-Frequency Learning for Parameter-Efficient PPG-Based Heart Rate Estimation

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Anh Khoi Pham, Phat Lam, Thien Truong Nguyen Ly, Lam Pham
- 机构：Austrian Institute of Technology, International University, Vietnam National University HCMC, University of New Brunswick, Ho Chi Minh City University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28693v1) · [PDF](https://arxiv.org/pdf/2610.28693v1)

## TLDR
The paper proposes TF-IG, a lightweight dual-branch time–frequency framework with interaction-gated fusion that combines PPG pulse morphology and spectral periodicity for accurate, parameter-efficient heart rate estimation.

## Abstract
Photoplethysmography (PPG) enables low-cost and non-invasive heart rate (HR) monitoring but remains sensitive to waveform distortion, physiological variability, and measurement interference. Temporal waveform characteristics and frequency-domain periodicity provide complementary information for HR estimation; however, effectively exploring and integrating these representations within a compact model remains challenging. This paper proposes TF-IG, a parameter-efficient interaction-gated time-frequency learning framework for PPG-based HR estimation. TF-IG employs a dual-branch architecture in which a temporal branch captures pulse morphology via dilated depthwise-separable convolutions, while a frequency branch extracts cardiac periodicity information from bounded log-spectrogram representations. To combine the two domains, we introduce an interaction-gated fusion module that explicitly models feature agreement and discrepancy, while also learning feature-wise weights to balance temporal and spectral information. A parameter-shared regression head further maps the temporal, spectral, and fused representations into the final HR prediction space. Experiments on the benchmark BIDMC PPG and Respiration Dataset using a subject-exclusive training, validation, and test protocol show that TF-IG achieves a mean absolute error (MAE) of 1.227 BPM, a root mean square error (RMSE) of 2.060 BPM, a Pearson correlation coefficient of 0.9934, and 92.28 percent of estimates within 3 BPM, while remaining parameter-efficient with only 84.6K parameters. Ablation results further demonstrate the complementary contributions of the temporal and frequency branches, interaction-gated fusion, and shared regression head. These results indicate that explicitly modeling cross-domain interactions provides an effective accuracy-complexity trade-off for lightweight PPG-based HR estimation.
