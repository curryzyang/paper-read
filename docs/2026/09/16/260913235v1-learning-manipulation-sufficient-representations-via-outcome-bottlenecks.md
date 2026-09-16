# Learning Manipulation-Sufficient Representations via Outcome Bottlenecks

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Md Selim Sarowar, Sungho Kim
- 机构：Yeungnam University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13235v1) · [PDF](https://arxiv.org/pdf/2609.13235v1)

## TLDR
The paper proposes learning a compact, stochastic manipulation-sufficient representation via a policy-free, action-conditioned outcome bottleneck, achieving stronger grasp-outcome prediction and executed-grasp success than reconstructed-geometry baselines with a 512-byte, 16 ms perception-to-decision interface.

## Abstract
Networked manipulation endpoints couple perception to actuation across compute- and bandwidth-limited links, yet commonly exchange dense geometric states optimized for fidelity rather than action outcomes. A stochastic representation is learned with a policy-free, action-conditioned outcome bottleneck: marginal outcome log-loss supplies distortion and a KL term regularizes rate. The construction is motivated by the minimal statistic that preserves the outcome distribution of every admissible action, while the implemented finite model is evaluated as a rate-regularized mixture predictor. The same encoder and outcome head support grasp selection, singleton conformal filtering, active viewpoint selection, and latent test-time adaptation. A finite-probe theorem identifies the local level-set tangent space with the null space of an outcome Jacobian. The synthetic oracle verifies this result; on scanned objects, an analytic surrogate agrees with measured simulator invariances within \(0.56^\circ\). Across 11,979 simulated grasps on 13 objects, a reconstructed-geometry wrench score attains 0.542 AUC against lift success and falls below chance on curved objects, while our representation attains 0.876. At 25\% commitment, executed-grasp success is 0.503 versus 0.984. The 512-byte interface is \(288\times\) smaller than one RGB-D frame and runs at 16\,ms per CPU decision. Independent synthetic points track the tested conformal levels; scanned-object all-pair coverage is reported as a clustered empirical diagnostic. On unseen objects, within-scene AUC falls to 0.569, and a full-feedback update raises empirical mean pairwise coverage from 0.728 to 0.883.
