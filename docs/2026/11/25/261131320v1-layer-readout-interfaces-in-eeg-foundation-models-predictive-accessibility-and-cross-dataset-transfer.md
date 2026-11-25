# Layer-Readout Interfaces in EEG Foundation Models: Predictive Accessibility and Cross-Dataset Transfer

- 区域：速读区
- 排名：6
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Yanlin Fu, Wei Liu, Liming Zhao
- 机构：QMindTech
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31320v1) · [PDF](https://arxiv.org/pdf/2611.31320v1)

## TLDR
By disentangling readout design from layer depth in frozen EEG foundation models, the paper shows that better final-layer readout recovers much of the apparent intermediate-layer advantage, while intermediate layers still add predictive utility and source-selected layer-readout interfaces transfer across datasets, reducing target-side layer search.

## Abstract
Intermediate layers often outperform final layers when foundation models are used as frozen feature extractors, but the source of this advantage is unclear. We study this question in EEG foundation models by separating three factors: how representations are read out, whether intermediate layers provide predictive utility beyond the final-layer interface, and whether useful depth structure transfers across datasets. Across five models and three tasks, improving the final-layer readout consistently recovers substantial predictive performance, yet intermediate layers remain advantageous within frozen extraction. We also find that layers selected on one dataset remain useful on another across five dataset pairs and four task families, and that a compact set of source-derived task directions retains predictive value after transfer in sleep staging. Together, these results show that predictive utility varies across depth, and its usefulness depends on how representations are read out and transferred. More crucially, source-selected layers provide a reusable feature interface across datasets, reducing the need for target-side layer search while outperforming final-layer baselines on target datasets.
