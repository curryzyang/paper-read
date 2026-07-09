# Inertia-1: An Open Exploration of Wearable Motion Foundation Models

- 区域：精读区
- 排名：6
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Zongzhe Xu, Aakarsh Anand, Sarah Jiang, Chuntung Zhuang, Zitao Shuai, Sriram Sankararaman, Yuzhe Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06617v1) · [PDF](https://arxiv.org/pdf/2607.06617v1)

## TLDR
Inertia-1 is an open exploration of wearable motion foundation models that systematically investigates data, model, and training choices using over 18.2 million hours of accelerometer data to achieve state-of-the-art generalization across diverse downstream tasks.

## Abstract
Wearable motion sensing provides a continuous and scalable window into human behavior and health, making it a natural fit for foundation models, yet its pretraining and scaling principles remain poorly understood. Prior work studies isolated design choices, such as sensor placement or sampling frequency, often under fixed settings and narrow downstream tasks that fail to capture real-world sensing diversity. We introduce Inertia-1, a fully open exploration of wearable motion foundation models. Using massive corpora of accelerometer data from global sources spanning more than 18.2M hours, we build a controlled framework for studying the full lifecycle of wearable motion foundation models, covering data choices such as sensor modality, device placement, sampling rate, window length; model choices such as architectures and model size; and training choices such as pretraining objective and data scale. Extensive evaluations across 15 datasets spanning human activity recognition, freezing-of-gait detection, and disease prediction reveal intriguing findings for building motion foundation models that generalize across tasks and sensing conditions. Collectively, Inertia-1 not only presents state-of-the-art recipes for diverse downstream tasks, but also serves as a comprehensive, practical, and open cookbook for wearable motion representation learning.


## 精读解读（中文）
### 一、研究动机
可穿戴运动感知为人类行为与健康提供了连续可扩展的观察窗口，天然适合构建基础模型，但其预训练和缩放原理尚不明确。现有研究多在固定设置和狭窄下游任务下孤立探索传感器放置或采样频率等设计选择，无法反映真实世界感知的多样性，亟需系统性的开放探索。

### 二、技术方案（Method）
使用来自全球来源超过1820万小时的加速度计数据构建大规模预训练语料。建立一个可控框架研究全生命周期设计：数据选择涵盖传感器模态、设备放置位置、采样率、窗口长度；模型选择包括不同架构（如Transformer、CNN）和模型大小；训练选择探索预训练目标（如对比学习、掩码重建）和数据规模。预训练完成后，在15个下游数据集上进行微调评估，覆盖人类活动识别、冻结步态检测和疾病预测等任务。

### 三、结果（Result）
在15个基准数据集上的广泛评估显示，通过系统优化数据、模型和训练选择得到的Inertia-1在多个下游任务中达到最先进性能。研究揭示了构建泛化运动基础模型的关键发现，例如传感器模态和放置位置对迁移能力有显著影响，而更大的模型规模和更长的预训练窗口并不总是带来收益。

### 四、结论（Conclusion）
Inertia-1不仅为多种下游任务提供了最先进的实用配方，还作为可穿戴运动表示学习的全面、开放食谱，填补了该领域从数据到训练再到评估的系统性空白，推动了可穿戴基础模型的发展。

### 五、方法论与关键技术细节
数据规模达1820万小时，涵盖全球多源加速度计数据，确保多样性。实验系统控制了20余种设计变量，包括6种采样率、5种窗口长度、多种模型架构和大小。评估覆盖15个多样化的公开数据集，任务差异大。自监督预训练目标选用对比学习和掩码自编码器，训练超参数如学习率和批量大小经过网格搜索。局限性在于仅使用单模态加速度计数据，未融合陀螺仪等模态，且模型对传感器放置位置的泛化能力仍有提升空间。
