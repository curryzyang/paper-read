# FourierQK: Filter Shape, Admissibility and the Leakage-Coverage Law

- 区域：速读区
- 排名：8
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Athanasios Zeris
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00009v1) · [PDF](https://arxiv.org/pdf/2610.00009v1)

## TLDR
This paper ablates FourierQK’s frequency-collapse attention filters and finds that effective performance requires suppressing DC/Nyquist, using an admissible bandpass filter with σ≈2 centered at paragraph scale, and avoiding broadband leakage—since FFT leakage scales monotonically with spectral coverage, making FourierQK suited to bidirectional attention while autoregressive generation needs a causal variant like MorletQK.

## Abstract
Frequency-collapse attention [Zeris, 2026e] achieves large gains over standard dot-product attention by replacing the Q/K dot product with a bandpass-filtered inner product at a learned frequency. A natural follow-up question is: which filter shape works best, and why? We test five hypotheses about filter properties -- DC suppression, Nyquist suppression, bandwidth, centre frequency, and multi-scale coverage -- using a controlled ablation on character-level language modelling (TinyShakespeare, 6-layer GPT). Our main findings are: (1) DC and Nyquist components are actively harmful (val ~= 2.0, equivalent to phase randomisation), confirming that oscillatory bandpass structure is essential, not just any low-dimensional spectral summary; (2) the optimal single-scale bandwidth is sigma ~= 2 bins centred at paragraph scale (~70 tokens), giving a clean gain of Delta = +1.15 nats over BASE-DOT; (3) admissible filters (zero-mean, Mexican Hat DOG m = 2) outperform non-admissible Gaussians at the same scale and provide partial protection against bilateral FFT leakage; (4) bilateral FFT leakage scales monotonically with spectral coverage -- narrowband filters (gap > +4) are clean, wideband filters (gap < +2) are leaky; and (5) causal time-domain Morlet at character scale cannot beat BASE-DOT (K=128 taps covers 50% of T=256 context), motivating word-level experiments in the companion MorletQK paper [Zeris, 2026f]. Together, findings (1)-(5) characterise FourierQK as effective in bidirectional attention settings (encoder-style, e.g. BERT), where full-sequence context is available at both training and inference time; autoregressive generation requires a causal spectral variant such as MorletQK [Zeris, 2026f] (decoder-style, e.g. GPT). Code available at: https://github.com/AthanasiosZeris/energy-gated-attention
