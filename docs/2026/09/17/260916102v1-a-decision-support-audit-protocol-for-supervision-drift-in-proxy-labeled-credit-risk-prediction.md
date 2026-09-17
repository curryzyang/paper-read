# A Decision-Support Audit Protocol for Supervision Drift in Proxy-Labeled Credit-Risk Prediction

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Mehrdad Shoeibi, Muhammad Shabanpour, Waldemar Karwowski, Niloofar Yousefi
- 机构：University of Central Florida, Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16102v1) · [PDF](https://arxiv.org/pdf/2609.16102v1)

## TLDR
This paper proposes a locked, multi-signal audit protocol for diagnosing supervision drift in proxy-labeled credit-risk prediction, demonstrating on LendingClub data that ranking remains stable while the clearest temporal signal is a prevalence and probability-scale mismatch largely reduced by diagnostic recalibration, with the results offered as bounded evidence.

## Abstract
Credit-risk models are trained on proxy labels and deployed under temporal and segment change, yet no single transfer metric separates base-rate shift, probability-scale shift, and feature-label relationship change. We contribute a design-science artifact: a locked, multi-signal audit protocol for supervision drift in proxy-labeled credit-risk prediction. Five layers (transfer performance, an oracle-gap probe, a calibration diagnostic, feature-label stability, and a synthetic positive control), thresholds, and decision rules were locked before interpretation; a bounded reading is a designed outcome. On a public LendingClub dataset (temporal 2013 to 2016 and cross-segment transfer), ranking is stable and oracle gaps are small; the clearest temporal signal is a prevalence and probability-scale mismatch that intercept-only diagnostic recalibration largely reduces, though its cause is not identifiable from the available release. The positive control responds only to larger injected shifts; subtler drift cannot be excluded. Mapping diagnostic patterns to governance actions is conceptual guidance, not validated here.
