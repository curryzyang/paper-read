# High-accuracy Low-Bit KV-Cache Quantization via Local Distribution Restoration

- 区域：速读区
- 排名：1
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Gradwell Dzikanyanga, Yanqi Pan, Weihao Yang, Donglei Wu, Wen Xia, Hao Huang
- 机构：Harbin Institute of Technology, Shenzhen
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16248v1) · [PDF](https://arxiv.org/pdf/2607.16248v1)

## TLDR
DGAP restores accuracy under aggressive low-bit KV-cache quantization by detecting and correcting local distribution misranking in the top‑K candidate region, recovering RULER accuracy on Llama‑3.1‑8B from 47.8% to 83.2% without increasing persistent memory footprint.

## Abstract
Long-context large language model inference relies on the KV cache to avoid redundant attention computation, but incurs high memory and bandwidth overheads. Low-bit KV-cache quantization reduces this cost, yet it severely degrade quality; particularly, one-bit quantization reduces accuracy from 84.2% to 47.8% on Llama-3.1-8B under RULER.
  Rather than common beliefs that absolute error of logits, we find that the root cause is structured local misranking, where the distribution of logits in top-K region is drifted. We thereby propose local distribution restoration, a new technique that detects steps with high local distribution risk from quantized-logit features and restores only the selected top-K candidate distribution before token selection. We implement DGAP to achieve local distribution restoration, with efficient risk detcetors and correctors. Expeirments show that on Llama-3.1-8B, DGAP recovers K1V1 RULER accuracy from 47.8% to 83.2% and reduces distribution drift from 0.38 to 0.14; across Llama, Mistral, and Qwen models, it preserves the persistent low-bit KV-cache footprint with modest decode overhead.
