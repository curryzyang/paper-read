# KVE-KD: Key Visual Evidence-Guided Knowledge Distillation for Vision-Language Models

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Jianbin Zhang, Xin Sun, Shanwen Wang, Wei Ye, Susanto Rahardja
- 机构：Tongji University, Zhejiang University, City University of Macau
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03842v1) · [PDF](https://arxiv.org/pdf/2610.03842v1)

## TLDR
KVE-KD is a vision-language model knowledge distillation framework that dynamically identifies task-relevant visual tokens as key visual evidence—by locating the cross-modal fusion layer and adaptively selecting tokens using anchor-conditioned attention entropy—to guide focused feature distillation and improve cross-modal reasoning without adding inference-time overhead.

## Abstract
Knowledge distillation is crucial for deploying vision-language models on resource-constrained devices. However, existing methods typically impose uniform supervision across visual tokens or rely on static token selection, which confuses task-relevant cues with background noise and degrades cross-modal reasoning. To address this limitation, we propose Key Visual Evidence-guided Knowledge Distillation (KVE-KD), a framework that dynamically focuses feature distillation on task-relevant visual tokens identified by the teacher model. Specifically, KVE-KD appoints the final pre-generation textual token as a unified semantic anchor and identifies the target cross-modal fusion layer by analyzing changes in the anchor representation through iterative visual-token contribution removal. Within this layer, KVE-KD ranks visual tokens via the anchor-conditioned attention distribution and selects the most informative visual tokens as key visual evidence with normalized entropy. The key visual evidence subsequently guides focused visual feature distillation, making the student align closely with the teacher's task-relevant visual representations while suppressing irrelevant background information. Extensive experiments on six benchmarks demonstrate that KVE-KD outperforms state-of-the-art cross-modal distillation methods, with particularly pronounced gains on tasks requiring complex reasoning and fine-grained visual understanding. Importantly, these improvements are achieved without introducing any inference-time overhead. The source code is available at https://github.com/zhangjianbin07/KVE-KD.
