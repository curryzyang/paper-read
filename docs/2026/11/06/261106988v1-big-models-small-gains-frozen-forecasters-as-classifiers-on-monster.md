# Big Models, Small Gains: Frozen Forecasters as Classifiers on MONSTER

- 区域：速读区
- 排名：11
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Rishit Jain, Rishit Kar, Chetashri Bhadane, Nilesh Patil
- 机构：University of Mumbai
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.06988v1) · [PDF](https://arxiv.org/pdf/2611.06988v1)

## TLDR
Frozen forecasting foundation models improve over random-weight controls on most MONSTER datasets but do not reliably outperform strong non-pretrained time series classifiers, even when labels are scarce.

## Abstract
Forecasting foundation models are increasingly used as frozen feature extractors for time series classification, but it remains unclear whether their pretrained representations offer an advantage over strong classifiers that do not require pretraining. This raises an important question: do these representations provide useful information beyond what the model architecture alone can capture, particularly when labelled data are scarce? We present a controlled benchmarking of two forecasting models, Reverso and Chronos-Bolt, on six large datasets from the MONSTER benchmark, using 1%, 10%, and 100% of the available training labels. We compare their frozen representations against four established time series classification methods and random-weight versions of the same forecasting models. Our results show that pretraining improves classification accuracy over random-weight counterparts on five of the six datasets, with gains of up to 23 percentage points. However, the frozen representations do not reliably outperform the strongest non-pretrained baseline in any setting: they perform worse in 15 of 17 settings and tie in the remaining two. Further experiments show that restoring amplitude information recovers part of the performance gap, while fine-tuning and forecast-error features do not close it. These findings highlight the importance of strong task specific baselines and random weight controls when evaluating forecasting foundation models for classification. Our code is available at https://github.com/Rachet2006/frozen-forecasters-monster.
