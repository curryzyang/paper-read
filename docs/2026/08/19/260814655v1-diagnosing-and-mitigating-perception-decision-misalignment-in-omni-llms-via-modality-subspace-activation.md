# Diagnosing and Mitigating Perception-Decision Misalignment in Omni-LLMs via Modality Subspace Activation

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Hongbo Jiang, Jie Li, Yunhang Shen, Tianyu Xie, Pingyang Dai
- 机构：Shanghai Artificial Intelligence Laboratory, Tencent YouTu Laboratory, Xiamen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14655v1) · [PDF](https://arxiv.org/pdf/2608.14655v1)

## TLDR
Omni-LLMs suffer from perception-decision misalignment where decisions ignore key modalities, so the authors propose CMS metrics and a training-free Modality Subspace Activation method to diagnose and restore modality sensitivity.

## Abstract
Omni-Large Language Models (Omni-LLMs) power complex multi-modal reasoning in applications like World Action Models and autonomous agents. However, their strong performance often masks a profound Perceptual-Decision Misalignment (PDM), where decisions remain unfaithful to multi-modal perceptions. To diagnose this, we formalize Causal Modality Sensitivity (CMS), operationalized via a dual-lens framework: Answer Retention Rate (ARR) at the macro behavioral level, and Logit Angular Discrepancy (LAD) to track microscopic distribution shifts. We also curate CausalMSBench, a diagnostic dataset isolating language priors. Benchmarking reveals that popular Omni-LLMs exhibit critically low CMS, showing negligible distribution shifts even when key modalities are removed. To rectify this, we propose Modality Subspace Activation (MSA), a training-free inference-time framework that uses Singular Value Decomposition (SVD) to estimate modal activation strengths. MSA dynamically balances modal projections in the last hidden state, effectively restoring CMS across benchmarks.
