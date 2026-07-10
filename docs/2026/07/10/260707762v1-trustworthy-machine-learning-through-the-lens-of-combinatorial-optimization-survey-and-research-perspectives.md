# Trustworthy Machine Learning through the Lens of Combinatorial Optimization: Survey and Research Perspectives

- 区域：精读区
- 排名：8
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Thibaut Vidal, Julien Ferry
- 机构：Polytechnique Montreal
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07762v1) · [PDF](https://arxiv.org/pdf/2607.07762v1)

## TLDR
This survey explores how combinatorial optimization provides a framework for trustworthy machine learning, offering global guarantees and formal certificates for tasks like interpretable learning, explanation, robustness, fairness, and privacy, while discussing scalability challenges and research perspectives.

## Abstract
Modern machine learning (ML) increasingly relies on complex models whose behavior is difficult to characterize beyond empirical performance metrics. Across a wide range of tasks, including prediction, generation, and decision-making, models with similar empirical performance can exhibit markedly different properties in terms of their transparency, interpretability, robustness, fairness, privacy, and certifiability. This survey highlights how optimization- and certification-oriented reasoning can provide a useful framework for reasoning about such differences, supporting tasks ranging from model training and selection to auditing and certification. We review and synthesize recent advances at the intersection of combinatorial optimization (CO) and trustworthy ML, covering both training and post-training tasks, including interpretable model learning, explanation generation, robustness analysis, fairness auditing, model compression, and privacy attacks and protections. Across these domains, CO formulations offer additional capabilities over purely heuristic approaches, e.g., gradient-based ones, notably global guarantees, formal certificates, and explicit treatment of trade-offs. While scalability remains an important challenge, continued progress in solvers and hybrid algorithms suggests a growing role for CO in the design and deployment of trustworthy ML systems.


## 精读解读（中文）
### 一、研究动机
现代机器学习模型日益复杂，仅凭经验性能指标难以全面刻画其行为，模型在透明度、可解释性、鲁棒性、公平性、隐私和可认证性等可信赖属性上可能存在显著差异。组合优化能够提供全局保证、形式化证书和显式权衡处理，弥补纯启发式方法的不足，因此有必要系统梳理CO在可信ML中的应用。

### 二、技术方案（Method）
本文采用结构化、子领域驱动的方法，通过组合机器学习与整数规划/组合优化的关键词搜索，结合各可信赖维度（透明性、可解释性、公平性、鲁棒性、隐私）的特定术语进行文献筛选，并以高被引工作和综述为锚点进行前后向引用拓展。最终覆盖了可解释模型学习、解释生成、鲁棒性分析、公平审计、模型压缩、隐私攻击与保护等训练和训练后任务，并提炼了MILP、SAT、SMT、CP、MaxSAT等多种CO范式的代表性模型和算法策略。

### 三、结果（Result）
组合优化方法在多个可信ML任务中展现出优于纯启发式（如梯度方法）的能力：提供全局最优性保障、形式化证书以及显式的权衡分析；例如在稀疏回归和稀疏SVM中，CO公式能精确控制特征数量并达到更优的泛化性能；在鲁棒性验证和公平审计中可输出可认证的边界。尽管可扩展性仍是主要挑战，但现代求解器（MILP等）的加速（三至六个数量级）和混合算法的发展使得CO在可信ML中的实际应用前景广阔。

### 四、结论（Conclusion）
组合优化为可信机器学习提供了一个强力的方法论框架，能够系统处理透明度、可解释性、公平性、鲁棒性和隐私等关键维度，在模型训练、选择、审计和认证中实现全局最优性和形式化保证。未来需进一步解决可扩展性瓶颈，并推动CO与深度学习、大模型的深度融合。

### 五、方法论与关键技术细节
方法论上，CO建模依赖于精确的数学公式（如决策变量、目标函数和约束），并利用分支定界、切平面、预求解、分解等技术求解。关键细节包括：对于稀疏回归，采用big-M或视角重构的MISOCP松弛以获得紧界；对于决策树学习，利用动态规划或MIP精确全局优化；鲁棒性验证通过MIP或SMT编码对抗扰动约束；公平审计通过约束违反的优化检测差异。局限性方面，CO方法在处理超高维数据（p>10^5）或大规模神经网络时仍面临扩展性挑战，且依赖问题结构的凸性/线性特征。
