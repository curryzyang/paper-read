# Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement

- 区域：速读区
- 排名：4
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Qianli Liu, Kaibin Guo, Zicong Hong, Peng Li, Fahao Chen, Haodong Wang, Jian Lin, Song Guo
- 机构：The Hong Kong University of Science and Technology, Xi’an Jiaotong University, Shandong University, Sun Yat-Sen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.08782v1) · [PDF](https://arxiv.org/pdf/2607.08782v1)

## TLDR
Director introduces a prediction-driven, online proactive expert placement system that minimizes end-to-end latency in distributed Mixture-of-Experts serving by using cascaded predictors or quantized replicas, near-zero-downtime migration, and a polynomial-time optimizer with a (1+ε) approximation ratio, achieving 11–55% latency reduction over existing methods.

## Abstract
Expert parallelism has become the prevailing paradigm to serve Mixture-of-Experts (MoE) models. Its efficiency depends on the communication and computation latencies of the GPUs, which are linked to the placement of experts in the GPUs. Existing works for optimizing expert placement focus on leveraging past requests' expert activation patterns. However, they demonstrate deficiencies facing diverse and rapidly changing request patterns, calling for an online, proactive approach. Implementing such an approach requires addressing several challenges: the uncertainty associated with incoming requests' expert activation, the cost of expert migration, and the NP-hard complexity in optimization. Therefore, we present Director, a new distributed MoE serving system that minimizes end-to-end latency via prediction-driven, online expert placement. Director uses either a lightweight cascaded predictor or a low-bit quantized replica for expert activation patterns of incoming requests. An online migration module then enacts the changes with near-zero downtime by executing migrations in compute-bound phases, keeping disruption bounded. At its core, a relaxation-based expert placement optimizer operates under capacity constraints, runs in polynomial time, and achieves a $(1+ε)$ approximation ratio. Finally, we implement a prototype and demonstrate, through extensive experiments, a reduction in end-to-end latency of $11\sim55\%$ for popular MoE models (e.g., Mistral, DeepSeek and Qwen) compared to existing work.
