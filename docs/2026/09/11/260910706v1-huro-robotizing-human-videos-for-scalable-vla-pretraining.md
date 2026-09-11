# HuRo: Robotizing Human Videos for Scalable VLA Pretraining

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jinho Jeong, Se June Joo, Jaehyun Kang, Dongyun Kim, Yena Kim, Hanjung Kim, Seon Joo Kim
- 机构：RLWRLD, Yonsei University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10706v1) · [PDF](https://arxiv.org/pdf/2609.10706v1)

## TLDR
HuRo robotizes large-scale heterogeneous human videos into robot-aligned observation–action episodes (~630K episodes/142M frames) and shows that pretraining VLA policies on this scalable data substantially improves real-world manipulation and out-of-distribution robustness.

## Abstract
Human video datasets have emerged as a compelling alternative to expensive real-robot data, offering rich diversity at scale. To bridge the human-to-robot embodiment gap, existing approaches either robotize videos in task-matched settings or address observation and action alignment separately at scale. In this work, we systematically examine whether robotized human videos can provide effective and scalable supervision for pretraining vision-language-action (VLA) policies. To this end, we develop a robotization pipeline that converts heterogeneous human videos into robot-aligned observations and action trajectories while inferring missing intermediate signals across annotation levels. Using this pipeline, we construct the HuRo dataset, comprising about 630K robotized episodes and 142M processed frames from five human-video sources. Across four real-world manipulation tasks, increasing robotized pretraining scale improves overall completion from 51.5% to 80.3% and OOD completion under spatial and visual shifts from 34.9% to 72.2%. Ablations further show that visual robotization improves OOD robustness and that end-to-end pretraining with retargeted actions outperforms visual-only transfer. Code and data are released on our website: https://3587jjh.github.io/HuRo.
