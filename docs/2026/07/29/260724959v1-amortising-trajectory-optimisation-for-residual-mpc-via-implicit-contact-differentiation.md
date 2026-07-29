# Amortising Trajectory Optimisation for Residual MPC via Implicit Contact Differentiation

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Daniel Layeghi, Thomas Corbères, Calum Arnott, Aditya Kamireddypalli, Hashim Al-Obaidi, Steve Tonneau, Michael Mistry
- 机构：University of Edinburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24959v1) · [PDF](https://arxiv.org/pdf/2607.24959v1)

## TLDR
This paper introduces a memory-efficient implicit differentiation method for smooth contact-rich simulation using the Implicit Function Theorem, which avoids solver unrolling and hand-assembled KKT systems, and combines it with optimiser distillation for residual MPC to significantly improve success rates on Finger, Franka, and Unitree robots.

## Abstract
Differentiable simulation can accelerate contact-rich trajectory optimisation by exposing local sensitivities of task outcomes to controls. Existing approaches either use finite differences, which are expensive and step-size sensitive; differentiate iterative contact solvers by unrolling automatic differentiation (AD), which stores a growing computation trace; or require intricate, solver-specific KKT sensitivity derivations. We introduce an AD-assisted implicit derivative for regularised smooth contacts and apply it to Mujoco MJX, based on the Implicit Function Theorem (IFT). The method differentiates the stationarity residual at the tolerance-converged solution, avoiding both solver unrolling and hand-assembled KKT systems. IFT keeps compiled temporary memory nearly constant with solver effort, changing by less than 4$\%$ from one to ten iterations versus 10.6$\times$ growth for unrolled AD. IFT memory grows slower with active contacts and model dimension, using 20$\times$ less memory at 256 contacts and 6$\times$ less at 16 contacts and 96 DoF. We further introduce optimiser distillation for residual MPC, amortising batched full-horizon iLQR into a policy that guides short-horizon residual iLQR. Across Finger, Franka, and Unitree, this raises six-step success by 28-98 percentage points over standard iLQR.


## 精读解读（中文）
### 一、研究动机
现有可微仿真方法在接触丰富轨迹优化中存在计算和内存瓶颈：有限差分昂贵且对步长敏感，展开自动微分存储增长的计算轨迹，而KKT灵敏度推导复杂且依赖求解器。这限制了并行轨迹数量和长时间跨度的优化。

### 二、技术方案（Method）
基于隐函数定理，对正则化光滑接触问题的驻留残差进行自动微分辅助的隐式微分，应用于MuJoCo MJX。方法不修改前向求解器，避免展开求解器轨迹和手工组装KKT系统。同时提出优化器蒸馏：利用批量全水平iLQR生成教师轨迹，将优化动作蒸馏为策略网络，部署时策略提供长期名义动作，短水平残差iLQR提供局部模型校正。

### 三、结果（Result）
隐式微分保持编译临时内存几乎恒定，随求解器迭代变化小于4%，而展开自动微分增长10.6倍；在256个主动接触时内存减少20倍，在16个接触和96自由度时减少6倍。在Finger、Franka和Unitree机器人上，残差MPC的六步成功率比标准iLQR提高28-98个百分点。

### 四、结论（Conclusion）
提出的隐式微分方法有效解决了接触求解器内存扩展问题，使大规模并行轨迹优化成为可能。结合优化器蒸馏，显著提升了短水平模型预测控制的成功率和规划性能，验证了可微仿真与学习结合的潜力。

### 五、方法论与关键技术细节
方法基于Mujoco MJX的正则化光滑接触模型，利用隐函数定理微分收敛解；梯度仅在固定接触集和光滑摩擦区域内有效，接触创建/分离或摩擦模式变化时可能不准确。内存优势随求解器迭代、主动接触数和广义速度维度增大而更加显著。局限性包括对光滑正则化的依赖，且未处理接触非光滑事件；蒸馏需要离线生成教师轨迹，可能引入分布偏移。
