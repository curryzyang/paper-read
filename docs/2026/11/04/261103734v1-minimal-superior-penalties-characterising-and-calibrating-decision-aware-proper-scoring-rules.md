# Minimal Superior Penalties: Characterising and Calibrating Decision-Aware Proper Scoring Rules

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Rouhollah Ahmadian
- 机构：Amirkabir University of Technology (Tehran Polytechnic)
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03734v1) · [PDF](https://arxiv.org/pdf/2611.03734v1)

## TLDR
The paper characterizes decision-aware superiority for Brier and logarithmic scoring rules as separation between closed-form score ranges on correct versus incorrect predictions, derives the minimal penalty needed to guarantee it (substantially smaller than prior published penalties), and embeds these penalties in a strictly proper one-parameter family, while a pre-specified case study finds only inconclusive descriptive evidence linking larger penalties to higher selected-model macro-F1.

## Abstract
Training a classifier means letting a validation metric decide which model is kept and when training stops. A natural requirement on that metric is superiority: every correctly classified forecast should score better than every incorrectly classified one, however close the underlying probabilities are. Neither the Brier score nor the logarithmic score satisfies this on its own. We show that superiority is governed by the separation between two endpoints -- the supremum of the score on correct predictions and the infimum on incorrect predictions -- and derive both in closed form for each score. Their difference is the infimal penalty, the greatest lower bound on the penalty needed to restore superiority. Prior work restores superiority with a penalty calibrated from the first endpoint alone; for the Brier base, our infimal penalty is smaller than that published penalty by a factor ranging from 4.00 at three classes to 2.11 at twenty. We further embed the published and infimal penalties in a one-parameter family and show that, under a single-valued tie convention, every member of the family is strictly proper. In a pre-specified two-dataset case study, mean selected-model macro-F1 rises with the penalty in the reported ten-class regimes, though not distinguishably from noise once seed/selection-mode nesting is accounted for; a fifth regime at forty-seven classes does not reproduce even this descriptive pattern. The intended no-superiority baseline is algebraically a rescaling of the family under test, so the experiment cannot attribute the observed pattern specifically to superiority. When superiority itself is the objective, any penalty strictly above the infimal value suffices; choosing a larger penalty is a separate calibration trade-off rather than a requirement for the guarantee.
