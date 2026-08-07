# Contour integral methods and model order reduction for parametric linear control systems

- 区域：精读区
- 排名：2
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Serkan Gugercin, Mattia Manucci
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05363v1) · [PDF](https://arxiv.org/pdf/2608.05363v1)

## TLDR
The paper introduces a contour integral method combined with projection-based model order reduction—using a greedy algorithm with an error estimate and naturally enforcing Hermite interpolation—to efficiently and accurately compute outputs of parametric linear control systems across the parameter domain.

## Abstract
This paper introduces a contour integral method (CIM) for efficiently computing outputs of parametric linear systems in control form over specified time intervals and to a user-prescribed accuracy. The CIM approximates the inverse Laplace transform via a quadrature rule applied along a modified integration contour. For parametric systems, we show how CIM integrates effectively with projection-based model order reduction (MOR) where a greedy algorithm builds the projection spaces following an error estimate we derive for this setting. We additionally demonstrate that the developed projection framework naturally enforces Hermite interpolation conditions. This combination substantially lowers the cost of evaluating the input-output relations across the parameter domain, for a wide range of input functions, and for initial conditions well captured by a low-dimensional subspace.. We demonstrate the accuracy and efficiency of the approach on benchmark non-parametric and parametric control systems, comparing against state-of-the-art projection-based MOR methods.


## 精读解读（中文）
### 一、研究动机
针对参数化线性控制系统在全阶模型下进行参数域内多查询模拟时计算代价过高的问题，本文旨在发展一种可高效计算指定时间区间内系统输出、并能达到用户给定精度的数值方法，同时与投影型模型降阶相结合，降低参数扫描和输入输出关系评估的成本。

### 二、技术方案（Method）
以控制形式的参数化线性系统为对象，输入包括系统矩阵、输入/输出矩阵、输入函数、初始条件、时间区间和用户精度tol。方法核心是轮廓积分法：通过沿一条修正积分轮廓应用数值求积规则，近似逆拉普拉斯变换，将时域输出计算转化为复平面上的求积问题；对参数化系统，进一步将CIM与基于投影的模型降阶结合，推导适用于该设置的误差估计，并利用贪婪算法根据误差估计自动选择参数样本并构建投影空间，得到参数化降阶模型；该投影框架还自然满足Hermite插值条件。推理流程为先在选定的参数样本和求积节点上求解全阶系统，构造投影基，再对全阶系统做Galerkin投影得到ROM，最后在参数域内快速计算任意参数下的输入-输出响应。

### 三、结果（Result）
在基准的非参数和参数化控制系统中，本文方法能够在保持用户指定精度的前提下，显著降低参数域上评估输入-输出关系的计算成本；与最新的基于投影的模型降阶方法相比，验证了所提误差估计、贪婪子空间构造以及Hermite插值性质的有效性和效率优势。

### 四、结论（Conclusion）
轮廓积分法与投影型模型降阶可以有效结合，为参数化线性控制系统的时域输出计算提供一种高精度、低成本的方案；该方法适用于多种输入函数，并且当初始条件能被低维子空间较好刻画时，能够大幅加速跨参数域的模拟与评估。

### 五、方法论与关键技术细节
关键细节包括：采用逆拉普拉斯变换的轮廓积分与求积规则，通过修正积分轮廓和用户指定精度tol控制误差；贪婪算法基于本文推导的误差估计选择参数点和投影空间，避免穷举参数采样；投影框架自动满足Hermite插值条件，增强了ROM对原系统的匹配能力；方法适用于控制形式的线性系统，输入函数类型较广，但假设初始条件可由低维子空间有效表示；计算代价主要取决于求积节点数、约化维度和所选参数样本数，避免了在每个参数点执行全阶时域积分；潜在局限性包括误差估计可能保守、积分轮廓与求积参数需要根据时间区间和精度要求调整，以及强非线性参数依赖或高维参数情形下贪婪采样可能面临更大挑战。
