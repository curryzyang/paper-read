# Efficient Learning of Differentiable MPC Policies on the GPU via Smoothed ADMM and First-Order Reinforcement Learning

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Jianghan Zhang, Roland Schwan, Gabriel Bravo-Palacios, John Zhang, Thomas Lew, Brian Plancher
- 机构：Massachusetts Institute of Technology, Toyota Research Institute, Dartmouth College
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.09937v1) · [PDF](https://arxiv.org/pdf/2611.09937v1)

## TLDR
The paper introduces **SmoothedTurboMPC**, a GPU-parallel differentiable MPC solver using log-barrier-smoothed ADMM within SQP, and pairs it with first-order RL (SHAC) that reuses rollout solutions to enable fast, stable end-to-end training of MPC policies, demonstrated with up to 4.4× higher training throughput and validated on a full-scale race car.

## Abstract
Differentiable model predictive control (MPC) enables structured, constraint-aware policies to be optimized end-to-end. However, learning MPC policies faces two bottlenecks: (1) nonsmooth sensitivities at active-set transitions and (2) expensive policy evaluation, since each requires an optimization solve. We first introduce SmoothedTurboMPC, a GPU-parallel differentiable MPC solver combining sequential quadratic programming (SQP) with a log-barrier-smoothed alternating direction method of multipliers (ADMM) inner solver. Its design enables smooth gradients, exact sensitivities at convergence, and efficient execution on GPUs. Second, to efficiently train MPC policies, we pair our solver with first-order reinforcement learning (FORL) using Short-Horizon Actor-Critic (SHAC), which reuses rollout MPC solutions instead of repeatedly re-evaluating them. Comparisons with state of the art solvers show that the approach achieves up to $4.4\times$ higher end-to-end training throughput. On a vehicle racing task, our method achieves higher returns than MPC PPO with a $46\times$ speedup, training on 3.3 million transitions in only 7 minutes. Finally, we use the framework to train a more reliable MPC racing policy via RL with domain randomization, and validate it on a full-scale race car. We integrate our advances into the open-source TurboMPC solver.


## 精读解读（中文）
### 一、研究动机
可微模型预测控制（MPC）能把约束感知的结构化策略端到端优化，但学习MPC策略面临两个瓶颈：约束主动集切换导致解映射敏感性不光滑，以及每次策略评估都需一次优化求解，训练昂贵。现有log-barrier内点法和反复重评估的RL-MPC方法未能同时高效解决这两个问题，因此需要协同设计GPU可微MPC求解器与一阶强化学习训练流程。

### 二、技术方案（Method）
本文提出SmoothedTurboMPC：前向以SQP求解MPC非线性规划，内层在TurboMPC的ADMM中把投影式不等式更新替换为log-barrier近端更新，用扰动互补条件ν∘y=κ1平滑主动集边界，并在GPU上并行执行。反向传播对收敛KKT条件做隐式微分，通过伴随变量求外层次优问题的参数梯度，避免显式构造解对参数的雅可比；κ>0保证乘子与松弛不同时消失，κ→0时逼近原硬约束问题。训练端将求解器与Short-Horizon Actor-Critic（SHAC）一阶强化学习配对，复用rollout中的MPC解做单次策略更新而非在收集状态上反复重求解，并可结合域随机化学习MPC成本网络后部署MPC策略。

### 三、结果（Result）
与最先进可微MPC求解器相比，该方案端到端训练吞吐最高提升4.4×；在车辆竞速仿真中，MPC-SHAC回报高于MPC PPO，墙钟时间加速46×，仅用7分钟训练3.3百万个transition。双积分器玩具实验中，log-barrier平滑使梯度下降从θ0=0.1和10两个初值均收敛到θ*=1.10并加速收敛；实车Lexus LC500水坑弯道测试中，学习策略完成全部四次试验、共12次过水坑，而名义MPC四次均打滑失控。

### 四、结论（Conclusion）
结果表明，将GPU并行log-barrier平滑ADMM可微MPC与SHAC一阶强化学习结合，可在保持约束结构的同时显著提高MPC策略学习效率与梯度稳定性，并能在实车竞速场景获得比名义MPC更可靠的闭环表现。该工作把相关进展集成到开源TurboMPC中，为约束感知结构化策略的高效端到端学习提供了可复现路径，但平滑参数带来的近似偏差和每步优化求解成本仍需权衡。

### 五、方法论与关键技术细节
关键实现包括SQP外层加log-barrier平滑ADMM内层、以近端更新替代投影、通过KKT雅可比和伴随变量做隐式微分，以及SHAC短视界actor-critic的单次一阶更新复用rollout解；双积分器实验取H=6、学习率η=0.1、初值θ0∈{0.1,10}，竞速实验统计3.3M transitions与7分钟训练时间。方法以κ控制平滑度与原NLP近似误差，κ过小仍可能不光滑、过大引入偏差；每次策略评估仍需MPC求解，实车验证依赖域随机化且平台和任务范围有限，结论外推需谨慎。
