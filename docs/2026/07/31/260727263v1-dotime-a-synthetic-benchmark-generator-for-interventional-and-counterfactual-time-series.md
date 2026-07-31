# DoTime: A Synthetic Benchmark Generator for Interventional and Counterfactual Time Series

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Dennis Thumm, Billy Tim Anthony, Ying Chen
- 机构：National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27263v1) · [PDF](https://arxiv.org/pdf/2607.27263v1)

## TLDR
DoTime is an open, scalable, and theoretically grounded synthetic benchmark generator for multivariate temporal structural causal models (TSCMs) with interventions and counterfactuals, released as a PyPI package with frozen evaluation suites, that addresses the lack of interventional and counterfactual time-series benchmarks and demonstrates a measurable advantage for interventional training over observational models.

## Abstract
Most benchmarks for causal inference over time series are observational, small, or domain-specific, leaving interventional and counterfactual estimation under-served exactly where it matters most, such as in healthcare, policy evaluation, and climate science. We introduce \textbf{DoTime}, an open, scalable, and theoretically grounded generator of multivariate temporal structural causal models (TSCMs) with interventions, released as the \code{dotime} PyPI package together with four frozen evaluation suites. Beyond existing work, it adds capabilities absent from prior generators: continuous-time intervention \emph{windows}, counterfactual sampling modes with a positivity guard, regime-switching SCMs as a strict generalization of interrupted time series, non-stationary dynamics by construction with switching SCM parameters, and deterministic ramp and sinusoidal intervention profiles that place trends and structural breaks \emph{inside} the evaluation window. Moreover, it demonstrates the suitability of the generator as a prior for a causal foundation model reference implementation. The released suites span a training-scale snapshot of $100{,}000$ trajectories and eight named identification structures, each with exact ground truth: paired interventional trajectories from the same SCM throughout, and shared-noise counterfactuals in the continuous-time suite. We ship reference baseline implementations with an evaluation harness, and pose a falsifiable claim: interventional training buys a measurable direction-accuracy advantage over an observational model of identical capacity. It is tested across three training seeds per arm. Under structure-matched evaluation on held-out episodes, the interventional prior-fitted network's (PFN) gap is positive in every structure, trajectory length, and seed tested.
