# WISP: Composable Representations for Wrist-Worn Activity Recognition

- 区域：速读区
- 排名：14
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Zipeng Wu, Shiqiao Zhou, Fabian Spill, James Andrews
- 机构：University of Birmingham
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28033v1) · [PDF](https://arxiv.org/pdf/2611.28033v1)

## TLDR
WISP introduces a wrist-only HAR benchmark and a composable representation space that combines complementary wrist-motion patterns—such as local shape, rhythm, temporal order, and cross-axis relationships—to outperform external baselines on wrist-worn activity recognition (70.20% vs. 59.62% mean Macro-F1).

## Abstract
Smartwatches and fitness bands are among the most common wearable devices, and large national health studies record movement at the wrist. Yet existing human activity recognition benchmarks mix sensors worn on different parts of the body, so they do not show how well activities can be recognised from the wrist alone. We introduce WristHARBench, a benchmark that standardises participant-disjoint evaluation across nine wrist-acceleration datasets and two additional multichannel inertial datasets. We hypothesise that different human activities leave complementary patterns in wrist motion, such as local shape, rhythm, temporal order and cross-axis relationships, and propose WISP (Wrist-Informed Space of Predictive Representations), a composable representation space that combines representations of these patterns with compatible classifiers. Across the nine primary datasets, WISP with random search achieves 70.20% mean Macro-F1, compared with 59.62% for the strongest of 18 external baselines. Controlled ablations and baseline comparisons indicate that recognition improves mainly when a representation adds motion patterns that the others lack, rather than when it represents the same pattern in a different way.
