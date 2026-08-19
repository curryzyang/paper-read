# Do Uncertainty Signals Help? A Systematic Study of Uncertainty-Aware Decoding with Rollback Mechanisms

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Xianzong Wu, Xiaohong Li, Yuejun Guo, Xinyang Liu, Tianlin Li, Junjie Wang, Qiang Hu
- 机构：Luxembourg Institute of Science and Technology, Beihang University, Tianjin University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14653v1) · [PDF](https://arxiv.org/pdf/2608.14653v1)

## TLDR
Uncertainty-aware rollback decoding—using token-level uncertainty signals to identify and roll back unreliable generation prefixes—consistently improves LLM code generation across models and benchmarks, with information-theoretic signals like token entropy and negative log-likelihood being the most effective.

## Abstract
Prediction uncertainty is a widely adopted metric for quantifying model confidence, with downstream applications spanning model explanation, data selection, and prediction rollback. Despite its demonstrated utility, the potential of uncertainty quantification to enhance code generation in large language models (LLMs) remains largely underexplored, raising a critical question: to what extent can uncertainty serve as an effective signal for improving LLM-based code generation?
  To answer this question, we study uncertainty-aware rollback decoding, an inference-time strategy that uses uncertainty signals to identify unreliable generation regions and roll back to earlier valid prefixes without retraining the model. We evaluate this framework on seven code LLMs, five code generation benchmarks, and eight token-level uncertainty signals under a unified decoding setup.
  Our results show that the complete rollback framework improves over equal-budget restart across the evaluated benchmarks and model settings, with gains of up to 0.26 in pass@1 and 0.35 in AvgTestPassRate on functional code generation benchmarks, and an absolute improvement of up to 6.4\% in Patch-Aligned Safe Rate on Dsec-Python. Among the evaluated signals, information-theoretic measures such as token entropy and negative log-likelihood show the most favorable overall trend, frequently achieving the best or near-best results on standard benchmarks. A component-controlled ablation further shows that feedback-guided rollback provides the main improvement, while uncertainty localization provides an additional gain when checking, budget, rollback, and branch decay are held fixed.
