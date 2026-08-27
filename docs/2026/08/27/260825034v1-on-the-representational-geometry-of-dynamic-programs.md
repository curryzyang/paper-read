# On the Representational Geometry of Dynamic Programs

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Richard F. M. Lim, Ruriko Yoshida
- 机构：Bowdoin College, Naval Postgraduate School, Aalborg University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.25034v1) · [PDF](https://arxiv.org/pdf/2608.25034v1)

## TLDR
Standard neural architectures fail to length-generalize on dynamic programs because, although DAGs, tropical polynomials, and Newton polyhedra form isomorphic semiring descriptions of DP, the native operations of substitution and composition are structurally insufficient to determine larger instances from smaller ones.

## Abstract
Standard neural architectures often fail to generalize to longer inputs for dynamic programming (DP) targets. We investigate what makes this hard geometrically. Every finite min-plus DP is a shortest path on a DAG, which is equivalently a tropical polynomial whose extended Newton polyhedron encodes the decision boundary of which path wins. We prove these three descriptions (graph, polynomial, polyhedron) form isomorphic semirings at two levels --- formal polynomials and their computed functions --- connected by operations that characterize all structural redundancies. We then address the length-generalization question geometrically: does the decision boundary at length $T$ decide the boundary at $T+1$? We present two structural negatives. The semiring's two native ways to reduce dimension (setting a variable to each identity) are neither injective nor always closed within the DP. Series and parallel composition fail to construct all DAG topologies from smaller sub-DAGs, and even all terminal-only operations do not capture all DP compositions.


## 精读解读（中文）
### 一、研究动机
标准神经架构在处理动态规划（DP）目标时往往无法泛化到更长输入。论文从几何角度探究这一困难的根源：每个有限min-plus DP可视为DAG上的最短路径，等价于热带多项式，其扩展牛顿多面体编码了路径获胜的决策边界。作者旨在回答：长度T的决策边界是否能决定长度T+1的边界？

### 二、技术方案（Method）
论文建立图、热带多项式、扩展牛顿多面体三种描述之间的半环同构定理，在形式多项式和计算函数两个层面上统一为同一代数结构。基于该框架，定义两种恒等替换（变量设为+∞的P_i和设为0的Q_i），分析它们在代数、多面体、超曲面和图上的变换规则，并研究这些替换的封闭性与单射性。进一步考察级联（串行）和并联（取最小）两种基本组合操作能否由小子图生成所有DAG拓扑，以及仅终端操作能否捕获所有DP组合。通过构造反例和正规形式（deshared正规形式和函数正规形式）完成证明。

### 三、结果（Result）
证明了三重半环同构定理：图/多项式/多面体在形式层和函数层各自构成同构半环，且两个层面间有满射同态。得到两个结构性否定：其一，两种恒等替换既非单射也并非总在DP内封闭；其二，级联和并联组合不能从更小子DAG构造所有DAG拓扑，仅终端操作也无法捕获所有DP组合。此外，deshared正规形式和函数正规形式的存在使得两种图等价关系可判定。

### 四、结论（Conclusion）
长度泛化在几何上存在根本性障碍：T时刻的决策边界不能决定T+1时刻的边界，且DP的组合结构不足以由小规模实例重构所有大规模实例。这解释了标准神经架构在DP长度外推上的系统性失败，表明需要额外的归纳偏置或不同表示。

### 五、方法论与关键技术细节
关键细节包括：使用min-plus（热带）半环，其恒等元为+∞（min）和0（+）；扩展牛顿多面体由凸包加向上锥构成；两种替换操作分别对应坐标面和坐标投影；定义四个局部操作实现图到正规形式的归约；证明依赖理论反例而非实验，未提供数值指标；局限性在于结果是否定性的，没有提出新架构，但为设计长度外推模型提供了几何约束。
