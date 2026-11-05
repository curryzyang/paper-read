# FedSharp: Byzantine Robust Decentralized Federated Learning Under Noisy Channel

- 区域：速读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ojaswi Sinha, Amin Farajzadeh, Animesh Yadav, Melike Erol-Kantarci
- 机构：Ohio University, University of Ottawa
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05546v1) · [PDF](https://arxiv.org/pdf/2611.05546v1)

## TLDR
FedSharp is a Byzantine-robust decentralized federated learning framework that combines suspicious-model screening, low-loss candidate averaging, and noise-adaptive proximal regularization to jointly mitigate channel-noise accumulation, Byzantine attacks, and non-IID drift, substantially outperforming benchmark methods.

## Abstract
Decentralized federated learning (DFL) eliminates the central aggregation server but remains vulnerable to data heterogeneity, Byzantine attacks, and channel noise. We show that noise accumulates as models propagate across nodes, becoming increasingly significant as the learning rate decays. Moreover, accumulated noise enables Byzantine attackers to exploit loss-based model selection by mimicking honest model averages. To address these challenges, we propose screened, hop-aware, ranked, proximal averaging, a robust DFL framework (FedSharp). In this approach, each node maintains models from its 2b predecessors, ensuring at least b honest candidates when at most b nodes are Byzantine. FedSharp screens suspicious models using coordinate-wise median deviations, averages the b lowest-loss candidates to reduce fresh channel-noise variance by a factor of b, and applies noise-adaptive gradient-norm regularization and proximal training to mitigate accumulated noise and non-IID drift. Experiments on a 100-node ring with 33 Byzantine nodes show that FedSharp achieves 93.5-94.9% accuracy on MNIST, compared with 29.4-38.1% for a state-of-the-art single-model-selection benchmark, and 32.8-48.8% on CIFAR-10, compared with 10.0-30.5%, across Gaussian and hidden attacks under IID and non-IID data. On MNIST, FedSharp also achieves accuracy within approximately one percentage point of the benchmark operating without channel noise.
