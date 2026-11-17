# Stagewise Adaptive Boosting

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Valerie R. Fu, Brayden Lu, Lu Tian
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18662v1) · [PDF](https://arxiv.org/pdf/2611.18662v1)

## TLDR
**TLDR:** The paper proposes **stagewise adaptive boosting**, a general pathwise framework that adaptively selects coordinate updates to build a monotone solution path encouraging stronger sparsity and flexible structural preferences—such as group selection, multi-outcome similarity, and predictor priorities—while often matching baseline predictive performance with substantially smaller models.

## Abstract
Stagewise algorithms and sparsity-inducing regularization are two influential approaches to high-dimensional modeling. Existing stagewise theory, however, largely centers on convex regularization, whereas stronger sparsity and other structural preferences are often pursued through fixed-level nonconvex optimization rather than generating an entire adaptive solution path. We develop stagewise adaptive boosting, a general framework that builds a monotone path by selecting the update consistent with structural preference. The framework can encourage sparsity along the path itself and also admits extensions that promote other properties of the solution, including group selection, similarity across models for multiple outcomes, and known priorities or prerequisite relations among predictors. We study its theoretical property as well as finite sample performance using simulations and real-data analyses. Across these studies, the proposed pathwise approach often achieves predictive performance comparable to commonly used baselines while selecting substantially smaller models. These results suggest that adaptive stagewise learning provides a practical route to stronger sparsity and richer structural control without repeatedly solving separate weighted or nonconvex optimization problems.


## 精读解读（中文）
### 一、研究动机
高维建模中，stagewise算法与稀疏正则化各自重要，但现有stagewise理论主要围绕凸正则（尤其ℓ1），难以在生成整条解路径的同时实现更强稀疏性和结构偏好；非凸惩罚虽可增强稀疏，却多用于固定正则水平的优化而非自适应路径。本文旨在提出一个统一的逐阶段自适应提升框架，在单条单调路径上持续鼓励稀疏性，并扩展到组选择、多结局模型相似性和预测变量优先级等结构约束。

### 二、技术方案（Method）
设数据为(x_i,y_i)，损失L(β)为凸且二阶可微，梯度g(β)=∇L(β)。SAB每步对每个坐标计算候选步长Δβ_j=p(|β_j|)，其中p(·)为单调递增且下界为δ0的函数；用自适应得分S_j=|g_j|p(|β_j|)评估新激活或符号一致方向，对已激活且与梯度同号的坐标设为负无穷以避免符号翻转，然后选择得分最大的坐标并沿保持符号的下降方向更新，输出从零开始的单调系数路径。实现上可由bridge约束P_γ(β)=Σ|β_j|^γ的预算增量δ0导出p(|β_j|)=(|β_j|^γ+δ0)^{1/γ}-|β_j|，γ<1时更强稀疏；训练流程包括用交叉验证或信息准则选γ、用验证误差和停止迭代K控制路径长度，并可选学习率ν、子采样观测或坐标等稳定化措施，框架还可通过修改更新优先级扩展至组选择、多结局相似性和变量先验/前置关系。

### 三、结果（Result）
理论部分比较了SAB在递增权重p(·)下与常数权重经典forward stagewise路径的局部更新和活跃集差异，给出切换权重的局部展开性质，用以刻画路径自身带来的稀疏性差异。模拟和真实数据分析显示，该路径式方法在预测性能上常与常用基线相当，但会选择显著更小的模型；摘要强调这种优势跨多项研究一致出现。

### 四、结论（Conclusion）
自适应stagewise学习为获得更强稀疏性和更丰富结构控制提供了一条实用路径，无需反复求解单独的加权或非凸优化问题。它把结构偏好直接嵌入单条单调解路径的更新选择中，因此可作为传统凸正则stagewise和非凸固定水平优化之间的通用替代方案，尤其适合需要小模型和先验结构约束的高维建模场景。

### 五、方法论与关键技术细节
关键实现点包括：以bridge泛函增量δ0定义步长，γ控制稀疏强度并需调参，δ0控制路径分辨率且建议按标准化特征尺度选取，学习率ν和子采样可加速稳定，停止规则依赖验证误差以防过拟合；计算上每步评分所有坐标至少O(p)并需梯度，光滑损失通常O(np)，平方误差损失可用预计算Gram矩阵实现每步O(n+p)增量更新。方法不依赖先验拟合权重，与adaptive lasso等两步加权法不同，而是在路径中连续重分配预算；局限是非凸bridge约束的精确路径可能不连续，SAB路径不保证等于某个固定非凸正则解，且对p(·)、γ、δ0和停止点较敏感。
