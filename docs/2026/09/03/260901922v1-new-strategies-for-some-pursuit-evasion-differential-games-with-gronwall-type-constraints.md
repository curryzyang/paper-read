# New strategies for some pursuit-evasion differential games with Gronwall-type constraints

- 区域：精读区
- 排名：10
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Jamilu Adamu, Mehdi Salimi, Farouq Abba Wabi, Jewaidu Rilwan
- 机构：Federal University of Health Sciences, Bayero University Kano, Federal University Gashua, Kwantlen Polytechnics University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01922v1) · [PDF](https://arxiv.org/pdf/2609.01922v1)

## TLDR
The paper studies pursuit-evasion differential games in the sequence space \(l_2\) under Gronwall-type (history-dependent) control constraints, constructing new admissible strategies for both pursuer and evader and deriving sufficient conditions for capture and evasion, thus extending prior results from classical geometric and integral constraints to this broader class.

## Abstract
This paper studies a class of non-cooperative pursuit-evasion differential games in the sequence space $l_{2}.$ The motions of the pursuer and the evader are described by certain first-order differential equations while their control functions are subject to Gronwall-type constraints which impose history-dependent bounds on their control resources. Two fundamental problems are investigated. For the pursuit problem, new strategy for the pursuer is constructed and sufficient conditions guaranteeing the completion of pursuit are established. For evasion problem, an admissible strategy of the evader ensuring avoidance of capture is obtained, and corresponding sufficient conditions for successful evasion are derived. The proposed approached extends existing results on differential games with classical geometric and integral constraints to a broader class of systems governed by Gronwall-type restrictions.


## 精读解读（中文）
### 一、研究动机
现有追逃微分博弈研究多采用经典几何约束、积分约束或混合约束，这些约束只限制控制函数的当前取值或总能量消耗，难以刻画具有记忆、疲劳、资源消耗和累积能量反馈等历史依赖特征的现实系统。为此，本文在序列空间 l2 中研究一类双方控制函数均满足 Gronwall 型约束的追逃微分博弈，试图将相关结论从经典约束推广到更广的历史依赖约束框架。

### 二、技术方案（Method）
博弈建模采用一阶微分方程 dp_j/dξ=λ(ξ)a_j(ξ)、de/dξ=λ(ξ)b(ξ)，状态和控制均取值于 Hilbert 空间 l2；追捕者 p_j 的控制 a_j 满足 Gronwall 型不等式 ||a_j(ξ)||^2≤α_j^2+2c∫_0^ξ λ(s)||a_j(s)||^2 ds，逃逸者 e 的控制 b 满足 ||b(ξ)||^2≤β^2+2c∫_0^ξ λ(s)||b(s)||^2 ds。文中先定义可达域闭球，再针对单追捕者情形构造追捕策略：a(ξ)=(e0-p0)/π(θ)+∫_0^θ λ(s)b(s)/π(θ)ds，并要求在终端时刻逃逸者状态落入由不等式 2<e0-p0,z>≤R^2(θ)-r^2(θ)+||e0||^2-||p0||^2 定义的半空间 H 中，从而保证追捕完成。对于逃逸问题，则构造逃逸者的容许避捕策略，并推导保证对所有 ξ≥0 都能回避捕获的充分条件。

### 三、结果（Result）
在 Gronwall 型约束下，本文为追捕问题给出了使追捕者能在有限时间内完成捕获的充分条件，其核心条件与可达域半径 R(θ)、r(θ) 以及半空间 H 有关；为逃逸问题给出了逃逸者能成功避捕的充分条件。文中结果将已有关于几何约束、积分约束和混合约束的微分博弈结论推广到 Gronwall 型历史依赖约束，表明记忆型控制资源边界会显著影响博弈的胜负条件。

### 四、结论（Conclusion）
本文在 l2 序列空间中建立了 Gronwall 型约束下追逃微分博弈的可解性理论，分别给出追捕成功与逃逸成功的充分条件及相应策略构造，拓展了无限维微分博弈的研究范围，为分析具有记忆效应和累积资源约束的冲突控制系统提供了新的理论工具。

### 五、方法论与关键技术细节
关键细节包括：Gronwall 型约束通过积分不等式给出控制资源的历史依赖上界，并由 Gronwall 引理可推出 ||a(ξ)||≤α e^{c∫_0^ξ λ(s)ds} 和 ||b(ξ)||≤β e^{c∫_0^ξ λ(s)ds}，但文中特别指出该指数上界并不等价于原 Gronwall 约束；控制函数要求 Borel 可测且属于相应容许控制集 A_j(α)、B(β)；可达域定义为闭球，半径由控制参数、常数 c、λ 积分以及整个区间上的实际控制范数积分共同决定；追捕策略是开环地利用逃逸者在 [0,θ] 上的控制 b(·) 构造的，需要追捕者预先掌握逃逸者完整控制信息；求解过程强调策略的容许性和系统解的唯一性；本文属于纯理论分析，未提供数值仿真，局限在于充分条件未必必要，且实际应用中逃逸者完整控制函数的可获知性也可能受限。
