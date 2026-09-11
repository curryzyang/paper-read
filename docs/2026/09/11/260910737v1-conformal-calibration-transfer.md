# Conformal Calibration Transfer

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Achref Doula
- 机构：Technical University of Darmstadt, Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10737v1) · [PDF](https://arxiv.org/pdf/2609.10737v1)

## TLDR
The paper proposes Transported Conformal Calibration (TCC), which uses unlabeled paired source-target observations to transport labeled source calibration into a target space and then corrects residual mismatch with only unlabeled target inputs to provide valid target-domain conformal prediction sets.

## Abstract
Conformal prediction converts point predictions into set-valued predictions with coverage guarantees under exchangeability between calibration and deployment data. We study conformal calibration transfer, where this requirement fails because labeled calibration is available only in a source space, while prediction sets are needed in a target space linked to the source through unlabeled paired observations (e.g., paired modalities or sensor changes). We propose Transported Conformal Calibration (TCC): we transport labeled source calibration into the target space using the paired data, and then correct residual post-transport mismatch using only unlabeled target inputs. We instantiate this correction with two complementary methods: TCC-KS, which uses a label-free uncertainty surrogate to detect mismatch and adjust calibration conservatively, and weighted-TCC, which reweights transported calibration toward the target domain for improved efficiency when weights are stable. We provide finite-sample target-domain coverage guarantees that adapt to an observable measure of mismatch. Across CIFAR-100-C, Tiny-ImageNet-C, and SEN12MS, we show reliable target-domain coverage transfer without labeled target calibration data, with label-free diagnostics that predict when correction is needed.
