# Earth World Model: Physics-constrained latent dynamics for forecasting and environmental scenario analysis

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Huijun Qiao, Ziqiang Zhang, Jinnong Liao
- 机构：Beijing Latent Vector Technology Co., Ltd., Beijing University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18654v1) · [PDF](https://arxiv.org/pdf/2611.18654v1)

## TLDR
The paper proposes the Earth World Model (EWM), a physics-constrained latent-dynamics framework that compresses multi-source observations into a reusable low-dimensional state and uses replaceable exogenous drivers with a shared transition operator and physical decoder to support multi-step forecasting and environmental scenario analysis, validated on photovoltaic and wind power forecasting with strong predictive accuracy and faithful perturbation-response behavior.

## Abstract
World models have been widely applied to multi-agent planning and forecasting, but exogenous environmental changes are rarely incorporated as replaceable drivers in a unified state-evolution process. This limits assessment of whether environmental perturbations propagate through physical systems with faithful dynamics. We propose the Earth World Model (EWM), an Earth-centred forecasting framework that compresses heterogeneous multi-source observations into a reusable low-dimensional latent state representing the system's history and current condition. Given explicit exogenous drivers, a shared transition operator recursively updates the latent state, and physics-constrained decoding produces multi-step forecasts. Replacing the drivers enables environmental scenario analysis and evaluation of dynamic-response fidelity. We evaluated EWM for power forecasting and environmental-perturbation response at six photovoltaic sites and one wind-power site. Across four photovoltaic sites and three forecast horizons, three independent training runs yielded mean $R^2$ values of 0.8578-0.9095. In a separate six-site decoder ablation, the mean net per-unit response $ρ$ under the prescribed irradiance intervention increased from 0.180 with a multilayer perceptron decoder to 0.922 with an analytic physical decoder, close to site- and horizon-specific analytic references. The wind model achieved an injection elasticity of $0.9990 \pm 0.0006$, while pre-intervention outputs remained unchanged. These results show that forecast fit and intervention response should be evaluated separately and that the tested EWM configurations preserved response amplitude and temporal boundaries under the prescribed interventions.


## 精读解读（中文）
### 一、研究动机
现有世界模型多面向多智能体规划与预测，未将外生环境变化作为统一状态演化过程中的可替换驱动，天气模型通常把未来气象变量当条件输入而非可替换控制，物理约束方法又常仅以损失惩罚引入。由此难以评估环境扰动是否按可信动力学在物理系统中传播，也限制了可再生能源预测与环境情景分析。

### 二、技术方案（Method）
EWM定义为(Z,T,C,D)：BRC编码器先按可用时间过滤、时间对齐、归一化和特征构造，将多源观测与历史驱动经Patch局部标记化、Pool聚合和Proj投影压缩为低维潜状态z_t；未来驱动不进入初始编码。共享转移算子T以GRU实现，按发布的未来外生驱动递推更新潜状态，物理解码器D将演化状态与当前驱动映射为决策输出。训练目标为L_task+λ_repr L_repr+λ_phys L_phys，其中表示预测器用训练期目标表示做监督，物理约束同时进入结构与损失；预测时历史只编码一次，按H步递推生成，情景查询保持z_t、T、D不变，仅替换声明驱动并重算由查询控制导出的特征。

### 三、结果（Result）
在4个光伏站点、3个预测时域和3次独立训练中，EWM平均R²为0.8578—0.9095，跨站点与时域表现稳定。六站点解码器消融中，规定辐照干预下平均净单位响应ρ由MLP解码器的0.180提升到解析物理解码器的0.922，接近站点和时域特定的解析参考。风电模型注入弹性达0.9990±0.0006，且干预前输出保持不变，说明扰动幅度传递和时间边界保持较好。

### 四、结论（Conclusion）
EWM在保持光伏与风电预测性能的同时，能在规定干预下保持响应幅度与时间边界，支持将预测与环境情景分析统一到同一潜状态演化框架中。结果强调预测拟合优度与干预响应保真度应分开评估；但所测为模型层面的响应一致性与时间局部性，物理因果结论仍需来自实际系统的独立证据。

### 五、方法论与关键技术细节
关键实现包括：多源异构观测按可用时间过滤并固定训练集归一化参数，历史窗口只编码一次，递推中共享转移参数且不喂入未来真值；查询路径与基线共享z_t、T、D，中性替换应复现基线，最早改变步之前输出用于时间局部性检查。物理先验通过夜间钳制、运行门控等结构规则及L_phys体现，而非仅作损失惩罚；表示目标仅在训练期使用，推理不依赖目标表示。实验以R²、净单位响应ρ和注入弹性分别刻画拟合与干预响应，并用MLP与解析物理解码器消融隔离解码器作用。局限性在于结论属模型界面内的响应评估，依赖确定性推理和域特定编码器/转移权重，λ_repr、λ_phys、H、L、d_z等需按实验配置设定，且未证明真实物理因果。
