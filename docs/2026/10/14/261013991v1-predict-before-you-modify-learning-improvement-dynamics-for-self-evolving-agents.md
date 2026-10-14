# Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Zixuan Xie, Chang Xu, Yuhua Jiang, Li Zhao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13991v1) · [PDF](https://arxiv.org/pdf/2610.13991v1)

## TLDR
The paper introduces an editable Improvement Dynamics Model that predicts the task-level outcomes of proposed self-modifications before costly evaluation to guide revisions and accumulates predictive knowledge across generations, outperforming HyperAgents by up to 46% average performance across multilingual coding, paper review, robotics reward design, and Olympiad-level math grading.

## Abstract
Self-evolving agents improve through repeated cycles of modification and evaluation. However, existing methods receive feedback on modifications only after costly evaluations, and aggregate scores may obscure distinctions between failures that require different repairs. We introduce predictive self-evolution through an editable Improvement Dynamics Model (IDM). Before evaluation, the IDM predicts task-level outcomes of a proposed modification and guides an optional revision. After evaluation, past modifications and their observed outcomes are used to improve the IDM, allowing predictive knowledge to accumulate across generations. The system can thus improve how it solves tasks, proposes modifications, and predicts their effects. Building on HyperAgents, we evaluate this approach across multilingual coding, paper review, robotics reward design, and Olympiad-level mathematical grading. Our approach outperforms HyperAgents across all four domains, with up to 46% higher average performance over generations. Gains also persist under matched token budgets that include both agent evolution and task evaluation, and extend to held-out tasks. Forecast accuracy improves as the IDM evolves, and the learned predictive knowledge transfers to improve evolution in a new domain.
