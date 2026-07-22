# Beyond Output-Space Calibration: Spectral Evidence Bundling for Selective Reliability Estimation in Time-Series Classification

- 区域：速读区
- 排名：15
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Filippo Cenacchi, Longbing Cao, Runze Yang
- 机构：Macquarie University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18279v1) · [PDF](https://arxiv.org/pdf/2607.18279v1)

## TLDR
This paper introduces SEB-Cal, a validation-gated reliability estimation method for time-series classification that augments output confidence with deterministic whole-sample spectral descriptors (band energy, entropy, peak dominance, phase stability) to selectively estimate prediction trustworthiness, improving correctness-aware selective-reliability metrics like Corr-AURC from 0.693 to 0.786 and reducing false high-confidence errors.

## Abstract
Post-hoc calibration for time-series classification usually remaps output scores, but deployment decisions such as trust, abstention, and review depend on whether a confident prediction is supported by the current temporal signal. We address three time-series reliability gaps: identical confidence values can hide different temporal support, average calibration can miss false high-confidence errors, and output-space recalibration offers limited input-linked auditability. We introduce a validation-gated fixed-label reliability policy that keeps the backbone prediction unchanged while estimating whether it should be trusted. The method combines output-side cues with whole-sample spectral descriptors, including band energy, entropy, peak dominance, period support, and phase stability, to form a scalar reliability estimate and diagnostic band-level evidence. A validation gate enables spectral conditioning only when correctness ranking improves without breaching FalseConf@0.9 or AURC tolerances; otherwise it reverts to the safer output-space baseline. Across eight heterogeneous UCR/UEA datasets, eight time-series backbone families, and standard recalibrators, the unconstrained method improves fixed-label selective-reliability metrics on the matched evaluation subset, raising Corr-AURC from 0.693 to 0.779. The validation-gated policy further improves Corr-AURC to 0.786 and reduces FalseConf@0.9 to 0.094. These results suggest that reliability estimation for time-series classifiers benefits from bundling output confidence with spectral evidence, while validation gating prevents unsupported spectral conditioning.
