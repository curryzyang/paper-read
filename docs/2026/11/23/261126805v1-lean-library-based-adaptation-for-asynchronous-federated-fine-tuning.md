# LEAN: Library-Based Adaptation for Asynchronous, Federated Fine-Tuning

- 区域：速读区
- 排名：3
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Erdong Hu, Zhimin Ding, Yuxin Tang, Chris Jermaine
- 机构：Rice University, Amazon AGI Lab
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26805v1) · [PDF](https://arxiv.org/pdf/2611.26805v1)

## TLDR
LEAN replaces adapter averaging in federated LoRA fine-tuning with a server-maintained library of rank-1 basis pairs that participants randomly check out, locally fine-tune, and check back in, enabling fully asynchronous, communication-efficient adaptation that is robust to data heterogeneity and asynchrony.

## Abstract
Federated fine-tuning of foundation models with low-rank adapters (LoRA) is typically reconciled by averaging locally trained adapters. In cross-device settings, where participants hold heterogeneous data and join or leave asynchronously, averaging is poorly suited: locally trained adapters are not identifiable up to permutation, and averages of adapters trained on dissimilar data can be uninformative or unstable. We propose a simple idea called federated library-based adaptation (LEAN), which replaces averaging altogether. The server maintains a library of rank-1 basis pairs; participants check out random subsets, fine-tune them locally as a LoRA adapter, and check them back in, so that each pair is shuffled across sites and trained on many participants' data. Because no aggregation step is required, LEAN operates fully asynchronously and communicates only low-rank parameters. We prove that, in a synchronous setting, LEAN converges to a neighborhood of a stationary point, with the shuffle canceling data heterogeneity at first order. Across image and text fine-tuning benchmarks, LEAN outperforms averaging-based baselines in most settings with substantially less communication, and remains effective under heavy data heterogeneity, where averaging-based methods fail to reach nontrivial accuracy, and under heavy asynchrony, where they degrade substantially.
