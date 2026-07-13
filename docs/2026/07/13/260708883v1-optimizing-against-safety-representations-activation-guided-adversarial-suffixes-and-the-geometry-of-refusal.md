# Optimizing Against Safety Representations: Activation-Guided Adversarial Suffixes and the Geometry of Refusal

- 区域：速读区
- 排名：6
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Ege Çakar, Hannah Guan, Kayden Kehe
- 机构：Harvard University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08883v1) · [PDF](https://arxiv.org/pdf/2607.08883v1)

## TLDR
This paper introduces Activation-Guided GCG and Soft-GCG to probe and exploit the distributed geometry of safety representations in LLMs, showing that suppression of refusal across all layers is most effective and that smaller models remain more vulnerable than larger, better-aligned ones.

## Abstract
Behavioral alignment in large language models often masks fragile internal safety representations. Recent work suggests that refusal behavior is mediated by low-dimensional directions in activation space. This raises questions about how such representations are structured, localized, and accessed by optimization. We study adversarial suffix attacks as a probe of representational alignment. We introduce Activation-Guided GCG, which replaces output-based objectives with losses that directly target a model's internal refusal direction. Across several objective variants, we find that suppressing refusal globally across all layers and positions is more effective than targeting a single layer-position pair. This suggests that safety representations are distributed across the forward pass rather than causally localized to a single site. We further introduce Soft-GCG, a continuous relaxation of discrete suffix optimization using Gumbel-Softmax. Soft-GCG achieves a 33 $\times$ speedup over standard GCG while improving attack success rates. Evaluating across model scales, we find that smaller models remain vulnerable while larger models resist both activation- and suffix-based attacks at our compute-constrained settings, consistent with larger and better safety trained models being harder to jailbreak. Together, our results clarify how safety mechanisms are encoded and can be broken in contemporary models. These insights provide concrete guidance for designing more robust and representation-aware alignment strategies.
