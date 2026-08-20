# Hierarchical Data Selection via Manifold Coverage and Sparse Feature Coverage in LLM Post-training

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Peng Sun, Yi Yang, Antong Zhang, Chunxiao Li, Yanbo Wang, Dianbo Liu, xin chen, Kai Yu, Lu Chen, Tianfan Fu
- 机构：Fudan University, Nanjing University, Suzhou Laboratory, Shanghai Jiao Tong University, Brown University, North University of China, National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16927v1) · [PDF](https://arxiv.org/pdf/2608.16927v1)

## TLDR
MASS improves LLM post-training data selection by formulating it as a coarse-to-fine hierarchical coverage problem—using a dense autoencoder for principal manifold grouping and a TopK sparse autoencoder for quality-aware fine-grained feature coverage—consistently outperforming baselines and often matching full-data training with only a small subset.

## Abstract
As supervised fine-tuning data continues to scale, selecting high-value subsets from large candidate pools is crucial for reducing training cost and improving model performance. Existing methods often measure diversity directly in the original embedding space, where geometric metrics entangle dominant semantic directions, fine-grained supervision differences, and local noise. We address this limitation by formulating data selection as a coarse-to-fine hierarchical coverage problem and propose MASS. MASS learns low-dimensional principal manifold coordinates with a dense autoencoder for coarse semantic grouping, and then performs quality-aware sparse feature coverage within each group using a TopK sparse autoencoder. Experiments on Vision Flan and LLaVA-CoT show that MASS consistently outperforms strong data selection baselines across multiple budgets, and in several settings matches or surpasses full data training with only a small subset of data.
