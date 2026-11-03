# A Preconditioned Semismooth Newton Method for Box-Constrained Elliptic Optimal Control Problems with Random Coefficients

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Zhendong Li, Akwum Onwunta, Hailing Wang
- 机构：The Hong Kong Polytechnic University, Lehigh University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00246v1) · [PDF](https://arxiv.org/pdf/2611.00246v1)

## TLDR
This paper develops a Fenchel-duality-based, matrix-free preconditioned semismooth Newton–PCG method for box-constrained elliptic optimal control problems with random diffusion, solving an exact reduced adjoint formulation after stochastic Galerkin–finite element discretization with a current-set preconditioner and demonstrating robust, mesh- and stochastic-dimension-independent convergence.

## Abstract
We consider the optimal control problem of an elliptic PDE with random diffusion under pointwise box constraints on the control. The constraints make the optimality conditions nonsmooth, with an active set that is not known in advance, and the random diffusion couples the state and the adjoint across all stochastic modes. To design a solution algorithm for this problem, we rely on the Fenchel duality viewpoint. Fenchel duality absorbs the box constraint into the objective and yields an exact reduced problem in the elliptic adjoint variable alone. After a stochastic Galerkin--finite element discretization, eliminating the state leaves a strongly monotone, piecewise smooth equation, which we solve directly by a matrix-free semismooth Newton method with the box projection retained exactly and with no outer iteration, penalty or smoothing parameter. Next, we introduce and analyze a current-set preconditioner, which adds the active-set correction of the current Newton step to a mean-diffusion reference operator and is inverted exactly by a rank-1 update. For implementation, we use a cheaper preconditioner that keeps only a fraction of free control values. Numerical experiments show second-order convergence of the state, and Newton and PCG counts that stay bounded under mesh refinement and growth of the stochastic dimension.


## 精读解读（中文）
### 一、研究动机
随机扩散系数椭圆PDE最优控制带逐点箱约束时，最优性条件非光滑且活跃集未知，随机扩散又使状态与伴随在所有随机模态上耦合。惩罚、内点或平滑方法需引入额外参数且仅极限恢复精确约束，而随机Galerkin下活跃集项破坏Kronecker结构，因此需要直接处理箱约束且可扩展的求解框架。

### 二、技术方案（Method）
从Fenchel对偶视角将箱约束吸收到目标中，得到仅以椭圆伴随变量为未知量的精确约化问题；经随机Galerkin-有限元离散并消去状态后，得到强单调分段光滑方程。采用无矩阵半光滑牛顿法直接求解，保留精确箱投影，不需外层迭代、惩罚或平滑参数；提出current-set预条件子，将当前牛顿步的活跃集修正加到均值扩散参考算子上，并用秩1更新精确求逆。实现中使用仅保留部分自由控制值的廉价预条件子，配合PCG内迭代，并复用空间矩阵的稀疏Cholesky分解。

### 三、结果（Result）
数值实验显示状态变量达到二阶收敛，且在网格加密和随机维数增长时Newton迭代数与PCG迭代数保持有界。这表明所提对偶半光滑牛顿-PCG方法在精确处理箱约束的同时，对离散规模和随机维度具有较好的稳健性。

### 四、结论（Conclusion）
该工作表明，Fenchel对偶结合半光滑牛顿与结构化预条件可有效求解随机系数椭圆PDE箱约束最优控制，避免惩罚、平滑参数和外层迭代。current-set预条件分析缓解了活跃集变化与非Kronecker结构带来的困难，为高维随机最优控制提供了可扩展求解思路。

### 五、方法论与关键技术细节
问题在Bochner空间L2_rho(Gamma;H0^1)中建模，约束为关于空间和随机参数几乎处处成立的a<=u<=b；对偶推导给出最优性系统及原始-对偶恢复关系。离散采用随机Galerkin投影到全局正交多项式基，离散状态算子呈Kronecker和结构；理论预条件子P_W由均值扩散参考算子加当前活跃集修正构成，并用Sherman-Morrison-Woodbury秩1更新精确求逆。实际预条件子P_k仅保留一部分自由控制值，需一次稀疏Cholesky分解并在Newton步间复用；方法无惩罚或平滑参数，但P_W的精确分析对应理想预条件，数值实现采用其廉价近似，且随机维数维数K有限。
