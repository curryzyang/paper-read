# ArcFlow: Training Flow Policies for Multiple Solver Budgets

- 区域：精读区
- 排名：1
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Hieu Tran, Hong Yu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28788v1) · [PDF](https://arxiv.org/pdf/2610.28788v1)

## TLDR
ArcFlow is a deployment-aware training algorithm that trains one flow-matching policy across a range of solver budgets using action-aligned supervision, budget exposure, and worst-budget checkpoint selection, achieving stronger low-step control than baseline flow policies across most tasks.

## Abstract
Flow-matching policies adjust inference cost through the number of solver steps, but reinforcement learning at a single fixed solver budget can hide degradation at cheaper deployment budgets and even erase useful one-step behavior present in a pretrained policy. We introduce Action-Ratio-Clip Flow (ArcFlow), a deployment-aware algorithm for training one flow policy across a specified range of solver budgets. ArcFlow combines action-aligned supervision, budget exposure, and worst-budget checkpoint selection. For reconstruction objectives, its bridge aggregates temporal probes into one surrogate ratio and one PPO-style clip per action, with a boundary residual exactly equal to deployed one-step reconstruction error. Cycling exposes the shared field to the deployment range, and selection optimizes its performance floor. For native velocity objectives, multi-budget endpoint supervision applies the same principle without replacing the native update. Both realizations preserve the architecture and deployment-time cost. Across DM Control, manipulation, and locomotion, ArcFlow attains the highest mean one-step return among five flow-policy baselines on 25 of 30 tasks under each method's reported training settings. Component studies identify complementary improvements from boundary supervision, the fixed-grid bridge, budget exposure, and deployment selection. These results establish deployment-budget-aware training as an effective route to strong low-step control with one policy serving multiple inference costs.


## 精读解读（中文）
### 一、研究动机
Flow-matching 策略可通过增减求解器步数调节推理成本，但只在单一固定求解预算上做强化学习，可能掩盖更低部署预算下的性能退化，甚至抹掉预训练策略已有的一步生成能力。因此需要一种面向部署预算的训练方法，使同一个流策略在指定的一整套求解器预算上都具有可用性能。

### 二、技术方案（Method）
ArcFlow（Action-Ratio-Clip Flow）在预训练流策略与给定预算区间上做部署感知训练：对重构型目标，将同一动作在时间/求解器探针上的监督聚合为一个动作级代理比率，并只做一次 PPO 风格裁剪，同时加入边界残差项，该项精确对应部署时一步重构误差；训练中循环暴露不同预算（固定网格/预算 cycling），并以最差预算表现选择检查点。对原生速度目标，则采用多预算端点监督实现同一原则，不替换原有更新；推理时仍用原流策略架构和标准求解器，仅改变步数，不增加部署成本。

### 三、结果（Result）
在 DM Control、操作与 locomotion 任务上，按各方法报告的设置评估，ArcFlow 在 30 个任务中的 25 个取得五种流策略基线中最高的平均一步回报；消融/组件研究显示边界监督、固定网格桥接、预算暴露和部署式检查点选择带来互补提升，并支持一个策略服务多个推理成本。

### 四、结论（Conclusion）
结果表明，部署预算感知训练是获得强低步控制性能的有效路径：它避免单预算 RL 对廉价部署预算的忽视，在保持架构与推理成本不变的前提下，用单个流策略覆盖多个求解器预算。

### 五、方法论与关键技术细节
关键实现包括：以预训练流策略为初始化，在指定预算集合上采样/循环训练，输入为环境交互或轨迹中的状态-动作及预训练流策略；重构目标使用时间探针聚合的动作级 surrogate ratio 与单次 PPO clip，边界残差锚定一步重构误差；原生速度目标使用多预算端点监督；检查点按最差预算性能（性能下限）选择。方法不改变网络架构或部署时求解器成本，但依赖预设预算范围与探针/裁剪等超参，摘要未给出具体数值；实验结论基于所报告训练设置和 30 个任务的一步回报均值。
