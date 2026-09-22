# ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation

- 区域：速读区
- 排名：10
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Zhengyu Tao, Xin Li, Xin Wang
- 机构：Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20980v1) · [PDF](https://arxiv.org/pdf/2609.20980v1)

## TLDR
ForeTac-VLA is a forecasting-based tactile-vision-language-action model that predicts future tactile states and fuses them with vision-language features to guide action generation, achieving 95% average success across four real-world contact-rich manipulation tasks and outperforming prior VLA and tactile-enhanced VLA baselines.

## Abstract
Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, yet their reliance on visual perception limits robustness in contact-rich environments, where critical physical interaction states may not be visually observable. Existing tactile-enhanced VLA methods improve physical grounding using observed tactile feedback, but most remain largely reactive rather than explicitly modeling how contact may evolve. Therefore, we propose ForeTac-VLA, a forecasting-based tactile-vision-language fusion model that predicts future tactile states to guide action generation. Specifically, ForeTac-VLA encodes recent tactile observations into temporal representations and integrates them with vision-language features through bidirectional cross-attention. Further, a transformer-based forecasting module predicts multi-step future tactile states, enabling the model to reason jointly over observed and anticipated contact. Finally, the fused multimodal representations and predicted future tactile states are fed into the VLA backbone to condition action generation. To stabilize training, a ground-truth-to-prediction curriculum is employed when early forecasts are unreliable. Across four real-world contact-rich manipulation tasks, ForeTac-VLA achieves an average success rate of 95%, outperforming the fine-tuned VLA model by 36.25 percentage points and state-of-the-art tactile-enhanced VLA baselines by over 22 percentage points. ForeTac-VLA also maintains strong performance under low-illumination and visually cluttered conditions. Video demonstrations can be found on https://foretac-vla.github.io/
