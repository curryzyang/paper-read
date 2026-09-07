# AquaBEV: Monocular Underwater BEV Occupancy with 3D Sonar Supervision

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Trung Tien Dong, Shengji Jin, Chen Chen, Yi Sheng, Xiaomin Lin
- 机构：University of Central Florida, University of South Florida
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04411v1) · [PDF](https://arxiv.org/pdf/2609.04411v1)

## TLDR
AquaBEV predicts local bird's-eye-view occupancy from a single underwater RGB image by using paired 3D imaging sonar as geometric supervision during training, leveraging a calibration-free polar representation with causal range decoding—achieving over 4% relative improvement in Visible and Observed IoU compared to transferred terrestrial baselines.

## Abstract
Autonomous underwater robots are widely used for exploration, monitoring, and inspection, where safe navigation depends on understanding the surrounding free and occupied space. Bird's eye view (BEV) occupancy provides such a representation, but predicting it from a single underwater RGB image is difficult due to limited, unreliable geometric cues from appearance alone. 3D imaging sonar offers complementary geometric measurements to supervise this task.
  We introduce AquaBEV, a monocular underwater occupancy model that predicts local BEV occupancy from a single RGB image, using paired 3D imaging sonar as geometric supervision during training. AquaBEV maps visual features into a calibration free polar representation and applies causal decoding along the range dimension before reconstructing the prediction in Cartesian BEV coordinates. A controlled underwater occupancy benchmark was established, adapting representative occupancy methods to the same RGB to sonar task under a unified protocol. AquaBEV achieves 31.4 Visible IoU and 38.6 Observed IoU, 4.0% and 4.3% relative improvements over the strongest transferred baseline.
