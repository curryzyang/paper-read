# Sequential Testing on Complex and High Dimensional Data Streams Leveraging Unsupervised Model Errors

- 区域：速读区
- 排名：4
- 匹配度：3.7/10
- 来源：arxiv
- 作者：George Stamatelis, Iordanis Koutsopoulos
- 机构：Athens University of Economics and Business
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33238v1) · [PDF](https://arxiv.org/pdf/2611.33238v1)

## TLDR
The paper proposes distribution-free sequential hypothesis testing and change-point detection methods for complex, high-dimensional data streams that require only null/pre-change data and monitor the clipped errors of an unsupervised model trained on that data, leveraging performance degradation on out-of-distribution data to provide rigorous error and detection-delay guarantees while remaining highly scalable.

## Abstract
We propose two general, distribution-free test statistics for binary Sequential Hypothesis Testing (SHT) and Sequential Change Point Detection (SCPD) respectively, in streaming environments where the data (e.g., network traffic metadata) are too complicated for the exact probabilistic modeling required by conventional likelihood ratio-driven tests. Our framework also addresses the challenge of information asymmetry, where data is available only from the null/pre-change regime and not from the alternative/post-change one such as zero-day attacks or emerging disease related regimes. The proposed statistics monitor the errors of a predictive or reconstructive machine learning model trained solely on null/pre-change data, relying on imperfect generalization (the model's performance will degrade when deployed on data from the alternative/post-change class). Under mild assumptions on the model's errors, we establish rigorous analytical guarantees: strict non-asymptotic error control for SHT, and explicit bounds on the Average Run Length (ARL) and the Expected Detection Delay (EDD) for SCPD. Extensive evaluations in target tracking, chaotic dynamical systems, and real-world network security datasets, demonstrate that our framework consistently satisfies prescribed constraints where existing algorithms succumb to inflated missed detections and/or false alarms. Finally, because our methods operate on scalar errors without requiring online retraining or kernel evaluations, they are highly scalable.
