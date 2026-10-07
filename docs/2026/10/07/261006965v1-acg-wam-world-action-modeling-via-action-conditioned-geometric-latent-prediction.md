# ACG-WAM: World-Action Modeling via Action-Conditioned Geometric Latent Prediction

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Jiangtao Liu, Zishang Xiang, Yage He, Lingguo Cui, Baihai Zhang, Runqi Chai, Senchun Chai
- 机构：Beijing Institute of Technology, LimX Dynamics
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06965v1) · [PDF](https://arxiv.org/pdf/2610.06965v1)

## TLDR
TLDR: ACG-WAM improves world-action robot policies by adding an auxiliary ACG-JEPA objective that predicts action-conditioned geometric features of future observations from a frozen VGGT teacher using the current observation and intervening actions, supervising the shared visual embedding before temporal mixing and removing the auxiliary modules at inference, achieving strong RoboTwin 2.0 and real-robot manipulation results.

## Abstract
World action models jointly learn visual predictionand robot actions, providing a way to use observations ofscene evolution for policy learning. Their video and actionlosses, however, provide no explicit target for the geometricconsequences of a demonstrated action sequence. Moreover,visual features taken after temporal attention can contain futureobservations, making them unsuitable as the sole current visualinput to an auxiliary predictor. We introduce ACG-WAMand its auxiliary objective, the Action-Conditioned GeometricJoint-Embedding Predictive Architecture (ACG-JEPA), whichpredicts geometric features at several horizons from the currentobservation and intervening actions, using the future slot of afrozen VGGT encoding of each current and future image pairas the target. We apply this supervision from the head and wristcameras to a shared visual embedding before temporal mixing,and remove the teacher and auxiliary modules at inference.On 50 RoboTwin 2.0 tasks, ACG-WAM achieves 93.46%success in clean scenes, with the best randomized success(92.68%) and mean across both settings (93.07%) among thecompared methods; across three tasks on a real robot, itachieves 85.00% success and 91.67% partial completion score,exceeding Motus by 10.00 and 9.17 percentage points, respec-tively. Code:https://github.com/RoboOpus/ACG-WAM.Website:https://RoboOpus.github.io/ACG-WAM.
