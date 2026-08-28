# Dispersive Forward Tree Search for Optimal Control: Coverage, Complexity, and Computation

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Shashank A. Deshpande, Jonathan P. How
- 机构：Massachusetts Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26314v1) · [PDF](https://arxiv.org/pdf/2608.26314v1)

## TLDR
The paper develops Dispersive Forward Tree search (DFT*), a propagation-based kinodynamic planner with deterministic finite-sample near-optimality guarantees for differentially flat systems, using locally dispersive control samplers and cost-conditioned dominance pruning to achieve polynomial tree complexity and strong practical performance on parallel hardware.

## Abstract
Steering-based planners require solutions to state-to-state boundary value problems, which can be inaccessible for nonlinear platforms. Forward propagation evades the steering requirement, but the finite-sample behavior of the associated planners remains uncharacterized and their implementations underperform in practice. This paper develops a propagation-based kinodynamic planner with deterministic finite-sample near-optimality guarantees. We work within the large class of differentially flat nonlinear systems and show that a forward tree of locally dispersive control commands contains a near-optimal trajectory at a certified tree size. We provide a general mechanism to construct dispersive command sets for control-affine systems, which are necessary to implement the search algorithm prescribed by the theory. We show that covering the certified trajectory class irrespective of cost provably demands a tree exponentially sized in the problem horizon, and present a cost-conditioned dominance pruning procedure that retains near-optimality at a tree size polynomial in the horizon. We implement the resulting search algorithm, Dispersive Forward Tree search (DFT*), as breadth-first expansion of the forward tree, which maps naturally onto parallel hardware. We design efficient dispersive samplers for the unicycle, the trailer car, and the quadrotor and evaluate challenging planning tasks for these platforms. DFT* delivers consistently competitive and often substantially better solution quality than state-of-the-art kinodynamic planners at comparable solution times on embedded-tier processors, accelerating further as parallel compute is scaled. We also implement DFT* in a receding-horizon loop to demonstrate real-time planning in dynamic environments at embedded-tier compute budgets.


## 精读解读（中文）
### 一、研究动机
基于转向（steering）的规划器需要求解状态到状态的边值问题，这对非线性平台通常不可行；前向传播虽能避免转向要求，但其有限样本行为缺乏刻画且实际实现性能不佳。本文针对微分平坦非线性系统，提出一种基于前向传播的动力学规划器，并给出确定性有限样本近最优性保证，以弥补该方向理论空白。

### 二、技术方案（Method）
提出 Dispersive Forward Tree Search (DFT*)：在微分平坦系统框架下，通过对控制命令集进行局部分散（locally dispersive）采样，以广度优先方式扩展前向树，无需求解边值问题。具体地，利用微分平坦性构造关于平坦输出喷流（flat output jets）的轨迹类覆盖，给出控制仿射系统分散命令集的一般构造机制；搜索采用前向传播+广度优先扩展，天然适合并行硬件。为控制树规模，引入基于代价的条件支配剪枝（cost-conditioned dominance pruning），在保留近最优性的前提下将树大小从关于问题时域指数级降为多项式级。还实现了单轮车、拖挂车和四旋翼的高效分散采样器，并给出用于动态环境的滚动时域版本 WWDFT*。

### 三、结果（Result）
在 Dynobench 离线基准上，DFT* 在嵌入式级处理器上与最先进动力学规划器在相近求解时间内相比，解质量持续具有竞争力且经常显著更优；随并行计算规模扩展可进一步加速。滚动时域版本的 WWDFT* 在嵌入式计算预算下实现了动态环境中的实时规划。理论方面，证明了分散前向树在认证树规模下包含近最优轨迹，并对无约束代价类给出了指数下界和经剪枝后的多项式上界。

### 四、结论（Conclusion）
DFT* 表明，对于微分平坦非线性系统，基于前向传播的动力学规划可以在不依赖转向求解的前提下获得确定性有限样本近最优性保证；结合代价条件支配剪枝，算法在理论上和工程实现上均高效可行，可作为基于前向搜索的最优控制规划新范式。

### 五、方法论与关键技术细节
关键点包括：理论保证针对微分平坦非线性系统，参考轨迹类需满足侵蚀控制权限（ε-eroded control authority）和约束鲁棒性；有限样本近最优性用命令集分散度 δ_A(n) 刻画，代价泛函需足够正则且可随时间递归聚合，约束需可时间组合，否则覆盖认证轨迹类要求树指数级增长。实际实现采用广度优先并行扩展与支配剪枝，复杂度和计算量由时域指数级降为多项式级；方法依赖微分平坦性，控制仿射系统有通用分散命令集构造，并针对单轮车、拖挂车、四旋翼设计了采样器。局限在于目前目标是等价的鲁棒最优代价而非精确全局最优，且对非平坦系统需另行设计覆盖机制。
