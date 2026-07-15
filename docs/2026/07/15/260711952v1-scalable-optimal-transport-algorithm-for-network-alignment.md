# Scalable Optimal Transport Algorithm for Network Alignment

- 区域：速读区
- 排名：9
- 匹配度：2.0/10
- 来源：arxiv
- 作者：Elaheh Hassani, Durga Mandarapu, Qi Yu, Hanghang Tong, Ariful Azad
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11952v1) · [PDF](https://arxiv.org/pdf/2607.11952v1)

## TLDR
FastAlign is a scalable, sparsity-aware framework for optimal transport-based network alignment that achieves comparable accuracy to state-of-the-art methods while substantially reducing runtime (up to 9.45× on CPU and 32.54× on GPU) through reinterpretation of OT computation as mixed sparse-dense operations, custom SpMM kernel, and domain-specific kernel fusion.

## Abstract
Network alignment identifies node correspondences across different networks and is a fundamental primitive in many data science applications, including social network analysis, fraud detection, and knowledge graph integration. However, state-of-the-art network alignment methods often achieve high accuracy by repeatedly constructing and updating dense matrices, sacrificing scalability in the process. To address this scalability limitation without compromising alignment accuracy, we present FastAlign, a scalable, sparsity-aware framework for optimal transport-based network alignment. Rather than introducing a new alignment model, FastAlign preserves the original OT formulation and reinterprets its computation as a set of recurring mixed sparse-dense operations. FastAlign combines sparsity-aware graph computation with domain-specific kernel fusion, including a custom SpMM kernel. Our results show that FastAlign achieves alignment quality comparable to state-of-the-art OT-based methods while substantially reducing end-to-end runtime up to 3.89x-9.45x on CPU and 2.24x-32.54x on GPU.
