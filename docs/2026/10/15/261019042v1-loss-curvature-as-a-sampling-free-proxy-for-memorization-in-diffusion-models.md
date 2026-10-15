# Loss Curvature as a Sampling-Free Proxy for Memorization in Diffusion Models

- 区域：精读区
- 排名：3
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Shashank Sule, Xinyue Yu, Boonam Shin, Yuxuan Liu, Abolfazl Hashemi, Hayden Schaeffer
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19042v1) · [PDF](https://arxiv.org/pdf/2610.19042v1)

## TLDR
This paper proposes input loss curvature as a sampling-free proxy for memorization in diffusion models, showing that training-averaged curvature predicts when models begin regurgitating training data and that input-dependent curvature, theoretically linked to counterfactual memorization via the leave-one-out model, indicates which samples are likely to be memorized.

## Abstract
Understanding the mechanism behind why diffusion models memorize their training data remains an open question in generative modeling. In this paper, we examine this question from two perspectives: (a) the model-level perspective concerning the onset of memorization in a model during training, and (b) the sample-level perspective concerning the proclivity of an individual sample to be memorized by a given model. We show that the so-called input loss curvature, or the Frobenius norm of the Hessian of the diffusion model's training loss, is an effective metric for quantifying both perspectives on memorization. In particular, we empirically demonstrate that input curvatures averaged across training and validation samples can identify when a model is likely to start regurgitating its training data when tracked over training time. However, this metric is not sufficient for measuring an individual sample's likelihood of being memorized. To address this perspective, we introduce a counterfactual definition of memorization in diffusion models, extending the analogous notion from supervised learning proposed by [Feldman, 2019]. We prove that this counterfactual memorization is controlled by the input curvature of the leave-one-out model, thus establishing a direct theoretical link between a sample's local loss landscape and its generation likelihood. We validate our derived bounds through several empirical experiments and show that input-dependent curvature provides a proxy for memorization.


## 精读解读（中文）
### 一、研究动机
扩散模型为何以及何时记忆训练数据仍是生成建模中的开放问题，且现有检测常依赖采样或仅关注模型整体行为。本文从模型级（训练过程中记忆何时开始）与样本级（单个样本为何易被记忆）两个角度研究该问题，并试图找到无需采样即可量化记忆的代理指标。

### 二、技术方案（Method）
论文将扩散模型训练损失关于输入的 Hessian 的 Frobenius 范数定义为输入损失曲率，并对每个样本计算该曲率；在模型级，对训练集与验证集样本的曲率取平均并随训练时间追踪，以识别模型可能开始复述训练数据的时刻。在样本级，论文引入扩散模型的反事实记忆定义，扩展 Feldman 2019 在监督学习中的对应概念，即通过比较包含与移除该样本（leave-one-out）训练所得模型在生成该样本上的似然或表现差异来定义记忆。理论上证明该反事实记忆由 leave-one-out 模型的输入曲率控制，从而建立样本局部损失景观与其生成可能性之间的直接联系；实验上训练扩散模型、计算输入依赖曲率并验证推导出的界。

### 三、结果（Result）
实验表明，训练集与验证集平均输入曲率随训练时间的轨迹能够指示模型何时可能开始 regurgitate 训练数据，但该平均或样本无关曲率不足以判断单个样本被记忆的概率。进一步实验验证了反事实记忆与 leave-one-out 模型输入曲率之间的理论界，说明输入依赖曲率可作为样本级记忆的代理。

### 四、结论（Conclusion）
输入损失曲率是一种采样无关的记忆量化指标，既能在模型级刻画训练过程中记忆 onset，也能在样本级通过反事实记忆与 leave-one-out 曲率建立理论联系。该工作为理解扩散模型记忆机制、检测潜在训练数据泄露以及后续缓解记忆提供了新的分析工具。

### 五、方法论与关键技术细节
关键细节在于曲率定义为训练损失关于输入的 Hessian 的 Frobenius 范数，因此需要二阶梯度或 Hessian-vector product 等实现，计算与显存开销是主要约束；模型级指标依赖对训练集和验证集样本做平均并沿训练时间追踪，样本级指标则依赖反事实/leave-one-out 比较，理论上由 leave-one-out 模型的输入曲率控制。潜在局限包括平均曲率不能直接判定单样本记忆、leave-one-out 或反事实评估可能训练成本高，以及曲率代理会受模型架构、数据分布和扩散噪声调度等因素影响。
