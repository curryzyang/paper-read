# SAFE: Unified Slip and Fracture Detection with Low-Cost Acoustic Sensing in Robotic Grasping

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Zerun Wang, Vivek Kamat, Shekhar Bhansali
- 机构：Georgia Institute of Technology, Vanderbilt University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08802v1) · [PDF](https://arxiv.org/pdf/2610.08802v1)

## TLDR
SAFE is a low-cost, vision-free robotic grasping system that uses two passive PVDF acoustic sensors and motor proprioception with a unified HistGradientBoosting classifier to detect slip, fracture, or normal contact in real time and enable adaptive grasp control with 91.3% success and 82.4% success on unseen objects.

## Abstract
Manipulating fragile objects remains challenging as robots must understand the state of what they grasp, such as slip or fracture, to respond appropriately, especially when material properties are unknown. In this paper, we present SAFE: a low-cost, general-purpose sensing approach that detects both slip and fracture in real time using two passive polyvinylidene fluoride (PVDF) acoustic sensors and motor proprioception, without relying on vision or prior material knowledge. The sensors are mounted on a compliant Fin Ray gripper, and a unified HistGradientBoosting classifier reports the state (normal, slip, or fracture) from a 79-dimensional feature vector. Under leave-one-grasp-out cross-validation, SAFE achieves an Alert-F1 of 0.884 with near-zero slip-fracture confusion, and ablations confirm that acoustic sensing is indispensable. An adaptive grasp controller built on this detection layer runs at 104 Hz on a Jetson Orin Nano, achieving 91.3% success across 46 closed-loop robot trials spanning diverse object categories, while each fixed-force strategy drops to 0% on object conditions that mismatch its preset. It further reaches 82.4% success on novel objects unseen during training, demonstrating robust, failure-aware grasp control without object-specific calibration.
