# SEDR-Seq2P: A Lightweight Dilated Residual Sequence-to-Point Network for Multi-Task Industrial NILM

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Hatem Haddad, Feres Jerbi, Issam Smaali
- 机构：Wattnow
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28693v1) · [PDF](https://arxiv.org/pdf/2607.28693v1)

## TLDR
SEDR-Seq2P, a lightweight dilated residual Seq2Point network with squeeze-and-excitation attention, improves multi-task industrial NILM accuracy while cutting inference latency by ~58% versus WaveNet, offering a favorable accuracy-delay trade-off for scalable deployment.

## Abstract
Industrial NILM remains challenging because measurement noise and widespread concurrent machine operation reduce the generalization of models tuned on residential data. This work adopts a one-to-many, multi-task disaggregation setting, in which a single network estimates multiple industrial machine loads from aggregate power. Under a unified evaluation protocol on IMDELD, we benchmark Seq2Seq, Seq2SubSeq, Seq2Point, GRU, and WaveNet using energy-estimation metrics and the accuracy-delay criterion. While Seq2Point offers a stronger accuracy-delay balance than Seq2Seq/Seq2SubSeq, GRU and WaveNet achieve higher accuracy at markedly higher computational cost. To close this gap, we propose SEDR-Seq2P, a lightweight Seq2Point extension with dilated residual blocks and squeeze-and-excitation attention. Relative to the Seq2Point baseline, SEDR-Seq2P reduces MAE by approximately 7%, improves the coefficient of determination by approximately 1%, and increases the match rate by approximately 0.8%. In addition, compared to WaveNet, SEDR-Seq2P reduces inference latency by approximately 58%, yielding a favorable accuracy-delay trade-off for scalable industrial deployment.
