# Opacity of Discrete Event Systems under Sensor Attacks

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Shengbao Zheng, Yu Liu, Shaolong Shu, Feng Lin
- 机构：Tongji University, Shenyang Ligong University, Wayne State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13053v1) · [PDF](https://arxiv.org/pdf/2611.13053v1)

## TLDR
The paper investigates opacity of discrete event systems under sensor attacks in both settings where the user does or does not know the attack model, and develops augmented-automaton and observer-based verification methods, including polynomial algorithms using detectors for weak opacity and non-opacity.

## Abstract
Many information control problems in discrete event systems can be addressed using strong opacity, weak opacity, and non-opacity. These opacities depend on observations. If cyber attackers can attack sensors (or observation channels), then opacities will change. An opaque system may become not opaque, or a not opaque system may become opaque. Therefore, it is important to investigate opacities under sensor attacks. In this paper, we consider opacities under sensor attacks for two settings. The first one is the user has prior knowledge of sensor attacks in which the opacities are called as W-CA-opacities. The second one is the user has no prior knowledge of sensor attacks, and opacities are called as N-CA-opacities. For the former, we construct an augmented automaton that integrates the information of sensor attacks and then converts W-CA-opacities into classical opacities to solve the verification problem. For the latter, we construct the observers for the given system without sensor attacks and with sensor attacks, respectively. We then do the parallel operation on these two observers to obtain a method of verifying N-CA opacities. Furthermore, by adopting the detector technique, we find polynomial algorithms for verifying weak opacity and non opacity for both settings.
