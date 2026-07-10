# Selective Left-Shift: Turning Test-Time Compute and Difficulty-based Curation into Training Data for Low-Resource Code Generation

- 区域：速读区
- 排名：4
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Didula Samaraweera, Anjana Supun, Srinath Perera
- 机构：WSO2
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07748v1) · [PDF](https://arxiv.org/pdf/2607.07748v1)

## TLDR
A three-phase pipeline that decouples syntax acquisition from algorithmic reasoning by left-shifting inference-time compute to offline data synthesis, then applying supervised fine-tuning and reinforcement learning with difficulty-curated data, achieves state-of-the-art code generation for low-resource languages like Julia and Ballerina while using significantly less data and cost.

## Abstract
Large Language Models achieve strong code generation for high resource languages like Python and Java but suffer sharp performance drops on Low-Resource Programming Languages~(LRPLs) such as Julia. Improving Small Language Models~(SLMs) for these languages faces a trilemma: Supervised Fine-Tuning~(SFT) is bottlenecked by data scarcity, inference-time scaling is too expensive for deployment, and Reinforcement Learning from scratch yields near zero advantages. We propose a three-phase pipeline that resolves this trilemma by decoupling syntax acquisition from algorithmic reasoning. First, we \emph{left-shift} inference-time compute to an offline data synthesis engine that uses iterative compiler and test feedback to generate verified training examples. Second, we fine-tune an SLM on this synthetic, verified data to embed strong syntactic priors. Third, we apply Reinforcement Learning with Verifiable Reward~(RLVR) grounded by language-agnostic Input/Output tests, where the SFT prior constrains exploration away from syntax errors. Applied to Qwen3-8B, our pipeline improves pass@1 by up to +7.6 points on MultiPL-E and +14.2 points on the Agnostics LiveCodeBench for Julia compared to SOTA results. Furthermore, the pipeline only used $\frac{1}{3}$ data and $\frac{1}{6}$ cost over the previous state-of-the-art. We further demonstrate that the pipeline generalizes to Ballerina achieving 49.7\% MultiPL-E Pass@1, a language with near-zero pretraining representation. Ablations confirm that both the SFT phase and execution-grounded rewards are necessary for stable training.
