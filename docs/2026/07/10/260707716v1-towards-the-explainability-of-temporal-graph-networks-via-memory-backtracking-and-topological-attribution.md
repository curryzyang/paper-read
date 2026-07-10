# Towards the Explainability of Temporal Graph Networks via Memory Backtracking and Topological Attribution

- 区域：速读区
- 排名：11
- 匹配度：1.7/10
- 来源：arxiv
- 作者：Yazheng Liu, Xi Zhang, Sihong Xie, Hui Xiong
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07716v1) · [PDF](https://arxiv.org/pdf/2607.07716v1)

## TLDR
This paper introduces MemExplainer, a method that explains Temporal Graph Network predictions by using topology attribution and memory backtracking trees to trace the influence of historical events on node memories, and demonstrates its superior faithfulness and performance across multiple temporal graph tasks.

## Abstract
Temporal graphs are ubiquitous in real-world applications and Temporal Graph Networks (TGNs) have achieved superior predictive accuracy. Understanding which historical events drive model predictions can enhance trustworthiness of TGNs. Existing explanation methods overlook the memory module, the core component that records and updates node histories, leaving the influence of past events unexplored. To address this, we attribute TGNs predictions through the topology attribution tree and memory backtracking tree. The topology attribution tree captures the influence of neighbors and their memory vectors, then the memory backtracking tree quantifies how historical events shape node memory vectors. We apply the LRP in TGNs, ensuring that the total contribution of events equals the logits of model. Finally, top-k selection may be unfaithful due to the nonlinear mapping from logits to probabilities, we design optimization objectives to identify the important events. Experiments on nine temporal graph datasets, spanning node property prediction, link prediction tasks and graph classification tasks, show that our method provides faithful explanations and outperforms state-of-the-art baselines. The code is available at https://github.com/yazhengliu/MemExplainer
