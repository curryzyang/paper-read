# QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series Forecasting

- 区域：精读区
- 排名：1
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Shah Nawaz Haider, Steve Austin, Arnab Barua, Sarowar Morshed Shawon, Hadaate Ullah
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02632v1) · [PDF](https://arxiv.org/pdf/2607.02632v1)

## TLDR
QuantFlow integrates inverted embedding, bidirectional Mamba state-space decoders, quantile regression, TSMixup augmentation, and federated learning to enable scalable, uncertainty-aware, and privacy-preserving probabilistic time-series forecasting, achieving strong centralized performance and retaining useful accuracy in a 20-client non-IID federated setting.

## Abstract
Time-series forecasting supports decisions in finance, en-ergy, transportation, public health, and industrial monitoring. Recent foundation models improve transfer across forecast-ing tasks, but many depend on centralized data and Trans-former attention, which restricts their use for long, high-di-mensional, and privacy-sensitive signals. This paper presents QuantFlow, a probabilistic forecasting framework that com-bines inverted sequence embedding, bidirectional Mamba state-space decoders, quantile regression, and federated learning. Each variable is embedded over the complete ob-servation window, processed in forward and reverse direc-tions, and projected to five conditional quantiles. TSMixup expands temporal diversity through Dirichlet-weighted inter-polation while preserving sequence structure. Experiments cover cryptocurrency, traffic, electricity, Electricity Trans-former Temperature, influenza, and weather data. QuantFlow obtains mean squared errors of 0.2834 on ETTm1 and 0.2218 on Weather, and a 20-client non-IID deployment retains use-ful accuracy after three communication rounds without cen-tralizing raw records. The results indicate that selective state-space modelling is a promising basis for scalable, uncer-tainty-aware, and privacy-conscious time-series prediction, while also revealing limitations on irregular epidemiological signals and long-horizon generalization.
