# Beyond Distribution Matching: Semantics-Consistent Tabular Diffusion with Weak Semantic Priors

- 区域：速读区
- 排名：1
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yili Wang, Ruxue Shi, Mengnan Du, Hangting Ye, Yi Chang, Xin Wang
- 机构：Jilin University, The Chinese University of Hong Kong, Shenzhen
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16069v1) · [PDF](https://arxiv.org/pdf/2609.16069v1)

## TLDR
TLDR: SCTab-Diff is a semantics-consistent tabular diffusion framework that uses LLM-extracted weak semantic priors—intra-column semantics and inter-column symbolic rules—as generation conditions rather than post-hoc filters to produce synthetic tables that are both distributionally faithful and semantically valid.

## Abstract
Synthetic tabular data can match real data distributions while still violating the semantic constraints that govern valid tabular rows. This reveals a key limitation of existing tabular generators: they mainly optimize distributional fidelity, but do not explicitly model weak semantic priors encoded in tabular schema and textual descriptions. In this paper, we propose \ours, a semantics-consistent tabular diffusion framework for high-fidelity synthetic data generation under weakly specified semantic priors. \ours\ first constructs two types of priors, namely intra-column semantics and inter-column symbolic rules, with LLM-assisted extraction from metadata and validation on the real training split. These priors are then used as generation conditions rather than post-hoc filters. Specifically, \ours\ maps heterogeneous column values, column identities, and semantic priors into a unified semantic space, and performs column-wise forward corruption and prior-conditioned reverse denoising to preserve both marginal distributions and rule-consistent cross-column dependencies. Extensive experiments on six real-world tabular benchmarks show that \ours\ consistently improves distributional fidelity, semantic consistency, and downstream task utility over representative VAE-, GAN-, LLM-, and diffusion-based baselines. Additional analyses further demonstrate the robustness of \ours\ when semantic priors are partially unavailable.
