# Trust-Region Optimization for Performative Prediction without Response Modeling

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Siqi Du, Miaolan Xie, Roy Dong
- 机构：University of Illinois Urbana-Champaign, Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31492v1) · [PDF](https://arxiv.org/pdf/2611.31492v1)

## TLDR
The paper proposes Performative Trust-Region Optimization (PTRO), which optimizes performative risk without specifying or fitting a population response model by exploiting the known loss and using deployment-based finite-difference estimates with adaptive trust regions, and proves high-probability convergence to an ε-stationary point.

## Abstract
Performative prediction studies learning problems in which deployed decisions change the distribution of future data. Existing methods often impose structure on the population response, which limits their applicability when a fixed model class poorly captures that response. Generic black-box optimization avoids response modeling but does not exploit the known loss function.
  We introduce Performative Trust-Region Optimization (PTRO), which bridges these two approaches by optimizing performative risk without specifying or fitting a response model while still exploiting the known loss. The key idea is sampling from the current population to evaluate the known loss at nearby decisions, and use additional deployments only to estimate the effect of population response. This gives a local approximation of performative risk without committing to a model of how the population responds. PTRO then uses a trust-region mechanism to determine and adapt how far this local information can be trusted.
  Under moment-bounded losses and suitable smoothness and estimator-accuracy conditions, we establish high-probability convergence to an $ε$-stationary point of the performative risk in $O(ε^{-2})$ iterations, with $O(d^{3}ε^{-4})$ samples per iteration, where $d$ is the decision dimension and $q\geq2$ is the loss-moment order.
  Experiments illustrate methods built around a specified response model can be more sample-efficient when their structural assumptions are accurate, whereas PTRO remains effective as the population response is poorly captured by a fixed model class. Ablations further show that both exploiting the known loss and adaptive trust-region updates are important for controlling the accuracy and efficiency.


## 精读解读（中文）
### 一、研究动机
现有performative prediction方法常假设或拟合参数化总体响应模型，在异质人群或固定模型类无法刻画响应时适用性受限；黑箱优化虽避免响应建模但丢弃了已知损失函数结构。论文旨在不指定或估计响应模型的前提下优化performative risk，同时利用已知损失。

### 二、技术方案（Method）
定义解耦风险R(x1,x2)=E_{z~D(x2)}[ell(z;x1)]，将PR(x_k+s)分解为当前总体上的期望损失与总体响应效应；每轮从D(x_k)采样估计当前总体损失并可在邻近决策处评估已知损失，用对x2的有限差分和额外部署估计响应梯度g2,k，构造局部模型m_k(s)=f(x_k+s,x_k)+g2,k^T s+1/2 s^T H_k s，在信赖域内近似最小化得到步长并满足分数Cauchy下降条件，再用新部署样本比较预测与实测风险下降来决定接受步和调整半径。

### 三、结果（Result）
在损失矩有界q>=2、PR光滑和估计精度条件下，PTRO以高概率在O(epsilon^-2)次迭代收敛到performative risk的epsilon-平稳点，每轮样本复杂度O(d^3 epsilon^-4)。实验显示响应模型正确设定时结构化方法更省样本，而PTRO在响应难以被固定模型类刻画时仍有效；消融表明利用已知损失和自适应信赖域半径对精度与效率均重要。

### 四、结论（Conclusion）
PTRO提供了一种不建模总体响应、但利用已知损失与解耦结构的performative优化框架，将假设从响应模型形式转移到诱导风险的正则性条件上；其代价是较高的每轮样本复杂度和对部署及光滑性条件的依赖，适合响应机制未知或异质的场景。

### 五、方法论与关键技术细节
关键实现包括用当前总体样本评估已知损失、用独立部署的有限差分估计响应梯度、局部模型中的H_k只需一致有界而非精确Hessian，采用预测与实测下降比进行信赖域接受与半径更新；理论依赖PR的L-Lipschitz梯度、损失光滑性、q阶矩界和估计器精度，复杂度含每轮O(d^3 epsilon^-4)样本，且目标是epsilon-平稳点而非全局最优，响应低维且结构化模型正确时结构化方法可能更省样本。
