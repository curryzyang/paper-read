# Compressed Per-Player Local Methods for Multiplayer Federated Learning: Exact Convergence via Increment Sharing

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Bhavika Balani, TaeHo Yoon, Nicolas Loizou
- 机构：Johns Hopkins University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08686v1) · [PDF](https://arxiv.org/pdf/2611.08686v1)

## TLDR
The paper reformulates PEARL-SGD for multiplayer federated learning to communicate local strategy increments rather than full strategies, enabling compressed communication with exact convergence and yielding new compressed and variance-reduced variants (C-PEARL-SGD, PEARL-SVRG, and C-PEARL-SVRG) with unified convergence guarantees.

## Abstract
Multiplayer Federated Learning (MpFL), introduced by Yoon et al. (2025), extends classical federated learning to settings where clients are rational players in a game with individual objectives and strategies, seeking an equilibrium. A natural baseline is Per-Player Local SGD (PEARL-SGD), where each player performs several local SGD steps before exchanging strategies through a central server. However, the original PEARL-SGD formulation does not extend cleanly to compressed communication. Directly compressing the players' strategies can prevent convergence to the equilibrium, even with deterministic gradients. To address this issue, we reformulate PEARL-SGD so that players communicate local strategy increments rather than the strategies themselves. Without compression, the two formulations are equivalent, but with compression, increment sharing preserves exact convergence, allowing us to design the communication-efficient compressed PEARL-SGD (C-PEARL-SGD). Beyond compression, we also consider variance reduction as another axis of improvement, introducing PEARL-SVRG and its compressed variant C-PEARL-SVRG. Under the original MpFL assumptions, we establish convergence guarantees for all variants through a unified parametric inequality. Numerical experiments, including distributed spectrum sensing, demonstrate the practical benefits of our methods over vanilla PEARL-SGD.
