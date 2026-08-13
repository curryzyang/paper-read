# Diffusion-Based Data-Driven Assortment Optimization

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Junyi Liao, Xiaohui Jiang, Zhengwei Tong, Ethan X. Fang, Vahid Tarokh
- 机构：Duke University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11419v1) · [PDF](https://arxiv.org/pdf/2608.11419v1)

## TLDR
The paper proposes a model-agnostic, guided discrete diffusion framework for assortment optimization that stochastically generates high-quality, diverse assortments via reward-biased reverse diffusion, offering robustness to model misspecification and scalability without explicit parametric choice models.

## Abstract
Assortment optimization is a fundamental problem in revenue management, typically addressed using parametric choice models such as the multinomial logit (MNL) and its variants. While these models enable tractable formulations, their performance is sensitive to model misspecification and often struggles to capture complex customer behavior. In this paper, we propose a model-agnostic framework for assortment optimization based on guided discrete diffusion. We represent assortments as binary vectors and perform stochastic search via a learned reverse diffusion process, avoiding explicit combinatorial enumeration. To incorporate decision objectives, we introduce a reward-guided mechanism that biases local transitions using estimates of expected revenue. This allows the method to effectively balance exploration and exploitation during generation. Empirically, we show that the proposed approach consistently identifies high-quality assortments and remains robust under model misspecification, often recovering near-optimal solutions in high-dimensional settings. Moreover, the generative nature of diffusion enables the production of diverse high-performing assortments, offering flexibility beyond a single deterministic solution. These results highlight the potential of generative modeling as a scalable and robust paradigm for combinatorial optimization in data-driven decision-making.


## 精读解读（中文）
### 一、研究动机
现有集配优化通常依赖MNLogit等参数化选择模型，这些模型在配置正确时可行，但对模型误设敏感，难以捕捉复杂的顾客替代行为与异质偏好；同时高维组合决策空间导致精确优化在计算上不可行。因此需要一种不依赖强参数假设、对模型误设鲁棒且能高效扩展的通用方法。

### 二、技术方案（Method）
D3AO采用三阶段流程：首先，利用离线交互数据{(S_i,A_i)}训练一个神经选择模型p_theta(a|s)，以交叉熵损失做极大似然估计，输出被限制在s∪{0}上的masked概率分布；其次，基于该模型和已知奖励函数构建每个集配的期望收益估计器R̂(s)；最后，将可行集配编码为二进制向量，训练一个离散扩散模型作为集配空间的先验，并在反向去噪过程中引入奖励引导机制——用R̂(s)偏置局部状态转移，从而在随机生成中平衡探索与利用，避免显式组合枚举，最终采样出多个高质量的集配。

### 三、结果（Result）
在合成基准实验中，D3AO一致地找到高质量集配，在模型误设条件下表现稳健，且在高维设置中常能恢复接近最优的解。生成式扩散还能产出多样化且性能优越的集配集合，超越了单一确定性解的限制。

### 四、结论（Conclusion）
生成式建模为数据驱动的组合优化提供了一种可扩展、鲁棒的新范式；D3AO作为模型无关的集配优化框架，能够在不依赖参数化选择模型的情况下有效逼近最优集配，并适用于离线决策场景。

### 五、方法论与关键技术细节
关键细节包括：集配被表示为二进制向量，利用离散扩散模型进行随机搜索；奖励引导机制基于期望收益估计，通过调节局部转移概率实现，隐含了探索与利用的平衡；行为策略假设服从玻尔兹曼分布并与最大熵正则化收入最大化问题对应；离线数据由行为策略生成，存在覆盖不全和分布偏移，模型需对未观测集配进行外推；神经选择模型采用masked softmax结构确保非法选择概率为零；方法避免了显式枚举，但受扩散模型采样质量和奖励估计误差影响，且在高维或强约束下仍有进一步优化空间。
