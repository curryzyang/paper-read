# MMFGU: Multimodal Federated Graph Unlearning

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Haodong Lu, Zekai Chen, Weiwei Ji, Shihao Li, Xunkai Li, Xun Wu, Yinlin Zhu, Rong-Hua Li
- 机构：Beijing Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28708v1) · [PDF](https://arxiv.org/pdf/2607.28708v1)

## TLDR
MMFGU introduces a unified multimodal federated graph unlearning framework that maps fine-grained removal requests (entity/relation, modality, and pairing) into target-specific carrier decoupling, enabling selective forgetting with retained utility preservation and a 41.5× speedup over retraining.

## Abstract
Multimodal federated graph learning enables clients to collaboratively train graph models over structural, textual, and visual signals without sharing private local data. However, the presence of heterogeneous multimodal content also makes unlearning requests more frequent and fine-grained: users may delete accounts or interactions, remove a particular image or text while retaining the associated entity, or revoke the learned correspondence between retained modalities or graph attributes. Existing federated graph unlearning mainly handles entity/relation or client removal and cannot directly satisfy these multimodal requests. They introduce three challenges: removing only the requested information without damaging retained content, preventing the target from being recovered through remaining modalities or graph neighborhoods, and stopping related traces on other clients from re-entering the global model after aggregation. To address them, we propose \textsc{\textbf{MMFGU}}, a multimodal federated graph unlearning framework built around target-specific representation decoupling. \textsc{MMFGU} maps heterogeneous requests into unified target carriers, decouples requested representations while anchoring retained semantics, exposes and repairs propagated residuals with lightweight probes, and selectively purges affected clients through compact prototype and response signals. Experiments show that \textsc{MMFGU} effectively removes requested information, preserves retained graph utility, and achieves a $\boldsymbol{41.5\times}$ speedup over full retraining.
