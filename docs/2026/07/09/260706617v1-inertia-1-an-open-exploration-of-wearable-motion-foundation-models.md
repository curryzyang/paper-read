# Inertia-1: An Open Exploration of Wearable Motion Foundation Models

- 区域：速读区
- 排名：2
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Zongzhe Xu, Aakarsh Anand, Sarah Jiang, Chuntung Zhuang, Zitao Shuai, Sriram Sankararaman, Yuzhe Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06617v1) · [PDF](https://arxiv.org/pdf/2607.06617v1)

## TLDR
Inertia-1 presents an open, comprehensive framework for pretraining and evaluating wearable motion foundation models using over 18.2 million hours of accelerometer data, achieving state-of-the-art results across diverse downstream tasks.

## Abstract
Wearable motion sensing provides a continuous and scalable window into human behavior and health, making it a natural fit for foundation models, yet its pretraining and scaling principles remain poorly understood. Prior work studies isolated design choices, such as sensor placement or sampling frequency, often under fixed settings and narrow downstream tasks that fail to capture real-world sensing diversity. We introduce Inertia-1, a fully open exploration of wearable motion foundation models. Using massive corpora of accelerometer data from global sources spanning more than 18.2M hours, we build a controlled framework for studying the full lifecycle of wearable motion foundation models, covering data choices such as sensor modality, device placement, sampling rate, window length; model choices such as architectures and model size; and training choices such as pretraining objective and data scale. Extensive evaluations across 15 datasets spanning human activity recognition, freezing-of-gait detection, and disease prediction reveal intriguing findings for building motion foundation models that generalize across tasks and sensing conditions. Collectively, Inertia-1 not only presents state-of-the-art recipes for diverse downstream tasks, but also serves as a comprehensive, practical, and open cookbook for wearable motion representation learning.
