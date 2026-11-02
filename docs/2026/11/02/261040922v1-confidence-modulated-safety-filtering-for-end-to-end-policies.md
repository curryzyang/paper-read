# Confidence-Modulated Safety Filtering for End-to-End Policies

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Javier Borquez, Jaime F. Fisac
- 机构：Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40922v1) · [PDF](https://arxiv.org/pdf/2610.40922v1)

## TLDR
The paper proposes a filter-agnostic safety-filtering pipeline that uses an end-to-end policy’s runtime confidence to modulate the filter’s conservativeness—remaining permissive inside the filter’s certified ODD to preserve performance while becoming more conservative beyond it to add safety margin.

## Abstract
End-to-end policies, from task-specific controllers to robot foundation models, learn complex behavior from raw observations but are not guaranteed to remain safe, so they are often wrapped in a safety filter. The resulting system operates under two domains: the filter's operational design domain (ODD), where its assumptions hold and safety is certified, and the policy's competence domain, where it is reliable. Filters typically fix their conservativeness regardless of the policy's competence, trading performance inside the ODD against margin beyond it. We ask whether the policy's confidence should set that level, and propose a filter-agnostic pipeline that modulates it at runtime: inside the ODD, where every setting is safe, confidence buys performance; beyond it, low confidence adds margin, which helps when it flags where the filter's model fails. Preliminary F1TENTH simulations, where this holds, show the modulated filter combining the strengths of permissive and conservative filters.


## 精读解读（中文）
### 一、研究动机
端到端策略从原始观测学习复杂行为，但无法保证安全，常需外加安全过滤器。现有过滤器通常固定保守程度，忽视策略自身的能力域：在过滤器运行设计域内过度保守会损害高性能策略，在域外过度宽松又可能在策略不可靠时失去安全余量。本文因此追问：任务策略的置信度是否应在线决定安全过滤器的保守程度。

### 二、技术方案（Method）
论文提出与过滤器无关的置信度调制流程：以回退策略、安全监控器和干预方案构成基础安全过滤器，并以基础监控器给出的安全余量定义保守性偏序和分级过滤器族；置信度监控器将当前信息状态映射为[0,1]的信任分数，再用非增调度函数把该分数映射到分级族参数，低置信度选择更保守过滤器，系统执行调制后的干预动作，且在运行设计域假设成立时继承基础安全证书。实验在F1TENTH仿真中进行，任务策略为输入两层LiDAR扫描的TD3端到端策略，置信度取策略观测自编码器的重构误差，过滤器为带直行制动、全左转和全右转三种备份机动的backup CBF，按离散CBF条件构造分级族，调度将无信任时的γ设为0.08、全信任时的γ设为0.55；过滤器按标称摩擦μ=1.05构建，并以μ=0.6测试域外泛化。

### 三、结果（Result）
在每方法60圈的F1TENTH仿真中，无过滤器在ODD内碰撞45圈、域外60圈全部碰撞。ODD内各过滤器均无碰撞，调制过滤器完成60圈且圈时30.2±0.2秒，接近最宽松固定γ=0.55的30.4±0.2秒，快于最保守固定γ=0.08的31.4±0.2秒。域外最宽松固定过滤器有10圈碰撞、2圈超时、48圈完成，而调制过滤器完成全部60圈，与最保守固定过滤器一样安全，但圈时30.8±0.2秒，比其31.3±0.2秒快约0.5秒；图示调制过滤器在直道和缓弯保持宽松，在策略置信度下降的急弯转为保守，而固定宽松过滤器在同一急弯碰撞。

### 四、结论（Conclusion）
论文提出用任务策略置信度调制安全过滤器保守性，以同一流程在过滤器ODD内换取性能、在ODD外增加安全余量。初步F1TENTH仿真支持该假设：调制过滤器在ODD内达到最宽松固定过滤器的性能，在ODD外达到最保守固定过滤器的安全性且更快。作者指出结果仍需更广泛的仿真和真实机器人验证，并认为该流程只依赖置信度分数，可扩展到能力不均衡的机器人基础模型。

### 五、方法论与关键技术细节
关键细节包括：保守性由基础监控器在干预后保留的安全余量比较，分级族需满足过滤器条件且参数有序；置信度调度须非增，低置信度对应更保守成员；调制不要求系统知道ODD边界，但依赖两个条件，即低置信度处策略更可能不安全，以及ODD外监控器失效处置信度较低。实验中置信度来自自编码器重构误差，无法观测摩擦变化，因此急弯处置信度下降既反映几何不熟悉，也对应低摩擦使监控器失效。局限是仅初步单一仿真基准、每方法60圈、域外仅通过降低摩擦构造，尚未在真实机器人验证；文中未给出额外计算复杂度或训练损失细节。
