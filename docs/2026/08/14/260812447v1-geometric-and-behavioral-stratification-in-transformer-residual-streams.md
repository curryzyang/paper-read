# Geometric and Behavioral Stratification in Transformer Residual Streams

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Nelson Guda
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12447v1) · [PDF](https://arxiv.org/pdf/2608.12447v1)

## TLDR
Transformer residual streams are geometrically and behaviorally stratified by proximity to the model’s current prediction direction, forming a narrow, scale-invariant readout interface surrounded by a large, causally essential complement—a pattern that holds across all 18 models tested and explains how high-dimensional computation coexists with linear readout.

## Abstract
Trained transformer models develop privileged bases: coordinate axes whose statistics differ from the rest of the residual stream. But what kind of direction does such a basis select? We investigate the prediction direction, the unembedding direction of the token a model currently predicts, and find that it functions as a content-defined privileged anchor. Measured with respect to this anchor, residual-stream variation is geometrically and behaviorally stratified by proximity to the prediction.
  The stratification holds in all eighteen models tested (dense and mixture-of-experts, 7B-120B, base and instruction-tuned). A narrow, scale-invariant prediction interface concentrates readout-relevant structure, while the vast prediction-distal complement expands with model scale. Because the prediction direction sits nearly orthogonal to the principal variance axes, variance-based analyses recover this organization only partly, and the shortfall grows with prompt heterogeneity.
  Anchoring reveals a steep geometric gradient: prediction-proximal regions are highly structured and cluster related prompts, while the complement is flatter and anti-discriminates among prompt groups. The interface is a narrow slice but functionally decisive. Disrupting the variance directions closest to the prediction causes immediate divergence and frequent task-frame shifts; disrupting the next level down delays divergence and preserves framing. The complement is weakly readout-aligned per direction yet causally and temporally load-bearing, and behavior is driven by direction rather than magnitude.
  These results establish the prediction direction as a privileged anchor distinct from previously described coordinate axes, and give a geometric account of how high-dimensional computation coexists with linear readout.
