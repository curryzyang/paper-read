# FERRETS: A Scalable Symbolic Transform for Time Series Classification

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Antoine Guillaume
- 机构：Novahe
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33249v1) · [PDF](https://arxiv.org/pdf/2611.33249v1)

## TLDR
FERRETS is a fast, label-free symbolic dictionary transform for time series classification that encodes random windows into exact 8-bit words with additional level and cross-channel words, enabling linear-time/streaming training and competitive accuracy while being substantially faster than leading methods.

## Abstract
Dictionary methods for time series build bags of symbolic words from subsequences, but the accurate ones scale poorly. Against other families of methods, their accuracy no longer pays for their cost. We present FERRETS, a label-free dictionary transform built on WEASEL~2. It keys windows of random length and dilation into exact eight-bit words, adds a level word of each window's mean and spread, and on multivariate data adds cross-channel words. We compare it with leading classifiers, deep networks and foundation models included, on the UCR, Multiverse and MONSTER archives. FERRETS is the fastest of the eleven methods timed on UCR under a ten-thread budget. Of the ten others, only MultiRocket-Hydra is significantly more accurate, taking 24.7 times as long. FERRETS is not significantly different from WEASEL~2, the most accurate earlier dictionary method, which takes 125 times as long, and is significantly ahead of the other dictionary methods. On the Multiverse core, it is not significantly different in accuracy from HIVE-COTE~2 and MultiRocket-Hydra, though behind both on UCR. It is also significantly more accurate than five frozen foundation models on UCR's published split. On the MONSTER problems both complete, MiniRocket takes 3.7 times as long to fit as the streaming FERRETS classifier, which is significantly more accurate.
