# Costate Estimation and Covector Mapping for Bernstein Polynomial Direct Methods in Optimal Control

- 区域：精读区
- 排名：1
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Venanzio Cichella, Isaac Kaminer, Claire Walton, Naira Hovakimyan, Antonio Pascoal
- 机构：University of Iowa, University of Texas at San Antonio, Naval Postgraduate School, University of Lisbon, University of Illinois at Urbana-Champaign
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00250v1) · [PDF](https://arxiv.org/pdf/2611.00250v1)

## TLDR
This paper establishes that a Bernstein-polynomial direct method for constrained nonlinear optimal control, imposing dynamics and path constraints at the Bernstein control points, is consistent and enables costate estimation through a Covector Mapping Theorem based on scaled relaxed KKT multipliers.

## Abstract
Bernstein polynomial approximation of continuous functions has a slower rate of convergence as compared to other approximation methods. ``The fact seems to have precluded any numerical application of Bernstein polynomials from having been made. Perhaps they will find application when the properties of the approximant in the large are of more importance than the closeness of the approximation.'' -- has remarked P.J. Davis in his 1963 book Interpolation and Approximation. This paper presents a direct approximation method for nonlinear optimal control problems with mixed input and state constraints based on Bernstein polynomial approximation, in which the dynamic and path constraints are imposed at the Bernstein coefficients (control points). We provide a rigorous analysis showing that, under convergence assumptions on the control polygons, the proposed method yields consistent approximations of time continuous optimal control problems and can be used for costate estimation of the optimal control problems. In particular, multipliers satisfying a relaxed Karush Kuhn Tucker system of the resulting nonlinear program, scaled by the quadrature weight, approximate the costate and the multipliers of the optimal control problem. Owing to the structure of the Bernstein differentiation matrix, the discrete transversality conditions are contained in the relaxed Karush Kuhn Tucker system, and no additional closure conditions need to be added to it. This result leads to the formulation of the Covector Mapping Theorem for Bernstein polynomial approximation.


## 精读解读（中文）
### 一、研究动机
直接法虽可将非线性最优控制问题转写为NLP并用现成求解器求解，但原问题的协态通常不能直接获得；在安全关键机器人运动规划等应用中，协态对于检验必要性最优条件和评估解的有效性很重要。已有Bernstein直接法主要处理原问题可行性/一致性与在时间节点施加约束的协态估计，而将动态与路径约束施加在Bernstein系数（控制点）上的公式尚缺乏严格的对偶分析与协态映射理论。

### 二、技术方案（Method）
针对含混合输入与状态约束的Bolza型非线性最优控制问题，用Bernstein多项式近似状态与控制，以控制点作为决策变量，并在Bernstein系数处施加动态约束和路径约束；利用Bernstein微分矩阵计算导数、利用积分权重构造目标与约束离散，形成NLP。随后推导该NLP的松弛KKT系统，将乘子按求积权重缩放后与连续时间最优控制问题的一阶最优性条件比较，在控制多边形收敛假设下证明一致性并建立Bernstein逼近的Covector Mapping Theorem，从而由离散乘子估计协态和约束乘子。

### 三、结果（Result）
论文证明在控制多边形收敛假设下，所提出的Bernstein直接法给出连续时间最优控制问题的一致逼近；缩放后的松弛KKT乘子可逼近原问题的协态及路径约束乘子。由于Bernstein微分矩阵的特殊结构，离散横截条件自动包含在松弛KKT系统中，无需额外加入闭包条件；这促成了Bernstein多项式直接法的协态映射定理，并给出比在时间节点施加约束的公式更简单的离散最优性条件。

### 四、结论（Conclusion）
该工作表明Bernstein多项式直接法不仅能求原问题近似解，还能为非线性约束最优控制问题提供有理论保证的协态估计，从而支持必要性最优条件的检验。其核心贡献是将协态估计与covector mapping推广到在控制点施加约束的Bernstein离散框架，并严格建立离散乘子与连续协态之间的关系。

### 五、方法论与关键技术细节
关键实现包括采用等距节点t_j=j/N与Bernstein系数/控制点建模，动态与路径约束直接施加在控制点上；导数通过三对角Bernstein微分矩阵计算，积分采用权重w=1/(N+1)的Bernstein求积；对偶分析基于NLP的松弛KKT系统，乘子需按求积权重缩放后映射为协态和约束乘子，且微分矩阵结构保证离散横截条件无需额外闭合条件。理论依赖控制多边形收敛与光滑性假设，Bernstein逼近收敛率相对较慢是固有限制；摘要未给出具体数值指标，但强调一致性、均匀收敛性质及数值示例。
