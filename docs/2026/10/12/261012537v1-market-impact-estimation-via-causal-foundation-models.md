# Market Impact Estimation via Causal Foundation Models

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Dennis Thumm, Ying Chen
- 机构：National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12537v1) · [PDF](https://arxiv.org/pdf/2610.12537v1)

## TLDR
**TLDR:** The paper introduces a continuous-time causal prior-data fitted network (PFN) trained on a synthetic market prior with controllable confounding, which avoids the information-channel bias of classical price-on-flow regressions and estimates market impact as a true interventional (do-operator) quantity, showing zero-shot transfer to ABIDES limit-order books and real crypto/equity metaorders.

## Abstract
When a trader executes a large order, the relevant question is not \emph{what will the price be?} but \emph{what would the price have been had I not traded?} Market impact is thus a causal quantity, yet classical models (Almgren--Chriss, propagators) regress price on flow, which is biased whenever informed flow moves prices through information as well as trading. We present a proof-of-concept \emph{Causal Market Simulator}: a continuous-time causal prior-data fitted network (PFN) trained on a synthetic market prior in which a hidden informational flow confounds the flow--price relation by construction, with confounding strength an exact per-episode knob. On this prior, the naive estimator's bias follows a closed form we confirm empirically (up to 68\% overestimation), while the PFN tracks the unbiased true-parameter oracle at high confounding. Its \emph{do-ablated twin}, the same model with the intervention inputs removed, collapses onto the pre-window mean. Zero-shot, the model responds at the ground-truth scale to metaorders in an ABIDES limit-order book ($+0.38$ pre-onset standard deviations against seed-replay counterfactuals), and its intervention response replicates on about 2,300 detected flow bursts in BTC/ETH/SOL perpetuals and 3,800 on Nasdaq equities, evidence consistent with, though not proof of, causal transfer. Off-prior the response degrades gracefully, and split-conformal recalibration repairs interval calibration. Transfer hinges on encoding the metaorder as added flow rather than a clamped price level, not on more training. A recurrent state-space variant closes the remaining shape gap: its impact accrues over execution duration where the transformer's stays flat, raising the correlation with measured metaorder impact from $+0.68$ to between $+0.92$ and $+0.96$, at the cost of weaker on-prior deconfounding that traces to the training recipe rather than to recurrence.
