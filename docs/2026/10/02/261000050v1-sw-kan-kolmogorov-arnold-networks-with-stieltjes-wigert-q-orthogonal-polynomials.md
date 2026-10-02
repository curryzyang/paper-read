# SW-KAN: Kolmogorov-Arnold Networks with Stieltjes-Wigert q-Orthogonal Polynomials

- 区域：精读区
- 排名：6
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Amirhosein Azarpour, Seyyed Moein Kazemi
- 机构：Shahid Beheshti University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00050v1) · [PDF](https://arxiv.org/pdf/2610.00050v1)

## TLDR
SW-KAN replaces B-spline edge activations in Kolmogorov-Arnold Networks with Stieltjes-Wigert q-orthogonal polynomials on the semi-infinite domain \((0,\infty)\), using an exponential-of-tanh mapping and a stable \(\mathcal{O}(N)\) recurrence to achieve superior accuracy-efficiency and robust performance in resource-constrained tasks.

## Abstract
Kolmogorov-Arnold Networks (KANs) represent a paradigmatic shift in deep learning by replacing fixed node activations with learnable univariate functions on edges, offering enhanced interpretability and parameter efficiency. While recent polynomial-based KAN variants have addressed the computational overhead of original B-spline implementations, they introduce a fundamental yet underexplored challenge: the domain mismatch between unbounded real-valued inputs and the bounded or semi-infinite support of orthogonal polynomial bases. To address this limitation, we propose the Stieltjes-Wigert Kolmogorov-Arnold Network (SW-KAN), a novel architecture that employs Stieltjes-Wigert q-orthogonal polynomials defined on the semi-infinite domain (0, infinity). We introduce a smooth exponential-of-tanh mapping that stably bridges the domain gap while preserving well-conditioned gradients, and leverage a numerically stable three-term recurrence that evaluates polynomial expansions in O(N) operations without special-function calls. Through comprehensive experiments spanning image classification and continuous function approximation, we demonstrate that SW-KAN achieves superior accuracy-efficiency trade-offs across diverse tasks. The log-normal weight structure and learnable q-parameter of Stieltjes-Wigert polynomials provide a distinct inductive bias that enables robust performance under resource-constrained conditions, including reduced feature dimensionality and limited training data. The proposed architecture not only outperforms established polynomial KAN baselines on standard benchmarks but also exhibits strong representational capacity for approximating complex multivariate functions with remarkably few parameters, making it a compelling alternative for efficient function approximation and classification in resource-constrained settings.


## 精读解读（中文）
### 一、研究动机
KAN将可学习单变量函数放在边上，比MLP参数高效且可解释；但多项式KAN虽缓解B-spline的计算开销，却存在无界实数输入与正交多项式有界或半无限支撑之间的域不匹配，常用tanh压缩在尾部饱和并导致梯度衰减。SW-KAN旨在利用定义在(0,∞)、带对数正态权的Stieltjes-Wigert q-正交多项式，配合稳定域映射解决该问题，并提升资源受限场景下的鲁棒性。

### 二、技术方案（Method）
对每条KAN边，输入x∈R先经φ(x)=e^{tanh(x)}双射到(e^{-1},e)⊂(0,∞)，从而匹配SW多项式支撑并保持有界良态梯度；边激活建模为Stieltjes-Wigert q-正交多项式基的线性组合，系数与q参数可学习，多项式阶数N控制容量。基函数由数值稳定的三项递推计算，每次O(N)、无需超几何特殊函数调用，随后按KAN结构求和与逐层传播，端到端反向传播训练，推理时同样用递推前向评估。

### 三、结果（Result）
在MNIST上SW-KAN取得98.24%测试准确率，在相近参数量下与Gottlieb-KAN、Vieta-Pell-KAN等多项式KAN基线相比具有竞争力；在Fashion-MNIST的降维特征和有限训练数据设定以及连续多元函数逼近任务中，SW-KAN表现出更优的精度-效率权衡和更强的小参数量逼近能力，验证了其优势跨任务泛化。

### 四、结论（Conclusion）
SW-KAN通过把Stieltjes-Wigert q-正交多项式引入KAN边激活，并用指数-of-tanh映射和稳定三项递推同时缓解域不匹配与B-spline网格开销，提供了一种高效、可解释且适合资源受限条件的函数逼近与分类架构。其对数正态权重结构与可学习q参数构成独特归纳偏置，使少参数、少数据场景下仍具竞争力。

### 五、方法论与关键技术细节
关键实现点包括：域映射φ(x)=e^{tanh(x)}将R映到(e^{-1},e)，避免tanh边界饱和但有效支撑仍限于该有限子区间；SW多项式相对对数正态权在(0,∞)正交，q可学习以调节集中度和振荡频率；三项递推实现O(N)基评估且不调用特殊函数库，规避B-spline的knot grid维护与网格扩展。实验覆盖MNIST、Fashion-MNIST和连续函数逼近，但主要验证仍属中小规模基准，理论逼近误差界、不同q初始化或阶数选择及更广泛大规模任务上的局限仍需进一步检验。
