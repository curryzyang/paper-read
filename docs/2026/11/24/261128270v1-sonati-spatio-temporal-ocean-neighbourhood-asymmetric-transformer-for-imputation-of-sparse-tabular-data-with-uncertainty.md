# SONATI: Spatio-temporal ocean neighbourhood asymmetric transformer for imputation of sparse, tabular data with uncertainty

- 区域：速读区
- 排名：9
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Yvonne Jenniges, Boris Peter Koch, Maike Sonnewald, Sebastian Maneth
- 机构：University of Bremen, Alfred-Wegener-Institut, Helmholtz-Zentrum für Polar- und Meeresforschung, University of California, University of Washington, University of Applied Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28270v1) · [PDF](https://arxiv.org/pdf/2611.28270v1)

## TLDR
SONATI is a factorized time-space transformer that imputes sparse tabular oceanographic data using local spatio-temporal neighborhoods and quantifies aleatoric and epistemic uncertainty, outperforming classical and transformer-based methods by at least 12.5% RMSE on North Atlantic observations.

## Abstract
Missing value imputation is often a prerequisite for downstream analyses. In oceanography, observational data are frequently structured in a tabular manner, highly sparse and exhibit spatio-temporal structures that classical imputers such as k-nearest neighbours or MissForest are not suited to exploit. We present the Spatio-temporal Ocean Neighbourhood Asymmetric Transformer for Imputation (SONATI), a masked, factorised time-space transformer operating on pre-computed, local time and space neighbourhoods, which reduces computational complexity compared to global attention. SONATI is designed to work with tabular data and is thus in principle able to work on both gridded and unstructured data, though evaluation here was performed on gridded North Atlantic data only. It provides aleatoric and epistemic uncertainties through a negative log-likelihood loss and multiple forward passes with Monte Carlo dropout. Systematic ablations on attention type and masking strategies guided the final architecture design. The results showed that SONATI outperformed classical and transformer-based methods by at least 12.5% in terms of root mean squared error (RMSE) on a large observational oceanographic dataset with key biogeochemical and physical parameters in the North Atlantic (potential temperature, salinity, oxygen, nitrate, silicate and phosphate). Attention type and masking strategy strongly affected imputation accuracy and smoothness of the produced oceanographic fields. Best results were achieved by factorised time-space attention and combined geographic and per-sample masking. The combined masking strategy reduced the imputation error by 14.3% compared to per-sample masking only. Uncertainties were moderately well calibrated (miscalibration area at observed locations $0.074\pm0.012$) and moderately correlated with the imputation error.
