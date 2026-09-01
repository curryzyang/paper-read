# ERR+: Sequential Entropy Resolution for Efficient and Decisive LLM Reasoning

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Xin Jiang, Minhao Wang, Wen Wu, Zhentao Xie, Shangheng Du, Jinxin Shi, Jiabao Zhao
- 机构：ByteDance, East China Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28771v1) · [PDF](https://arxiv.org/pdf/2608.28771v1)

## TLDR
ERR+ is a two-phase RLVR framework that improves LLM reasoning by first rewarding entropy drops in the thinking phase (uncertainty resolution without suppressing exploration) and then optimizing response length via a robust relative efficiency reward, jointly improving accuracy and conciseness.

## Abstract
Large reasoning models achieve strong performance on complex tasks by generating extended chain-of-thought (CoT) traces via reinforcement learning with verifiable rewards (RLVR). While current RLVR methods have achieved strong results with correctness-based reward signals, they provide limited guidance on the quality of the reasoning process itself, leaving the internal reasoning structure largely unoptimized. Through empirical analysis across multiple model families, we identify a consistent pattern: correct reasoning trac es exhibit more frequent and larger token-level entropy drops within the thinking phase than incorrect ones. We propose ERR+, a two-phase RLVR framework grounded in this observation. The first phase trains with the Entropy Relief Reward (ERR), a bonus proportional to cumulative token-level entropy drops in the thinking phase, log-normalized by response length. Unlike prior methods that suppress entropy, ERR rewards the resolution of uncertainty while leaving exploratory high-entropy states unconstrained. The second phase introduces the Robust Relative Efficiency Reward, which scores each response's length against co-generated peers via a $\tanh$-transformed within-group $z$-score. We provide a formal analysis showing that joint optimization of the two objectives induces gradient conflict in early training, motivating the sequential design . Experiments on five datasets demonstrate consistent improvements in both accuracy and response conciseness across model backbones. Our code is available at https://github.com/XrkArul/err_response
