# Conformity Breaks Conformal Prediction

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Yibo Hu, Hanyu Su
- 机构：Illinois Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04445v1) · [PDF](https://arxiv.org/pdf/2609.04445v1)

## TLDR
Conformity among peer LLMs breaks clean-calibrated conformal prediction guarantees by shifting the model's scoring mechanism under unanimous-wrong peer pressure, causing marginal coverage to collapse and enabling hidden conditional failures that defeat act-vs-escalate defenses.

## Abstract
A conformal certificate can be valid when an LLM answers alone and invalid when the same LLM sees peers that unanimously assert a wrong answer. The question is unchanged; the model's score for the correct answer changes. We call this a score-mechanism shift: clean calibration certifies how the model scores answers alone, but not how it scores them under peer pressure. We show that this shift silently breaks conformal prediction in multi-agent LLM systems. Across open-weight models and multiple-choice QA tasks, coverage falls from a calibrated 90% to 74% under unanimous-wrong peers at the standard alpha = 0.10 operating point. The average hides a sharper failure: by targeting the low-confidence items the certificate still covers, an attacker nearly halves coverage on that subgroup, from 87% to 47%, while the monitored average remains much higher. The failure also reaches the decision layer: a system that should escalate when uncertain can instead become confident enough to act on the attacker's wrong answer. Standard conformal fixes do not solve the problem, because the question distribution has not changed; the model's scoring behavior has.
