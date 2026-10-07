# Learning to Remember: Distilling Memory Retention for Compact Recurrent Neural Networks

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Nilushika Udayangania, Kishor Nandakishora, Marimuthu Palaniswami
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06942v1) · [PDF](https://arxiv.org/pdf/2610.06942v1)

## TLDR
The paper introduces Memory-Discrepancy Knowledge Distillation (MemKD), a knowledge distillation framework that uses a specialized loss to align teacher and student memory retention across time-series subsequences, enabling compact recurrent neural networks to match teacher performance while significantly reducing parameters and memory usage.

## Abstract
Deep learning models, particularly recurrent neural networks and their variants, such as long short-term memory, have significantly advanced time series analysis. These models capture complex, sequential patterns in time series, enabling real-time assessments. However, their high computational complexity and large model sizes pose challenges for deployment in resource-constrained environments, such as wearable devices and edge computing platforms. Knowledge Distillation (KD) offers a solution by transferring knowledge from a large, complex model (teacher) to a smaller, more efficient model (student), thereby retaining high performance while reducing computational demands. Current KD methods, originally designed for computer vision tasks, neglect the unique temporal dependencies and memory retention characteristics of time series models. To bridge this gap, we propose a novel KD framework termed Memory-Discrepancy Knowledge Distillation (MemKD). MemKD leverages a specialized loss function to capture memory retention discrepancies between the teacher and student models across subsequences within time series data, ensuring that the student model effectively mimics the teacher's behaviour. This approach facilitates the development of compact, high-performing recurrent neural networks suitable for real-time, time series analysis tasks. We provide additional experiments, in-depth theoretical analysis, and insights into the proposed framework across extended time series benchmarks. Our experiments demonstrate that MemKD significantly outperforms state-of-the-art KD methods. Additionally, we demonstrate that it can match the teacher model's performance across a wide range of compression levels, achieving notable reductions in parameter count and memory usage without a significant loss in accuracy.
