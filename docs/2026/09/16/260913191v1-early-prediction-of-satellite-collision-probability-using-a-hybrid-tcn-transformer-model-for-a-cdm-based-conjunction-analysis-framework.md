# Early Prediction of Satellite Collision Probability Using a Hybrid TCN-Transformer Model for a CDM-Based Conjunction Analysis Framework

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Rabia Tüylek Tok, Burak Yağlıoğlu, Enes Dağ, Emre Onur Kahya
- 机构：TÜBİTAK UZAY, Istanbul Technical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13191v1) · [PDF](https://arxiv.org/pdf/2609.13191v1)

## TLDR
This paper proposes a hybrid TCN–Transformer model that predicts the next CDM’s collision probability from sequential, physically enriched conjunction data to enable earlier and more consistent satellite collision risk assessment in LEO.

## Abstract
The rapid expansion of operational satellites and orbital debris has increased the frequency of close approach events in low Earth orbit (LEO), creating a higher operational burden for satellite operators. This problem is especially critical for satellites using electric propulsion, where low-thrust maneuver capability imposes additional time constraints on collision avoidance planning. In current practice, Conjunction Data Messages (CDMs) provide relative state, covariance, miss distance, time of closest approach, and probability of collision (PoC) information for conjunction assessment. However, the nonlinear propagation of orbital uncertainties and the sensitivity of PoC to covariance evolution make the interpretation of sequential CDMs challenging. This study proposes a learning-based framework for early prediction of satellite conjunction risk by estimating the PoC expected in the subsequent CDM update of the same close approach event. In the proposed methodology, an Unscented Transform-based propagation and backpropagation framework is first used to evaluate the sensitivity of the collision risk metric to CDM parameters. In addition, Principal Component Analysis is applied to the numerical CDM parameters to identify the features most relevant to PoC variation. The results obtained from the sensitivity analysis and PCA are then used to justify the selected raw CDM parameters and to construct derived metrics representing relative motion, encounter geometry, and covariance-related uncertainty. Using the resulting sequential enriched conjunction dataset, a hybrid Temporal Convolutional Network (TCN)-Transformer model is trained to learn the temporal evolution of conjunction risk. The framework is applied to CDMs received and analyzed within TÜBİTAK UZAY, demonstrating its potential for earlier and more consistent operational risk evaluation for LEO satellite conjunctions.
