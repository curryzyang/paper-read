# Language-Forcing: Advancing Humanoid Loco-Manipulation via Semantic Alignment of Whole-Body World Action Models

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yanjun Li, Jiarui Ye, Weiyu Guo, Zixiao He, Kangjie Ye, Dihan Wang, Yishuo Cheng, Zishang Xiang, Mingju Gao, Hao Tang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23894v1) · [PDF](https://arxiv.org/pdf/2610.23894v1)

## TLDR
**TLDR:** LANGUAGE-FORCING is a training-only strategy that uses language to align task-relevant future state changes with the intermediate action-conditioned visual features of a whole-body World Action Model, improving humanoid loco-manipulation without adding inference overhead.

## Abstract
World Action Models (WAMs) jointly predict robot actions and future observations. However, their visual prediction objectives do not explicitly distinguish task-relevant transitions from incidental scene changes. For whole-body policies, this distinction matters because task progress depends on coordinated changes in body pose, contact, and object state. We introduce LANGUAGE-FORCING, a training strategy that uses language to emphasize task-relevant changes in the future visual representations of a whole-body WAM. Given paired current and ground- truth short-horizon future frames, a frozen vision-language model assesses task progress and predicts plausible subsequent state changes. We encode these descriptions with a frozen text encoder and align their embeddings with intermediate, action-conditioned future-visual features, complementing the original visual and action prediction objectives. All auxiliary components are used only during training, introducing no additional inference overhead. On HumanoidArena, LANGUAGE-FORCING achieves an average success rate of 79.17%, exceeding the strongest competing policy by 9.46 percentage points and the same WAM without language alignment by 10.77 percentage points. Across five real-world tasks, language alignment raises average success from 53.33% to 71.33% over the same WAM baseline.
