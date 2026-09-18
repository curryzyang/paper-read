# ULOHA: An Underwater Bimanual Robot System for Robot Learning

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Masato Kobayashi, Takeru Tsunoori
- 机构：Kobe University, The University of Osaka
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19200v1) · [PDF](https://arxiv.org/pdf/2609.19200v1)

## TLDR
ULOHA is an integrated underwater bimanual robot learning platform that combines custom leader–follower hardware with LeRobot-based software for teleoperation, demonstration collection, policy training, and autonomous deployment, enabling real-water evaluation of ACT, Diffusion Policy, and SmolVLA on coordinated bimanual tasks and studies of underwater challenges such as bubble disturbances, buoyancy-driven motion, execution horizons, and air–water policy transfer.

## Abstract
Underwater visuomotor policy learning has focused primarily on single manipulators, while bimanual imitation learning has been studied largely in air. We present ULOHA, an underwater bimanual robot learning platform that combines custom-designed leader--follower hardware with software extensions to LeRobot, integrating teleoperation, multi-view sensing, demonstration collection, policy training, and autonomous deployment. Real-robot experiments demonstrate a range of coordinated underwater bimanual behaviors, including inter-arm transfer, shared-object manipulation, and buoyancy-driven interception. We evaluate ACT, Diffusion Policy, and the vision--language--action model SmolVLA on the platform. We investigate how learning methods and execution strategies developed for manipulation in air perform underwater, examining bubble disturbances, buoyancy-driven object motion, action-execution horizons, and real-time chunking. A separate single-arm study examines policy transfer between air and water and shows that demonstrations spanning both media support execution in both under the tested conditions. ULOHA provides a unified experimental platform for studying underwater bimanual robot learning under the coupled perceptual and physical effects of underwater environments. Additional material: https://mertcookimg.github.io/uloha/
