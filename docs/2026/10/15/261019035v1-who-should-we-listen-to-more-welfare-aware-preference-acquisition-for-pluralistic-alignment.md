# Who Should We Listen to More? Welfare-Aware Preference Acquisition for Pluralistic Alignment

- 区域：速读区
- 排名：13
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Ruomeng Ding, Tianwei Gao, Lianrui Geng, Mohit Bansal, Zhun Deng
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19035v1) · [PDF](https://arxiv.org/pdf/2610.19035v1)

## TLDR
The paper introduces Welfare-Aware Preference Acquisition (WAPA), a method that optimally allocates limited human preference feedback across individuals according to a social welfare objective—especially prioritizing underrepresented groups—to improve pluralistic alignment, showing that labeling only 20% of comparisons can recover 75–86% of the predictive utility gap between AI-labeled and fully human-labeled training.

## Abstract
Pluralistic alignment needs to accommodate diverse preferences under limited human feedback. Using AI simulators to label preference comparisons reduces annotation costs, but variation in simulation accuracy across individuals can leave some people's preferences poorly represented in training. We study how to allocate human feedback across people to construct training data for pluralistic alignment, and how this allocation affects the trained policy. To make this allocation explicit and controllable, we define a social welfare objective over individual supervision utilities that measure label quality. Each query's marginal welfare gain depends on its expected supervision improvement, the recipient's current utility, and application-designated priority. Welfare-Aware Preference Acquisition (WAPA) uses auxiliary reference models to estimate query gains and individual utilities, then selects queries by estimated marginal welfare gain while updating recipient utilities. We prove exact optimality of the acquisition algorithm for the estimated welfare objective under a fixed query budget and model predictions. Experiments on six Roleplay collections and four OpinionQA regions demonstrate improved supervision and controllable allocation tradeoffs. Policy training on four Roleplay collections improves preference prediction for both seen and unseen individuals. When prioritizing a designated group and poorly represented individuals, acquiring human labels for 20% of comparisons recovers 75-86% of the average predictive utility gap between policies trained entirely on AI-generated labels and entirely on ground-truth labels.
