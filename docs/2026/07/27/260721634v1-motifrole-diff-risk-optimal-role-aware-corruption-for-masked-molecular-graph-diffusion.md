# MotifRole-Diff: Risk-Optimal Role-Aware Corruption for Masked Molecular Graph Diffusion

- 区域：速读区
- 排名：15
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Tasfia Nuzhat Ornee, Elias Hossain, Ivan Garibay, Niloofar Yousef
- 机构：University of Central Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21634v1) · [PDF](https://arxiv.org/pdf/2607.21634v1)

## TLDR
MotifRole-Diff improves molecular graph generation by replacing the uniform corruption schedule in masked diffusion with a role-aware allocation of masking rates based on empirical denoising difficulty and structural impact, significantly boosting validity and reducing FCD on QM9 and MOSES benchmarks while keeping architecture and compute fixed.

## Abstract
Masked discrete diffusion for molecular graph generation typically applies a uniform corruption schedule to all tokens in a lossless graph-to-sequence representation, implicitly treating structurally heterogeneous molecular components as equally difficult and equally important to reconstruct. However, different molecular graph token roles exhibit substantial variation in denoising difficulty and their influence on the decoded molecule, motivating role-specific corruption strategies. We introduce MotifRole-Diff, a role-aware corruption process that allocates masking rates according to empirically measured denoising difficulty and graph-level perturbation impact while preserving the model architecture, clean sequence space, and lossless molecular-graph decoder. We formulate schedule selection as the risk-optimal allocation of a fixed masking budget across token roles. Our theorem characterizes optimality for the modeled role-weighted residual risk, while downstream generation performance is evaluated empirically. Under matched architecture, training budget, and sampling compute, MotifRole-Diff improves validity on QM9 from 0.905 to 0.944 while reducing FCD from 1.701 to 1.609, and on MOSES improves validity from 0.920 to 0.938 while reducing FCD from 2.125 to 1.850. Role-wise diagnostics further show improved reconstruction across molecular graph token categories. Together, these matched-compute results indicate that structurally informed corruption is a more effective masking strategy than uniform schedules for serialized molecular graph diffusion.
