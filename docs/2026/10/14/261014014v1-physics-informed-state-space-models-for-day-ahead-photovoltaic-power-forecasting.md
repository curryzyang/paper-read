# Physics-Informed State Space Models for Day-Ahead Photovoltaic Power Forecasting

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Phil Aupke, Muhammad Hassan, Khalid Ali, Seema, Andreas Kassler, Andreas Theocharis
- 机构：Deggendorf Institute of Technology, Karlstad University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14014v1) · [PDF](https://arxiv.org/pdf/2610.14014v1)

## TLDR
The paper proposes a physics-informed state space framework that combines a differentiable PV conversion model with a PowerMamba selective state space backbone via physics-residual decomposition to improve day-ahead photovoltaic power forecasting accuracy and physical feasibility.

## Abstract
Accurate day-ahead photovoltaic (PV) power forecasting requires both strong temporal modeling and adherence to physical PV system constraints. Purely data-driven models often ignore the underlying PV conversion process and may produce predictions that are outside the operational range of a PV system. In this paper, we propose a physics-informed state space framework that combines a differentiable PV conversion model with a selective state space backbone (PowerMamba). Our approach follows a physics-residual decomposition. The physics module provides a structured baseline based on solar geometry, irradiance, temperature effects, and inverter limits, while the state space model learns residual corrections from numerical weather prediction (NWP) inputs over a 24-hour horizon. Experiments on one year of utility-scale PV data show that the proposed method significantly improves forecasting accuracy, reducing RMSE by 38.5% and MAE by 45.8% compared to a physics-only baseline, and outperforming a purely data-driven model. Results further show that incorporating system-level physics provides the largest performance gains, while additional refinements offer only marginal improvements. Beyond accuracy, the model improves robustness by constraining predictions toward physical feasibility, reducing unrealistic predictions under corrupted measurements.


## 精读解读（中文）
### 一、研究动机
日前光伏功率预测既需要强时序建模，也必须满足光伏系统物理约束；纯数据驱动模型忽略光伏转换过程，可能输出超出逆变器容量等运行范围的预测，并在传感器漂移、测量损坏或分布偏移下退化。现有物理信息方法通常只纳入热动态或温度效率等局部效应，尚未将系统级光伏转换物理与现代选择性状态空间模型结合用于 NWP 驱动的日前预测。

### 二、技术方案（Method）
提出物理-残差分解框架：输入历史观测窗口 L=288 步（3天）和未来 NWP 序列 H=96 步（24小时，15分钟分辨率），特征包括 NWP 全球辐照度、温度、风速、风向、NWP 功率估计、实测 PV 功率、太阳高度角、晴空功率以及小时/年积日正余弦编码。物理模块为可微光伏转换链，基于太阳几何与 POA 辐照转换、Faiman 温度模型、温度依赖效率和逆变器容量约束生成物理基线 P_phys；PowerMamba 选择性 SSM 以线性复杂度学习残差修正 P_res；最终预测为 ReLU(P_phys+P_res)。训练使用 MSE 加物理参数边界惩罚的复合损失，λ_phys=0.01，30 个 epoch、batch size 64、Adam、lr 1e-3，前 10 个 warm-up epoch 冻结残差骨干预拟合物理模块，随后联合训练；骨干为两个 Mamba 块，d_model=128、d_state=64、d_conv=2、扩展因子 2、dropout 0.2，并使用 RevIN。

### 三、结果（Result）
在河北某公用事业规模光伏电站一年数据（2018年7月至2019年6月，逆变器容量约13.2 MW）上，所提物理信息 PowerMamba 取得 RMSE 1.631 MW、MAE 0.756 MW、nRMSE 8.16%，相对物理-only 基线 RMSE 降低 38.5%、MAE 降低 45.8%。它同时优于纯数据驱动 PowerMamba（RMSE 2.035 MW、MAE 0.996 MW、nRMSE 10.15%）和 smart persistence（RMSE 2.272 MW、MAE 1.167 MW、nRMSE 11.36%）。消融显示系统级光伏转换物理带来主要精度增益，更高阶细化仅边际提升；在测量损坏下，嵌入物理模块可将预测约束向物理可行范围，减少不合理预测。

### 四、结论（Conclusion）
将系统级光伏转换物理与选择性状态空间骨干结合，并通过物理-残差分解联合优化，可显著提升日前光伏功率预测精度与鲁棒性。物理基线提供结构先验并约束输出可行性，数据驱动残差则修正 NWP 误差和站点效应，因此该框架优于纯物理和纯数据驱动方法。

### 五、方法论与关键技术细节
数据为 15 分钟分辨率实测功率、地面气象与约 4 km 空间分辨率 NWP 预报，采用四折按时间滚动的扩展窗口交叉验证；静态电站参数（纬度、经度、倾角、方位角、额定容量）作为物理模块配置输入。物理公式包括 T_c=T_a+G_POA/(U_0+U_1 v)、η=η_STC(1+γ(T_c-25))、P_phys=min(η G_POA A_eff, P_inv,max)，其中 η_STC、γ、U_0、U_1 可学习但受物理合理边界惩罚；ReLU 保证非负，逆变器限幅仅在物理项内通过平滑饱和实现。作者有意省略行间阴影、积灰、光谱失配和详细逆变器效率曲线，认为其低于 15 分钟与 4 km NWP 输入的噪声底；局限包括实验仅基于单一电站一年数据，结论外推需更多站点和更长时段验证。
