# A Hybrid Edge Cloud Digital Twin for Welfare-Constrained Control in Poultry Production

- 区域：精读区
- 排名：9
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Suresh Neethirajan
- 机构：Dalhousie University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20367v1) · [PDF](https://arxiv.org/pdf/2608.20367v1)

## TLDR
This paper proposes a hybrid edge-cloud digital twin framework that integrates physics-based modeling, learned residuals, and model predictive control for real-time welfare-constrained environmental control in poultry barns, significantly improving prediction accuracy, reducing ammonia violations, and cutting communication overhead.

## Abstract
Poultry production operates under tightly coupled environmental and biological dynamics, yet commercial climate control remains largely heuristic, limiting welfare assurance and operational efficiency. We introduce an edge-cloud digital twin framework for real-time, welfare-constrained environmental control in poultry facilities. The framework integrates distributed sensing, on-device state estimation, a hybrid physics-data model, and model predictive control to enable anticipatory and adaptive management under practical farm constraints. A grey-box thermodynamic and mass-balance formulation is augmented with a learned residual that captures unmodeled biological variability, including activity-dependent metabolic heat. This hybrid model is embedded within a state-space representation for real-time estimation and control at the edge, while cloud coordination supports cross-farm learning and long-horizon optimization. Bandwidth-aware processing and asynchronous synchronization enable deployment in connectivity-limited environments. Evaluation in a high-fidelity broiler production testbed demonstrates substantial gains over rule-based control and physics-only modeling. Temperature prediction error is reduced from 1.8 degrees Celsius to 0.4 degrees Celsius, ammonia constraint violations decrease by 90 percent, and communication requirements are lowered approximately 30-fold through edge-first processing. A Domain Transfer Score of 0.92 further indicates strong robustness across facility conditions. These results show that physically grounded digital twins, coupled with real-time control, enable scalable and welfare-aware management of biological production systems.


## 精读解读（中文）
### 一、研究动机
商业禽舍环境控制仍以启发式规则为主，依赖人工与被动调节，难以应对畜禽生物过程与外界环境强耦合、高度时变带来的福利风险；同时农村地区网络连接受限，云中心式监控与闭环控制难以落地。现有物理仿真计算量大、数据驱动方法缺乏可解释性与跨场泛化能力，IoT平台又缺乏控制理论基础。因此需要一种将物理一致性、实时控制与分布式边缘-云架构结合的数字孪生框架，在保证动物福利硬约束的前提下实现规模化、可部署的环境管理。

### 二、技术方案（Method）
提出一种面向家禽生产的边缘-云数字孪生框架，包含物理感知层、边缘计算层、数字孪生核心层、监督控制层和云分析治理层。物理层通过分布式温湿度、CO2、氨气、视频、音频、称重及垫料水分传感器采集数据，以Modbus TCP、OPC UA、MQTT等协议接入；边缘层利用扩展卡尔曼滤波融合多模态传感流并估计不可观测状态，如代谢产热，同时进行视频活动指数、音频呼吸异常等特征提取。数字孪生核心采用灰盒热力学电阻-电容网络与质量平衡方程构建状态空间模型，并串联一个学习残差模块补偿未建模生物变异性（如活动依赖性代谢热、气流不均匀性、传感器漂移）；残差网络以物理模型预测与数据偏差的加权目标训练，同时惩罚违反能量/质量守恒的预测。控制层在边缘侧部署模型预测控制，以生理热中性区和空气质量限值作为硬约束，目标函数最小化输出偏离参考轨迹与控制能耗，预测时域为6-12步（30-60分钟），求解有限时域优化问题；云端负责跨农场学习、长期优化、模型再训练和法规日志。系统采用带宽感知的卸载决策与异步同步，高频数据仅在边缘处理，仅向云发送聚合统计或异常事件，保证弱连接环境下实时控制自主性。

### 三、结果（Result）
在高保真肉鸡生产数值试验台上，该框架相较规则控制和纯物理模型取得显著提升：温度预测误差从1.8°C降至0.4°C，氨气约束违规减少90%，通信需求因边缘优先处理降低约30倍，领域迁移分数达0.92，表明跨设施条件具有较强的鲁棒性。结果验证了混合物理-数据建模与MPC结合相比基线方法在预测精度、福利约束满足和部署可行性上的优势。

### 四、结论（Conclusion）
研究表明，将物理可解释的灰盒模型与数据驱动残差学习、模型预测控制及边缘-云协同调度集成于数字孪生框架，能够在生物生产系统中实现可扩展且福利感知的自主环境管理。该方法既保持了热力学和质量守恒的一致性，又通过边缘计算适应农村弱连接环境，为商业家禽养殖从启发式管理走向闭环优化提供了可行路径。

### 五、方法论与关键技术细节
关键实现细节包括：灰盒RC热模型与质量平衡方程构成连续时间状态空间表示，状态向量为[T_air, T_wall, c_CO2, c_NH3, c_humidity, m_bird, θ_bio]；系统矩阵可由递归最小二乘在调试阶段标定。氨气浓度硬约束设为<20 ppm，温度约束为18-25°C，相对湿度≤90%，执行器约束包括风机0-100%、加热器0-50 kW；MPC权重矩阵Q/R可调。混合模型采用串行结构f_total = f_phys + f_ML(φ_k)，训练损失兼顾数据失配与能量/质量守恒违反惩罚，从而保障学习残差的物理合理性。边缘采样率为1-5 Hz，视频帧等中频数据本地处理、事件触发上云；模型与ISO 23247及Asset Administration Shell语义兼容。局限性方面，当前基于高保真数值试验台验证，尚未在实际农场充分部署；残差学习依赖站点数据积累，跨场应用虽有0.92迁移分数但仍需校准；多节点RC扩展、遗留设备协议转换和4G/卫星链路的异步同步是实际部署中的关键约束。
