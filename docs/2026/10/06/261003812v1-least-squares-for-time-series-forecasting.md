# Least Squares for Time Series Forecasting

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Weiu-qiou Ciang, Yuzhou Hong, Sherry Chen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03812v1) · [PDF](https://arxiv.org/pdf/2610.03812v1)

## TLDR
The paper argues that time-series forecasting should minimize least-squares error directly on the reported future coordinate rather than on a fixed-rank next-latent representation, since the former matches ordinary least squares with isotropy as a refittable gauge, while the latter can waste rank on nuisance dimensions and miss the target.

## Abstract
A time-series forecast is scored on a future value of the series. A representation loss that regresses the next latent, as in LeNEPA, is a different least-squares problem on the same bottleneck. We write both programs down. The forecast program minimizes the error of a decoded latent on the coordinate that will be reported. For a scalar target and a linear decoder, every latent rank of at least one matches ordinary least squares, and an isotropy constraint is only a rescaling: after the decoder is refit, the forecast does not move. The other program fits the whole next vector at a fixed rank, then freezes the encoder and attaches a head. On a four-dimensional series whose last three coordinates are the same autoregression, that rank-1 fit puts mass $0.9998$ on the repeated coordinate and forecasts the remaining signal at the marginal variance $2.794$. The forecast program puts mass $1$ on the signal and matches the innovation variance $0.992$. Rank $2$ gives the vector fit a second direction, and the two programs agree. Iterating the fitted one-step coefficient $0.803$ raises the open-loop error from $0.992$ at one step to $2.700$ at eight steps.
