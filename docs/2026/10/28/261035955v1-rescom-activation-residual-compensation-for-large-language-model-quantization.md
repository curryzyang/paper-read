# ResCom: Activation Residual Compensation for Large Language Model Quantization

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ning Yang, Bohan Cui, Zhuowen Liu, Yuting Wang
- 机构：Fudan University, The Chinese University of Hong Kong, Chinese Academy of Sciences, University of Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35955v1) · [PDF](https://arxiv.org/pdf/2610.35955v1)

## TLDR
ResCom is a post-calibration low-rank correction that uses activation rounding residuals to compensate for layer-output errors in low-bit LLM quantization, improving accuracy without retraining or modifying calibrated weights.

## Abstract
Low-bit weight--activation quantization reduces the memory and computation needed to deploy large language models, but activation rounding can still degrade accuracy after calibration. Reconstruction from rounded inputs cannot distinguish activations within the same quantization bin. We propose ResCom, a low-rank correction that uses the activation rounding residual to compensate for the resulting layer-output error. An output-aware calibration procedure selects residual directions by their contribution to output reconstruction and computes the correction in closed form, without gradient training or updates to the calibrated weights. On Llama-3-8B with 4-bit weights and activations, rank-32 attention corrections reduce WikiText-2 perplexity from 7.708 to 7.147, improve MMLU by 2.89 percentage points, and raise five-shot GSM8K accuracy from 23.96 to 36.16 percent. Evaluations on models from 1B to 70B parameters and on held-out C4 test the method beyond this setting. The evaluated FP32 implementation adds 2.25 percent to 4K prefill time; a separate compact-storage implementation retains a 27.7 percent peak-memory reduction relative to FP16.
