# GeoID-PINN: Identifiability-Aware Regional Epidemic Inference with Geographic Coupling

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Weixiong Hua, Fan Bu
- 机构：University of Michigan
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02633v1) · [PDF](https://arxiv.org/pdf/2608.02633v1)

## TLDR
GeoID-PINN introduces a physics-informed neural network for regional SIRD epidemic inference that couples regions through a row-stochastic source-composition matrix regularized by spatial priors, achieving improved point forecasts for COVID-19 in Louisiana while demonstrating that accurate trajectory fits do not guarantee identifiability of the underlying regional coupling structure.

## Abstract
Regional surveillance data reflect local transmission, reporting, seeding, and external infection pressure, which are difficult to identify separately. We introduce GeoID-PINN, a physics-informed neural network (PINN) for susceptible-infectious-recovered-deceased (SIRD) dynamics. The model represents spatial dependence with a row-stochastic source-composition matrix whose rows assign nonnegative source weights that sum to one. We regularize this matrix toward a spatial prior constructed from distance, adjacency, commuting, or lead-lag information. In a four-region simulation with known truth, a compatible distance prior gives source-composition error 0.099. The error rises to 0.159 without regularization and 0.577 under a strongly misspecified prior, while trajectory fit and transmission-scale estimates remain similar. Accurate trajectories therefore do not guarantee recovery of the regional dependence structure. We also evaluate GeoID-PINN retrospectively using COVID-19 data from 64 Louisiana counties. Relative to an autoregressive negative-binomial baseline, Forecast-Trained Geo-PINN reduces mean squared error (MSE) from 32,957 to 11,468 and mean absolute error (MAE) from 70.60 to 57.73. The baseline has lower negative log likelihood (NLL), 5.158 versus 5.346, indicating better distributional fit but worse point accuracy. In a controlled 15-county comparison, county adjacency reduces MSE by 6.85 percent and MAE by 3.1 percent. Similar performance across plausible priors supports structured regularization but not unique edge recovery. These results require prior-sensitivity and observation-model checks before interpretation.


## 精读解读（中文）
### 一、研究动机
区域监测数据反映本地传播、报告、初始种子和外部感染压力，这些成分难以分别识别。现有流行病PINN在估计区域相互依赖结构时存在敏感性和可识别性问题，因此需要一种能感知可识别性并进行区域耦合推断的方法。

### 二、技术方案（Method）
提出GeoID-PINN，一种用于易感-感染-恢复-死亡（SIRD）动力学的物理信息神经网络。状态网络输出未约束logit，经softmax映射为四个仓室状态，保证非负且每个区域人口总数守恒。空间依赖通过行随机源组成矩阵C建模，其元素非负且行和为1，采用带结构掩码的行softmax参数化；将该矩阵正则化到由距离、邻接、通勤或领先滞后信息构建的空间先验C0。损失函数包括状态通道NMSE、发病率NMSE（权重20）、SIRD残差物理损失、初始条件损失和先验损失；训练采用两阶段优化：先冻结C的logit参数B进行warmup，再联合优化所有参数。

### 三、结果（Result）
四区域仿真中，相容距离先验给出源组成误差0.099，无正则化误差升至0.159，强错误先验下误差达0.577，而轨迹拟合和传播尺度估计保持相似。路易斯安那64县COVID-19回顾评估中，预测训练的GeoID-PINN相对自回归负二项基线将MSE从32957降至11468，MAE从70.60降至57.73；基线NLL更低（5.158对5.346），分布拟合更好但点预测精度更差。15县对照中，县邻接先验使MSE降低6.85%，MAE降低3.1%。

### 四、结论（Conclusion）
准确拟合轨迹并不能保证恢复区域依赖结构；结构化正则化有助于稳定推断，但无法唯一恢复边权重。结果支持使用先验正则化，但在解读前必须进行先验敏感性和观测模型检验。

### 五、方法论与关键技术细节
数据输入为区域S、I、R、D状态观测和发病率，观测掩码和尺度预先固定；恢复率γ和死亡率μ可固定或通过sigmoid约束学习，报告因子固定以防额外不可识别性。C通过掩码行softmax构造，先验损失使用固定尺度s_C=0.10，正则化强度λ_C按场景变化。损失权重为：每个状态通道1、发病率20、物理损失1、初始条件10。优化使用Adam，合成实验800 epoch且前200冻结B，学习率3e-3。局限性：在可用观测下模型存在实际不可识别性，C应解释为条件源组成而非真实移动或因果传播网络。
