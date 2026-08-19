# DUET: Dual-Teacher On-Policy Distillation via Same-Weight Disagreement for Prohibition Compliance

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Zihan Li, Feifei Li, Wenhui Que
- 机构：Tencent Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14644v1) · [PDF](https://arxiv.org/pdf/2608.14644v1)

## TLDR
DUET improves LLM prohibition compliance by using two same-weight teachers that differ only in whether they see the prohibition, and distills from their per-token disagreement to select violation-relevant tokens and apply token-level preference-directed learning—outperforming existing distillation baselines while preserving general utility.

## Abstract
Real-world LLM deployments increasingly rely on runtime-injected prohibitions--enterprise policies, PII redlines, tool boundaries--that vary per request and per tenant. Conventional post-training is structurally ill-suited: SFT hides the violation signal in compliant labels, and DPO's sequence-level preferences mismatch token-localized violations. We propose DUET, a token-selective on-policy distillation method for prohibition compliance. DUET pairs a teacher that sees the prohibition (positive) with an identical-weight teacher that does not (negative). Because the two teachers differ only in prohibition visibility, their per-token disagreement isolates the prohibition's causal effect--yielding a clean supervision signal uncontaminated by model capacity or mismatch. This disagreement drives two complementary mechanisms: signal cleaning, which discards agreement tokens as redundant or prefix-corrupted, and preference-directed learning, which pushes the student away from the negative teacher and toward the positive one at token granularity, embedding DPO-style optimization directly into OPD without offline preference data. We construct an industrial Prohibition-Compliance benchmark spanning five task families covering explicit-refusal, paraphrase robustness, and over-refusal. Across 1.5B-8B Qwen variants, DUET achieves 72.3-85.2% violation compliance while preserving 88-93% normal utility, dramatically outperforming teacher model and other distillation baselines. External evaluation on SysBench confirms improved safety alignment with minimal degradation on GSM8K and MATH-500.
