# Multimodal Graph Learning: A Survey of Models, Benchmarks, and Frontiers

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Rui Xue, Tianfu Wu
- 机构：North Carolina State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.12990v1) · [PDF](https://arxiv.org/pdf/2611.12990v1)

## TLDR
This survey provides an algorithm-centric, evaluation-grounded overview of multimodal graph learning, unifying graph-centric and foundation-model-centric methods through a common message-passing framework with five integration levels, while reviewing benchmarks and evaluation protocols and outlining connections to AI agents and future research directions.

## Abstract
Multimodal attributed graphs (MAGs), in which nodes carry text, images, and other modalities while edges encode relations among entities, underlie e-commerce, social media, content platforms, and creative applications. Learning on MAGs has developed along two complementary lines: graph-centric methods redesign how modalities are fused, propagated, and connected within message passing, while foundation-model-centric methods pretrain transferable multimodal graph encoders or bring graph context into multimodal large language models for prediction and generation. In parallel, several benchmarks have appeared with different datasets and evaluation protocols. This survey takes an algorithm-centric and evaluation-grounded view of the field and makes three contributions. Modeling: we introduce a unified message-passing formulation and organize methods into five integration levels (feature, propagation, topology, learning, and foundation model), covering discriminative and graph-conditioned generative models; within this formulation we derive representative methods as special cases, compare their assumptions, expressiveness, and cost, and identify cross-modal sensitivity as a property that separates otherwise similar architectures. Datasets and evaluation: we review recent benchmarks, summarize their datasets and metrics, define model-independent descriptors (label homophily, average degree, clustering, and edge provenance), and map each evaluation protocol to the baselines it uses. Frontiers: we connect multimodal graph learning to AI agents, covering the multimodal graphs that agents perceive and remember and graph engineering, the practice of organizing agent workflows as explicit graphs; we then discuss open problems, concrete efforts for the community, and research directions, including when graph structure helps in the presence of strong multimodal foundation models.
