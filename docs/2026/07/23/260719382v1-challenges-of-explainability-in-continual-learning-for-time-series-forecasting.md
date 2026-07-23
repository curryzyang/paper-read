# Challenges of Explainability in Continual Learning for Time Series Forecasting

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Quentin Besnard, Emmanuel Doumard, Nicolas Labroche, Nicolas Ragot, Nicolas Ringuet
- 机构：Université de Tours
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19382v1) · [PDF](https://arxiv.org/pdf/2607.19382v1)

## TLDR
This paper explores how explainability methods like attention rollout and Grad-CAM can be used to analyze and interpret continual learning dynamics in non-stationary time series forecasting, revealing challenges and opportunities for guiding data selection and model adaptation.

## Abstract
Deep learning models have shown strong potential for time series forecasting, yet their deployment in real-world environmental monitoring remains challenging due to non-stationary dynamics and limited explainability. In this work, we investigate explainability as a central tool for understanding continual learning in adaptive time series forecasting, with Experience Replay strategies. We study neural forecasting architectures such as PatchMixer, PatchTST and DLinear, augmented with attention-based sampling mechanisms to support model adaptation over time. Explainability is leveraged through attention rollout and gradient-based attribution methods (Grad-CAM) to analyze both predictive behavior and sampling strategies within a continual learning framework. Experiments conducted on real-world piezometric time series exhibiting heterogeneous patterns and regime shifts show that analyzing model and sampling behaviors provides valuable insights into the dynamics of the continual learning framework. Beyond predictive performance, our results highlight the challenges and opportunities of using explainability to understand continual learning behaviors, revealing how attribution patterns evolve over time and how they can inform data selection and adaptation strategies in non-stationary forecasting scenarios.


## 精读解读（中文）
### 一、研究动机
尽管深度学习模型在时间序列预测中展现出潜力，但由于非平稳动态和有限的解释性，它们在现实世界环境监测中的部署仍具挑战。本文研究可解释性作为理解持续学习自适应时间序列预测的核心工具，特别关注经验回放策略，旨在通过分析模型和采样行为来揭示持续学习框架的动态特性，并为非平稳预测场景中的数据选择和适应策略提供信息。

### 二、技术方案（Method）
采用模型无关的持续学习框架，结合知识蒸馏和回放记忆管理。使用三种预测架构：PatchMixer、PatchTST和DLinear。回放采样策略包括随机、基于损失（最大/最小）以及基于注意力的方法。注意力采样模块通过自注意力机制识别信息性时间片段。解释性方法包括注意力展开（用于采样分析）和梯度加权类激活映射（Grad-CAM，用于模型级归因）。实验在真实地下水水位时间序列（Piezometer 3和17）上进行，这些序列呈现异质模式和状态转变。模型先在50%数据上训练，然后以固定频率（freq=300）触发适应，回放缓冲区大小1500，内循环参数inner_loop=3。训练超参数一致：hidden_size=256, lr=1e-3, epochs=100, batch_size=16，早停patience=3。

### 三、结果（Result）
注意力引导的回放策略提高了非平稳条件下的预测精度。Grad-CAM分析显示架构差异：PatchMixer（卷积）的归因分布较均匀，而PatchTST（Transformer）的归因集中在最近时间步，反映自注意力和位置编码的时序偏差。注意力展开揭示稳定的、模型无关的采样模式，表明模型能学习共同的信息性时间片段。采样策略对比表明：随机采样均匀但无解释性；注意力采样产生结构化选择，与学得的重要性分数直接关联，提供可解释性；最大损失聚焦困难样本但可能放大噪声；最小损失重复选择低误差样本导致冗余，限制适应性。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
数据集：法国两个代表性钻孔（Piezometer 3和17）的长期地下水水位时间序列，呈现长期漂移和季节规律破坏（1990年代至2010年代水位下降）。超参数：hidden_size=256, lr=1e-3, epochs=100, batch_size=16, freq=300, buffer_size=1500, inner_loop=3（注意力策略）。损失：知识蒸馏（未明确损失函数，但学生模型通过蒸馏从教师学习）。解释方法：注意力展开用于采样模块，Grad-CAM（最后线性层）用于预测模型。复杂度：实验在单个GPU上运行，时间成本未明确。局限性：分析集中于单一案例（Piezometer 3），未泛化至更多钻孔；采样策略评估偏重解释性而非全面性能基线；注意力采样的额外计算开销未量化。
