# Hierarchical Copula-Gumbel-Top-\texorpdfstring{$K$}{K} Routing: Two-Sided Dependence Control for Frozen Mixture-of-Experts at Fixed Per-Token Routing Laws

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Richard Yi Da Xu
- 机构：TadReamk Limited, Hong Kong Baptist University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28670v1) · [PDF](https://arxiv.org/pdf/2607.28670v1)

## TLDR
Hierarchical Copula-Gumbel-Top-K routing introduces two complementary dependence dials—positive within-group coupling for expert coherence and tunable negative cross-group coupling for load-variance control—over frozen mixture-of-experts routers, while provably preserving every token's complete per-token routing law.

## Abstract
A stochastic Gumbel-Top-$K$ router defines, for every token of a mixture-of-experts (MoE) model, a \emph{routing law}: a distribution over ordered expert lists and mixture weights. We ask which \emph{joint} distributions over the routing choices of different tokens are reachable while every individual token's complete routing law is held exactly fixed. We give a two-sided construction, \emph{Hierarchical Copula-Gumbel-Top-$K$} (\CGA{}). Within a group of related tokens, an exchangeable Gaussian copula positively correlates the Gumbel perturbations at each expert coordinate, which can increase within-group expert-set coherence. Across disjoint pairs of groups, a tunable antithetic construction introduces a selectable amount of negative dependence. We prove that both operations leave each token's ordered Top-$K$ sample, mixture weights, and inclusion probabilities identical in distribution to independent routing \emph{at a routing layer conditioned on its pre-routing logits}; conditional expected expert traffic is preserved as a consequence. We characterize the resulting trade-off: positive within-group coupling can only inflate the variance of realized expert loads relative to independent routing, while nonnegative cross-group opposition can only reduce it relative to flat coupling at the same within-group strength. Coherence and load dispersion are thus controlled by two complementary dependence dials on the invariance constraint surface. Because the base model is untouched, the dials can be driven by a small controller over frozen features, trainable with a score-function estimator: the frozen network is evaluated only in the forward direction, and gradients are confined to the controller. An initial small-scale pilot validates the mechanism and the training route, but does not establish task-level fine-tuning gains.
