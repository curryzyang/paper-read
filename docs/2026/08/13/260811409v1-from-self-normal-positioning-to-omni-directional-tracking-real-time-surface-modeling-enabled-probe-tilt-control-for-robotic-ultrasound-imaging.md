# From Self-Normal-Positioning to Omni-Directional Tracking: Real-Time Surface Modeling Enabled Probe Tilt Control for Robotic Ultrasound Imaging

- 区域：速读区
- 排名：6
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Xihan Ma, Haichong Zhang
- 机构：Worcester Polytechnic Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11409v1) · [PDF](https://arxiv.org/pdf/2608.11409v1)

## TLDR
A robotic ultrasound framework using dual RGB-D perception and quadratic surface modeling enables real-time omni-directional probe tilt tracking relative to the body surface, achieving low angular error and clinically useful non-normal views for echocardiography.

## Abstract
Ultrasound (US) provides real-time, radiation-free imaging, but the image quality depends strongly on how the probe is oriented against the patient body. Robotic US can reduce operator workload and improve acquisition consistency; however, most existing systems focus on normal positioning, where the probe is maintained perpendicular to the local surface. This constraint is inadequate for examinations like echocardiography, where obtaining a diagnostic view requires a non-normal probe angle. Consequently, a clinically useful robotic system must sense the local surface in real-time and preserve the desired probe orientation. Here, we propose an omni-directional probe-orientation control framework that integrates RGB-D perception, local-surface modeling, and task-space orientation control. The surface model fuses multi-view point clouds and provides a quadratic estimate of the local surface. A desired imaging direction is then encoded relative to the normal, enabling the probe to track arbitrary angles. The framework was evaluated through flat-surface tracking, phantom target-angle recovery, and in-vivo tracking of an expert selected view. Results show that the mean angular tracking error was 1.06 +- 0.66 deg. The system recovered a non-normal tilt angle of up to 44.39 +- 2.59 deg relative to the surface normal, and acquired the desired heart chamber view in the phantom and in-vivo experiments.
