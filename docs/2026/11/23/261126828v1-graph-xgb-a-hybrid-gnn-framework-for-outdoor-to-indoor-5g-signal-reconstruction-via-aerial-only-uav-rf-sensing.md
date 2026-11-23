# Graph-XGB: A Hybrid GNN Framework for Outdoor-to-Indoor 5G Signal Reconstruction via Aerial-Only UAV RF Sensing

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：David Hason Rudd, Eunkwang Shin, Nithiwat Pattrapong, Huan Huo, Xiangmeng Wang
- 机构：University of Technology Sydney, The Hong Kong Polytechnic University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26828v1) · [PDF](https://arxiv.org/pdf/2611.26828v1)

## TLDR
Graph-XGB is a hybrid GNN–XGBoost framework that reconstructs multi-floor indoor 5G signal metrics from aerial-only UAV exterior RF measurements by using a floor-aware graph encoder and PCA to create indoor embeddings that are decoded by target-specific XGBoost regressors, achieving strong RSSI/RSRP prediction without any interior RF input.

## Abstract
Delivering robust In-Building Coverage (IBC) is critically impeded by severe Outdoor-to-Indoor (O2I) attenuation, a constraint that intensifies as deployments move from 5G mid-band towards mmWave and prospective 6G sub-THz carriers, where losses of 60-80 dB have been reported across modern building envelopes. While Unmanned Aerial Vehicles (UAVs) offer scalable exterior RF sensing platforms, a fundamental inversion problem persists: interior 3D signal states cannot be directly sampled from constrained exterior flight paths. This paper proposes Graph-XGB, a hybrid inference framework that decouples spatial topology reasoning from non-linear signal regression to resolve this challenge. A modified SpiderGNN encoder, operating on a topology-aware graph constructed with a physically grounded Floor-Aware 3D Distance metric and Bridge Edge Guarantees, propagates UAV boundary measurements into 128-dimensional indoor embeddings. Principal Component Analysis (PCA) compresses these into a 10-dimensional manifold retaining 96.6% of embedding variance, fused with raw spatial features and decoded by independent, physics-tailored XGBoost regressors. This decoupling mitigates the optimization conflict between smoothly decaying path-loss signals and volatile interference-dependent metrics. Evaluated on a real-world 5G NR dataset of 613 verified nodes spanning the 10 floors of a single building, Graph-XGB attains the strongest accuracy among the architectures compared, with $R^2$ of 0.759 (RSSI) and 0.770 (RSRP), improvements of 35.5% and 64.9% over the SimpleGNN baseline, using no interior RF measurement as a model input; indoor observations enter only as training supervision, with evaluation on held-out internal nodes. Interference-dependent targets (RSRQ, SNR and CQI) remain bounded well below the path-loss metrics, delimiting the reach of purely spatial inference.
