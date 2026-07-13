# A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions

- 区域：速读区
- 排名：9
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Qingzhuo Wang, Ruiyang Qin, Zhenxin Qin, Wen Shen, Zhihua Wei
- 机构：Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08776v1) · [PDF](https://arxiv.org/pdf/2607.08776v1)

## TLDR
This paper reveals that knowledge distillation for large language models works by sparsifying interactions (especially complex ones) and proposes the Complex Interaction Penalty (CIP) loss to explicitly enforce this sparsity, thereby improving distillation performance.

## Abstract
Despite the success of knowledge distillation (KD) in Large Language Models (LLMs), the underlying mechanism behind its efficacy remains unclear. In this paper, we propose a unified approach to explore the common mechanism of various KD methods using interactions. Specifically, we decompose the output score of the LLM into the sum of numerous interactions. Each interaction represents a nonlinear relationship involving a set of input variables (e.g., words). Based on the decomposed interactions, we discover that the common mechanism underlying various KD methods is the sparsification of interactions, i.e., student models retain fewer interactions for inference while suppressing other interactions to zero effects. Furthermore, we discover that the performance variance across different KD methods arises from their capabilities in handling complex interactions. A KD method typically yields better performance if it enables the student model to achieve higher sparsity of complex interactions. Motivated by these insights, we propose a plug-and-play loss function called Complex Interaction Penalty (CIP) to explicitly enforce the sparsity of complex interactions during the distillation process. Extensive experiments demonstrate that integrating CIP consistently improves the performance of diverse KD methods on both in-domain and out-of-distribution benchmarks.
