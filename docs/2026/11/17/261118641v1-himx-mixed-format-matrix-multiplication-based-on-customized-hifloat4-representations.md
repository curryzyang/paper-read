# HIMX: mixed-format matrix multiplication based on customized HIFLOAT4 representations

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Zhiyuan Zhang, Yanzhao Li, Hui Dong, Sifan Cheng, Jingwei Zhang
- 机构：Huawei Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18641v1) · [PDF](https://arxiv.org/pdf/2611.18641v1)

## TLDR
HiMX is a mixed-mantissa W4A4 quantization framework that uses HIF4-S1P2 for weights and HIF4-E2M1 for activations, maps the heterogeneous formats to fixed-point integer operands for a shared MAC array, and improves LLM inference accuracy over homogeneous HIF4 quantization.

## Abstract
4-bit weight-activation quantization (W4A4) is an important approach for efficient large language model (LLM) inference. Recent hierarchical formats such as HiFloat4 (HIF4) improve the representational range of 4-bit quantization through multi-level scaling. However, the same local mantissa representation in HIF4 may not be equally suitable for weights and activations, which exhibit distinct distribution characteristics. To address this limitation, we propose HiMX, a mixed-mantissa framework built upon the hierarchical scaling structure of HIF4. Our key observation is that the two HIF4-compatible mantissa representations, S1P2 and E2M1, exhibit complementary quantization behavior: the denser S1P2 format provides higher resolution for concentrated weight distributions, while the wider-spaced E2M1 format provides complementary quantization characteristics for activation tensors. HiMX enables operand-tailored mantissa representations while converting heterogeneous mantissas into fixed-point integer operands with operand-specific widths, allowing different operand formats to share a unified integer multiply-accumulate (MAC) array. Block-level analysis on Qwen3-8B shows that HIF4-S1P2 is better suited for weights while HIF4 E2M1 is better suited for activations, and their mixed-format combination achieves lower output MSE than homogeneous configurations. Across multiple benchmarks, HiMX reduces the average end-to-end accuracy loss from 2.38 to 1.77 points on Qwen3-8B and from 2.23 to 1.85 points on Qwen3-30B-A3B, demonstrating the potential benefit of heterogeneous mantissa representations for W4A4 LLM inference.
