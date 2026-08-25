# Infrared Hotspot-Guided Early Warning of Lithium-Ion Battery Thermal Runaway Under Mechanical Abuse

- 区域：速读区
- 排名：10
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Syed Sajid Ullah, Salman Khan, Muhammad Zunair Zamir
- 机构：Chang'an University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20383v1) · [PDF](https://arxiv.org/pdf/2608.20383v1)

## TLDR
The paper proposes a two-stage, leakage-controlled early-warning framework that distills infrared hotspot dynamics into an interpretable thermal-instability score before fusing it with multimodal features to predict lithium-ion battery thermal runaway 20 frames ahead, outperforming direct multimodal fusion while achieving a 14.8-frame mean lead time.

## Abstract
Mechanical abuse can trigger thermal runaway (TR) in lithium-ion batteries through localized heat generation before sensor signals become decisive. This paper proposes a two-stage early-warning approach that estimates localized thermal instability from infrared hotspot dynamics and then fuses this instability score with mechanical, electrical, thermal, and image-intensity features for a 20-frame warning horizon. Evaluation uses repeated experiment-wise three-fold validation, with out-of-fold Stage-I scores during Stage-II training to prevent stacked-model optimism. Hotspot dynamics alone achieve Stage-I ROC-AUC 0.945, and the two-stage classifier reaches Stage-II ROC-AUC 0.908, exceeding direct multimodal fusion while preserving an interpretable intermediate instability signal. Thermal gradient rise precedes voltage-based detection by 40 frames (4 seconds) on average, enabling earlier battery management system intervention. Lead-time analysis at a fixed 0.5 threshold yields a 14.8-frame mean lead time.
