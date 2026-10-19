# Sparse Autoencoders Can Induce Local Geometry for Mitigating Catastrophic Forgetting

- 区域：速读区
- 排名：3
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Kamil Faber, Katarzyna Filus, Łukasz Pawela
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22439v1) · [PDF](https://arxiv.org/pdf/2610.22439v1)

## TLDR
SAGA mitigates catastrophic forgetting by converting a task-boundary sparse autoencoder into input-dependent low-rank constraints on representation drift, achieving higher Class-IL accuracy and lower forgetting than evaluated replay baselines on three pretrained ViT-B/16 benchmarks.

## Abstract
Catastrophic forgetting remains a challenge in supervised continual learning, as adapting to new tasks causes representation drift and loss of previously learned information. This raises the question of which representational changes should be constrained while preserving plasticity. We therefore introduce Sparse Autoencoder Geometric Anchoring (SAGA), which converts a Sparse Autoencoder (SAE) trained at each task boundary into local, low-rank constraints on representation drift. Replay examples specify where the constraints apply, while leading right singular directions of the encoder Jacobian specify which changes are penalized. The resulting geometry is input dependent and can be retained without keeping the SAE for subsequent tasks' training. We establish its local relation to latent code matching, define its spectral truncation error, and derive a conditional bound on frozen-readout drift. With replay and snapshot history, the method achieves the highest mean Class-IL accuracy and lowest mean forgetting among the evaluated ER, DER++, ER-ACE, and SGD baselines on three pretrained ViT-B/16 benchmarks, with accuracy gains of 12.15, 4.79, and 3.22 percentage points over the strongest conventional baseline on CIFAR-100, CUB-200, and ImageNet-R, respectively. From scratch results are more mixed, while rank ablations and geometry controls show that SAE-induced low-rank geometry offers useful stability-plasticity trade-offs.
