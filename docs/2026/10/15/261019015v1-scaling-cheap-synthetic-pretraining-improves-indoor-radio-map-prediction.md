# Scaling Cheap Synthetic Pretraining Improves Indoor Radio-Map Prediction

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Khoren Petrosyan, Artashes Mkrtchyan, Rafayel Mkrtchyan, Hrant Khachatrian, Theofanis P. Raptis
- 机构：YerevaNN, Yerevan State University, National Research Council
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19015v1) · [PDF](https://arxiv.org/pdf/2610.19015v1)

## TLDR
By generating 128M synthetic indoor layouts with a fast approximate ray tracer to pretrain ResNet-101 and Swin-T encoder-decoders, this paper shows that scaling cheap synthetic pretraining improves indoor radio-map prediction, reducing error by 15% on average across five benchmark tasks despite simulator mismatch.

## Abstract
Real measurements are too limited to train an accurate indoor pathloss predictor that works across a wide range of buildings. Large-scale synthetic pretraining offers a way forward, but real building layouts are also scarce, and accurate ray-tracing simulators are slow, expensive, and often proprietary. We address both problems by introducing a generator that automatically creates diverse indoor layouts and a fast, open-source approximate ray tracer that computes radio maps for them. Using this pipeline, we generate 128M synthetic samples, pretrain ResNet-101 and Swin-T encoder-decoders, and fine-tune them on high-quality benchmark data. Despite simulator mismatch, our ResNet-101 model reduces error by 15% on average relative to the best known methods across five indoor radio-map prediction tasks and improves transfer on a small real-measurement dataset. Both architectures show predictable data-scaling trends: power laws fitted on 2M-16M samples predict the mean normalized downstream RMSE at 32M-128M with 3.33% mean absolute percentage error for ResNet-101 and 7.10% for Swin-T. These results show that pretraining on large amounts of cheap simulated data can improve indoor radio-map prediction, even when real measurements and high-quality simulations are limited.
