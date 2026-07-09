# Cross-Trajectory Chimera Interventions Reveal Dissociable Roles of Weight Magnitude and Direction in Grokking

- 区域：精读区
- 排名：2
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Truong Xuan Khanh
- 机构：Clevix LLC
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06628v1) · [PDF](https://arxiv.org/pdf/2607.06628v1)

## TLDR
Cross-trajectory chimera interventions on grokking tasks reveal that weight direction carries transferable circuit identity with a threshold-like transfer predicted by recipient norm, while weight magnitude only modestly affects grokking delay.

## Abstract
Which properties of a partially trained network are causally portable to a different, independently trained network? Single-trajectory interventions show necessity within one run, not portability across runs. We introduce cross-trajectory chimera interventions: given two runs from different seeds, we split each weight vector into a norm and a unit direction, recombine one run's norm with the other's direction, and continue training. On two modular-arithmetic tasks that grok, the components dissociate. Direction carries a transferable, donor-specific circuit identity: implanting a donor's direction at the recipient's norm drives the run to the donor's circuit in 40/40 cases, while an angle-matched random control yields no shift. The transfer is threshold-like, and its location is predicted by the recipient's norm, separating perfectly by norm class over all 20 pairs (joint permutation probability 1.9e-4). Norm carries only a modest, distributed delay effect and no identity signal. An adaptive bisection procedure localizes the threshold to +/-1/64. Direction indexes which solution a trajectory approaches; norm governs how susceptible that identity is to being overwritten.


## 精读解读（中文）
### 一、研究动机
单轨迹干预只能证明属性在单个训练运行中的必要性，但无法证明其在不同独立训练运行之间是否可移植。本研究引入跨轨迹嵌合体干预，通过分解权重大小与方向并重组，探索哪些属性具有跨轨迹因果可移植性。

### 二、技术方案（Method）
在两个模算术任务（模59加法和乘法）上训练单层Transformer（嵌入维度128），使用全批次AdamW优化（学习率1e-3，权重衰减1.0，β=(0.9,0.98)）。从不同种子训练的两个预泛化检查点，将权重向量分解为范数r和单位方向u，形成嵌合体（如r_B u_A）并继续训练。通过球面线性插值（slerp）沿方向插值施加剂量反应，并用角度匹配随机方向控制（matched_random）区分供体特异性内容与一般角扰动。电路身份度量采用token嵌入功率谱的余弦相似度（加法直接FFT，乘法先按离散对数域重排后FFT）。阈值定位通过自适应二分法以±1/64分辨率实现。

### 三、结果（Result）
方向携带可转移的供体特异性电路身份：40/40个独立重组中最终电路遵循方向供体（符号一致，每任务每变体符号检验p=2×10^{-3}），而角度匹配随机对照无身份偏移（平均值接近零，58/60和60/60可区分）。范数仅对泛化延迟有微小分布广泛的效应（约−0.707 vs −0.719），不携带身份信号。阈值位置完全由接收者范数预测，20对两任务中按范数类完美分离（联合精确排列概率1.9×10^{-4}），并且阈值在±1/64分辨率内可定位。

### 四、结论（Conclusion）
权重的方向索引轨迹接近的解身份，而范数控制该身份被覆盖的易感性。跨轨迹嵌合体干预揭示了权重幅度和方向在grokking中的可分离作用：方向是解身份的便携载体，范数提供状态依赖的开关。

### 五、方法论与关键技术细节
关键数据：模59加法和乘法，50/50训练/测试分割；模型为单层Transformer（嵌入维度128），优化器为AdamW（学习率1e-3，权重衰减1.0）。分解使用径向-角度分解θ=r·u。电路身份度量需按任务选择FFT域：加法直接对token索引变换，乘法先对离散对数域重排。统计采用10对独立种子（无种子重用），使用精确符号检验和簇级统计。阈值定位通过自适应二分法，每个对约三次评估达到±1/64分辨率，考虑到CUDA非确定性报告为分辨率界限。局限性包括：结果依赖于全批次训练和重置优化器（但优化器状态消融后结论成立）；延迟效应较弱且不可局部化；方法要求训练协议稳定。角度匹配随机控制是创新点之一，用于分离供体特异性内容。
