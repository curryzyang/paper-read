# I\textsuperscript{2}RiMA: Spectral Riemannian Representation with Temporal Attention for Mental Stress Detection based on EEG Signals

- 区域：精读区
- 排名：3
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Cheng He, Kunyu Peng, Shangen Han, Jinming Ma, Jinhong Ding, Likun Xia
- 机构：Karlsruhe Institute of Technology, Capital Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.01279v1) · [PDF](https://arxiv.org/pdf/2607.01279v1)

## TLDR
I²RiMA proposes a frequency-aware Riemannian manifold attention network that constructs per-frequency covariance matrices and integrates intra-inter slice temporal attention to capture both local spectral and global temporal EEG features, achieving state-of-the-art cross-subject stress detection performance.

## Abstract
Cross-subject EEG stress detection remains challenging because discriminative stress-related patterns are both subject-dependent and frequency-specific. Conventional Riemannian methods model spatial covariance mainly in the time domain, overlooking neural oscillations that are critical for high-level cognitive state decoding, while standard temporal tokenization often fragments inter-slice temporal coherence. To address these limitations, we propose \method{}, an Intra-Inter Riemannian Manifold Attention Network for EEG-based stress detection. \method{} constructs spatial covariance matrices independently at each frequency point and maps them to the SPD tangent space, preserving channel-wise geometry together with frequency-specific discriminative cues. It further introduces frequency cluster aggregation to select informative spectral components and reduce redundancy by forming compact, data-driven frequency clusters aligned with EEG rhythms. Finally, an intra-inter slice attention module adaptively integrates local slice-level spectral dynamics and global temporal context across EEG sequences. Experiments on three datasets show that \method{} consistently outperforms five state-of-the-art baselines, achieving up to 82.78\% balanced accuracy while remaining efficient with only 1.60M parameters and 31.95M FLOPs.
