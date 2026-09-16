# Discovering and Preserving Category Correlation Knowledge via Adaptive Reciprocal Knowledge Distillation

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Dawen Jiang, Zhishu Shen, Zeyu Liu, Tiehua Zhang
- 机构：Wuhan University of Technology, Tongji University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13199v1) · [PDF](https://arxiv.org/pdf/2609.13199v1)

## TLDR
Adaptive Reciprocal Knowledge Distillation (AR-KD) is a bidirectional distillation framework that adapts the teacher by matching its class-correlation matrix to the student’s relational representation, thereby simplifying overconfident outputs and improving student accuracy on CIFAR-100 and ImageNet-1k.

## Abstract
Knowledge distillation aims to improve the performance of lightweight student models by transferring knowledge from larger and more powerful teacher models. However, a substantial size gap between teacher and student models often impedes effective knowledge transfer. Most existing approaches adopt a static, one-way teacher-to-student distillation paradigm, which overlooks the dynamic nature of student learning and fails to provide targeted guidance on hard samples. In this paper, we propose adaptive reciprocal knowledge distillation (AR-KD), a novel method that improves knowledge transfer by simplifying the teacher's output distribution. Specifically, AR-KD performs reciprocal adaptation on the teacher by matching its class correlation matrix to the student's relational representation, which reshapes the teacher's prediction structure to better suit the student's capacity. This relational alignment mitigates the collapse of inter-class dark knowledge caused by overconfident teachers, enabling the student to learn from richer and more compatible supervisory signals. We evaluate AR-KD on CIFAR-100 and ImageNet-1k classification datasets, where it outperforms state-of-the-art knowledge distillation baselines. Specifically, AR-KD improves student performance across homogeneous and heterogeneous setups: up to 7.13% accuracy gain for students, 1.42% to 4.15% higher than vanilla KD on average, and further improvements when integrated with other advanced methods. Our code is available at https://anonymous.4open.science/r/ARKD/.
