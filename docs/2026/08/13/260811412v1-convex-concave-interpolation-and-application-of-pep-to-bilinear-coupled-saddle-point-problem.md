# Convex-Concave Interpolation and Application of PEP to Bilinear-Coupled Saddle-Point Problem

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Valery Krivchenko, Alexander Gasnikov, Dmitry Kovalev
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.11412v1) · [PDF](https://arxiv.org/pdf/2608.11412v1)

## TLDR
This paper derives interpolation conditions for convex-concave, bilinear, and composite bilinear-coupled functions and uses them to construct performance estimation problems (PEP) for analyzing first-order methods on composite saddle-point problems.

## Abstract
The Performance estimation problem (PEP) approach reformulates finding the exact worst-case performance of an algorithm as the solution to an optimization problem. Tractable formulation of the problem requires necessary and sufficient interpolation conditions. We present the interpolation conditions for convex--concave functions, bilinear functions, and composite functions with bilinear coupling. We also construct PEP for first-order methods for composite saddle-point problem.


## 精读解读（中文）
### 一、研究动机
性能估计问题(PEP)通过求解优化问题来得到算法的最坏情况性能，但将其应用于鞍点/极小极大问题需要凸-凹函数、双线性函数以及带双线性耦合复合函数的插值条件，而这些条件此前缺乏。本文旨在填补这一空白，建立可处理的PEP公式，用于分析一阶方法在复合鞍点问题上的最坏情况性能。

### 二、技术方案（Method）
本文从插值性定义出发：给定一组迭代点对(x_i,y_i)、分块次梯度(g_i^x,g_i^y)和函数值f_i，判断是否存在目标函数类中的函数复现这些数据。针对非光滑凸-凹函数、双线性函数以及p(x)+y^T A x-q(y)形式的复合函数，推导必要且充分的插值条件。随后将这些条件作为约束，把算法的最坏情况性能（如对偶间隙或迭代点误差）构造成一个有限维优化问题，即标准PEP；并进一步构造Lyapunov形式的PEP，通过自动生成Lyapunov函数来验证和估计一阶方法在复合鞍点问题上的收敛性。求解该有限维优化问题（通常为半定规划）即可得到精确的最坏情况性能界。

### 三、结果（Result）
本文给出了非光滑凸-凹函数、双线性函数和带双线性耦合复合函数的必要且充分插值条件，将PEP从凸极小化推广到鞍点/极小极大设置；同时构造了复合鞍点问题上一阶方法的标准PEP与Lyapunov-PEP，可以用数值优化自动获得精确最坏情况性能并生成Lyapunov函数。论文还包含初步数值实验，验证了所提PEP构造的有效性。

### 四、结论（Conclusion）
本文为PEP应用于凸-凹及双线性耦合鞍点问题奠定了理论基础，提供了可计算的插值条件与PEP构造。研究者可据此对一阶方法进行精确最坏情况分析、对比算法并自动发现Lyapunov函数，进而设计更优的鞍点优化算法。

### 五、方法论与关键技术细节
关键细节包括：插值条件必须同时满足必要性和充分性，以保证PEP与原无限维问题同解；非光滑情形允许次梯度，并用有界次梯度或Lipschitz常数M刻画，M=+∞时表示无额外Lipschitz假设；双线性耦合项y^T A x需在凸-凹复合结构内单独处理；光滑情形可引入L_x、L_y、L_xy以及强凸/强凹参数μ_x、μ_y来刻画更紧的函数类；PEP的决策变量为迭代点、分块梯度和函数值，目标函数根据具体性能指标选择；标准PEP与Lyapunov PEP在构造和用途上有区别，后者能额外输出Lyapunov函数；局限性包括：目前主要针对确定性一阶方法，扩展到随机或高阶方法、以及大规模问题时的半定规划求解复杂度仍需进一步研究。
