# Valid Per-Field Selective Risk Control for Document Extraction: Three Failure Modes, a Validity Ladder, and When Conditioning Pays

- 区域：速读区
- 排名：15
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Bhaskar Gurram
- 机构：Zasti AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14639v1) · [PDF](https://arxiv.org/pdf/2608.14639v1)

## TLDR
This paper diagnoses three failure modes (document clustering, score-refit leakage, and tie-mass pathology) that make naive per-field selective risk control invalid on real document extraction outputs, then proposes a "validity ladder" of guarantee tiers—from expected-risk split protocols to per-group PAC certificates—showing that taxonomical conditioning on provenance pays exactly when pooled thresholds cannot certify, and is subsumed by learned scores elsewhere.

## Abstract
Per-field accept/review with selective risk at most alpha -- accept a field only if the error rate among accepted fields is controlled -- is the trust contract document-extraction systems need, and the natural procedure silently violates it on real documents. On 13,859 genuine claude-sonnet-5 fields from 800 CORD receipts (49.0% correct) we diagnose three failure modes: document clustering (design effect 1.84-2.45), score-refit leakage (coverage 0.416 at risk 0.127, violating alpha=0.10 in 95% of splits), and a tie-mass pathology (a degenerate score collapses the threshold grid, 0.030 to 0.001). We organize the fixes as a validity ladder, guarantee form stated per tier. A fit/val split protocol restores expected-selective-risk control for a learned fusion: coverage 0.318 at risk 0.096 at nominal alpha=0.10, no tolerance band (production variant 0.326) -- an on-average point whose realized risk exceeds alpha in 47.5% of resplits, not a certificate. Mondrian Learn-then-Test with exact binomial tails yields per-group PAC certificates: field-iid 0.171 at risk 0.068, cluster-corrected 0.140, doc-iid 0.060 -- the only tier matching documents, honestly near-vacuous today. Support-bin, the pre-specified provenance taxonomy, wins every rigor tier on the sonnet CORD capture (p<1e-4, Bonferroni-corrected) -- a win that does not replicate on the same documents under haiku or qwen -- while on higher-accuracy corpora pooled thresholds win: conditioning helps exactly where pooled cannot certify, subsumed by a learned score elsewhere. A frozen-configuration confirmation on selection-untouched claude-haiku-4-5 held at both risk levels, and a blind three-annotator human-gold audit verifies the practical tier's accepted-set risk at 1.3% against its 10% budget (Fleiss' kappa=0.83; labels err one-sidedly pessimistic). Released Apache-2.0 with seed-pinned, regression-gated procedures.
