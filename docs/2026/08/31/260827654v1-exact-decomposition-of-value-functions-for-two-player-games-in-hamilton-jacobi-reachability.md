# Exact Decomposition of Value Functions for Two-Player Games in Hamilton-Jacobi Reachability

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Dylan Hirsch, William Sharpless, Sylvia Herbert
- 机构：University of California, San Diego
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27654v1) · [PDF](https://arxiv.org/pdf/2608.27654v1)

## TLDR
This paper extends the algebraic decomposition of composite reachability value functions to the two-player (adversarial) setting in continuous-time, finite-horizon Hamilton-Jacobi reachability, proving that a key decomposition result holds under a critical monotonicity assumption, demonstrating failure without it via a counterexample, and recovering analyses for a variety of tasks.

## Abstract
Hamilton-Jacobi reachability (HJR) is an important framework in safe control theory. HJR provides theoretical tools and numerical methods to obtain value-functions for tasks involving target-reaching and obstacle-avoidance. A recent work proposed an algebraic framework to scale to complex, composite tasks via decomposing the value functions of the composite tasks into value functions for the fundamental tasks traditionally studied in HJR, all in the one-player setting. Many of these decomposition results, however, do not directly translate to the two-player setting. In this technical note, we nevertheless show that one of the previous work's key results for analyzing various tasks involving reaching multiple targets while obeying constraints still holds in the two-player setting, so long as a critical monotonicity assumption is satisfied. In particular, we detail the analogous result and its proof (which structurally differs from the one-player case), we show via a counter-example what can go wrong if this monotonicity assumption is not satisfied, and we show how the analysis of a variety of tasks can be performed using this result. We note that, whereas the prior work considered discrete-time, infinite-horizon tasks, which are more standard in reinforcement learning, we here consider continuous-time, finite-horizon tasks, which are more standard in HJR.


## 精读解读（中文）
### 一、研究动机
汉密尔顿-雅可比可达性（HJR）是安全控制中计算目标到达与障碍规避值函数的重要框架。近期工作曾在单玩家（无对抗扰动）离散时间/无穷时域下提出复合任务值函数的代数分解框架，但这些结果大多不能直接推广到含对抗扰动的两玩家设定。本文希望证明其中关键分解公式在两玩家、连续时间、有限时域设定下仍然成立，从而支持在对抗环境下分析多目标到达且满足约束的复合任务。

### 二、技术方案（Method）
本文在连续时间有限时域HJR中建立两玩家微分博弈：系统由控制u和扰动d驱动，扰动采用非预期（non-anticipative）策略，值函数定义为扰动策略取inf、控制信号取sup的性能泛函。对由上游约束与下游任务组成的复合任务，将下游任务用其值函数V0表示，并用该值函数构造新的时变目标函数；然后计算以该时变目标为目标、以上游约束为约束的reach-avoid值函数。文中证明，在关键单调性假设下，该三步分解给出的值函数与原复合任务值函数精确相等；证明结构上与单玩家情形不同。

### 三、结果（Result）
论文给出了两玩家设定下该分解定理的精确形式与证明，并通过反例说明若下游任务的单调性假设不成立，分解会失效。该结果可用于恢复并扩展两玩家的reach-always-avoid、reach-reach以及sequential reach-avoid等任务的值函数分解结论，且所有结论均针对连续时间、有限时域设定。

### 四、结论（Conclusion）
在满足关键单调性假设时，两玩家HJR中的复合任务值函数可被精确分解为下游任务值函数与带时变目标的reach-avoid值函数；若不满足该假设则不能直接分解。因此，该工作将单玩家代数分解框架推广到了含对抗扰动的两玩家场景，为复杂安全任务分析提供了理论保障。

### 五、方法论与关键技术细节
值函数定义采用inf_{扰动策略} sup_{控制信号}，且扰动策略限为非预期的；假设控制/扰动集合紧致且动力学满足线性增长和Lipschitz连续以保证轨迹存在唯一。性能泛函（reach、avoid、reach-avoid）连续且past-independent，因此对应值函数连续；值函数符号用于判定任务可满足性。关键限制是下游任务必须满足单调性条件，否则需先验证或重新建模；方法适用范围为有限时域连续时间系统，计算上仍需求解reach-avoid类HJI方程。
