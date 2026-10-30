# DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Anas Houssaini, Hugo He, Junming Shi, Amin Abyaneh, Ricardo Chahine, Shuo Wen, Mohamad H. Danesh, Charles-Étienne Fréchette, Mariana Sosa Guzman, Mathias Desrochers, Rayan Houssaini, Adam Landa, Theophile Soulie, Charlotte Morissette, Annie Tims, Martino Russi, Jonathan Lussier, Gregory Dudek, Doina Precup, Julen Urain, Hsiu-Chin Lin, David Meger
- 机构：Hugging Face, McGill University, Kinova, Mila, Amazon FAR
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37799v1) · [PDF](https://arxiv.org/pdf/2610.37799v1)

## TLDR
DexSuite is an open-source, all-in-one Genesis-based simulation framework and benchmark for dexterous manipulation that integrates 30 tasks, 100+ single-arm robots and thousands of bimanual configurations, teleoperation, tactile sensing, standardized APIs, and a 4,700-episode demonstration dataset to enable reproducible cross-embodiment training and evaluation.

## Abstract
Human-level dexterity remains a central open problem in robotics, yet few simulation frameworks cover the full workflow of dexterous manipulation, from setting up a robot to collecting dexterous demonstrations and evaluating policies. We present DexSuite, an all-in-one simulation framework for dexterous manipulation built on the Genesis simulator. DexSuite provides 30 tasks and assembles its 10 arms and 12 end-effectors, from parallel-jaw grippers to dexterous hands, into more than 100 single-arm robots and thousands of bimanual pairs. It also ships a standardized environment API, integrated teleoperation, and simulated tactile sensing. Moreover, we define a benchmark of 16 task-embodiment pairs spanning diverse contact complexities and horizons, and release a dataset of 4,700 successful episodes in simulation from human teleoperation, scripted experts, and learned policies. We release DexSuite as open source and hope others will build on it. Videos and datasets are available at https://dexsuiteorg.github.io
