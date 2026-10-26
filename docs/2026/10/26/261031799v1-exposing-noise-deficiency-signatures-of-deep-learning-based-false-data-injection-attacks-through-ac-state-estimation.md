# Exposing Noise-Deficiency Signatures of Deep Learning-Based False Data Injection Attacks Through AC State Estimation

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yichen Liu, Hongyu Wu, Bo Liu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31799v1) · [PDF](https://arxiv.org/pdf/2610.31799v1)

## TLDR
The paper shows that reconstruction-based deep-learning false-data-injection attacks suppress unpredictable measurement noise, leaving abnormally low and directionally concentrated residual energy in AC state-estimation residual space, which enables label-free detection via a simple two-sided test on the conventional BDD statistic—detecting up to 99% of representative attacks at false-alarm rates comparable to BDD.

## Abstract
Deep learning (DL)-based false data injection (FDI) attacks can resemble normal measurements and evade both conventional bad data detection (BDD) and measurement-space data-driven detectors. This paper identifies a previously overlooked signature of such attacks in state-estimation (SE) residual space. The residuals of reconstruction-based DL attacks exhibit deficient stochastic variation, manifested as abnormally small residual energy and reduced directional dispersion. We establish the conditions under which this signature emerges and explain why the attacks carrying it can evade conventional BDD. We show that SE can reveal residual-space differences obscured by operating-state variation in measurement space. We then explain the origin of the signature through the noise-suppression mechanism of DL attack generation. A generator can learn the reproducible structure of historical measurements but cannot reproduce stochastic measurement components that are unpredictable from its input. This signature enables label-free detection using a simple two-sided test on the conventional BDD statistic, while the full residual vector can also be exploited when labeled attack samples are available. Experiments on the IEEE 14-bus and 118-bus AC systems show that the label-free test detects up to 99% of three representative DL attacks at a false-alarm rate comparable to that of BDD, which detects at most 5%. Ablation studies further examine the effects of residual representation, decision rule, and measurement-noise magnitude and distribution.
