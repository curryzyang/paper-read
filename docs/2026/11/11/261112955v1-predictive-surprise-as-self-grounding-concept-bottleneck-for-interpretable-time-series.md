# Predictive Surprise as Self-Grounding Concept Bottleneck for Interpretable Time Series

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Sachith Abeywickrama, Emadeldeen Eldele, Min Wu, Xiaoli Li, Chau Yuen
- 机构：A*STAR, Khalifa University, Nanyang Technological University, Singapore University of Technology and Design
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.12955v1) · [PDF](https://arxiv.org/pdf/2611.12955v1)

## TLDR
ConceptTime uses predictive surprise from a frozen probabilistic forecaster as a single self-supervised signal to jointly segment time series and ground an interpretable concept vocabulary, enabling accurate, interpretable, and abstention-capable classification without expert annotations.

## Abstract
Time-series classifiers deployed in risk-sensitive domains must be (1) accurate, (2) interpretable, and (3) able to abstain when evidence is weak. Existing methods do not deliver all 3 at once, and the obstacle is structural, rather than logistical. Meaningful temporal patterns cannot be defined without knowing segment boundaries, yet meaningful boundaries cannot be placed without knowing which patterns to expect. Existing approaches break this circularity by using fixed windows or expert-annotated vocabularies, thereby sacrificing at least one of the 3 properties. We introduce ConceptTime, which closes the loop through a single self-supervised signal. A frozen probabilistic forecaster predicts a distribution over the next observation at every timestep of the sequence. We call the mismatch between its prediction and the realized signal the predictive surprise. This signal both locates segment boundaries and characterizes each resulting segment through the forecaster. Segments are thus grounded by how they behaved relative to expectation, not by what they look like. These summaries cluster into a vocabulary of dynamical regimes that we call concepts. A lightweight head classifies from the concept sequence, and the distance to the nearest concept yields reliability by design. Across 17 public benchmarks, ConceptTime is competitive with state-of-the-art black-box accuracy, beats every interpretable baseline, and retains near-98% accuracy on Epilepsy with 1% of labels. It further remains competitive with softmax, prototype-distance, and SHAP/TimeX/TimeX++ on OOD detection and deletion faithfulness, without a single annotation, language model call, or domain expert. Code is available at: https://github.com/Sachithx/ConceptTime.git.
