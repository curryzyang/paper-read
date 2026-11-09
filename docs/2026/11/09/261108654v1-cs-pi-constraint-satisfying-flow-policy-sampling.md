# CS-Pi: Constraint-Satisfying Flow Policy Sampling

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Soumojit Bhattacharya, Oliver Kroemer, Shubham Tulsiani
- 机构：Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08654v1) · [PDF](https://arxiv.org/pdf/2611.08654v1)

## TLDR
**TLDR:** CS-Pi is a training-free draw–project–renoise sampler for flow-matching policies that projects each sampled action to the nearest constraint-satisfying action, renoises it in proportion to the projection distance, and re-runs the unmodified policy until the draw is safe, yielding actions that are both safe and plausible.

## Abstract
A flow-matching policy deployed in the field must often satisfy a constraint that was absent from its demonstrations, such as avoiding an obstacle it has never seen. Retraining for every new constraint is impractical, so the constraint must be enforced at inference time. Enforcing it must not discard what the policy learned: an action the policy would rarely sample may avoid the obstacle yet fail the task. We therefore want actions that are both safe, satisfying the constraint, and plausible, remaining likely under the policy. Gradient guidance, the most common approach, steers noisy states, so it must evaluate its cost on the policy's running estimate of the clean action; when the policy is uncertain between passing left or right of an obstacle, this estimate is their average and can pass straight through it. We instead build on rejection and projection. Rejection redraws actions until one is safe: every output is plausible, but the wait is intractable when safe actions are rare. Projection moves an action to the nearest safe one: it is efficient, but the result need not be plausible. Our key insight is that flow-matching sampling lets us combine the two, keeping projection's efficiency and rejection's plausibility. CS-Pi, our draw-project-renoise sampler, projects each draw to the nearest safe action, adds noise back scaled to how far the projection moved it, and re-runs the unmodified policy until a draw is safe. Replacing only the projection step extends CS-Pi to continuous costs. Across a 2D diagnostic, a 7-DoF shelf pick-and-place, an orientation preference, and a zero-shot Franka deployment, CS-Pi reaches 81% safe success on the shelf and 55% on hardware, against 55% and 40% for projection, while staying plausible.


## 精读解读（中文）
### 一、研究动机
部署中的流匹配策略常需满足训练示范中未出现的约束，例如避开未见障碍物；为每条新约束重新训练不现实，因此必须在推理时施加约束。但约束修正不能丢弃策略已学到的任务与运动先验：仅安全但策略几乎不会采样的动作可能仍然失败。梯度引导在含噪中间状态上依赖对干净动作的代理估计，当策略在障碍物左右绕行等多模态间不确定时，该代理可能落在两模态平均处并穿过障碍；拒绝采样虽保持策略似然但在安全动作稀少时不可行，投影虽高效但结果未必合理。

### 二、技术方案（Method）
CS-Pi将部署时约束表述为安全集 C 及其欧氏投影 P(a)=argmin_{a'∈C}||a'-a||。给定流匹配策略 πθ，从高斯噪声 a0 积分学习到的速度场得到干净动作 a=πθ(a0;0)；每轮对当前干净采样 ahat 先投影到 C 得到安全锚点 ac=P(ahat)，再按投影位移残差 δ 将锚点回噪到时间 n=k/(k+δ)（δ 越大回噪越多），随后从该噪声级用未修改的策略重新去噪得到下一次采样，循环直到某次采样本身落在安全集内。该方法不需要在含噪状态上对约束求梯度；扩展到连续代价时只替换投影步骤，并可同时结合硬约束与软代价。

### 三、结果（Result）
在2D诊断、7-DoF货架抓取放置、方向偏好和零样本Franka部署中，CS-Pi在货架任务达到81%安全成功率、硬件达到55%，而仅投影分别为55%和40%，同时保持动作在策略下合理。论文报告CS-Pi是唯一在约束允许处同时满足安全性与合理性的采样器，并且计算成本远低于拒绝采样。

### 四、结论（Conclusion）
CS-Pi是一种无需重训、仅推理期执行的draw-project-renoise采样器，以投影为锚点、按投影残差回噪并用原策略重新去噪，从而结合投影的效率与拒绝采样的合理性。它避免了梯度引导在噪声代理上评估约束梯度的缺陷，可扩展到连续代价，并能零样本用于现有流匹配策略和VLA策略。

### 五、方法论与关键技术细节
关键实现包括：安全集只需提供可计算的欧氏投影；回噪量由投影残差 δ 决定，回噪时间设为 n=k/(k+δ)，并迭代至采样安全；连续代价仅替换投影步；无需CBF所需可微屏障、Lie导数或学习动力学模型。实验中硬件使用π0.5策略和由视觉估计的障碍框进行零样本Franka部署；局限是方法依赖可用的投影算子，且未评估需要学习动力学模型的SAD-Flower。
