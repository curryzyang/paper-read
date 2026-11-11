# INTENT: Out-of-Sample, Out-of-Time, and Cold-Start Evaluation on User Event Sequences

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Mattias Kvist, Erik Lidman Hillbom, Edoardo de Cal, Davis Siemens, Adam Fredriksson, Rickard Brüel-Gabrielsson
- 机构：Unbox AI, KTH AI Society, MIT
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13069v1) · [PDF](https://arxiv.org/pdf/2611.13069v1)

## TLDR
INTENT is a public next-action benchmark that evaluates sequence models across seven cells separating seen vs. new users, pre- vs. post-cutoff time, and seen vs. new items on five audited datasets with per-dataset temporal cutoffs, showing that the evaluation cell changes which model wins and that simply repeating a user’s last item is a strong cold-start baseline.

## Abstract
Banks now train foundation models on ordered sequences of customer events such as transactions, app sessions, and authorizations. Deployed, such a model predicts forward in time, often for customers and merchants absent from training, yet each is evaluated on private data, so no two can be compared. Public benchmarks for such sequences rarely test a period the model has not seen; recommendation studies usually hold out each user's last events instead. We present INTENT (INTEraction, Novelty, and Transfer evaluation for next-action prediction), a public benchmark that scores a model in seven cells defined by whether the user, the period, and the target item appeared in training. An audit of 59 public dataset families retains five datasets; the most common defect is the lack of a calendar timestamp that orders events. No date lies within the time span of all five datasets, so each is split at its own cutoff, chosen by one rule fixed before any model is evaluated. Summed over the datasets, every cell holds at least 111,769 users. In reference results the cell determines the best model: a transformer leads on seen items after the cutoff but scores zero on new items, a variant that embeds item metadata helps mainly on MicroLens, and repeating the user's last item leads on new items in four of five datasets. This parameter-free control also shows that on three datasets most of the score lost after the cutoff reflects changed behavior rather than the model. The pipeline, the cutoff rule, and the per-cell user counts are publicly available.
