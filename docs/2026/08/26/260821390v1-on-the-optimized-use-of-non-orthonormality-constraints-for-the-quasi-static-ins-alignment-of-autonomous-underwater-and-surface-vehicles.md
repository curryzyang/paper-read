# On the Optimized Use of Non-Orthonormality Constraints for the Quasi-Static INS Alignment of Autonomous Underwater and Surface Vehicles

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Carlos Renato C. Durao, Felipe O. Silva, Itzik Klein, Vinıcius M. G. B. Cavalcanti, Adriano Frutuoso, Ettore A. de Barros, Jay A. Farrell
- 机构：Federal Institute of Education, Science and Technology of Amazonas, Federal University of Lavras, University of São Paulo, University of Haifa, Fluminense Federal Institute of Education, Science and Technology, Zoox, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21390v1) · [PDF](https://arxiv.org/pdf/2608.21390v1)

## TLDR
This paper introduces an optimized TRIAD-CBE method and a novel fine-alignment EKF observation model using TRIAD-derived non-orthonormality error constraints, accelerating INS misalignment and bias convergence from minutes to seconds for autonomous underwater and surface vehicles while maintaining accuracy comparable to traditional techniques.

## Abstract
Inertial navigation systems are specialized navigation apparatuses that equip almost all autonomous underwater and surface vehicles. They require precise initial alignment, i.e., determination of their initial attitude, which is typically achieved: (a) in quasi-static conditions (whenever possible); and (b) in two stages: Coarse Alignment (CA), using methods like TRI-axis Attitude Determination (TRIAD), and Fine Alignment (FA), via Zero Velocity Update (ZVU)-based Extended Kalman Filtering (EKF). However, conventional methods suffer from slow convergence and limited bias estimability. In response, this paper introduces: (a) an optimized version of a recently proposed CA method, namely, TRIAD with Coarse Bias Estimation (TRIAD-CBE); and (b) a novel FA EKF observation model that incorporates Non-Orthonormality (NON) error constraints derived from TRIAD, directly linking these errors to the inertial sensor biases. As validated through extensive Monte Carlo (MC) simulations, as well as real-world experiments using two Inertial Measurement Units (IMUs) of different grades, our approaches substantially accelerate the convergence of misalignment and bias estimates (from minutes to seconds), while maintaining accuracy/precision comparable to traditional techniques.
