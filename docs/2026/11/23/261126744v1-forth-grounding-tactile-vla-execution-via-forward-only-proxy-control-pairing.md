# FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Junde Li, Wei-Han Yu, Xiangyi Chu, Yaoxin Li, Jiawei Xu, Ka-Fai Un, Pui-In Mak
- 机构：University of Macau
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26744v1) · [PDF](https://arxiv.org/pdf/2611.26744v1)

## TLDR
FORTH is a forward-only tactile VLA execution framework that pairs proxy optimization objectives with physical control observables—through a forward-only tactile encoder, token-parallel zeroth-order adapter, and slip-triggered SlipGuard—to prevent object crush, achieve 97.6% success on LIBERO suites, and reduce peak activation memory by 7.12×.

## Abstract
Vision-Language-Action (VLA) policies are widely credited with force control, operating on the unverified assumption that proxy loss minimization implies physical force grounding. In this work, we demonstrate that this assumption breaks down at three core deployment levels: frozen visual backbones discard contact geometry, downstream losses mask token-level gradient alignment, and discrete indicators trigger optimization collapse. To address these disconnections, we present FORTH, a forward-only measurement harness and execution framework that explicitly pairs the optimization objective at each level with its physical control observable. FORTH incorporates three grounded pillars: a layer-local, forward-only tactile encoder that preserves spatial contact geometry without backpropagation, a token-parallel zeroth-order adapter enabling activation-space updates, and SlipGuard, a continuous tactile verification gate that fires on incipient slip. On an elasto-plastic structural shell, FORTH's closed-loop gate peaks at 29 times lower grip force than a monotone reflex ramp, preventing structural crush where the baseline leaves permanent deformation. Furthermore, FORTH matches state-of-the-art execution performance with a 97.6% average success rate across three evaluated LIBERO suites, while reducing peak activation memory by 7.12 times compared to a backpropagated step on the same backbone. Enhanced perception enables deeper physical intelligence.


## 精读解读（中文）
### 一、研究动机
触觉VLA被广泛认为具备力控能力，但现有工作默认代理损失最小化就等于物理力接地，论文指出该假设在冻结视觉主干丢弃接触几何、下游损失掩盖token级梯度对齐、离散指标导致优化崩溃三个部署层面均不成立。因此需要把每一层的优化目标与其物理控制可观测量显式配对，并在边缘硬件上实现可测量、可纠正的触觉执行。

### 二、技术方案（Method）
FORTH将触觉VLA执行分为表示、更新规则和控制器三层，并采用成对评估协议：按成本顺序执行floor、readout、validity、mechanism四项检查，用符号一致性和失配度量判断代理目标与物理量是否同步。表示层使用两个Forward-Forward块构成的层局部前向触觉主干，输入为48×d的patch token（d=128），以tanh激活、零中心化特征和平方和goodness计算局部logistic损失，正样本为真实接触、负样本为反事实触觉状态，阈值固定为2.0且不进行全局反向传播；更新层在动作头上挂接rank-8的token并行零阶适配器，仅用前向查询在激活空间更新，每次更新需16次前向（T=8 tokens）；控制器层SlipGuard用一类剪切比连续触觉验证门检测初现滑移，并以两帧去抖触发有界实时修正。推理与训练均在冻结4-bit VLA主干上前向执行，触觉伺服500 Hz、适配器1 Hz、策略30 Hz。

### 三、结果（Result）
在弹性-塑性结构壳上，SlipGuard闭环门控的峰值抓取力比单调反射斜坡低29倍，避免了基线造成的永久形变和结构压溃；在橡胶、塑料、金属三种材料越过摩擦极限时均能动态恢复稳定抓取。三个LIBERO套件上平均成功率达97.6%，与当前最优执行性能相当，同时同一主干上峰值激活内存比反向传播步骤降低7.12倍。前向触觉主干在接触相位任务和时间顺序任务上的trunk parity分别为0.0004和0.012，表明层局部前向表示可接近反向传播表示精度。

### 四、结论（Conclusion）
代理损失下降并不自动保证物理力接地，必须逐层报告优化量与受控物理量并在二者同步时接受策略；FORTH以纯前向、层局部的方式把触觉表示、动作头适配和滑移控制统一到可配对的执行框架中，在保持SOTA级任务成功率的同时显著降低峰值激活内存并防止物理损伤。该工作说明增强触觉感知可以转化为更深的物理智能，并为边缘部署的触觉VLA提供了可测量、可纠正的执行范式。

### 五、方法论与关键技术细节
关键实现包括冻结4-bit VLA主干、无全局反向传播、两个FF块、patch维度48×128、goodness阈值2.0、层局部正负样本logistic损失、rank-8 token并行零阶适配器、每次更新16次前向、SlipGuard的一类剪切比门与两帧去抖，以及500 Hz触觉伺服、1 Hz适配器和30 Hz策略的分层频率。评估采用成本非递减的四步诊断协议和符号一致性/失配度量，并报告代理指标与物理控制量；方法复杂度优势来自仅前向查询和低秩激活空间更新。局限性在于实验主要覆盖三个LIBERO套件及特定弹性-塑性壳与三种材料的滑移测试台，阈值τ_rank、去抖帧数和FF阈值等超参对跨硬件、跨任务泛化的影响仍需更广验证。
