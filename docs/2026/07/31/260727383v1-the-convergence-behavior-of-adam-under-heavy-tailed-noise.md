# The Convergence Behavior of Adam under Heavy-Tailed Noise

- 区域：精读区
- 排名：2
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Yijiang Pang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27383v1) · [PDF](https://arxiv.org/pdf/2607.27383v1)

## TLDR
Adam is proven to converge to stationary points under heavy-tailed stochastic noise via a generalized online-to-nonconvex framework, but with suboptimal iteration complexity that becomes optimal when the domain radius is known.

## Abstract
We establish the first convergence guarantees for the plain vector-form \emph{Adam} optimizer under heavy-tailed stochastic noise. While several Adam variants are known to achieve optimal iteration complexity in bounded-variance nonconvex optimization, little is understood about their behavior when stochastic gradients admit only a bounded $p$-th central moment for some $p \in (1,2]$, a setting increasingly observed in modern deep learning. To address this gap, we generalize the recent online-to-nonconvex conversion framework to accommodate heavy-tailed martingale-difference noise. Building on this generalized framework, we develop a discounted regret analysis for Adam, without restrictive parameter coupling. Our results show that Adam converges to $(ρ,ε)$-stationary points under heavy-tailed noise. However, it exhibits a suboptimal iteration complexity and $p$-dependent convergence, a suboptimality that persists even in the bounded-variance case ($p=2$). When the domain radius is known and used to control the online-learner output, a standard setup in related literature, the convergence rate improves to match the optimal complexity. These findings provide new theoretical insight into the robustness and limitations of Adam in heavy-tailed regimes.


## 精读解读（中文）
### 一、研究动机
现有关于Adam优化器的收敛性分析大多假设随机梯度具有有界方差，但现代深度学习中的随机梯度往往只具有有界p阶中心矩（p∈(1,2]），即存在重尾噪声。目前对Adam在重尾噪声下的行为缺乏理论理解，这促使作者建立首个针对plain vector-form Adam在重尾随机噪声下的收敛性保证。

### 二、技术方案（Method）
将最近的online-to-nonconvex转换框架推广到重尾鞅差噪声情形，以处理仅具有有界p阶中心矩的随机梯度。在此广义框架下，对Adam进行折扣遗憾分析，避免了对参数耦合的限制；通过构造在线学习器并利用折扣遗憾界来导出非凸优化中Adam的收敛性，同时在已知定义域半径的场景下，利用该半径控制在线学习器输出以改进收敛率。

### 三、结果（Result）
证明了Adam在重尾噪声下收敛到(ρ,ε)-稳定点，但得到的迭代复杂度是次优的，且收敛速度依赖于p；即使在有界方差情形（p=2）下次优性依然存在。当定义域半径已知并用于控制在线学习器输出时，收敛率可提升至匹配最优复杂度。

### 四、结论（Conclusion）
Adam在重尾噪声下具有鲁棒性，但其默认形式的迭代复杂度并非最优，且对噪声重尾程度敏感；只有借助已知定义域半径等额外信息，才能达到最优收敛率。这一发现揭示了Adam在重尾场景下的理论局限，并为后续改进提供了方向。

### 五、方法论与关键技术细节
核心假设是随机梯度仅满足有界p阶中心矩（p∈(1,2]），而非传统的有界方差；广义online-to-nonconvex框架需要处理重尾鞅差噪声；分析采用折扣遗憾而非累积遗憾，且不依赖Adam参数之间的耦合约束；在通用情形下收敛到(ρ,ε)-稳定点的复杂度为次优，且随p减小而恶化；当p=2时次优性依然存在；若已知域半径并据此调节在线学习器输出，可消除次优性达到最优复杂度。局限性包括需要额外半径信息、结果未给出显式复杂度常数，且未考虑自适应矩估计偏差等实现细节。
