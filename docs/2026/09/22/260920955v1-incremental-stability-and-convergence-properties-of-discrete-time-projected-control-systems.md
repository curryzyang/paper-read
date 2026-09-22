# Incremental Stability and Convergence Properties of Discrete-Time Projected Control Systems

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Riccardo Bertollo, S. J. A. M. van den Eijnden, W. P. M. H., Heemels
- 机构：Eindhoven University of Technology, Université catholique de Louvain
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20955v1) · [PDF](https://arxiv.org/pdf/2609.20955v1)

## TLDR
This paper develops discrete-time incremental stability and convergence analysis for projection-based control systems, showing that suitably designed projections preserve quadratic incremental stability and deriving small-gain and Lyapunov-based conditions for incremental input-to-state stability in closed-loop nonlinear systems.

## Abstract
Projection-based controllers can overcome fundamental limitations of classical linear time-invariant control by modifying the controller's input-output behavior via projection. A key example is given by the hybrid integrator-gain system, a projected integrator, which has recently found successful application in several industrial systems. While prior work on analysis and design of projection-based control systems has primarily focused on the continuous-time setting and non-incremental analysis, a more refined incremental analysis in discrete-time is needed to better reflect actual digital implementation and obtain more accurate (robust) performance assessment. To address this need, this paper considers incremental stability and convergence analysis of discrete-time projection-based control systems. Our first methodology is based on showing that such controllers preserve the quadratic incremental stability of their nominal (unprojected) dynamics, if the projection metric is well-designed. Building on this, we derive a small-gain condition guaranteeing incremental input-to-state stability for interconnections of projected controllers with general nonlinear plants. A second approach is grounded in a direct Lyapunov-based method for verifying incremental stability in input-affine piecewise-smooth systems, which can be seen as an extension of the classical discrete-time Demidovic conditions. We illustrate our results through several examples, and demonstrate performance quantification via nonlinear Bode plots, with a special focus on first-order projection elements.


## 精读解读（中文）
### 一、研究动机
投影型控制器（如HIGS）能突破LTI控制性能限制，但已有分析多在连续时间且偏非增量ISS/L2增益，难以准确反映数字实现并偏保守。为获得更精细的鲁棒性与性能评估，需要在离散时间框架下研究投影控制系统的增量稳定性和收敛性。

### 二、技术方案（Method）
论文以离散时间投影控制器与非线性被控对象互联为对象，输入包括投影控制器模型、名义未投影动力学、投影度量以及对象模型。第一条路线是先证明若投影度量设计合适，投影控制器可保持名义动力学的二次增量稳定QIS，再据此推导增量小增益条件，保证投影控制器与一般非线性对象互联的δISS。第二条路线把闭环显式表示为输入仿射分段光滑连续切换系统，构造二次增量Lyapunov函数验证δISS，并将其视为离散时间Demidovič条件的扩展；对线性对象，该条件可转化为LMI数值求解。两条路线均证明δISS可推出收敛，并用非线性/线性算例及非线性Bode图量化性能，重点讨论一阶投影元素FOPE与HIGS。

### 三、结果（Result）
核心发现是：在投影度量适当设计时，离散时间投影控制器能够继承名义未投影动力学的QIS性质；由此得到的增量小增益条件可保证投影控制器与一般非线性对象互联的δISS。对于输入仿射分段光滑闭环，二次增量Lyapunov方法和相应LMI可验证δISS；δISS进一步蕴含收敛，因此周期输入会产生同基频周期的稳态输出。算例展示了两种方法的适用性，并通过非线性Bode图给出性能量化，特别适用于一阶投影元素。

### 四、结论（Conclusion）
论文为离散时间投影控制系统提供了两套可验证的增量稳定与收敛分析工具，弥补了连续时间与非增量分析在数字实现和鲁棒性能评估上的不足。结果将HIGS等投影控制器与增量小增益、Lyapunov方法和LMI联系起来，为投影度量设计与闭环δISS证书提供理论依据。

### 五、方法论与关键技术细节
关键细节包括：采用δUGAS、δISS及增量ISS Lyapunov函数的KL/K类函数定义；QIS保持依赖投影度量设计，常涉及加权范数、扇区/锥约束和条件数；小增益条件要求互联环路增益满足收缩/稳定性要求；第二方法假设输入仿射、分段光滑且投影算子连续，从而可构造二次增量Lyapunov函数并扩展Demidovič条件，线性情形化为LMI。局限在于结论依赖度量与连续性/光滑性假设，LMI维数和保守性可能限制高维应用，且重点示例为一阶投影元素，整体仍以离散时间连续动力学模型为主。
