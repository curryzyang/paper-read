# CGDT-CESN: Correlation-Guided and Dynamics-Trained Clustered Echo State Network for Multivariate Time-Series Prediction

- 区域：速读区
- 排名：6
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Hariharan Srinivasan, Masoom Bhargava, Sayan Gupta
- 机构：Indian Institute of Technology Madras
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22430v1) · [PDF](https://arxiv.org/pdf/2610.22430v1)

## TLDR
CGDT-CESN is a clustered echo state network for multivariate time-series prediction that uses empirically observed inter-variable correlations to guide and train inter-cluster connections, thereby capturing both variable-specific dynamics and cross-variable dependencies more accurately than a conventional ESN.

## Abstract
Accurate prediction of multivariate time series requires models that simultaneously capture variable-specific dynamics and cross-variable interactions. In this work, a Correlation-Guided and Dynamics-Trained Clustered Echo State Network (CGDT-CESN) is proposed, which comprises a modular reservoir architecture with each cluster distinctly specializing in one of the variables in the multivariate time series. An innovative reservoir design is proposed in which inter-cluster connections are enabled by empirically observed correlations among variables, providing a data-driven coupling mechanism. Apart from conventional readout training, inter-cluster connection weights informed by correlations are trained, which in turn allows the reservoir to capture time-varying cross-variable dependencies without sacrificing computational efficiency and further improves forecasting accuracy. The prediction performance of CGDT-CESN is found to be superior to that of the conventional ESN when evaluated on two fundamentally different datasets: Twitter information cascade evolution and solar wind forecasting. Also, the improvement in performance is preserved across multiple prediction horizons, even when presented with a low volume of data. By unifying cluster-specific specialization with learned inter-variable coupling, CGDT-CESN offers a principled, data-driven route to multivariate time series prediction.
