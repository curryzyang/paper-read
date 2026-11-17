# Algebraic Interaction: A Recipe for Neural Architecture Generation

- 区域：精读区
- 排名：2
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Haonan Dong, Angelica I Aviles-Rivero
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18649v1) · [PDF](https://arxiv.org/pdf/2611.18649v1)

## TLDR
The paper proposes an algebraic framework that separates positional routing from feature algebra and shows that replacing only the feature algebra in existing architectures can improve accuracy, efficiency, and symmetry without redesigning information flow.

## Abstract
We introduce an algebraic foundation for neural architecture design in which convolution, attention, state-space models, and equivariant layers are expressed through compositions of bilinear product operators over two structures: a position algebra governing positional routing and a feature algebra governing feature interactions. This decomposition makes routing, feature algebra, and operator composition explicit design variables.We focus on the feature-algebra axis through an Algebraic Recipe: fix the routing and operator composition of an existing architecture while replacing its feature algebra. This preserves the information-flow structure while allowing computational and symmetry properties to be modified through algebraic specification.We instantiate the recipe in linear attention, Mamba, and equivariant networks. Structure-constant and Clifford algebras improve accuracy at comparable parameter count in linear attention; structure-constant algebras yield up to $3\times$ faster training and inference in Vision Mamba at competitive accuracy; and an $\mathrm{SO}(3)$-representation algebra provides rotational equivariance by construction. These results demonstrate that feature algebra alone can control accuracy, efficiency, and symmetry without redesigning positional routing.This turns algebraic structure into an explicit design variable and reduces architecture design, within our framework, to algebraic specification.


## 精读解读（中文）
### 一、研究动机
现有卷积、注意力、状态空间模型与等变网络通常作为彼此独立的架构族来设计，缺乏统一代数视角，导致位置路由、特征交互与算子组合混在一起，难以把代数结构作为显式设计变量来控制精度、效率与对称性。

### 二、技术方案（Method）
论文将上述算子统一表示为双线性乘积算子在两个结构上的复合：位置代数负责位置路由，特征代数负责特征交互。提出的Algebraic Recipe在固定已有架构的位置路由与算子组合、保持信息流结构不变的前提下，仅替换其特征代数，从而通过代数规格修改计算与对称性质；作者在线性注意力、Mamba和等变网络中实例化该配方。

### 三、结果（Result）
在参数量相当的条件下，结构常代数与Clifford代数可提升线性注意力的精度；结构常代数使Vision Mamba在保持有竞争力精度的同时实现最高约3倍的训练与推理加速；SO(3)表示代数则按构造提供旋转等变性。

### 四、结论（Conclusion）
结果表明仅改变特征代数即可在不重新设计位置路由的情况下控制精度、效率与对称性，因而代数结构可成为显式架构设计变量，并在该框架内把架构设计约化为代数规格选择。

### 五、方法论与关键技术细节
关键点是把架构分解为位置代数、特征代数与算子组合三个显式变量，并通过保持路由和组合不变来隔离特征代数的作用；等变性由SO(3)表示代数按构造保证，效率收益来自特征代数带来的计算性质变化。摘要未给出具体数据集、损失函数与超参数，且实验覆盖线性注意力、Vision Mamba和等变网络三类实例，尚未说明大规模架构搜索或更广泛任务的适用边界。
