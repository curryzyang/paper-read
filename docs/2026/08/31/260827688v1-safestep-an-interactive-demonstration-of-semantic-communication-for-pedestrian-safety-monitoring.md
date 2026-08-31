# SafeStep: An Interactive Demonstration of Semantic Communication for Pedestrian Safety Monitoring

- 区域：速读区
- 排名：3
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Christian McDowell, Andrea Panebianco, Jeremiah Yang, Sirin Chakraborty, Samuel Chamoun, Travis Ross, Yin Sun
- 机构：Auburn University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27688v1) · [PDF](https://arxiv.org/pdf/2608.27688v1)

## TLDR
SafeStep is an interactive browser-based semantic communication platform that demonstrates live pedestrian safety monitoring from traffic cameras, allowing users to compare Meta-VIB against baseline transceivers under varying SNR, codelength, and Age of Information, and is the first real-time system to make AoI-induced degradation directly observable in live monitoring.

## Abstract
In this paper, we develop SafeStep, an interactive browser-based semantic communication platform for live pedestrian safety monitoring. SafeStep extracts pedestrian information from four live traffic-camera feeds, transmits it through a semantic communication transceiver over an Additive White Gaussian Noise (AWGN) channel, and renders user-specific positions, trajectories, and risk labels. The platform allows to independently select the transceiver, Signal-to-Noise Ratio (SNR), codelength, and Age of Information (AoI), and demonstrates the transceiver performance of the selected configuration through live pedestrian safety monitoring to each browser. SafeStep compares a recently proposed semantic communication design called Meta-VIB with five baseline transceivers. Meta-VIB uses a compact neural model with only $4.16$ million parameters to generalize across varying SNR, codelength, and AoI values without online retraining. Experimental results show that Meta-VIB achieves mean task-loss reductions of up to $92.1\%$. On one high-end GPU server, the integrated concurrent-access workload maintains the target $5$ frames/s through $20$ users. At $100$ users, each requesting a distinct configuration, SafeStep records no request failures and a mean application response time below $1$ s, but its mean per-browser frame rate falls to approximately $1$ frame/s. To our knowledge, SafeStep is the first real-time semantic communication platform to make AoI-induced downstream degradation directly observable in live monitoring applications.
