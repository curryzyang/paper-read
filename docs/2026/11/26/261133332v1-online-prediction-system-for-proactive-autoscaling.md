# Online Prediction System for Proactive Autoscaling

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Jun Gao, Areg Poghosyan, Pavel Paulau, Sumit Mohanty, Tengfei Mu, Shawn Chen
- 机构：Meta Platforms, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33332v1) · [PDF](https://arxiv.org/pdf/2611.33332v1)

## TLDR
This paper presents a production online learning system that combines STL seasonality decomposition with lightweight linear residual correction, retraining each prediction cycle to enable high-accuracy, low-latency proactive autoscaling and saving an estimated 118K servers daily.

## Abstract
We present an online learning system for short-term time series forecasting that enables proactive autoscaling in large-scale distributed systems. Unlike traditional forecasting methods that focus on modeling seasonality and long-term trends, the system targets high-accuracy, low-latency predictions for immediate future intervals for dynamic resource management in internet-scale infrastructures. The system employs a two-stage architecture: a seasonality decomposition stage followed by a residual correction stage using lightweight linear models with engineered features. By retraining models on-the-fly for every prediction cycle, the online prediction system continuously adapts to changing demand patterns without requiring persistent model storage or feature drift monitoring. Deployed across many heterogeneous services, the system processes over 900K predictions per hour; in an offline evaluation on production traffic, its STL-based configuration reduces prediction error (MAPE) by 18.6\% relative to the previous production model. In production, the system has saved an estimated 118K servers daily.


## 精读解读（中文）
### 一、研究动机
生产环境中的自动扩缩容长期以反应式为主：先检测到负载升高再扩容，此时尖峰往往已造成性能退化，而需求下降时又难以及时释放资源，导致持续过度供给。基于短时时间序列预测的主动扩缩容可以缓解这一滞后，但既有生产方案主要是对按天聚合数据拟合的四次多项式回归，其函数形式刚性、无法适应产品发布等突发变化、提高时间分辨率也无明显收益、高阶还在边界处出现过拟合振荡，并且无法判断需求在预测窗口内是加速还是减速。此外，在大规模异构服务上落地还面临模型维护成本、亚秒级预测延迟、跨服务泛化与可解释性等运维约束，这构成了本文设计在线预测系统的出发点。

### 二、技术方案（Method）
系统由三部分组成：Smart Data Aggregator 从遥测流按 30 分钟粒度聚合吞吐量，为每个服务实体维护约 4 天（192 点）的滚动窗口，缺失点用线性插值补齐，偏离滚动均值 3σ 以上的异常值做截断；预测服务是无状态 RPC 端点，可独立横向扩展；结果回传给扩缩容系统。建模采用两阶段：第一阶段用 STL（周期 P=48，对应 24 小时）把序列分解为季节项 S、趋势项 T 与残差 R，并用外推得到下一时刻的 S、T；第二阶段不直接建模残差，而对其一阶差分 ΔR_t 构造滞后特征 LAG_{10,15,20,25,30} 与动量特征 MOM_{10,15,20,25,30}，z-score 归一化后拟合线性回归 ΔR̂_{t+1}=wᵀx_t+b，最终预测为 ŷ_{t+1}=(S_{t+1}+T_{t+1})+λ·(R_t+ΔR̂_{t+1})，λ∈[0,1] 平衡响应性与稳定性。推理流程上每个预测周期都在最新窗口上重新训练模型、用完即弃，无需模型存储、版本管理与特征漂移监控；预测目标为未来一个 30 分钟区间的需求，训练损失为平方误差（RMSE），下游扩缩容按 ŷ_{t+1}+α·σ 配置资源，σ 取训练残差标准差、α 为可配置安全系数；窗口长度、滞后集合、STL 周期与平滑因子等超参在离线用多周生产流量与多类服务做网格搜索确定。

### 三、结果（Result）
在来自生产扩缩容集群的 9 个代表性服务实体（覆盖平滑日周期、突发事件驱动与缓慢趋势型负载）上，用 4 天 30 分钟粒度序列按 80/20 划分，对比了沿两个改进维度（第一阶段多项式 vs STL、第二阶段人工 LAG/MOM 特征 vs CNN 学习特征）组织的 7 种配置。离线评估显示，基于 STL 的配置相对原生产多项式模型将预测误差（MAPE）降低 18.6%；同时 STL+线性回归（LAG/MOM）的精度优于所有 CNN 变体，说明在每实体仅约 192 个点的数据规模下复杂模型更易过拟合。系统整体每完整训练-预测周期（取数、STL 分解、特征计算、拟合、预测）在 500 毫秒内完成，每小时处理超过 90 万次预测，生产中估计每天节省约 11.8 万台服务器。

### 四、结论（Conclusion）
在面向自动扩缩容的短时预测场景中，关键约束是延迟、可维护性与跨异构服务的泛化，而非模型容量；因此“STL 季节分解 + 轻量线性残差校正 + 每周期在线重训”的简单方案不仅够用，而且在精度上优于更复杂的 CNN 方案，同时更可靠、更易部署。该无状态在线学习设计免去了模型持久化与漂移监控，已在大量异构服务上稳定运行并带来可量化的资源节省，说明分解式简单模型是生产级主动扩缩容预测的务实首选。

### 五、方法论与关键技术细节
数据侧为 30 分钟桶、约 4 天（192 点）滚动窗口，含线性插值与 3σ 截断清洗；先验侧用 STL（P=48）显式分离日周期与趋势，并把残差一阶差分作为更平稳的建模对象，特征只用 LAG/MOM（滞后 10/15/20/25/30），基于残差导数而非原始残差水平，实测比变化率、滑动平均等候选特征更有信息量。损失为平方误差（预测条件均值），风险控制放在下游：以训练残差标准差 σ 配合可配置安全系数 α 计算 ŷ+α·σ 的供给目标，λ 平滑因子权衡响应与稳定，窗口长度、滞后集合、STL 周期与 λ 均通过离线网格搜索确定。复杂度与约束方面，全流程亚秒级（<500ms）、无需 GPU 与模型仓库，可按实体水平扩展；局限在于单实体样本量小限制了模型容量，预测仅覆盖下一个 30 分钟区间、超参数离线调优难以逐实体自适应，且安全性依赖下游缓冲系数的人工设定。
