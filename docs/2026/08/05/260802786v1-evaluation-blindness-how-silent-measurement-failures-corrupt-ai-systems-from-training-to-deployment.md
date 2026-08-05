# Evaluation Blindness: How Silent Measurement Failures Corrupt AI Systems from Training to Deployment

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Priyanka Bajaj
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02786v1) · [PDF](https://arxiv.org/pdf/2608.02786v1)

## TLDR
Evaluation blindness — when AI system measurements remain indistinguishable from healthy states during failures — is formalized as a unified structural property across training and deployment, demonstrated through case studies, a six-class taxonomy of silent production failures, and a failure-budget framework.

## Abstract
AI systems can fail silently. The failure propagates through training loops, evaluation pipelines, and production monitoring stacks until downstream harm makes it visible. This paper introduces evaluation blindness: a measurement function M exhibits evaluation blindness with respect to failure class F when it produces readings indistinguishable from a healthy state while the system is actually failing, with no auxiliary signal flagging the gap.
  The problem surfaces at two lifecycle stages the literature has treated separately. At training time, reward models are gamed, importance-sampling corrections are silently miscalculated, and benchmark contamination inflates fine-tuning evaluations, all while loss curves look healthy and gradient updates proceed normally. At deployment time, monitoring fails to catch six classes of production failure, including an Operational category that is 100% silent by structural definition.
  We provide a formal detectability predicate unifying both stages. Four training-time case studies trace concrete breakdowns, including a real implementation bug in TRL PR #6594 where gradients are corrupted as loss decreases normally. A six-class taxonomy validated against 50 real-world incidents from court documents and regulatory filings finds that 53% of verifiable public failures were silent. A failure budget framework ties acceptable failure rates to use-case risk class.
  The implication is direct: measurement infrastructure is a correctness concern across the full AI lifecycle, not just at evaluation time. Data, code, and taxonomy schema are at https://github.com/priyanka25aug/llm-failure-taxonomy.
