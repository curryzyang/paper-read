# Dynamical principles of habituation across substrates and scales

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Matthew Smart, Stanislav Y. Shvartsman, Martin Mönnigmann
- 机构：Princeton University, Ruhr-Universität Bochum, Flatiron Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00249v1) · [PDF](https://arxiv.org/pdf/2608.00249v1)

## TLDR
TLDR: This review formalizes habituation's classical behavioral hallmarks as qualitative input–output constraints, shows that linear time-invariant systems cannot satisfy them, and identifies minimal nonlinear fading-memory motifs as the domain-general dynamical principles underlying habituation across biological and nonliving systems.

## Abstract
Habituation is a basic form of learning in which a system's response to repeated stimulation progressively diminishes but eventually recovers when the stimulus is withheld. Long studied in animals, it has increasingly been observed in unicellular organisms and non-living devices such as electronic circuits and neuromorphic materials, suggesting underlying dynamical principles that recur across domains. This review asks what those principles are: given qualitative constraints imposed by habituation on a system's response, what is the minimal dynamical structure that satisfies them? We formalize the classical hallmarks of habituation as behavioral constraints on input--output behavior, show that linear time-invariant systems are structurally incompatible with these constraints, and construct nonlinear motifs---linear fading-memory dynamics composed with static nonlinearities---that exhibit the hallmarks across diverse settings. We relate these motifs to models of specific biological systems and to physical and algorithmic realizations, from analog circuits to transient computation in machine learning.


## 精读解读（中文）
### 一、研究动机
习惯化是最基本的学习形式，表现为对重复刺激的响应逐渐减弱、停止刺激后恢复。该现象不仅见于动物，也在单细胞生物、电子电路和神经形态材料中出现，提示存在跨域复现的动力学原理。本文从系统与控制视角追问：在习惯化对输入-输出行为施加的定性约束下，满足这些约束的最小动力学结构是什么？

### 二、技术方案（Method）
将经典习惯化特征（H1-H10）形式化为对系统输入-输出算子的行为约束：以非负周期脉冲串（周期T、幅度A、占空比d）为输入，用每个周期内输出峰值y[k]刻画响应序列，从而把“递减、恢复、频率/强度依赖”转化为对峰值序列的不等式与序关系。假设系统为单输入单输出时不变状态空间模型x_dot=f(x,u), y=g(x,u)且具有唯一静息态；借Willems行为框架定义约束可行域。首先证明线性时不变（LTI）系统因叠加性与时间不变性无法满足单调衰减等习惯化约束，因而非线性是必要结构；随后构造最小motif——线性衰减记忆动力学与静态非线性（如阈值/饱和）复合，使其在参数和输入族变化下稳健满足H1、H2、H4、H5，并讨论H3、H6-H8的扩展；最后将motif与具体生物模型、模拟电路、神经形态材料和机器学习中的瞬态计算实现相关联。

### 三、结果（Result）
核心结果为结构性的：LTI系统无法实现习惯化，非线性并非建模选择而是必要前提；由线性衰减记忆加静态非线性构成的非线性motif可以同时满足习惯化的若干核心标志，并在多类系统中复现相同的衰减-恢复暂态行为。该结果将“衰减记忆”识别为习惯化的统一机制，为跨生物与非生物体系的对比提供了可复现的最小模型类。

### 四、结论（Conclusion）
习惯化的特征不是需拟合的数据，而是需要满足的行为规格；跨物种与非生命系统共现的现象背后存在与具体实现无关的动力学原理。最小结构可表述为线性衰减记忆动力学与静态非线性复合的非线性系统。这一视角为控制系统理论处理定性暂态约束提供了新问题，也为合成生物学、神经形态电路和机器学习中的瞬态计算设计给出了指导原则。

### 五、方法论与关键技术细节
关键细节包括：输入采用周期T、幅度A、占空比d的非负脉冲串，响应定义为每周期峰值y[k]；H0要求输出非负且有界，这是排除LTI的关键物理约束；只有H1（递减）和H2（自发恢复）是必要条件，其余标志刻画可选结构；研究重点为H1、H2、H4（频率敏感）和H5（强度敏感），H3、H6-H8可通过motif的微小修改实现，H9/H10未深入讨论；约束是跨输入族的定性关系而非单条轨迹拟合，与系统辨识、SINDy/符号回归的“逐点”拟合有本质区别；LTI不可能性依赖叠加性与时间平移不变性；衰减记忆与Volterra级数相关但Volterra构造仍属于逐点拟合；文中还讨论了与Willems行为框架、分岔理论中规范形的类比，并指出SISO、静息态假设、多稳态和奇异极限等局限。
