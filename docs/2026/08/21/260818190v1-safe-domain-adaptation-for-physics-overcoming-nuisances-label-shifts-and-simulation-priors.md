# Safe Domain Adaptation for Physics: Overcoming Nuisances, Label Shifts, and Simulation Priors

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Ivan Kharuk
- 机构：Institute for Nuclear Research of the Russian Academy of Sciences, Moscow Institute of Physics and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18190v1) · [PDF](https://arxiv.org/pdf/2608.18190v1)

## TLDR
The paper studies how standard adversarial domain adaptation fails in physics when simulations have genuine physical mismatches and the target label distribution (e.g., energy spectrum) is itself the measurement, and proposes adaptive domain adaptation with iterative reweighting plus a label-free model-selection rule to safely handle such shifts.

## Abstract
Domain adaptation is widely used to make neural networks trained on simulations applicable to experimental data. Its premise is that the two domains differ only in nuisances, and that the quantity of interest is distributed identically in both. In physics neither assumption holds: simulations can be wrong about the physics, and the distribution of the target quantity - an energy spectrum, a redshift distribution - is often the measurement itself. We study the consequences of such mismatches on a toy air-shower benchmark in which a detector-response nuisance, a physical simulation shift, and an energy-spectrum shift can be switched on separately or together. Standard adversarial adaptation handles the conditional shifts, but once the two spectra differ it aligns them, replacing an uncontrolled bias by one anchored on the simulation prior. We present adaptive domain adaptation, which reweights the simulated events so as to focus domain adaptation on the genuine physical mismatch alone. Since the predicted spectrum depends on model training configuration, we provide a label-free model selection rule for selecting the near-the-best operation point.


## 精读解读（中文）
### 一、研究动机
标准域自适应（DA）的前提是源域与目标域仅存在 nuisance 差异且目标量分布相同，但物理应用中两个假设均不成立：模拟器可能对物理本身有误，且能谱等目标量分布往往正是待测量的对象。若直接使用对抗式 DA，当源和目标能谱不一致时，模型会把实验谱错误地对齐到模拟先验上，从而污染待测物理量。

### 二、技术方案（Method）
构建了一个 toy 气簇射探测器阵列基准，包含 9 个台站、波形时间序列与横向分布函数（LDF）等特征，可分别/同时开启探测器响应 nuisance、物理模拟偏移（LDF 斜率变化）与能谱（label）偏移。网络由一维 CNN 波形编码器和 transformer 事件编码器组成，回归头输出能量，并附加基于梯度反转层（GRL）的对抗域判别器；训练使用带标签的源域回归批和由 DA-source 与无标签目标域组成的对抗批。针对 label shift 提出自适应域自适应（ADA）：在对抗损失中动态为模拟事件加权，使网络自身估计的源与目标能谱重合，从而把能谱差异从域判别特征中移除，让对抗只作用于真实物理失配；进一步提出迭代域自适应，将上一轮预测的目标谱作为下一轮改进先验，并给出基于跨随机种子预测分歧的无标签模型选择规则。

### 三、结果（Result）
标准对抗 DA 在两域能谱相同时表现良好，但一旦能谱不同，DANN 会把重建谱拉向模拟先验，产生系统性偏差；ADA 通过重加权消除了这一偏差并显著改善目标谱重建。局部域分类器只能去除局部探测器层面 nuisance，对非局部或全局事件属性失配无效，需使用全局事件级对抗。基于跨种子分歧的模型选择规则在研究的每个案例中都能选出接近最优的配置。

### 四、结论（Conclusion）
物理中的安全域自适应必须显式区分探测器 nuisance、真实物理失配和标签分布偏移；ADA、迭代先验更新与无标签模型选择相结合，可以在能谱本身是测量目标时避免对抗对齐带来的污染，实现可靠的物理量重建。

### 五、方法论与关键技术细节
数据侧使用 Beta 分布采样能谱，训练集为平坦谱，目标集谱未知，DA-source 谱取近似目标先验；评估指标为能量预测 MAE 与预测谱和真实谱的 Wasserstein-1 距离。ADA 在回归任务中在线推断权重，无需目标标签；迭代 ADA 把预测谱反馈为下一轮先验。训练上 Adam 会放大回归与对抗梯度的冲突，导致目标恢复差三倍，故采用动量 0.9 的 SGD；网络约 23,500 参数，训练 60 轮，λ 按 DANN 调度从零上升。局限性包括基于 toy 基准验证，实际复杂探测器下先验误差与迭代收敛性仍需进一步研究。
