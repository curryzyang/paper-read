# The Cost of Long Memory: State, Context, and Stability Complexity in Sequence Models

- 区域：速读区
- 排名：2
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Yuheng Song
- 机构：Huazhong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08816v1) · [PDF](https://arxiv.org/pdf/2610.08816v1)

## TLDR
For algebraically decaying predictive memory, the paper proves matching bounds showing that achieving forecast error τ with exponential or finite-state sequence models requires Θ(log²(1/τ)) states or modes, and it extends this resource analysis to context length, fractional long memory, and the stability margin needed by contractive nonlinear recurrences to avoid a forecasting floor.

## Abstract
Long-range temporal dependence poses a resource question for sequence models: for a specified predictive-memory law, how much state, context, or dynamical criticality is required in order to forecast accurately? We study this question directly in forecasting risk. For algebraically decaying predictive memory, we prove matching upper and lower approximation bounds for exponential and finite-state modes. The best $r$-mode forecast error decays as $e^{-Θ(\sqrt r)}$, so reaching forecast error $τ$ needs $r=Θ(\log^2(1/τ))$ states or modes. Earlier curse-of-memory results establish broad limitations of stable recurrent models under different approximation notions; here both sides match for one canonical predictive target in forecast risk, which fixes the optimal resource exponent for that target. We then show that genuine fractional long memory changes the geometry itself. In particular, forecast error is measured after fractional integration, prediction from a finite context of length $L$ has an exact $1/L$ leading order, and a fixed fractional strength $d$ keeps the square-log state-complexity law. Near the short-memory boundary, we identify the relevant $d^2$ and $d^4$ scales and give a uniform constructive law in the intermediate regime. For nonlinear contextual recurrences with uniformly contractive state dynamics, we derive an exponential first-chaos envelope and an explicit necessary condition that relates forecast accuracy to the contraction margin. Vanishing forecasting error on an algebraic target forces the recurrence quantitatively toward criticality, a condition that is necessary and not by itself sufficient. Finite-sample Kullback--Leibler calculations further connect the predictive geometry to statistical information. Theorem-matched experiments with contractive state-space, gated recurrent, and attention models reproduce the state and stability predictions.
