# Echo: Scaling Visual Reinforcement Learning with Off-policy Experience

- 区域：精读区
- 排名：7
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Gagan Khandate
- 机构：Columbia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37865v1) · [PDF](https://arxiv.org/pdf/2610.37865v1)

## TLDR
Echo is a single-stage off-policy visual RL framework that uses inverse distillation—a state-based auxiliary policy imitates the evolving visual policy to collect cheap unrendered experience—so that a shared privileged critic can improve the visual policy without proportionally increasing rendering and inference costs.

## Abstract
Scaling visual reinforcement learning (RL) with GPU-accelerated simulation is computationally expensive due to rendering and visual-policy inference costs. Consequently, two-stage teacher--student distillation is commonly used to train visual policies, but introduces an imitation gap. In this preliminary study, we introduce \echomethod{}, \textbf{a single-stage off-policy RL framework that scales experience collection without proportionally increasing visual computation}. Through \textbf{inverse distillation}, a state-based auxiliary policy imitates the evolving visual policy and collects inexpensive, unrendered experience. Echo leverages this experience for off-policy value learning, directly improving the visual policy through a shared privileged critic. We instantiate \echomethod{} with FastTD3 and evaluate it on three visual control tasks and two dexterous manipulation tasks in Genesis. Relative to \sdpgmethod{} under the evaluated configurations, Echo reduces time to reference returns by an average of \textbf{60\% across the three locomotion tasks} and \textbf{56\% across both hand tasks}, while improving peak mean returns by \textbf{62\% and 12\%}, respectively. Both hand tasks also achieve higher mean returns at matched simulator-transition budgets. These initial results suggest that scaling off-policy experience is a promising approach to efficient direct visual RL.


## 精读解读（中文）
### 一、研究动机
视觉强化学习受限于渲染和视觉策略推理的高计算成本，难以像状态型强化学习一样扩展经验规模；常见两阶段教师—学生蒸馏虽能利用特权状态，但会引入模仿差距和分布偏移。本文关注能否在不按比例增加渲染与视觉推理的前提下扩展离策略经验收集，从而直接高效训练视觉策略。

### 二、技术方案（Method）
Echo是一个单阶段离策略视觉强化学习框架：将并行环境分为M个渲染环境和N-M个无渲染环境，前者用视觉策略πθ(o)收集带状态—观测配对的经验，后者用状态型辅助策略μψ(s)收集廉价无渲染经验；辅助策略通过带停止梯度的均方误差模仿当前视觉策略的无噪声动作，实现逆向蒸馏。共享特权评论家同时从渲染与无渲染转移中学习，使用EMA辅助策略提供续行动作构造TD目标，并以FastTD3的双分布评论家、截断双Q和目标策略平滑训练；视觉策略则在渲染配对回放上固定评论家参数，通过评论家对动作的梯度进行一阶更新。

### 三、结果（Result）
在Genesis的三个视觉控制任务和两个灵巧手操作任务上，与SDPG在相同评估配置下相比，Echo将达到参考回报的时间在三个运动任务上平均减少60%、在两个手部任务上平均减少56%；峰值平均回报分别提升62%和12%。两个手部任务在相同模拟器转移预算下也取得更高的平均回报，表明无渲染离策略经验可直接改善视觉策略。

### 四、结论（Conclusion）
这些初步结果表明，通过逆向蒸馏让状态型辅助策略跟踪并扩展视觉策略的经验收集，再以共享特权评论家进行离策略价值学习，是一条提升直接视觉强化学习效率的可行路径。Echo将经验收集规模与视觉计算成本解耦，同时避免传统特权教师带来的模仿差距，但结论仍限于当前初步评估配置。

### 五、方法论与关键技术细节
实现上，渲染流保留(s,o)配对存入D_nom，所有流的状态转移(s,a,r,s',d)进入共享回放D；动作加探索噪声并裁剪，时间限制截断保留自举而真实终止置d。辅助策略损失为||μψ(s)-sg[πθ(o)]||²，仅更新辅助策略；评论家使用目标网络和EMA辅助策略生成TD目标，视觉策略更新时冻结评论家。关键约束是只有视觉策略部署且仅用部署观测，无渲染转移不需要后继图像；局限性包括研究尚属初步、仅在Genesis的三类运动和两个手部任务及特定配置下比较，且仍需少量渲染环境和评论家训练开销。
