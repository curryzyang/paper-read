# Leak It: A Probabilistic Approach to Training-Data Extraction from Black-Box Language Models

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Victor Maricato
- 机构：Karolinska Institutet
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00144v1) · [PDF](https://arxiv.org/pdf/2608.00144v1)

## TLDR
TLDR: This paper shows that while aggregate sampling-based membership inference on black-box language models is no better than model-free blind baselines, the same sampling approach can verbatim-extract training data and personally identifying information for a tail of documents—so privacy audits should report per-document extraction by domain rather than a single AUC.

## Abstract
Membership inference (MIA) on language models is usually summarised by an aggregate ROC-AUC, but such evaluations are confounded: model-free blind baselines separate members from non-members from surface text alone. We study black-box, sampling-based training-data leakage through a probabilistic lens, treating N samples from p(.|x) as an estimate of the output distribution and casting leakage signals as functionals of it. We extend the blind-baseline critique into the sampling regime: on WikiMIA a blind bag-of-words classifier reaches AUC 0.97 (TPR 0.90 at 5% FPR) and sampling adds nothing, while on an IID Pile split (MIMIR) neither self-concentration nor gold-continuation recovery significantly beats a blind baseline (incremental AUC 95% CI includes zero). Aggregate metrics hide the real harm. The same sampling verbatim-extracts training data for a tail of documents no blind attack can reach. On Pythia-6.9B, 83 of 500 Pile documents bearing a real identifier (16.6%; 21.3% of those bearing an email address) have that exact identifier reproduced AND not reproduced under a mismatched-prefix control, so each leak is attributable to that document, not to a globally common string. This per-document disclosure is invisible to aggregate AUC and grows with capacity (5.6% to 16.6% from 410M to 6.9B). The risk is uneven: identifier leakage is ~3x stronger in code than prose, though prose stays clearly positive and also grows with capacity (4.0% to 12.1%), while recovery of arbitrary held-out continuations is confined to code (+0.44 member gap on GitHub vs at most +0.014 on prose). Temperature and nucleus sampling matter little, a 16-token prefix suffices, and we detect no reduction from corpus deduplication. Privacy audits should report per-document extraction, decomposed by domain, not a single AUC. We release leakit, a black-box extraction-audit tool.
