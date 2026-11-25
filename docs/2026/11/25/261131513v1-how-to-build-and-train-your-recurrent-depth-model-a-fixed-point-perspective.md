# How to build and train your recurrent-depth model: A fixed-point perspective

- 区域：精读区
- 排名：3
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Thomas Pethick
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31513v1) · [PDF](https://arxiv.org/pdf/2611.31513v1)

## TLDR
TLDR: The paper shows that input injection in recurrent-depth models is exactly Halpern iteration, enabling provable convergence with polylogarithmic truncated backpropagation under Lipschitz constraints, and uses these constraints to design Sparrow, a drop-in Muon/MuonH optimizer that speeds up training.

## Abstract
Recurrent-depth models are trained with truncated backpropagation, yet it remains unclear why this works. We show that input injection, commonly used in recurrent-depth models, is exactly Halpern iteration, and that a slowly vanishing stepsize provably converges with a backpropagation window polylogarithmic in the depth. The guarantees require a Lipschitz operator, which for SwiGLU leads to a weight constraint in both row and spectral norm, while only a row norm constraint for gates. Based on these constraints, we develop an optimizer tailored to each parameter group, Sparrow, which provides a drop-in replacement of Muon/MuonH with no overhead, that speeds up training even beyond recurrent models.


## 精读解读（中文）
### 一、研究动机
循环深度模型通常用截断反传来训练，但这种做法为何有效仍不清楚；作者希望从不动点视角解释并给出可操作的构建与训练原则。

### 二、技术方案（Method）
将循环深度模型的前向迭代建模为不动点迭代，并指出常用的输入注入 exactly 是 Halpern 迭代；采用缓慢消失的步长，使收敛可在深度多对数级的反传窗口下得到保证。为保证算子 Lipschitz，对 SwiGLU 权重同时施加行范数与谱范数约束，对门控仅施加行范数约束；据此按参数组设计 Sparrow 优化器，以截断反传训练，作为 Muon/MuonH 的直接替代。

### 三、结果（Result）
核心发现是输入注入等价于 Halpern 迭代，且在缓慢消失步长与 Lipschitz 算子条件下可证明以深度多对数级反传窗口收敛；SwiGLU 需要行范数和谱范数约束，而门控只需行范数约束；Sparrow 无需额外开销即可加速训练，并可推广到非循环模型。

### 四、结论（Conclusion）
论文给出了从不动点迭代、Lipschitz 参数化到分组优化器的系统方案，解释了截断反传在循环深度模型中可行的理论原因，并提供可直接替换 Muon/MuonH 的训练优化器。

### 五、方法论与关键技术细节
理论保证依赖 Lipschitz 算子假设，反传窗口为深度的多对数级；参数约束按 SwiGLU 与门控区别处理；Sparrow 按参数组定制且无额外开销；摘要未给出具体数值指标，实验细节和超参需参考正文与附录；局限性在于保证依赖步长消失与约束满足。
