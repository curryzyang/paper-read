# When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Fangxin Wang, Ziyi Zhang, Diyi Zhuang, Langzhou He, Shiyu Wang, Baichuan Mo, Philip S. Yu
- 机构：University of Illinois Chicago, Texas A&M University, Massachusetts Institute of Technology, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05207v1) · [PDF](https://arxiv.org/pdf/2608.05207v1)

## TLDR
CRAFTER is a source-blind agent that mines a frozen forecaster’s residual via compositional search and LLM-proposed named features, using a validation-grounded gate to discover corrective features that consistently outperform dedicated feature-engineering systems across datasets and backbones.

## Abstract
Frozen pretrained forecasters often fail in structured, recurring ways that are costly to repair through fine-tuning. We study corrective feature discovery: mining interpretable features of a frozen forecaster's residual to drive a lightweight post-hoc corrector. Prior automated feature engineering models the data-generating process; corrective features instead model the model-failure process. We present CRAFTER (Corrective Residual Agent with Feature-based Temporal Exploration and Reasoning), which keeps the backbone frozen and mines its residual with two complementary generators: a compositional search over the raw input channels, and a large language model (LLM) that proposes named feature combinations, binary flags, and short executable code. A single validation-grounded gate accepts or rejects every candidate regardless of its origin, and a validation-selected corrector applies the accepted features or leaves the forecast unchanged. This source-agnostic pipeline also allows prior feature-engineering systems to be evaluated under identical conditions, making CRAFTER an instrument for attributing forecast improvements to the feature source alone. Across six public datasets and six frozen backbones, CRAFTER surpasses every dedicated feature-engineering system at every feature budget, roughly doubling the improvement achieved by the corrector alone and reducing the error of the weakest backbones by up to 27%. These gains are robust across different LLM backends and persist even when applied on top of fine-tuned backbones.
