# Towards an approach to multivariate outlier detection for District Heating System data

- 区域：速读区
- 排名：14
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Rajko Turudija, Dušan Stojiljković, Milan Zdravković, Marko Ignjatović
- 机构：University of Niš
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11375v1) · [PDF](https://arxiv.org/pdf/2608.11375v1)

## TLDR
The paper evaluates several multivariate outlier detection methods on district heating substation data (transmitted heat energy and ambient temperature) and adopts an ensemble of PCA, Isolation Forest, and Hotelling's T-squared test to identify irregular plant operation and reduce gas consumption and CO2 emissions.

## Abstract
In this paper, we test different methods for multivariate detection of outliers in the data of transmitted heat energy in the selected substation of local District Heating System, by also considering outside ambient temperature, namely Z-score (univariate, as a benchmark), Mahalanobis distances, Principal Component Analysis (PCA), Isolation Forest and Hotelling's T-squared test. The overall research aims at uncovering irregular plant operation, with a wider objective of identifying the opportunities for reducing the consumption of gas in central heating plants as well as the CO2 emission. The proposed approach considers specific domain circumstances, such as irrelevance of zero transmit-ted energy timepoints as indication of off-grid plant. The outcomes of the different methods are discussed with domain experts. It was concluded that PCA, Isolation Forest and Hotelling method provide relevant results. Finally, we adopt the ensemble method (selection based on the agreement of all three methods on the detected outliers) as the final approach.
