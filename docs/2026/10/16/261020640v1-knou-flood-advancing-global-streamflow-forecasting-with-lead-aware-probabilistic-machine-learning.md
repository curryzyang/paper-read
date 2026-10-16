# KNOU-Flood: Advancing global streamflow forecasting with lead-aware probabilistic machine learning

- 区域：速读区
- 排名：5
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Minjong Cheon
- 机构：Korea National Open University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20640v1) · [PDF](https://arxiv.org/pdf/2610.20640v1)

## TLDR
KNOU-Flood is a controlled extension of the AIFL LSTM recipe that adds lead-aware forecast inputs, a longer window, GraphCast alongside ECMWF HRES, and a latent-noise probabilistic ensemble trained with fair CRPS, improving global streamflow forecast skill and uncertainty across lead times over a reimplemented AIFL baseline.

## Abstract
Global streamflow forecasting supports flood preparedness, yet data-driven models trained on reanalysis lose skill when driven by operational forecasts, increasingly so with lead time. AIFL addresses this shift with a two-stage transfer-learning recipe and a deterministic LSTM, but it feeds one forecast lead time into the whole input window and gives no uncertainty. We ask how far this open recipe can be extended without changing its recurrent core. KNOU-Flood keeps a single-layer LSTM and the two-stage training and changes the information around it: a longer input window (424 days), lead-aware forecast inputs, GraphCast as a second forecast source next to ECMWF HRES, and a latent-noise ensemble trained with the fair CRPS. We compare against a re-implementation of the AIFL recipe (its code is not public) under identical data, stations, splits and metrics. Our contributions are threefold. First, over three seeds and 2,099 test basins (2021-2023), KNOU-Flood reaches a median KGE' of 0.65 at LT1 and 0.48 at LT10 against 0.62 and 0.34, with significant gains at all ten lead times under two scoring protocols, also against a 1024-unit baseline and on held-out basins (one seed each). Second, identical weights give an LT10 KGE' of 0.18 or 0.34 depending on how forecasts are fed, so much of the lead-time decay reported for AIFL is an input-protocol effect; the probabilistic head contributes most to the gain, followed by the raw GraphCast channels, the longer window and mixed fine-tuning. Third, the ensembles reach lower CRPS than probabilistic versions of the baseline, are nearly calibrated with inference-time dropout, and detect 1.5- and 2-year floods better than all baselines; the benefit for rarer floods depends on the seed, and an exploratory tail-weighted variant improves 10-year and larger events. KNOU-Flood is a controlled extension of an open recipe, not a new architecture.
