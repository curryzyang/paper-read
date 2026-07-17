# Augmentations for Robust and Efficient Imitation Learning in Streamed Video Games

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Somjit Nath, Abdelhak Lemkhenter, Pallavi Choudhury, Chris Lovett, Katja Hofmann, Sergio Valcarcel Macua, Lukas Schäfer
- 机构：McGill University, Mila, Microsoft
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14200v1) · [PDF](https://arxiv.org/pdf/2607.14200v1)

## TLDR
This paper proposes streaming augmentations that simulate common video streaming artifacts to train imitation learning agents that are robust and efficient under both stable and laggy streaming conditions in modern 3D video games.

## Abstract
Imitation learning is an appealing way to scale game-playing agents to complex 3D environments by training policies to map visual observations to actions from human demonstrations. However, these demonstrations are expensive to collect and modern game-playing is often done through streaming in which network delay and compression introduce spatiotemporally correlated visual artifacts that can cause a covariance shift at test time. To address these challenges, we propose streaming augmentations that mimic four types of artifacts commonly encountered during streaming with low-bandwidth network connection: pixelated blocks and scrubs, global blur, and ghosting. We instantiate our approach on top of predictive inverse dynamics models (PIDM), which combine future-state conditioning with an inverse dynamics policy in a learned latent space, and evaluate the impact of our augmentations across three tasks in modern 3D video games. Under stable streaming conditions, agents trained with spatiotemporal augmentations achieve up to 41% higher evaluation performance compared to agents trained without augmentations under an identical data budget. When network lag is introduced, agents trained with augmentations degrade by only 7.45% vs 49.82% of the original performance for agents trained only with the original data. These results clearly indicate that spatiotemporal augmentations tailored for the streaming setting are a simple yet powerful tool to train robust and efficient game-playing agents.


## 精读解读（中文）
### 一、研究动机
模仿学习通过从人类演示中训练策略将视觉观察映射到动作，是扩展复杂3D环境游戏代理的有吸引力的方式，但演示数据收集成本高昂，且现代游戏常通过流式传输，网络延迟和压缩引入时空相关的视觉伪影，导致测试时协变量偏移，影响代理性能。

### 二、技术方案（Method）
本文提出流式增强（streaming augmentations），模拟四种低带宽网络流中常见的伪影：像素化块和划痕、全局模糊、鬼影。在预测逆动力学模型（PIDM）基础上实现，该模型使用冻结的预训练视觉骨干（Theia）编码帧为潜在特征，并通过轻量级MLP作为逆动力学策略预测动作。增强按帧块（chunk，50-100帧）应用，参数通过正弦曲线和淡入淡出机制在块内平滑调制，确保伪影时空连贯。训练时预计算10个增强变体，以0.2概率采样原始轨迹。

### 三、结果（Result）
在稳定流条件下，使用时空增强的代理在相同数据预算下性能比无增强代理提升高达41%；在网络延迟引入时，增强代理性能仅下降7.45%，而无增强代理下降49.82%。在三个现代3D游戏任务中，组合标准增强和流式增强进一步提升了样本效率和鲁棒性。

### 四、结论（Conclusion）
为流式设置量身定制的时空增强是训练鲁棒且高效的游戏代理的简单而强大的工具，能有效应对演示数据稀缺和流式伪影导致的分布偏移问题。

### 五、方法论与关键技术细节
采用30个人类演示数据集，使用冻结的Theia视觉骨干和轻量MLP；增强块大小50-100帧，淡入淡出3帧，预计算M=10个增强变体，采样概率p_orig=0.2；预计算增强增加存储但保证可复现性；局限性：依赖演示质量，可能对未模拟的伪影类型泛化不足。
