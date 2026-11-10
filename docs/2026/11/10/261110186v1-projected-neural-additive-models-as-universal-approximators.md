# Projected Neural Additive Models as Universal Approximators

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Nhon N. Phan, Qiang Du, John D. Clayton, WaiChing Sun
- 机构：DEVCOM Army Research Laboratory, Columbia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10186v1) · [PDF](https://arxiv.org/pdf/2611.10186v1)

## TLDR
Projected neural additive models (PNAMs), which add a learnable linear projection to neural additive models to capture cross-variable interactions, are proven to be universal approximators with an optimal ridge-function approximation rate while retaining interpretability through structured sparsity and symbolic regression.

## Abstract
Neural additive models (NAMs) offer interpretability but lack expressivity due to their rigid additive structure, whereas multi-layer perceptrons (MLPs) achieve universal approximation at the cost of transparency. We establish the first theoretical foundation for projected neural additive models (PNAMs), which augment NAMs with a learnable linear transformation $\boldsymbol{T}$ to capture cross-variable interactions. While standard NAMs cannot approximate even the simplest interaction term $χ_1 χ_2$ because their cross-derivatives are identically zero, we prove that PNAMs are universal approximators and characterize the minimum number of projections required for exact polynomial representation. Furthermore, we derive an approximation rate of $\mathcal{O}(M^{-s / (N - 1)})$ for $\mathcal{C}^s$ functions (i.e., functions with $s$ continuous derivatives), where $M$ denotes the number of projections and $N$ the input dimension; this rate is known to be optimal for ridge function approximation. To recover interpretability from the projected inputs, we introduce structured sparsity regularizers and post-hoc symbolic regression techniques that enable global input ranking, parameter pruning, and the conversion of learned bases into compact analytical expressions. Experiments on knot theory invariants, MNIST, and phase field fracture mechanics demonstrate that PNAMs match or surpass similar architectures in accuracy while discovering salient features and yielding symbolic models with orders of magnitude fewer parameters.


## 精读解读（中文）
### 一、研究动机
神经加性模型（NAM）以单变量形状函数提供可解释性，但其刚性加性结构导致交叉导数恒为零，甚至无法表示最简单的交互项χ1χ2；多层感知机虽具有通用逼近能力却缺乏透明性。本文旨在为带可学习线性投影的PNAM建立首个理论基础，并在保持表达力的同时恢复可解释性。

### 二、技术方案（Method）
给定监督数据{(χ,y)}，PNAM将输入经可学习矩阵T投影为z=Tχ，再以加权和Σζ_i f_i(z_i)输出，其中f_i由独立一维MLP或多项式基参数化，并可选用固定高斯傅里叶特征增强高频表达能力；训练时联合优化T、权重ζ和MLP参数，并引入结构化稀疏正则以进行全局输入排序、交互筛选和剪枝。理论部分先用Stone–Weierstrass定理将连续函数逼近转化为多项式表示，再证明PNAM可通过岭函数叠加精确复现多变量多项式，从而得到通用逼近性，并借助Jackson定理推导逼近率；推理阶段还可对学习到的一维基做事后符号回归，将基函数转化为紧凑解析表达式。

### 三、结果（Result）
论文证明标准NAM因交叉导数为零而不能逼近χ1χ2，而PNAM是通用逼近器，并给出精确表示任意N变量P次多项式所需最小投影数的构造性上界与参数计数下界。对C^s函数，PNAM达到O(M^{-s/(N−1)})的逼近率，其中M为投影数、N为输入维数，该速率是岭函数逼近的已知最优速率。在纽结理论不变量、MNIST和相场断裂力学实验中，PNAM在精度上匹配或超过同类架构，同时识别显著特征，并得到参数量少数量级的符号模型。

### 四、结论（Conclusion）
PNAM通过单个可学习线性投影加一维非线性基，弥补了NAM缺乏交互表达能力的理论缺陷，并在通用逼近性与最优岭函数逼近率之间建立了联系。结构化稀疏与事后符号回归使其能够进行全局输入排序、参数剪枝和紧凑表达式提取，因此适合交互阶数较高、沿少数方向稠密或先验未知的问题。其加性基结构仍不适合紧凑表示除法等操作，精确物理定律恢复应留给专门的符号回归方法。

### 五、方法论与关键技术细节
关键理论点包括NAM的交叉导数恒为零、PNAM用投影方向捕获跨变量耦合、以及多项式精确表示所需最小M的上界与下界；逼近率中的常数依赖紧域、光滑阶s、维数N和函数范数界B。实现上，每个投影对应一个一维MLP基，可选傅里叶特征由固定高斯分布N(0,σ²)采样且初始化后不训练，T和ζ可优化以产生更稀疏解，结构化稀疏正则用于全局排序和剪枝。复杂度与约束在于M通常远小于成对交互数N(N−1)/2，但复杂交互可能需要很大M；局限性是加性结构难以紧凑逼近除法等非加性操作，符号回归主要用于剪枝而非保证恢复精确物理定律。
