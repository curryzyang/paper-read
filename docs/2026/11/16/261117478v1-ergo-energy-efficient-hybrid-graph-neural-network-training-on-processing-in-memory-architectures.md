# ERGo: Energy-Efficient Hybrid Graph Neural Network Training on Processing-In-Memory Architectures

- 区域：速读区
- 排名：5
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Pratyush Dhingra, Chibuike E. Ugwu, Janardhan Rao Doppa, Partha Pratim Pande
- 机构：Washington State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17478v1) · [PDF](https://arxiv.org/pdf/2611.17478v1)

## TLDR
ERGo is a hybrid GNN training framework for processing-in-memory architectures that uses conformal prediction to automatically switch from full-parameter training to a low-rank parameter-efficient phase, reducing off-chip memory access to improve speed and energy efficiency while extending NVM lifetime with negligible accuracy loss.

## Abstract
Processing-in-memory (PIM) has been proposed as an alternative computing paradigm for training Deep Neural Networks, including Graph Neural Networks (GNNs). Despite these advancements, training GNN workloads on PIM devices necessitates off-chip memory access. This off-chip access is expensive in terms of performance and energy, thereby impacting the overall energy efficiency of the training process on PIM platforms. In this paper, we propose a novel hybrid training framework called ERGo that automatically switches from a full-parameter phase to a parameter-efficient phase during the training process with negligible loss in predictive accuracy. The parameter-efficient phase employs low-rank representations of GNN weights, effectively reducing the number of trainable parameters. This helps in reducing the off-chip access during the end-to-end training process on PIM architectures, leading to notable improvements in both performance and energy efficiency. ERGo outperforms the conventional full-parameter GNN training on a PIM-based platform by up to 3.15x in speedup and enhances energy efficiency by 10.5x. Furthermore, ERGo offers additional advantages when utilized on heterogeneous architectures incorporating non-volatile memory (NVM) and static random-access memory (SRAM). Training on the heterogeneous NVM-SRAM architecture typically utilizes NVM for the forward-pass and SRAM for the backward-pass. However, NVM cells suffer from low device endurance and repeated write operations due to weight updates can lead to poor lifetime. ERGo improves the lifetime of NVM devices by freezing the weights and preventing weight updates in the parameter-efficient phase. Experimental results demonstrate that ERGo improves the lifetime of heterogeneous NVM-SRAM architecture by up to 33x in comparison to full-parameter implementation.
