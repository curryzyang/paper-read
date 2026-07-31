# EvoCause: LLM-Guided Evolution of Causal Graphs for Root Cause Analysis

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Lei Zan, Keli Zhang, Shifeng Xie, Jiale Zheng, Zehao Xiao, Zhiwei Dong, Ke Zhang, Ruichu Cai, Malik Tiomoko, Lujia Pan
- 机构：Peng Cheng Laboratory, Huawei Noah's Ark Lab, Guangdong University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27290v1) · [PDF](https://arxiv.org/pdf/2607.27290v1)

## TLDR
EvoCause uses an LLM to propose semantically plausible edits to causal alarm graphs, validated deterministically and selected via expert root-cause labels, improving root cause analysis and graph reconstruction while introducing the TeleRCA benchmark.

## Abstract
Modern telecommunication, cloud, and microservice systems emit correlated alarm cascades when components fail. Root cause analysis (RCA) aims to identify the small set of alarms that initiate each cascade. A common approach learns a causal graph from observational logs and predicts all zero-in-degree alarms in each incident-induced subgraph. However, the learned graph remains fixed and cannot benefit from expert diagnoses of historical incidents. We close this loop with EvoCause. Expert labels constrain which alarms should be source nodes but do not specify the edge edits needed to satisfy those constraints. EvoCause uses a large language model (LLM) to propose semantically plausible graph edits, while deterministic code validates node identities and acyclicity and retains the best graph on a labeled alignment set. At test time, the refined graph alone produces transparent predictions without an LLM call. We also release TeleRCA, an expert-annotated benchmark from a production telecommunication network containing $485{,}681$ alarm events spanning $194$ alarm types over $5{,}621$ resources. On synthetic data, EvoCause initialized with the PC causal discovery algorithm outperforms the unrefined PC baseline, raising Node F1, Case EM, and Graph F1 by $11.59$, $9.40$, and $4.59$ percentage points, respectively, while reducing nSHD by $0.2379$. On TeleRCA, replacing human-readable alarm titles with anonymous identifiers lowers Node F1 and Case EM by $6.12$ and $8.04$ percentage points, respectively, indicating that alarm-name information contributes to graph refinement.
