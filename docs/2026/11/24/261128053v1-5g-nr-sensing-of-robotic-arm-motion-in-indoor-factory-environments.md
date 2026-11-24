# 5G NR Sensing of Robotic Arm Motion in Indoor Factory Environments

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Neeraj Varshney, Anuraag Bodi, Steve Blandino, Jian Wang, Camillo Gentile, Nada Golmie
- 机构：National Institute of Standards and Technology, Prometheus Computing LLC
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28053v1) · [PDF](https://arxiv.org/pdf/2611.28053v1)

## TLDR
This paper evaluates 5G NR PRS-based monostatic ISAC sensing of an articulated robotic arm in 3GPP indoor factory environments using a measurement-derived kinematic target model, showing high LOS accuracy but severe dense-clutter blockage that reduces detection probability to about 10% and limits ≥90% detection coverage to roughly 13 m in sparse clutter.

## Abstract
This paper investigates the performance of monostatic Integrated Sensing and Communication (ISAC) systems for tracking robotic arm kinematics in industrial factory (InF) environments. Building on a part-specific quasi-deterministic channel model previously derived from high-resolution robotic-arm measurements using our context-aware channel sounder and digital twin, we develop a framework for generating arbitrary articulated motion profiles through hierarchical kinematic transformations. By integrating this high-fidelity target model with the standardized 3GPP InF channel model, we employ 5G New Radio (NR) Positioning Reference Signals (PRS) as the sensing waveform to enable comprehensive system-level evaluation. Simulations are conducted for both sparse clutters (InF-SH) and dense clutters (InF-DH) scenarios using 3GPP-compliant antenna radiation patterns and analog beamforming, allowing us to assess the impact of industrial clutter on sensing performance. The results show that while high estimation accuracy is achievable under Line-of-Sight (LOS) conditions, dense clutter in InF-DH environments introduces severe blockage that significantly limits sensing reliability. In particular, the effective sensing coverage in InF-DH is drastically reduced, with detection probability dropping to approximately \(P_d \approx 10\,\%\) even when the robotic arm is located directly beneath the Transmission Reception Point (TRP). Furthermore, in InF-SH, achieving a high detection probability (e.g., \(P_d \geq 90\,\%\)) requires the target to remain in close proximity to the TRP, with an effective coverage radius of approximately 13 m.
