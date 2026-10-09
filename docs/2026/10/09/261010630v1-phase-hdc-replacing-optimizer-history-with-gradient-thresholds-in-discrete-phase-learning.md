# Phase-HDC: Replacing Optimizer History with Gradient Thresholds in Discrete Phase Learning

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ahmed Nebli
- 机构：Mathalyse Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10630v1) · [PDF](https://arxiv.org/pdf/2610.10630v1)

## TLDR
Phase-HDC trains a discrete phase-memory hyperdimensional classifier using only thresholded one-step sign-gradient updates—eliminating optimizer history to store 16–23× less than float32 Adam (and 4–6× less than 8-bit Adam)—at the cost of about five accuracy points on average while still beating 8-bit Adam on 6 of 11 datasets.

## Abstract
Training a compact model often needs far more memory than storing it, because the optimizer keeps its own records of past gradients. For a hyperdimensional classifier whose learned parameters are low-bit angles, which we call a \emph{phase memory}, these records take several times more memory than the model itself. We ask whether such a model can be trained while storing nothing but the model. The proposed method, Phase-HDC, turns each stored angle by at most one step per update, against the sign of its current gradient, and only when that gradient is large enough. We show that this simple rule is the exact solution of a first-order loss model in which every changed parameter pays a fixed cost. When everything except the update rule is held fixed, Phase-HDC matches the accuracy of Adam with 6-bit moments while storing three times less. Across eleven image, tabular, and text datasets, it stores 16--23$\times$ less than standard float32 Adam and 4--6$\times$ less than 8-bit Adam. The price is an average loss of about five accuracy points against float32 Adam, while Phase-HDC is more accurate than 8-bit Adam on six of the eleven datasets, including byte-level text prediction, where 8-bit Adam collapses. Instrumented training runs explain these outcomes. Once parameters must sit on a discrete grid, Adam's moments mainly decide whether a parameter moves at all, a decision that a threshold on the current gradient can make without memory, and coarse quantization of the moments breaks this decision for inputs that the data rarely contain. The storage savings are logical state rather than measured hardware memory.


## 精读解读（中文）
### 一、研究动机
训练紧凑的相位超维分类器时，持久训练状态往往远大于模型本身：Adam 的一阶/二阶矩和低精度训练所需的 float32 主副本使 6-bit 相位参数模型的状态开销 Γ 可达 16，现有 8-bit Adam、Adafactor 等只压缩历史而未消除历史。作者因此追问：能否只存模型本身、以 Γ=1 完成学习，并量化这种极端内存节省的精度代价。

### 二、技术方案（Method）
Phase-HDC 将每个位置/值/类别坐标存为整数 q∈{0,…,K−1}，对应角度 2πq/K，K=2^k（实验用 6-bit、K=64）；前向仍按相位 HDC 做绑定（角度模 K 相加）、捆绑（单位相量求和）和与类别向量的模长重叠 softmax。训练时对每个坐标只依据当前 minibatch 梯度做一步离散更新：若 |g_j|>τ_j，则沿 −sign(g_j) 方向转动一个刻槽，否则不动；不保留一阶矩、二阶矩或高精度主副本。该规则被证明是带每坐标固定写入代价的一阶线性化损失模型的精确解，且相位宽度同时决定角度步长和有效阈值。

### 三、结果（Result）
在固定 6-bit 参数、分类头、初始化、数据划分与验证调参的受控实验中，Phase-HDC 以约三分之一的状态达到与使用 6-bit 矩的 Adam 相当的准确率。跨 11 个图像、表格和文本数据集，其逻辑持久状态比标准 float32 Adam 少 16–23 倍、比 8-bit Adam 少 4–6 倍，相对 float32 Adam 平均损失约 5.3 个准确率点（图像/表格 7.0，文本 3.3），并在 11 个数据集中的 6 个上优于 8-bit Adam，包括 8-bit Adam 崩溃的字节级文本预测。仪器化训练进一步发现，Adam 的矩在离散网格上主要充当“是否移动”的门控，而当前梯度阈值可无记忆地完成该判断；逐张量矩量化会破坏对稀有输入的判断，访问频率与大跳变率的 Spearman 相关为 −0.98。

### 四、结论（Conclusion）
Phase-HDC 表明，在离散相位学习中优化器历史可以被当前梯度阈值替代，从而以 Γ=1 的逻辑状态训练可学习相位记忆，代价是相对 float32 Adam 约 5 个准确率点的下降。其优势在内存极受限的边缘端就地学习场景，且机制上解释了量化 Adam 在稀有输入和字节级文本上的失效。主要局限是节省为逻辑数组状态而非实测硬件内存，且梯度仍以浮点计算，未实现端到端整数训练。

### 五、方法论与关键技术细节
关键实现点包括：模型参数为 K=2^k 的整数相位，绑定用模 K 加法、捆绑用单位复数求和、类别分数用重叠模长送入 softmax；更新规则无动量、无二阶矩、无主副本，每步每个坐标最多移动一个刻槽，阈值 τ_j 与 −sign(g_j) 构成死区；状态开销 Γ 定义为持久训练状态与持久模型状态之比，6-bit 模型配 float32 Adam+主副本时 Γ=16，而 Phase-HDC 为 Γ=1。实验覆盖 11 个图像/表格/文本数据集（含 5 个字符级文本语料、词表至 256 符号），受控基线包括 float32 Adam、8-bit Adam、6-bit 矩 Adam 和投影 Adam；模拟显示更新可容忍 4-bit 梯度算术。局限性包括：存储节省为逻辑状态而非硬件实测，8-bit Adam 基线使用逐张量仿射量化而非分块动态量化，未实现随机舍入和整数端到端流水线，且相对 float32 Adam 仍有平均精度差距。
