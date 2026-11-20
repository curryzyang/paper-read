# PsyWorld: Profile-Conditioned World Modeling for Human Behavior Prediction

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Ziyuan Qin, Yang Qiao, Summer B. Frandsen, Michael T. Treadway, Liang Zhao
- 机构：Emory University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.24999v1) · [PDF](https://arxiv.org/pdf/2611.24999v1)

## TLDR
PsyWorld introduces a profile-conditioned world model that learns from observed environment–behavior state transitions to predict human behavior for unseen participants, using transition-informed latent codes rather than treating personality as a direct action descriptor.

## Abstract
Understanding how stable psychometric traits and time-varying states jointly inform behavior is an important problem in computational behavioral science. Existing personalized agents commonly condition actions directly on a static profile, leaving realized state transitions unused as an explicit source of supervision. We introduce a profile-conditioned state world model that uses observed environment--behavior state transitions to learn transition-informed representations for behavioral prediction. During training, a posterior encoder quantizes realized transitions, while a prior predicts the resulting codes from the psychometric profile and pre-transition context. The prior code and predicted next state then condition macro-level behavior and simulator-grounded execution. Thus, the world model provides structured transition supervision instead of treating personality as a direct action descriptor. We evaluate the framework in VEET, a controlled behavioral simulator with human trajectories, and in AgentSociety as a structurally different synthetic environment. A participant-disjoint split of 240 training, 25 validation, and 48 test participants evaluates generalization to unseen people. On VEET, the model reaches 0.904 Top-1 accuracy (95\% CI: [0.895, 0.913]) and 0.0033 Macro KL. Ablations associate continuous next-state modeling with most of the Top-1 gain, while discrete codes and prior alignment mainly improve Top-3 and distributional alignment. These results establish transition-informed world-model supervision as useful for subject-generalized behavior prediction, without implying causal psychological mechanisms or calibrated long-horizon state dynamics.


## 精读解读（中文）
### 一、研究动机
现有面向个性化行为预测的智能体多将静态心理测量画像直接作为动作条件，未把已实现的环境—行为状态转移作为显式监督信号，因而难以刻画同一参与者在任务与环境变化中的状态动态。论文旨在利用稳定心理测量特质与随时间变化状态的区分，通过状态转移监督提升对未见参与者的行为预测泛化能力。

### 二、技术方案（Method）
论文将每位参与者的问卷画像q_i、49维环境—行为状态s_t和宏观行为a_t输入上下文编码器得到h_t，并联合建模下一状态与下一宏观行为。训练时，后验编码器利用已实现状态变化Δs_t=s_{t+1}-s_t生成连续潜变量，经K=128、维度64的码本向量量化得到后验转移码；先验仅由h_t经softmax预测码分布，并以硬argmax选取先验码，推理阶段只使用先验码以避免未来信息泄漏。世界模型解码器由h_t和转移码预测下一状态；宏行为解码器将转移条件分支与上下文分支用学习门控融合，输出下一宏观行为；随后由模拟器相关执行策略将宏观行为落实为短时程动作段，并以DPO按与人类轨迹偏差构造偏好对训练执行策略。

### 三、结果（Result）
在参与者不重叠的VEET划分（240训练、25验证、48测试）上，模型达到0.904的Top-1准确率（95% CI：[0.895,0.913]）和0.0033的Macro KL。消融显示，连续下一状态建模贡献了大部分Top-1增益，而离散转移码与先验对齐主要改善Top-3和分布对齐；AgentSociety作为结构不同的合成环境用于检验同一分解的可操作性。

### 四、结论（Conclusion）
结果表明，将已实现状态转移作为结构化世界模型监督，有助于面向未见参与者的行为预测，并把心理测量画像从直接动作描述子转化为条件化状态转移表示。作者强调该结论不意味着学习到了因果心理机制，也不声称具备校准良好的长时程状态动力学。

### 五、方法论与关键技术细节
关键实现包括：VEET提供问卷画像与人类行为轨迹并作为主要评测，AgentSociety提供LLM驱动的城市级合成环境且宏观动作集为work、consume、rest、leisure、move；联合损失由状态重构MSE（分别使用后验码和先验码）、VQ码本与承诺损失、先验对后验硬分配的交叉熵/KL对齐以及类平衡宏行为交叉熵组成，VQ变体额外使用轻量码使用正则以缓解码本坍塌；执行策略以DPO训练，正负样本按与对应人类轨迹的偏差排序，β控制偏好强度。局限性在于转移码是预测性摘要而非人格或临床构念，AgentSociety仅提供合成操作化而非独立心理验证，且长时程状态动力学未做校准保证。
