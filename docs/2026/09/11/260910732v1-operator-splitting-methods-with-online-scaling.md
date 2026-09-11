# Operator Splitting Methods with Online Scaling

- 区域：精读区
- 排名：3
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Wanyu Zhang, Wenzhi Gao, Madeleine Udell
- 机构：Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10732v1) · [PDF](https://arxiv.org/pdf/2609.10732v1)

## TLDR
This paper proposes a framework that uses online learning to adaptively tune preconditioners in operator splitting methods by interpreting them as preconditioned gradient descent on envelope functions, achieving asymptotically faster convergence and accelerating problems such as Lasso, \(\ell_1\)-regularized logistic regression, and quadratic programming.

## Abstract
This paper develops a principled framework for automatically tuning preconditioners in operator splitting methods, including forward-backward splitting, Douglas-Rachford splitting, and the alternating direction method of multipliers. We interpret these splitting methods as preconditioned gradient descent applied to their corresponding envelope functions and use online learning to adaptively learn the preconditioner during optimization. Our framework achieves asymptotically faster convergence rates and accelerates the solution of important optimization problems, including Lasso, $\ell_1$-regularized logistic regression, and quadratic programming. Extensive numerical experiments validate our theoretical results and demonstrate the practical effectiveness of the proposed approach.


## 精读解读（中文）
### 一、研究动机
算子分裂方法在求解优化问题时通常依赖预条件器，但预条件器的选择和调优往往需要人工经验，成为实际应用中的关键瓶颈。本文希望建立一个原则性框架，在优化过程中自动调优预条件器，从而提升收敛速度并减少调参负担。

### 二、技术方案（Method）
论文将前向-后向分裂、Douglas-Rachford 分裂和交替方向乘子法解释为作用于相应包络函数上的预条件梯度下降，并利用在线学习在优化过程中自适应学习预条件器。其核心方案包括把分裂迭代统一到包络函数与预条件梯度下降视角下，再通过在线学习模块动态更新预条件器，以覆盖 Lasso、l1 正则化逻辑回归和二次规划等优化问题。

### 三、结果（Result）
该框架被证明可获得渐近更快的收敛率，并在 Lasso、l1 正则化逻辑回归和二次规划等重要优化问题上加速求解。大量数值实验验证了理论结果，并展示了所提方法在实际中的有效性。

### 四、结论（Conclusion）
论文提出了一个自动调优算子分裂方法预条件器的原则性框架，将前向-后向分裂、Douglas-Rachford 分裂和 ADMM 统一到包络函数上的预条件梯度下降与在线学习视角中。理论和实验结果表明，该框架能够加快收敛并提升多类优化问题的求解效率。

### 五、方法论与关键技术细节
关键方法论细节包括：以包络函数刻画分裂方法，将分裂迭代视为预条件梯度下降，并用在线学习自适应调整预条件器；覆盖前向-后向分裂、Douglas-Rachford 分裂和 ADMM；在 Lasso、l1 正则化逻辑回归和二次规划上进行数值验证。摘要未提供具体数据集、先验、损失函数、超参数、复杂度界和局限性等实现细节，因此这些方面不能从给定材料中进一步确定。
