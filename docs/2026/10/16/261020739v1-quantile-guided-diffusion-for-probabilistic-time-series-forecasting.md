# Quantile-Guided Diffusion for Probabilistic Time-Series Forecasting

- 区域：精读区
- 排名：4
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Shadi Omari, Bashar Khoury, Assaf Schuster
- 机构：Technion -- Israel Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20739v1) · [PDF](https://arxiv.org/pdf/2610.20739v1)

## TLDR
This paper introduces Control-TS, a full-depth residual control method that uses predicted quantile trajectories to guide a frozen pretrained diffusion forecaster, consistently improving probabilistic time-series forecasting across benchmarks and introducing the CLPS metric to evaluate downstream forecasting utility.

## Abstract
Quantile forecasts summarize uncertainty at each future time step, while diffusion forecasters represent it through sampled future trajectories. We study how predicted quantiles can serve as distributional controls for diffusion forecasting. Specifically, we investigate how the mechanism of quantile integration affects its effectiveness in guiding a pretrained diffusion forecaster. We find that residual control throughout the denoising network yields the most consistent improvements. We instantiate this approach as Control-TS, which learns a quantile-control pathway while keeping the pretrained backbone frozen. Across eight benchmarks, Control-TS consistently improves the backbone's CRPS, achieves competitive performance against state-of-the-art forecasting models, and retains its gains in capacity-matched comparisons. Further analyses examine how these gains depend on quantile granularity, predictor choice, and forecast quality. Finally, we introduce the Conditional Linear Predictive Score (CLPS), which complements distributional metrics by evaluating the downstream forecasting utility of generated futures. Together, these findings support predicted quantiles as an effective interface between explicit uncertainty estimates and diffusion-based trajectory generation.


## 精读解读（中文）
### 一、研究动机
概率预测中，分位数预测能在每个未来时刻显式刻画不确定性的位置、离散度与偏态，而扩散预测器则通过采样完整未来轨迹来表达不确定性。二者所捕捉的预测信息可能互补，但预测分位数本身有噪声且不刻画跨时间步的依赖关系，因此核心问题是：外部预测的分位数轨迹能否作为分布层面的控制信号来引导扩散预测，以及应以何种方式注入才最有效。作者据此提出“分布控制”（distributional control）的研究视角，系统比较分位数与扩散模型的多种融合接口。

### 二、技术方案（Method）
作者以无条件扩散模型 TSDiff（基于 SSSD/DiffWave 与 S4 时序块）为冻结骨干，输入为观测上下文 y_ctx 与未来轨迹 Y_tar，外部预测器（GluonTS 中的 DeepAR 或 TFT）在给定上下文下输出分位数矩阵 Q_φ，分位数集合取 Q1={0.5}、Q3={0.1,0.5,0.9} 或 Q5（加入 0.25、0.75）。控制信号 c∈R^{(L_ctx+H)×Q} 由复制并缩放后的观测上下文与预测的未来分位数拼接而成，若启用滞后特征则对扩散输入与控制信号做相同扩展。作者对比四类融合机制：输出级线性池化集成、输入级拼接、FiLM 特征级调制，以及在冻结骨干各残差块处注入残差的全深度残差控制；后者实例化为 Control-TS，其控制器由三个与骨干残差栈结构一致的随机初始化残差块组成，逐块接收时间步嵌入 τ(t)，输出经零初始化的 1×1 投影 Z 加到骨干对应残差块输入上，即 h^(k)=B^(k)(h^(k-1)+Z^(k)(u^(k)),τ(t))。训练时仅优化控制通路参数 θ_C（含输入投影与零初始化残差投影），骨干与外部预测器全部冻结，损失为标准扩散噪声预测目标；推理时从高斯噪声出发执行受控反向扩散，并保留原骨干的观测自引导（observation self-guidance）以保证上下文一致性，用 100 条采样路径计算 CRPS。

### 三、结果（Result）
在 8 个 GluonTS 真实基准（Electricity、Exchange、KDDCup、M4-Hourly、Solar、Traffic、UberTLC、Wikipedia）上，所有融合机制都能在部分数据集上改善骨干 CRPS，但只有全深度残差控制（Control-TS）在全部 8 个数据集上一致提升，CRPS 降幅最高约 35%（如 M4-Hourly 从 0.034 降到 0.022，KDDCup 从 0.312 降到 0.249，Electricity 从 0.049 降到 0.047）。与当前最先进预测模型相比，Control-TS 在 5 个数据集上取得最优或并列最优 CRPS，并在 6 个数据集上优于容量匹配的扩散基线。此外作者提出条件线性预测得分 CLPS（Train-on-Hybrid, Test-on-Real），用共享线性预测器在真实上下文配生成未来的混合数据上训练、在留出真实数据上评估，Control-TS 在 8 个基准中的 6 个上优于其扩散骨干。

### 四、结论（Conclusion）
结果表明，外部预测的分位数轨迹可以作为显式不确定性估计与扩散轨迹生成之间的有效接口：在冻结的预训练扩散骨干上，通过全深度残差方式注入分位数控制，能在不改变骨干参数的前提下稳定提升概率预测精度，并与强基线竞争。不同注入机制的对比说明控制的作用位置显著影响效果，残差式、全深度、零初始化的控制通路是最一致的实现方式。CLPS 的引入进一步补充了分布型指标，说明生成未来轨迹在下游预测任务中也具有实际可用性。

### 五、方法论与关键技术细节
关键实现点：控制信号以逐时间步分位数矩阵形式提供（Q1/Q3/Q5 三档粒度，按验证集 CRPS 选优），并按 (L_ctx+H)×Q 与扩散序列对齐；残差注入点可为一、二或全部三个残差块，实验显示全深度最优；零初始化的 1×1 投影保证训练开始时受控噪声预测器与预训练骨干完全等价，避免破坏预训练先验。骨干与外部预测器全程冻结，仅训练轻量控制通路，因此参数量与计算开销可控，需权衡精度—成本；CRPS 基于 100 条采样路径、三次随机种子取均值与标准差。分析还覆盖了分位数粒度、预测器选择（DeepAR/TFT）、控制质量退化与错位情形，以及将该接口迁移到 CSDI 与 MG-TSD 等其他扩散骨干的可行性；局限在于分位数仅刻画边缘分布、不建模跨时间步依赖，控制效果依赖外部预测器质量，且主要在单变量设定下验证。
