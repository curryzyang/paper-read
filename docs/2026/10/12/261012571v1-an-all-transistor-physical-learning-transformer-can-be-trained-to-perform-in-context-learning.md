# An all-transistor physical-learning transformer can be trained to perform in-context learning

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Michael C. Abbott, Benjamin B. Machta
- 机构：Yale University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12571v1) · [PDF](https://arxiv.org/pdf/2610.12571v1)

## TLDR
This paper introduces an all-transistor physical-learning transformer that restores bidirectional error propagation using dyadic circuits and MOSFET-based attention, and shows in simulation that it can be trained to perform an in-context learning task.

## Abstract
Most systems trained by equilibrium propagation or coupled learning are in the same class as multi-layer perceptrons: while they may be universal function approximators, they struggle to learn associative tasks which are easy for transformers. Equilibrium propagation relies on a bidirectional flow of information through the physical system between input and output. The reverse flow is broken by more complex nonlinear systems, such as those performing multiplication which is needed to express dot-product attention. Here we explicitly restore this bidirectional flow by introducing extra circuit elements for this purpose into a double or dyadic circuit. We then use these ideas to construct an attention mechanism exploiting the exponential current law of sub-threshold MOSFET devices. We show that in simulations this circuit can be trained to perform a simple in-context learning task, despite using realistic reverse components which transmit only an approximate gradient. For this training to succeed we need cross-entropy loss (not mean squared error). We generate nudges appropriate for this loss using a novel floating circuit element, based on the same MOSFET sub-circuit used for softmax. We train the resistors in this circuit using the Lion optimiser, which can be implemented using one capacitor per parameter to store local memory of past gradient estimates.


## 精读解读（中文）
### 一、研究动机
现有平衡传播或耦合学习系统多对应多层感知机，虽可万能逼近函数，却难以学习Transformer擅长的关联与上下文任务；其关键限制是平衡传播依赖输入输出间的双向信息流，而点积注意力所需的乘法等非互易非线性会阻断误差信号反向传播。本文因此试图显式恢复物理系统中的双向误差流，构建能表达并训练注意力机制的全晶体管物理学习电路，以检验其是否可完成上下文学习。

### 二、技术方案（Method）
作者采用双/二元电路：每个节点和元件成对复制，输入钳位，输出取两拷贝均值作为前向计算，训练时在输出对之间注入与损失梯度成正比的nudge，两拷贝差值编码反向误差，并用1/(4β)电压平方差估计每个可调电阻的梯度。注意力部分利用亚阈值MOSFET的指数电流律构造类似Bahdanau/bump的匹配机制，并以共享固定尾电流实现softmax；交叉熵损失及其nudge由同一MOSFET子电路构成的浮置元件产生。在仿真中，字符序列输入被编码为嵌入向量，目标是让末字符与先前字符匹配并检索邻近输出；所有电阻参数用Lion优化器更新，每个参数仅用一个电容存储过往梯度估计。

### 三、结果（Result）
仿真表明，该双电路可在使用仅近似反向梯度的现实元件条件下被训练完成简单上下文学习任务，即执行类似归纳头的匹配与检索。训练成功依赖交叉熵损失而非均方误差，且浮置交叉熵nudge电路与Lion优化器均可有效工作。这为物理学习电路能学习MLP难以学会的关联任务提供了具体证据。

### 四、结论（Conclusion）
通过显式恢复双向误差传播，物理学习系统可超越MLP类电路，构建具备注意力与Transformer式上下文学习能力的可训练模拟电路。作者进一步提出猜想：仅由成对互易相互作用、其状态最小化能量的物理学习系统，无法高效学习上下文学习任务。该工作为模拟计算与物理学习结合提供了新路线，但仍需真实硬件验证及更复杂任务检验。

### 五、方法论与关键技术细节
任务为字符级简单ICL，输入矩阵规模小于MNIST，但该关联任务对MLP很难；电路参数为可调电阻，并保持成对拷贝g_ab=g_a'b'，梯度估计为dL/dg_ab≈[ (Δv_ab)^2-(Δv_a'b')^2 ]/(4β)，在β足够小且二极管不翻转时对电阻-二极管网络精确。前向输出为成对节点电压均值，交叉熵nudge由基于MOSFET的浮置电路产生，注意力使用亚阈值指数律、bump电路和共享尾电流softmax；Lion优化器以每参数一电容实现局部梯度记忆。局限性包括结果仅来自仿真、反向元件只传近似梯度、必须用交叉熵而非MSE、任务较简单，且精确dyadic实现需要特殊二极管或额外元件，尚未证明大规模与真实器件鲁棒性。
