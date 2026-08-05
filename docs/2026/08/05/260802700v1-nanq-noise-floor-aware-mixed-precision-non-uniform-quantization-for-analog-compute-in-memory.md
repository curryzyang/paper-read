# NANQ: Noise-Floor-Aware Mixed-Precision Non-Uniform Quantization for Analog Compute-in-Memory

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yizhe Chen, Wenshuai Yao, Saiya Wang, Yuannuo Feng, Wenbo Qi, Kechao Tang, Ngai Wong, Wenyong Zhou, Wang Kang
- 机构：Peking University, Beihang University, The University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02700v1) · [PDF](https://arxiv.org/pdf/2608.02700v1)

## TLDR
NANQ is a noise-floor-aware, training-free mixed-precision non-uniform quantization framework for analog compute-in-memory that adapts quantization density and layer-wise bit-widths to magnitude-dependent hardware noise, improving accuracy and perplexity over prior CIM quantization methods.

## Abstract
Analog compute-in-memory (CIM) enables energy-efficient neural network inference, but device variation and read noise can severely degrade low-bit quantized models. Existing CIM-oriented quantization methods mainly minimize ideal quantization error, ignoring the hardware noise floor and thus causing inefficient precision allocation. We propose NANQ, a noise-aware mixed-precision non-uniform quantization framework for analog CIM. NANQ models magnitude-dependent weight noise from measured responses of an eFlash CIM array and converts the noise profile into an adaptive quantization density, assigning finer resolution to low-noise regions while avoiding ineffective precision in noise-dominated regions. It further assigns layer-wise bit-widths by identifying each layer's precision saturation point under hardware noise using a unified threshold. On-chip experiments on an eFlash CIM SoC show that, under 2-bit weight-magnitude quantization, NANQ improves vision-model accuracy by 8.05 percentage points and reduces language-model PPL by 54.7% on average over PowerQuant. Mixed-precision NANQ captures most of the gains obtainable from additional quantization resources with only 3.2-3.8 equivalent bits.
