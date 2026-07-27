# Multi-Horizon Consistency as Geometry: When Latent Dynamics Contract, and When They Do Not

- 区域：速读区
- 排名：8
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Kavya Bhand, Aadi Joshi
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21645v1) · [PDF](https://arxiv.org/pdf/2607.21645v1)

## TLDR
Increasing multi-horizon latent consistency (λ) contracts latent dynamics and improves prediction error on Moving-MNIST, but this effect is domain-limited and does not appear in action-conditioned tasks or the KTH video dataset.

## Abstract
Multi-horizon latent consistency is a common training knob in video predictors and world models, but practitioners rarely know what it does to transition geometry. We treat lambda, the weight on multi-step latent agreement, as a diagnostic control and measure an empirical expansion proxy L20,q95 together with horizon-20 prediction error E20. On Moving-MNIST (n=6 seeds at the critical pair), raising lambda from 0 to 0.8 cuts L20 from 4.96 +/- 2.01 to 1.01 +/- 0.06 (paired t p=0.005, Wilcoxon p=0.031) and halves E20 (0.365 to 0.177, paired t p=1.1e-13). Four of six seeds cross L<1 at lambda=0.8. The same loss does not produce population L<1 on action-conditioned Pendulum-v1 or CartPole-v1, nor on KTH Actions video, even when E20 improves. An associational mediation analysis on MMNIST gives r-hat=0.94 (95% CI [0.88, 1.00], n=27, B=2000); lambda was not randomized. Defensive checks (architectural baselines, exogenous stress, WorldTest, MPC, scaling) mostly support a narrow claim: soft consistency can push passive video toward a near-contractive band, and that band is domain-limited. A stochastic-forcing law L20 ~ 1.23 + 1.82 eta at lambda=0.8 (bootstrap slope CI [1.73, 1.92], R^2=0.96) unifies control domains on the same curve via calibrated eta_eff. Complete joint slices at lambda in {0.4, 1.2} (30/30 cells, 5 eta x 3 seeds) show comparable linear L20(eta) slopes (~1.69 and ~2.00); we do not fit a continuous (lambda, eta) surface. We do not report DreamerV3 or TD-MPC2 returns.
