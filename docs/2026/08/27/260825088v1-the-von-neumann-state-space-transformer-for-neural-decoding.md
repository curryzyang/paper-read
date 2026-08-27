# The Von-Neumann State-Space Transformer for neural decoding

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Morteza Sarafyazd
- 机构：BrainCo
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.25088v1) · [PDF](https://arxiv.org/pdf/2608.25088v1)

## TLDR
VN-SST is a memory-augmented Transformer whose feed-forward weights are synthesized per token from a low-rank instruction bank controlled by a slow state-space memory, achieving far more data-efficient neural decoding than a standard Transformer on motor-cortex benchmarks.

## Abstract
Cortical computation is strikingly low-dimensional: a handful of latent variables, carried in a neural population's activity, steer the higher-dimensional responses of individual neurons. Our aim is sample efficiency-models that decode well from limited data and at small parameter budgets. In a standard Transformer layer, the feed-forward block applies the same operator to every token. We suggest a von-Neumann inspired hypothesis of efficient computation as an alternative for neural decoding: a controller decodes an instruction and then executes a token-specific operator; the usual realization-a soft mixture of experts-only blends their outputs, not operators. We introduce a von-Neumann State-Space Transformer (VN-SST), a memory-augmented Transformer whose feed-forward block is a low-rank instruction bank: a shared base operator plus a small set of learned low-rank instructions, from which a per-token code synthesizes the weight matrix actually used at that token. The code is read from a low- dimensional projection of a carried state-space memory, so a slow latent trajectory acts as an instruction pointer-mirroring how low-dimensional dynamics may route cortical computation. On three motor-cortex neural-decoding benchmarks, VN-SST is far more data-efficient than a modern Transformer, each jointly predicting spikes and decoding behavior. This model wins by a wide margin on the scarcest benchmark, leads on the other two, and turns longer context into rising rather than falling accuracy. We evaluated that the network compresses a large instruction bank to a few bits per token, so program capacity acts as a control channel, not an accuracy lever. The same model is also more parameter-efficient on two small text benchmarks used for language modeling (LLMs), suggesting a generic mechanism.


## 精读解读（中文）
### 一、研究动机
皮层计算具有显著的低维特性：少数潜在变量即可组织高维神经元群体的活动。本文的目标是在有限数据和小参数预算下提升神经解码的样本效率。标准Transformer的前馈模块对每个token应用相同的算子，而作者提出一种受冯·诺依曼架构启发的假设：由控制器解码指令并执行token特异的算子，而不是像软混合专家那样仅混合多个固定专家的输出。

### 二、技术方案（Method）
提出VN-SST（Von-Neumann State-Space Transformer），在Transformer骨架中用三条并行记忆通路替代普通注意力：局部因果注意力、对角选择性状态空间模型（SSM）和基于delta规则的快速权重联想记忆；三个通路输出由控制器门控融合。前馈模块改为可编程SwiGLU：每个token的权重由共享基算子加上K个低秩指令的加权和合成，即W(t)=W0+sum_k c_{t,k} U_k V_k^T，其中每个token的代码c_t由当前token和SSM慢状态的低维投影共同经MLP生成，tanh限制在[-1,1]。实际计算不物化权重，而是通过投影到K×r指令库并缩放读取实现。训练时使用分段的截断时间反向传播，状态(s,M)跨段携带并在若干段后截断；联合优化下一时刻spike的MSE与行为解码MSE，总损失为MSE_next-spike + λ·MSE_decode（λ=10）。模型在四个Transformer层上缩放宽度，并与同等参数窗口的现代Transformer基线比较参数、数据和上下文长度三个维度的表现。

### 三、结果（Result）
在MC_RTT、MC_Maze和Area2_Bump三个运动皮层神经解码基准上，VN-SST在有限数据下显著优于现代Transformer：在最稀疏的数据预算下解码R²为0.35对0.21，并在所有数据预算的三大基准上均领先。VN-SST是唯一能将更长上下文窗口转化为解码精度上升而非下降的模型。此外，32条指令的指令库被压缩为每个token约3.4-6.5个有效算子（几比特），说明程序容量是控制通道而非精度杠杆；该模型在两个小型文本语言建模基准上也表现出更高的参数效率。

### 四、结论（Conclusion）
通过让低维慢状态轨迹充当指令指针、按token合成前馈算子，VN-SST实现了比固定算子Transformer更高的样本效率和参数效率，并能更好地利用长上下文。这种可编程算子机制在神经解码和语言建模上均有效，暗示其是一种通用计算机制，而非仅针对特定任务的技巧。

### 五、方法论与关键技术细节
关键细节包括：spike以50ms分箱，经3个bin的高斯核平滑并z-score标准化，神经延续使用128-bin前缀；模型为4层固定深度，参数量约64K-270K非嵌入参数，VN-SST因携带状态和指令库而使用更窄宽度以对齐参数窗口；SSM为对角输入相关选择机制，每通道n个潜在状态，步长由写门控制；快速权重记忆写入当前预测误差而非原始值，使回忆具备内容寻址能力；指令库默认K=8、秩r=8、流形读出维度m=8，U和U_d初始化为零从而从共享基SwiGLU开始；每个token的程序计算开销为O(Kr(d+d_ff))，新增指令成本约为完整MoE专家的r/d_ff；训练使用AdamW、余弦学习率、warmup、梯度裁剪和50个epoch，所有神经扫描报告3个种子的均值；上下文长度扫描中固定优化器步数以避免与训练预算混淆。局限性包括：单试次spike预测接近单位方差噪声底，因此主要用行为解码R²比较；参数扫描未精确匹配参数数量，而是通过重叠参数窗口揭示效率。
