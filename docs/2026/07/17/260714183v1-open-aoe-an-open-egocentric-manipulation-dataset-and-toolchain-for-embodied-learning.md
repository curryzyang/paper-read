# Open-AoE: An Open Egocentric Manipulation Dataset and Toolchain for Embodied Learning

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Zishuo Li, Bowen Yang, Changtao Miao, Kai Zhu, Hao Chen, Qingze Guan, Zhengxing Wu, Wanke Zhan, Yang Sun, Zhiyi Huang, Zitong Shan, Zhenchao Jin, Jiadong Hong, Taowen Wang, Yushi Feng, You Liu, Yibo Wang, Yifan Yang, Zhaowen Zhou, Man Luo, Hao Cheng, Bo Zhang, Jianshu Li, Jiansheng Cai, Guocai Yao, Jize Zhang, Chenhao Lin, Renjing Xu, Lequan Yu, Chao Shen, Chunhua Shen, Zhe Li
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14183v1) · [PDF](https://arxiv.org/pdf/2607.14183v1)

## TLDR
Open-AoE provides a large-scale, open-source egocentric manipulation dataset and end-to-end toolchain, from smartphone capture to downstream model training, enabling scalable human-to-robot transfer for embodied learning.

## Abstract
Egocentric videos of human manipulation provide scalable supervision for embodied intelligence, yet existing resources rarely combine low-cost continuous capture, manipulation-level structured annotations, and reusable tools for robot learning. We present Open-AoE, an open, community-oriented egocentric manipulation dataset and toolchain spanning the full pipeline from smartphone capture to model training. Its first release contains approximately 2,000 hours of manipulation video collected in natural environments by 500+ contributors using 400+ smartphones. The dataset provides text annotations, MANO-based hand poses, camera trajectories, and temporally localized atomic actions. Open-AoE further includes a data processing pipeline that transforms raw recordings into structured samples through temporal action segmentation, semantic annotation, hand reconstruction, and camera trajectory reconstruction. Meanwhile, we provide a separate downstream toolchain supports visualization, cross-embodiment retargeting, model-specific data conversion, and training recipes for VLA policies, WAMs, and World Models. By integrating scalable capture, structured processing, and downstream adaptation, Open-AoE reduces the barriers to both data contribution and reuse, providing practical open infrastructure for embodied model training, human-to-robot transfer, and world modeling.
