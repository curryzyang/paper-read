# Learning infinite context windows in recurrent architectures via spatial neural computing

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Aleix Salvador-Pomarol, Arthur N. Montanari, Earl K. Miller, Adilson E. Motter, Jorge Cortés
- 机构：UC San Diego, Northwestern University, Massachusetts Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10690v1) · [PDF](https://arxiv.org/pdf/2610.10690v1)

## TLDR
The paper proposes SpatialRNN, a second-order recurrent architecture that replaces direct neuron-to-neuron connections with a PDE-governed spatial medium, yielding an implicit infinite-order memory with an unbounded receptive field and stable gradients for long-horizon sequence modeling with fewer parameters.

## Abstract
Recurrent neural networks (RNNs) offer linear-time scaling with sequence length while requiring only constant memory, yet they struggle to capture long-range dependencies due to vanishing gradients and limited receptive fields. To address these limitations, we introduce a second-order recurrent model in which the standard neuron-to-neuron communication is replaced by a spatially evolving field governed by (discretized) partial differential equations. Drawing inspiration from the role of cortical waves in brain computation, this mechanism allows structured spatiotemporal patterns to serve as an implicit, high-capacity memory. We show that the resulting model is equivalent to a structured infinite-order RNN in which the current state depends explicitly on its entire history of past states, yielding an effectively unbounded receptive field with a fixed number of parameters. We further derive constructive conditions to ensure marginal stability, constraining the gradient spectrum on the unit circle and thereby eliminating vanishing and exploding gradients. Empirically, the proposed architecture outperforms other recurrent models on long-horizon benchmarks while using substantially fewer parameters, demonstrating that spatial dynamics can effectively bridge the gap between efficient inference and long-term memory.


## 精读解读（中文）
### 一、研究动机
标准RNN虽以固定内存和线性时间处理序列，但受梯度消失/爆炸与有限感受野限制，难以建模长程依赖；Transformer等又带来O(T)推理内存与O(T^2)注意力开销。作者希望从动力学系统与皮层行波获得启发，找到一种能在固定参数量下保持任意长历史影响、且梯度不衰减的循环结构。

### 二、技术方案（Method）
提出SpatialRNN：用受离散偏微分方程控制的二维空间介质psi(x,t)替代神经元间直接全连接，介质由rho与gamma控制传播/阻尼，Laplacian等空间算子L与输入驱动beta(h(t))共同作用；离散后得到二阶线性差分方程psi_t = W_bar psi_{t-1} + W_bar2 psi_{t-2} + B h_{t-1}。循环更新为h_t = Phi(W_x x_t + W_psi psi_t + b_h)，输出softmax同时读取h_t、psi_t与psi_{t-1}，初始状态置零，Phi可为tanh或ReLU。该介质相当于隐式生成无限阶卷积核，使当前状态显式依赖全部历史，同时只需固定大小矩阵W_bar、W_bar2、B、W_psi等参数。

### 三、结果（Result）
理论上证明SpatialRNN在零初始条件下等价于结构化无限阶RNN，psi_t可写成对全部历史h_{t-k}的卷积，权重矩阵由递归W_k = W_bar W_{k-1} + W_bar2 W_{k-2}生成，因而获得参数高效、O(1)推理内存的无界感受野。通过构造性边际稳定条件，可将梯度谱约束在单位圆上，消除消失与爆炸梯度；实验显示训练后的SpatialRNN在长输入轨迹上梯度范数近乎恒定，并在长时程基准上优于其他循环模型且参数量显著更少。

### 四、结论（Conclusion）
空间动力学可作为循环网络的高容量隐式记忆基质，使模型在固定参数与常数内存下具备无限上下文窗口和长程保持能力。该工作表明，解决长程梯度问题的关键不只是循环矩阵谱，而在于让输入无关的二阶/空间项控制梯度模长，从而兼顾高效推理与长期记忆。

### 五、方法论与关键技术细节
关键实现包括波方程特例：取Psi的二阶时间差分与离散Laplacian W_Delta，得到Störmer-Verlet形式W_bar = 2I + c^2 Delta t^2 W_Delta、W_bar2 = -I；空间介质在二维坐标上演化，rho与gamma可空间变化，beta将神经活动写入介质；理论分析基于冻结时间梯度与边际稳定条件，而非仅循环矩阵特征值。复杂度上推理内存O(1)、计算量随序列长度O(T)，参数量不随阶数或历史长度增长；局限是无限感受野不等于无损记忆容量，也不自动保证长程影响，有限精度与固定维状态仍限制信息保持，且实际长程性能依赖梯度设计条件。
