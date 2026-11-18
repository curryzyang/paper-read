# FACE: Flow-Guided Angular Channel Estimation Framework for mmWave MIMO Systems

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Samitha Gunarathne, Eslam Eldeeb, Nurul Huda Mahmood, Matti Latva-aho
- 机构：University of Oulu
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21698v1) · [PDF](https://arxiv.org/pdf/2611.21698v1)

## TLDR
FACE introduces a flow-matching-based generative prior within a plug-and-play framework to exploit angular sparsity for accurate, pilot-efficient, and computationally efficient mmWave MIMO channel estimation, outperforming conventional and diffusion-based estimators with fewer sampling steps.

## Abstract
Acquiring accurate channel state information (CSI) is essential for millimeter-wave (mmWave) multi-input multi-output (MIMO) systems. However, it remains challenging due to high-dimensional channels, limited pilot observations, and measurement noise. To address these challenges, we propose flow-guided angular channel estimation (FACE), a novel channel estimation framework based on flow matching, an emerging generative modeling paradigm that learns continuous transport dynamics between probability distributions. FACE exploits the inherent angular-domain sparsity of mmWave channels and incorporates the learned flow matching model as a generative channel prior. Numerical results show that FACE consistently achieves higher channel estimation accuracy than both conventional estimators and diffusion-based generative estimator across diverse channel and system configurations. Moreover, FACE maintains high estimation accuracy with fewer pilot observations and achieves an average achievable rate close to the perfect-CSI benchmark. Compared with diffusion-based estimation, FACE requires substantially fewer sampling steps while achieving superior or comparable estimation accuracy, reducing inference time and computational cost. Overall, the proposed framework demonstrates the potential of flow matching for accurate, pilot-efficient, and computationally efficient mmWave MIMO channel estimation.
