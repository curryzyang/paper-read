# Threshold Compatibility and Support-Selection Diagnostics in Neural Discovery of Partial Differential Equations

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Zeen Song
- 机构：Beijing University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37726v1) · [PDF](https://arxiv.org/pdf/2610.37726v1)

## TLDR
The paper derives exact threshold-compatibility and stability diagnostics showing that accurate coefficient regression in neural PDE discovery can still yield incorrect support and equations, and uses finite experiments to distinguish threshold incompatibility, refit damage, and score rejection without claiming general correction or recovery.

## Abstract
Accurate regression need not yield the correct equation after support selection. For a median/sample-standard-deviation threshold in neural PDE discovery, we derive an exact two-signal retention boundary and a complete-vector perturbation bound. Exact advection-diffusion libraries lose diffusion despite coefficient recovery to numerical precision. True-support refits of forty saved sparse states reduce diffusion error without restoring all derivative accuracy. A fixed sequential threshold ridge comparator recovers exact support in sixty ideal controls but selects extra terms in every learned state. All-fold correct-support candidates are rejected by conditional validation; post hoc energy pooling preserves their higher minimum loss in all sixty states. Supplied-support estimates outperform unchanged selected equations in all 240 physical-residual comparisons on four unused analytic trajectories. With coefficients, observation points and weights fixed, exact replacement of the learned library and target reverses their learned-row ordering in 59/60 states. Weighting both losses also fails the specified Burgers diffusion-benefit criterion at every tested budget. These finite diagnostics distinguish threshold incompatibility, refit damage and score rejection; they establish neither automatic correction nor general recovery or predictive stability.


## 精读解读（中文）
### 一、研究动机
神经网络PDE发现中，回归准确并不保证支持选择后得到正确方程，阈值可能删除回归已准确估计的系数，而神经场误差、重拟合损伤与选择评分拒绝又可能相互混淆。现有流程把神经场重建、系数估计和稀疏支持选择耦合在一起，仅看系数误差难以判断失败来源。本文在固定流程内建立阈值保留边界，并用支持干预、冻结方程评分和外部物理残差比较来区分这些失败模式。

### 二、技术方案（Method）
对观测位置O构造均值一包含权重w_i，训练神经场f_theta，以数据误差和PDE残差r_i=f_t-Theta_i(f)beta联合优化，Theta为含12项直至f^2 f_xxx的库，惩罚为按观测行范数与目标范数归一化的L1，并比较M1、H_data、H_both三种损失。支持规则采用下中位数m与样本标准差s的严格阈值|z_j-m|>s，推导两信号保留边界r_p=(1+sqrt(1+(p-1)^3))/(p-1)^2及完整向量扰动界(2+sqrt(p/(p-1)))||e||∞。对40个稀疏状态做原始支持与供真支持{u_x,u_xx}的重拟合，复制场和保留系数、重置Adam并训练25001步；另用5折且仅训练行范数的STRidge比较器（主ridge为1e-6及预设网格）和4条未参与训练的解析轨迹外部物理残差评分评估冻结方程。

### 三、结果（Result）
20个精确库解的数值秩为12、物理系数恢复到1.267e-15，但中位数/SD阈值全部删除扩散项，缩放扩散/对流比0.229026至0.241197均低于r_12=0.309889，导致0/20精确支持且扩散误差恒为0.1；H_both在8/10掩码改善全场MSE（均值0.00136859至0.00111011），但平均网格相对L2 u_xx误差仍为30.8901和18.1893。供真支持重拟合在全部40对改善扩散误差并满足块级均值/中位数与聚合护栏，但观测u_xx在B1/B2分别有6/10、7/10和9/10、8/10对变差，u_xxx亦多处变差；STRidge在60个理想对照恢复精确支持却在每个学习状态多选，所有折正确支持候选被条件验证拒绝，事后能量池化在全部60状态保留其更高最小损失。供支持估计在4条未用解析轨迹的240次物理残差比较中全部优于未改选方程；固定系数、观测点和权重下精确替换学习库与目标使学习行排序在59/60状态反转；对两个损失同时加权在每个测试预算均未通过Burgers扩散收益准则。

### 四、结论（Conclusion）
这些有限诊断能够区分阈值不相容、真支持重拟合损伤和评分拒绝，说明精确回归或正确支持并不自动转化为正确方程、导数精度或预测稳定性。研究结果不支持自动纠正、通用恢复或预测稳定性的结论，且证据来自共享拟合状态的诊断性比较而非独立恢复试验或前向模拟。

### 五、方法论与关键技术细节
阈值实验使用p=12，下中位数、样本标准差和严格等号排除均按执行代码约定；Proposition 1要求p>=4且不适用于非零冗余系数，零填充系数可使p=17时排除而p=18时保留，扰动界只约束归一化向量而非物理系数或导数。数值设计使用256×101网格上的2000个候选点和高斯噪声，仅含噪场值进入训练，无边界损失或供给导数真值；60个解析状态来自两条轨迹且块内掩码共享噪声与初始化，不是60个独立问题。STRidge使用5个连续时间折、仅训练行范数、主ridge 1e-6及{0}∪{1e-6+j/8:j=0,...,48}网格，one-SE仅为稀疏启发式且验证条件于已见全部观测行的神经表示。外部评分在4条未用解析轨迹上用数值积分近似归一化PDE残差能量，规则在本地评分前冻结但无外部预注册；供支持比较器只用各状态原始学习行和权重拟系数，不使用真系数或外部数据。局限性包括有限诊断、oracle支持、共享状态复用、float32/float64评估筛查未替代float64重训练，以及Burgers加权负结果仅覆盖指定准则与预算。
