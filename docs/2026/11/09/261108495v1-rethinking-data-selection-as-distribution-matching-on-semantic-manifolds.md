# Rethinking Data Selection as Distribution Matching on Semantic Manifolds

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Peng Sun, Yi Yang, Mingshuo Chen, Chunxiao Li, Yao Zhu, Huawen Shen, Tianfan Fu
- 机构：Institute of Information Engineering, Fudan University, Beijing University of Posts and Telecommunications, Zhejiang University, Nanjing University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08495v1) · [PDF](https://arxiv.org/pdf/2611.08495v1)

## TLDR
QMAC is a quality-aware data selection method that selects a high-quality subset by matching its empirical characteristic function to the full dataset across multiple frequency scales, thereby preserving semantic-manifold distributional coverage while filtering noisy or low-quality samples.

## Abstract
Instruction tuning of large language models and large vision language models relies on massive training data, which incurs substantial computational and storage costs. Meanwhile, training data often contains redundancy, noise, and low quality samples. Existing data selection methods mostly rely on diversity, importance, or a combination of both, without explicitly constraining the distributional consistency between the selected subset and the full data in the embedding space. We propose QMAC, a quality aware multiband characteristic function matching method that formulates data selection as a joint optimization problem of distribution matching and quality filtering. QMAC matches the empirical characteristic functions of the selected subset and the full data across multiple frequency scales, capturing both global semantic coverage and local perturbations, while using task related quality scores to filter noisy and low quality samples. We systematically evaluate QMAC on 4 data types, 8 target models, and 44 benchmarks. Experimental results show that QMAC outperforms existing data selection baselines on standard image-text instruction data, substantially surpasses random selection on standard text instruction, image-text reasoning, and text reasoning data, and exceeds full data training in multiple model and budget combinations. The code will be made publicly available upon acceptance of the paper.
