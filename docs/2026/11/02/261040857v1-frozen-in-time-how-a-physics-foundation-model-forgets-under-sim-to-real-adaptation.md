# Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation

- 区域：速读区
- 排名：3
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Haaris Mian, Miles Cranmer, Alessandro Favero, Payel Mukhopadhyay
- 机构：Polymathic AI, University of Cambridge
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40857v1) · [PDF](https://arxiv.org/pdf/2610.40857v1)

## TLDR
Finetuning the Walrus-1.3B physics foundation model through two-stage sim-to-real adaptation causes rapid catastrophic forgetting—up to 35× higher one-step errors after just 20 epochs—but replaying as little as 1% simulated data during real-data finetuning recovers most lost simulation performance while retaining effective real-data adaptation.

## Abstract
Scientific foundation models (SciFMs) have achieved remarkable performance on a wide range of PDEs, including the ability to efficiently adapt to unseen data distributions with additional finetuning. As with all neural architectures, finetuning such models comes with the risk of catastrophic forgetting, whereby adapting to new tasks degrades prior knowledge of the model. We study catastrophic forgetting in Walrus-1.3B, a SciFM for continuum dynamics, over the course of a two-stage sim-to-real adaptation: first finetuning on simulated flow around a cylinder and then adapting to experimental data of the same system. We find that finetuning on the simulations rapidly degrades rollout performance on the original pretraining datasets, with one-step errors increasing up to 35x after just 20 epochs. Subsequent adaptation to real data further erodes performance on the simulated task. We characterize the potential drivers of forgetting, such as dataset dependence and task representation similarity. We then show that replaying as little as 1% simulated data during real-data finetuning recovers most of the lost simulation performance while retaining effective adaptation to the experimental dynamics. Our results identify catastrophic forgetting as a practical obstacle to sim-to-real adaptation of SciFMs and show that lightweight replay strategies significantly improve retention.
