# Tread: A Visuo-Inertial Framework for Terrain and Locomotion Context-Aware Gait-Phase and Speed Estimation in Wearable Robotics

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Debadrata Sarkar, Akash Bachhar, Aman Arora
- 机构：CSIR-Central Mechanical Engineering Research Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19067v1) · [PDF](https://arxiv.org/pdf/2610.19067v1)

## TLDR
Tread is a visuo-inertial wearable-robotics framework that uses a chest-mounted camera and four lower-limb IMUs in a causal pipeline to anticipate terrain and identify locomotion mode, then uses a probabilistic locomotion context to estimate bilateral gait phase and walking speed with high accuracy.

## Abstract
A wearable assistive robot must continuously estimate terrain, locomotion mode, gait phase, and walking speed. These quantities are commonly addressed by separate, terrain-specific models, with datasets rarely collected under a common protocol. This paper presents a visuo-inertial framework that connects these estimates through a causal pipeline using a chest-mounted camera and four lower-limb inertial measurement units (IMUs). Anticipatory Terrain Perception (ATP) classifies incoming terrain with 96.3% accuracy and anticipates terrain transitions by 1.46 s on average. Terrain-Aware Locomotion Mode Identification (TALMI) achieves 93.7% and 98.8% accuracy for its level-ground and stairs experts respectively, with mean transition latencies being below 200 ms. The relevant TALMI posterior is retained as a Probabilistic Locomotion Context (PLC) vector and provided to a shared Gait Kinematic Encoder (GKE), which supports 50-Hz bilateral gait-phase estimation and 2-Hz walking-speed estimation. Leave-one-subject-out evaluation yields gait-phase RMSEs of 1.75%, 2.97%, and 4.55% for level walking, stair ascent, and stair descent respectively while estimating speed over 3.5-5.5 km/h with a RMSE of 0.218 km/h. All inertial sensing based models use sensor-fused Euler angles as input rather than raw accelerometer and gyroscope signals, reducing dependence on sensor mounting variation.
