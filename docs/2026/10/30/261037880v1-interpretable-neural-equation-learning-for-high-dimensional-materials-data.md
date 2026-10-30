# Interpretable neural equation learning for high-dimensional materials data

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Philip Jacobson, Prasad Iyer, Remi Dingreville, Saaketh Desai
- 机构：Sandia National Laboratories
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37880v1) · [PDF](https://arxiv.org/pdf/2610.37880v1)

## TLDR
TLDR: nn-EQL is an interpretable equation-learning framework that generates and ranks compact candidate equations from sparse, high-dimensional materials data by iteratively training, pruning, and retraining a neural network with customizable neuron-level activations, then diagnosing term contributions, sensitivities, and uncertainties to support scientific interpretation.

## Abstract
Equation learning seeks to discover compact, interpretable equations from data using various machine-learning techniques. However, few workflows discover and interpret learned equations in sparse, high-dimensional materials datasets. We present nn-EQL, an equation-learning framework that generates candidate equations through iterative training, pruning, and retraining of a neural network with customizable, user-specified neuron-level activation functions. Candidate equations are ranked using a minimum description length (MDL)-inspired score, balancing error and sparsity, and diagnosed to assess term-wise contributions, input-scaled sensitivities, and uncertainties. We demonstrate nn-EQL on standard AI-Feynman benchmarks as well as multiscale high-dimensional materials datasets such as finite-element simulations of heterogeneous materials, and high-throughput experimental thin-film deposition data. nn-EQL integrates with tabular data and high-dimensional data via standard encoder models, learning equations and providing insight into learned terms. Looking forward, integrating physically interpretable representations, multimodal and multi-fidelity data, and adaptive data acquisition could enable equation learning to formulate and test mechanistic hypotheses.


## 精读解读（中文）
### 一、研究动机
传统深度学习虽能从材料数据中获得强预测能力，但缺乏可解释性；符号回归虽能学习紧凑方程，却较少能在稀疏、高维材料数据中完成候选方程生成、选择、诊断与解释。本文旨在构建一个面向高维材料数据的可解释方程学习流程，使学习到的方程可作为可检验的机制假设。

### 二、技术方案（Method）
nn-EQL 使用每神经元激活函数可定制的神经网络表示方程：先训练过参数化稠密网络，再依据连接贡献分数进行迭代剪枝并对保留连接重训练，逐步生成稀疏候选方程，并经 Sympy 组合为显式符号表达式。候选方程用受最小描述长度启发的评分排序，同时提供逐项贡献、输入尺度敏感性和不确定性诊断；高维数据可通过标准编码器接入。

### 三、结果（Result）
作者在 AI-Feynman 基准以及异质材料有限元模拟、高通量薄膜沉积实验等高维材料数据上演示了 nn-EQL，表明其能够生成和选择紧凑方程，并对学习到的项给出诊断与解释。结果支持该框架同时适用于表格数据和高维数据，并可用于比较竞争性方程所代表的不同机制假设。

### 四、结论（Conclusion）
nn-EQL 提供了覆盖方程生成、选择、诊断、解释和后续精炼的可解释方程学习工作流，将数据驱动拟合与传统方程表达结合，使学习方程可作为材料机制假设进行检验。未来结合物理可解释表示、多模态与多保真数据以及自适应数据采集，有望进一步支持机制假设的提出与验证。

### 五、方法论与关键技术细节
关键实现包括用户自定义算子库（如 x、幂、sqrt、sin、cos、exp、log 及二元乘法）、两层算子层加线性输出层、MSE 与 Adam 训练、基于权重与数据集平均激活乘积绝对值的贡献剪枝、剪枝连接置零后的重训练，以及 S=N/2 log(MSE)+λN_W 的 MDL 启发评分（λ 常取 0.25–1.0）。复杂度项依赖表示且仅作启发式代理，因此方法保留全部候选方程而不强制给出唯一最优方程；诊断涵盖逐项贡献、输入缩放敏感性和不确定性，局限包括稀疏噪声数据下的候选歧义与解释稳健性仍需结合领域知识判断。
