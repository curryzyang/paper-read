# Human-Centric Grasp State Assessment: Toward Transferring Subjective Evaluation to Robots

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Ryohei Kobayashi, Kosei Isomoto, Yuga Yano, Yuichiro Tanaka, Hakaru Tamukoh
- 机构：Kyushu Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17540v1) · [PDF](https://arxiv.org/pdf/2609.17540v1)

## TLDR
The paper proposes a human-centric framework that uses a vision-language model with few human-annotated anchors to semi-automatically generate supervision and trains a lightweight predictor on tactile and grasping-force time series, enabling robots to adjust grasping force on deformable objects according to human subjective grasp appropriateness.

## Abstract
We propose a framework that transfers tacit human subjective criteria to robotic systems for the appropriate grasping of deformable objects. Achieving such behavior is challenging because a semantic gap exists between qualitative human expectations and quantitative robotic measurements. Conventional deep learning approaches for bridging this gap also require prohibitive amounts of manually annotated data for each newly encountered object. To address these challenges, our framework integrates a Vision-Language Model (VLM)-based semi-automated supervisor generator with a lightweight grasp state predictor, using a minimal set of human-annotated trials as contextual anchors to propagate subjective criteria to unannotated data. The prediction model then enables rapid online adaptation by sequentially estimating the grasp state from time-series tactile and grasping force measurements. Through experiments on three representative deformable objects and a human evaluation study with 25 participants, we demonstrate the feasibility of the proposed framework for adjusting grasping force according to human-perceived grasp appropriateness in the evaluated task setting.
