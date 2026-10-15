# A Performative Control Approach to Day-to-Day Traffic Signal Retiming

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Shuchang Jiang, Xinwu Qian, Santiago Segarra, Zhongyuan Zhao
- 机构：Rice University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19022v1) · [PDF](https://arxiv.org/pdf/2610.19022v1)

## TLDR
The paper proposes a performative day-to-day traffic signal retiming approach that uses offline simulation-based zeroth-order local policy gradients to incrementally update fixed-time signal timings, enabling signal policy and traveler demand/route choices to co-evolve toward performative stability while improving congestion, throughput, and robustness under mismatched demand and routing behaviors.

## Abstract
Conventional fixed-time traffic signal optimization and recent day-to-day signal retiming generally model route adaptation under prescribed route-choice behavior and origin-destination (OD) demand, while neglecting the fact that travelers' behavior can be performative to the signal control policy. A signal timing policy learned from historical traffic observations must therefore account for how its own deployment changes the distribution on which it will be evaluated in the future. We formulate this problem as performative signal control under observed traveler responses and characterize performative stability of the coupled policy-demand system. We propose incremental day-to-day retiming using the local policy gradient at the current operating point, estimated offline through simulation-based zeroth-order optimization without an explicit day-to-day demand-response model. This gradual approach provides a feasible path for policy and demand to co-evolve toward stability. Experiments on a downtown Denver network show that our approach improves congestion, throughput, and stability, generalizes across different demand levels, and remains effective when the offline simulator contains mismatched travel demand and routing behaviors.


## 精读解读（中文）
### 一、研究动机
传统固定配时优化与日复一日信号重配时通常把路径选择和OD需求视为外生给定，忽略信号策略会反过来改变出行者路径与是否出行的决策，即存在表演性效应。历史观测上训练的策略可能在部署后改变其未来被评估的需求分布，因此需要显式刻画策略-需求耦合系统的表演性稳定性。

### 二、技术方案（Method）
将路网中p个可控信号交叉口的每日固定时段配时策略x(t)（如绿信比）作为控制变量，以估计OD需求F(t)、观测交通响应Φ_G及OD成本C(t)为输入，目标最大化总社会剩余J=∑_k (|V_k|/T_h)(b_k-C_k)。控制器不显式建模未知的感知成本更新f_c与弹性需求响应f_d，而是在每天观测并估计F(t)后，用离线交通仿真做零阶梯度估计：采样M个高斯扰动x(t)+n_m，在相同估计OD需求下仿真评估总社会剩余及交叉口平均等待时间，采用多点ZOO或ZoRD（高斯过程代理与后验不确定性融合）估计∇J，并对TSS目标附加交叉口等待时间L1正则。随后按投影梯度上升更新x(t+1)=Π_Z[x(t)+η_t∇J]，其中Π_Z施加最小和最大绿时约束；感知成本按指数移动平均更新，需求根据感知成本自适应，使策略与需求逐步共同演化。

### 三、结果（Result）
在丹佛市中心网络实验中，所提日复一日重配时方法相比静态配时和响应式配时基线改善了拥堵、吞吐量和稳定性，并能泛化到显著不同的需求水平。当离线仿真器中的出行需求与路径行为同真实系统存在失配时，方法仍然有效，说明基于零阶梯度的增量更新对模拟器偏差和OD观测噪声具有一定鲁棒性。

### 四、结论（Conclusion）
本文将日复一日信号重配时表述为表演性控制问题，并证明通过局部策略梯度增量更新可为信号策略与出行需求提供一条共同演化至表演性稳定的可行路径。该方法无需显式的日间需求响应模型，适合依赖聚合观测而非实时细粒度感知的固定配时系统，但其目标主要是表演性稳定而非表演性最优。

### 五、方法论与关键技术细节
关键先验与数据包括未知的Φ_G、f_c、f_d，控制器仅能从交通感知和估计获得V(t)、C(t)、F(t)，并假设仿真器能局部近似真实响应；数值环境中感知成本用参数γ的指数移动平均生成，需求用含F_min、F_ref、c_ref和敏感度β_k的指数弹性模型生成。目标函数为相对外部选项的总社会剩余，实际观测含噪声，优化时用w≥0的等待时间L1正则增强交叉口级信用分配，ZoRD用全局GP拟合TSS并由局部GP建模各交叉口等待时间。超参与实现约束包括ZOO样本数M、扰动尺度σ、步长η_t、最小和最大绿时投影；每日需进行M次仿真查询，计算成本随交叉口数与样本数增长。局限性在于省略了表演性梯度中的长期诱导需求项∂F*/∂x，因而只追求一阶稳定而非最优，且性能依赖OD估计精度与仿真器对路由和需求行为的近似质量。
