# Causal neural set filtering for online multi-target tracking

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Zhongdi Liu, Huangyu Dai
- 机构：Hangzhou Applied Acoustics Research Institute, Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16054v1) · [PDF](https://arxiv.org/pdf/2609.16054v1)

## TLDR
CNSF is a causal neural set filter for online multi-target tracking that encodes only current measurements while propagating a structured recursive track state with Sinkhorn association, Kalman-shaped moment-matched updates, and Bernoulli lifecycle modeling, reducing GOSPA and T-GOSPA by 19.3% and 30.4% over Track-MT3 with 55.9% fewer parameters and a 3.76× CPU inference speedup.

## Abstract
Transformer-based multi-target tracking (MTT) jointly learns data association and state estimation, but MT3/Track-MT3-style trackers repeatedly re-encode measurement windows, incurring redundant computation. We propose Causal Neural Set Filtering (CNSF)\footnote{\href{https://github.com/daihuangyu/CNSF}{Code: https://github.com/daihuangyu/CNSF}}, a neural set filter that encodes only current measurements while carrying past evidence in a structured recursive track state. CNSF combines exclusive Sinkhorn association, association-conditioned Kalman-shaped updates with moment matching, and recurrent Bernoulli lifecycle modeling with measurement-driven birth. These mechanisms impose soft one-to-one constraints, propagate association-induced state uncertainty, and support existence estimation under missed detections and birth--death transitions. On a held-out three-regime simulated test set, CNSF reduces mean GOSPA and T-GOSPA relative to Track-MT3 by 19.3\% and 30.4\%, with 55.9\% fewer parameters and a $3.76\times$ speedup in single-thread CPU inference.


## 精读解读（中文）
### 一、研究动机
现有 MT3/Track-MT3 等 Transformer 多目标跟踪器联合学习数据关联与状态估计，但会反复重编码测量窗口，造成冗余计算；其传播的查询也未在结构化滤波状态中显式携带运动不确定性与目标存在性。为此，CNSF 旨在用因果递归航迹状态替代窗口条件集合预测，仅编码当前测量并递归携带历史证据。

### 二、技术方案（Method）
CNSF 为每个航迹维护包含运动均值/协方差、学习查询、生命周期记忆、Bernoulli 存在概率和离散记账信息的递归状态。每帧仅用置换等变 Transformer 编码当前测量一次；预测阶段以匀速模型和傅里叶时间嵌入驱动轻量头，调整查询、加速度、过程协方差与生存概率。关联采用增广 Sinkhorn，在含 MISS、UNCLAIMED 和松弛项的分数矩阵上施加软一对一约束，分数融合学习对证据、物理马氏兼容门控和存在先验。对每个 PAIR 假设先用学习观测协方差执行带有限增益残差的 Kalman 形状更新和 Joseph 形式协方差更新，并用 GRU 更新查询；随后按 Sinkhorn 行权重重归一化，对 PAIR/MISS 假设做矩匹配，将多假设塌缩为单航迹高斯状态并保留关联诱导的协方差。生命周期通过 Bernoulli 存在概率、目标度加权支持和 GRU 记忆更新，未认领测量经 birth 头产生新航迹。训练使用跨帧目标对齐保持身份，Hungarian 仅用于出生候选匹配且离散分配在推理时不用，损失包含集合定位/分类、概率集合风险代理、关联、出生、存在、生存和基数项，并端到端 BPTT。

### 三、结果（Result）
在留出的三档仿真测试集上，CNSF 相对 Track-MT3 将平均 GOSPA 和 T-GOSPA 分别降低 19.3% 和 30.4%，同时参数量减少 55.9%，单线程 CPU 推理获得 3.76 倍加速。该测试覆盖出生率 0.04 到 0.12、检测概率 0.95 到 0.85、杂波率 5 到 15 的递增难度场景，评分帧为 20 到 99，并使用 GOSPA、Pro-GOSPA 与 T-GOSPA 评估。

### 四、结论（Conclusion）
CNSF 用结构化递归航迹状态替代窗口条件集合预测，仅编码当前测量，在软排他关联、关联条件矩匹配更新和 Bernoulli 生命周期/出生建模共同作用下，显式传播运动不确定性与存在性，并能处理漏检和出生死亡转换。结果表明该递归神经集合滤波器在仿真多目标跟踪中相较 Track-MT3 同时提升精度与效率，为在线 MTT 提供了可替代窗口重编码范式的方案。

### 五、方法论与关键技术细节
数据为三个 100 帧仿真点目标场景，dt=0.1，区域[-10,10]^2，初始与新生位置/速度采样自 N(0,3I2)，S1-S3 的出生率、生存概率、检测概率、过程噪声、测量噪声、杂波率为(.04,.99,.95,0,0,5)、(.08,.98,.90,.04,.02,10)、(.12,.97,.85,.08,.03,15)，起始目标数 6/6/10，真值基数上限 16，测试每档 50 条轨迹。损失权重为(1,.1,1,.5,.35,.25,.03)，风险截断 c_risk=2，关联事件权重(w_p,w_m,w_u)=(2,1,1)，漏检权重 lambda_miss=2，风险系数 rho 在 4k 到 6k 步渐增；Sinkhorn 在 log 空间执行 N_sk 次迭代并含温度 tau_sk。局限在于每个航迹仅保留矩匹配后的单高斯状态而不传播多关联假设，依赖匀速运动、高斯噪声和仿真身份监督；评估仅限仿真点目标，真实数据泛化与模型失配鲁棒性尚未验证，T-GOSPA 使用跟踪器原生身份且不做事后重连。
