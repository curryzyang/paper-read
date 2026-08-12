# Complexity of Local Observation Consistency in Discrete-Event Systems

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Tomáš Masopust
- 机构：Palacký University Olomouc
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10111v1) · [PDF](https://arxiv.org/pdf/2608.10111v1)

## TLDR
LOC and LROC verification in discrete-event systems are PSpace-complete for nondeterministic plants but decidable in polynomial time for deterministic plants.

## Abstract
Hierarchical and multi-agent supervisory control under partial observation relies on local consistency conditions between a plant and its abstraction: local observation consistency (LOC) for the projection abstractions of hierarchical control, and local relabeling observation consistency (LROC) for the relabeling abstractions of multi-agent systems. Both are companions to a global condition and both have been used without their verification complexity being settled. We show that both are PSpace-complete for nondeterministic plants and decidable in polynomial time for deterministic plants.


## 精读解读（中文）
### 一、研究动机
在部分观测下的分层与多智能体监督控制依赖于plant与其抽象之间的局部一致性条件：分层控制投影抽象中的LOC，以及多智能体系统重标签抽象中的LROC。这些条件虽已被使用，但其验证复杂度始终未被确定，本文旨在彻底解决LOC与LROC验证问题的计算复杂度。

### 二、技术方案（Method）
输入为一个NFA或DFA plant G、事件字母表及相应抽象映射（投影Q或重标签R）与观测P。对LOC，定义Fill(X,e)为从状态集合X经不可观测填充串到达事件e的观测语言，并构造其正则NFA；再构造同步乘积自动机G⊗ΞG（Ξ取Σ_hi或Σ_o）以追踪在子字母表Ξ上投影一致的字符串对(X,Y)=(δ(I,s),δ(I,s'))。将LOC等价拆分为C1与C2两个条件，分别用Π_Σ_hi和Π_Σ_o中的可达对验证。验证算法在多项式空间内非确定性地猜测违反条件的e与可达对，并调用Fill集合对应NFA的交集空性判定；上界经Savitch定理得到PSpace。对确定性plant，则利用状态子集可确定性给出多项式时间算法。LROC类似地通过重标签同步与不可观测事件条件构造并判定。

### 三、结果（Result）
结果表明，对于非确定性plant，LOC验证与LROC验证均为PSpace-complete；对于确定性plant，两者均可判定且在多项式时间内可解。特别地，确定性plant的LOC验证可在多项式时间内完成，修正了文献中未证明的断言；LROC对非确定性plant的复杂度也被闭合为PSpace-complete。

### 四、结论（Conclusion）
本文完整确定了局部观察一致性LOC与局部重标签观察一致性LROC验证的复杂度，为非确定性系统下的层次化与多智能体监督控制提供了理论复杂度界限，同时表明确定性系统具有实际可计算的验证算法。该结果填补了这些条件长期未被解决的复杂度空白。

### 五、方法论与关键技术细节
关键细节包括：Fill集合作为正则语言可由规模为|Q_G|的NFA识别；乘积自动机顶点为状态子集对，路径长度计数器不超过2^{2|Q_G|}以保证线性空间上界；Fill交集空性判定可在非确定性对数空间内完成；PSpace上界通过Savitch定理由NPSpace转化。下界通过归约证明，且当Σ_c=Σ_o=Σ_hi时LOC仍为PSpace-hard。LROC的验证与可观测性变体类似，但非确定性plant情形需要专门的PSpace-hard归约。局限性在于非确定性plant的PSpace-completeness意味着在P≠PSpace假设下不存在多项式时间算法；确定性plant的多项式时间算法依赖于确定性结构，不适用于一般NFA。
