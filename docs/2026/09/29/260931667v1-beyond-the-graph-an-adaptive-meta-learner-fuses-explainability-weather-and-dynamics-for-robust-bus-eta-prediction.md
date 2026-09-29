# Beyond the Graph: An Adaptive Meta-Learner Fuses Explainability, Weather, and Dynamics for Robust Bus ETA Prediction

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Pratham Payra, Jagadish
- 机构：Indian Statistical Unit
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31667v1) · [PDF](https://arxiv.org/pdf/2609.31667v1)

## TLDR
The paper proposes HYB(\(n_m\)), an adaptive meta-learner-based hybrid ensemble that dynamically fuses five complementary models—historical, periodic, Koopman, weather-integrated, and graph-convolutional predictors—to improve bus ETA prediction robustness, accuracy, and efficiency across varying conditions, validated on over 4,000 trips from three Kolkata routes.

## Abstract
Accurate bus Estimated Time of Arrival (ETA) prediction is vital for urban mobility, passenger satisfaction, and transit efficiency, yet existing models falter against nonlinear spatiotemporal dynamics, data sparsity, and factors such as weather. This paper proposes HYB(nm), an adaptive hybrid ensemble framework that dynamically fuses five complementary models - a historical baseline (MST-AV), periodical temporal pattern analysis (GDRN-DFT), Koopman Neural Operators for nonlinear dynamics (KOOP-NET), weather-integrated feature-engineered neural networks (FENN), and real-time graph convolutional networks (MGCN) - via a meta-learner attuned to real-time context. Evaluated on GPS and weather data from three Kolkata bus routes comprising more than 4,000 trips, the framework leverages the individual strengths of its components (for example, the low-latency explainability of MST-AV, the weather resilience of FENN, and the network-dynamics capture of MGCN) to deliver the superior robustness of HYB(2), state-of-the-art accuracy rivalling leading graph neural networks, and balanced trade-offs in stability and efficiency across prediction horizons and operating conditions. The extensible HYB(k) architecture equips transit agencies with flexible tools, ranging from economical single models to tailored high-fidelity hybrids, advancing predictive, equitable urban transport.


## 精读解读（中文）
### 一、研究动机
公交ETA预测对城市出行、乘客满意度和公交效率至关重要，但现有模型难以同时应对非线性时空动态、数据稀疏和天气等外生扰动，且常在精度、可解释性与计算成本之间失衡。为此，论文提出融合可解释性、天气感知和非线性动力学建模的自适应混合集成框架，以提升复杂运营条件下的鲁棒性。

### 二、技术方案（Method）
方法为HYB(nm)自适应混合集成：以Kolkata三条公交线路2024年8月至2025年3月的GPS轨迹和逐小时天气数据为输入，先计算Haversine速度，将空间离散为约50m×50m网格并以中位坐标作为节点，构建完全图后用最小生成树提取路网骨架，再用Dijkstra得到目标站点的最短路径。五个子模型分别提供历史平均基线MST-AV、图扩散循环网络结合DFT的周期模式GDRN-DFT、Koopman神经算子KOOP-NET、融合OpenWeatherMap天气特征工程神经网络FENN和实时掩码图卷积MGCN。元学习器根据实时上下文为各子模型分配可解释权重并动态融合，HYB(nm)仅激活贡献最高的top-nm模型以降低推理成本，训练/推理流程为各子模型先独立预测，再由元学习器在线选择与加权输出。

### 三、结果（Result）
在三条Kolkata线路、超过4,000次行程的GPS与天气数据上，HYB(2)表现出最优鲁棒性，精度可与领先图神经网络竞争，并在不同预测时域和运营条件下实现稳定性与效率的平衡。各组件贡献互补：MST-AV提供低延迟可解释性，FENN增强天气韧性，MGCN捕捉网络动态。摘要报告了优于单一模型和传统基线的综合表现，但全文预览未给出RMSE、MAE等具体数值。

### 四、结论（Conclusion）
HYB(k)架构可扩展，能够为交通机构提供从经济型单模型到定制高保真混合模型的灵活部署方案。该框架将可解释性、天气感知和非线性动力学统一起来，在复杂城市公交场景中提升预测鲁棒性和实用性，有助于推进预测性、公平的城市交通服务。

### 五、方法论与关键技术细节
数据包含三条线路DN2/1、KB22、KB16，分别约1,251、1,829、953次行程，45,321、62,553、35,268个GPS点，线路长度26、22、19km，站数13、11、10，平均速度18.3±2.1、15.7±1.8、20.1±2.4km/h；时间覆盖2024年8月至2025年3月并偏向季风月，天气变量包括温度、湿度、降水、风速和云量。关键先验是历史平均速度、日/周周期、Koopman潜空间线性演化、天气协变量和实时图消息传递；MST-AV用相邻节点历史平均速度均值估算边速度，ETA为路径上距离除以速度之和，Koopman与FENN用logit和sigmoid约束速度合理范围。全文预览未披露具体损失函数、优化器、学习率、训练轮数和超参搜索范围，主要约束是50m网格离散误差、MST近似路网、对GPS与天气数据质量的依赖，以及元学习器与多模型集成带来的训练和部署复杂度。
