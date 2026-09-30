# Learned Compression of SAR Phase-History Data: A Rate-Honest Feasibility Study on GOTCHA

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Alizishaan Khatri
- 机构：Wrynx Inc
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35848v1) · [PDF](https://arxiv.org/pdf/2609.35848v1)

## TLDR
This rate-honest GOTCHA feasibility study finds that a small convolutional autoencoder for on-board SAR phase-history compression fails to beat block-adaptive quantization, block KLT, or adaptive FFT thresholding at every rate, while exposing critical evaluation pitfalls and proposing a protocol for learned radar compression.

## Abstract
On-board compression of synthetic aperture radar (SAR) phase history is bandwidth-critical, and block-adaptive quantization (BAQ) remains the operational standard. We test whether a small convolutional autoencoder, with its encoder on the sensor, can compete with BAQ on complex phase-history patches from the AFRL GOTCHA collection. Every method is charged for all transmitted bits, rates are reported in bits per complex sample (b/cs), and detection is scored by one-to-one matching of CA-CFAR detections. The autoencoder (28,656 encoder parameters) loses at every rate. At 16 b/cs it reaches -2.87 dB NMSE, against -35.5 dB for 8-bit BAQ with $\pm 3σ$ clipping and -41.0 dB with a tuned clipping range. It also loses to a $16 \times 16$ block Karhunen-Loève transform (KLT), a local linear coder with a tenth of its encoder cost (-5.39 dB). Running the network in a companded Fourier domain helps, but its detection F1 remains bounded at 33%. The evidence points to this model, its normalization, and its objective, not to a fundamental limit of learned coding. Per patch, the data have modest lag-1 coherence ($|ρ| \approx 0.3$) and patch-specific spectral concentration. Two findings concern evaluation itself. First, 97% of CFAR crossings on raw $64 \times 64$ patches are border artifacts of the zero-padded detector. Second, on interior cells BAQ's clipping range decides detection: 8-bit BAQ keeps 69% F1 with tuned clipping but 17% at $\pm 3σ$, and at 8 b/cs or less adaptive FFT thresholding preserves more detections than BAQ. We close with an evaluation protocol for learned radar compression.
