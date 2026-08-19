# Calibrated Trust, Not Sharper Prediction: An Empirical Test of Uncertainty Fusion

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Surya Saka
- 机构：JudicialMind
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14617v1) · [PDF](https://arxiv.org/pdf/2608.14617v1)

## TLDR
Testing uncertainty-fusion pipelines on 1,000 ECtHR cases shows they do not improve prediction accuracy and can worsen calibration, so their real value is enabling calibrated, risk-controlled selective automation ("calibrated trust") rather than sharper prediction.

## Abstract
A recurring proposal in legal AI is to improve case-outcome prediction by fusing uncertainty tools (evidence graphs with belief propagation, sequential Bayesian odds updating, Dempster-Shafer combination, and conformal prediction) into one pipeline. We test this on 1,000 real European Court of Human Rights cases from LexGLUE and FairLex, predicting whether the Court found a Convention violation from the case's fact paragraphs. We compare three families across two frontier LLMs (Claude Opus 4.8 and GPT-5.5) as per-fact evidence estimators: (A) the raw LLM, (B) the LLM routed through the fusion pipeline, and (C) a term-frequency baseline through the same pipeline. Across roughly 4,750 tests we find: (1) on discrimination (AUROC around 0.83) the pipeline yields no improvement over either the raw LLM or the baseline; a frontier LLM used directly is the strongest single discriminator. (2) Naively composing an LLM with Bayesian-odds and Dempster-Shafer fusion more than doubles calibration error (ECE from about 0.16 to 0.46) via a prior-mismatch mechanism that replicates across both models. (3) Dempster-Shafer fusion is actively unsafe on long chains, committing confidently to wrong labels at below-chance accuracy; we recommend removing it. (4) The pipeline's genuine value is operational: routed through a conformal selective-prediction layer, the system decides which cases to automate and which to escalate. After removing Dempster-Shafer, recalibrating, and applying class-conditional risk control on the full 1,000-case set, the tuned engine auto-clears at 96.8 percent accuracy with 0.5 percent errors escaping and 96.3 percent caught for review, versus 85.9 / 3.8 / 72.1 for an untuned baseline. The contribution of such pipelines in law is calibrated trust, not sharper prediction.
