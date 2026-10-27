# Tiny Recursive Policy: Recursive Latent Refinement for Visuomotor Control

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Hakan Aktas, Cengiz Oztireli
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33288v1) · [PDF](https://arxiv.org/pdf/2610.33288v1)

## TLDR
TRP is a parameter-efficient behavior-cloning policy that maintains persistent latent context and recursively refines high- and low-level latent states with a shared module before decoding actions, improving long-horizon, context-dependent, and perturbation-robust visuomotor control with far fewer parameters than large generative baselines.

## Abstract
Behaviour cloning has become a powerful approach for robotic manipulation, but many modern policies reconstruct their internal representation from a fixed observation window at each prediction and do not maintain persistent latent context throughout execution. We introduce Tiny Recursive Policy (TRP), a parameter-efficient behaviour-cloning policy that combines persistent temporal state with recursive latent refinement. At each control step, TRP repeatedly updates high- and low-level latent states using a shared computation module before decoding an action sequence, and propagates the resulting state to subsequent predictions. We evaluate TRP across LIBERO-100, MetaWorld ML45, and the LIBERO-Mem benchmarks. TRP performs competitively across multi-task and few-shot settings and shows substantial gains on long-horizon and context-dependent tasks, while using significantly fewer parameters than large generative baselines. Execution-time perturbations show that reliance on the persistent carry increases with temporal-context demand, while training with carry perturbations substantially improves robustness to both carry and visual corruptions. Ablations reveal a strong interaction between persistent state and recursive refinement: the benefit of carry depends strongly on the amount of within-step computation, and the resulting performance cannot be explained by parameter count alone.


## 精读解读（中文）
### 一、研究动机
许多现代行为克隆策略在每个预测时刻仅从固定观测窗口重建内部表示，执行过程中不维护持久潜上下文，导致长时程和依赖历史上下文的任务表现受限。TRP 旨在用参数高效的方式同时引入持久时间状态与递归潜变量细化，提升视觉运动控制的上下文保持能力。

### 二、技术方案（Method）
TRP 是一种行为克隆策略：每个控制步以当前视觉观测为输入，并继承上一控制步的高层与低层潜状态；随后使用共享计算模块对高低层潜状态进行多次递归更新与细化，再解码出动作序列，并将更新后的潜状态传播到后续预测。训练采用行为克隆目标，并引入对持久携带状态的扰动训练以增强鲁棒性；推理时按控制步循环执行“观测输入—递归潜细化—动作序列解码—状态携带”。

### 三、结果（Result）
在 LIBERO-100、MetaWorld ML45 和 LIBERO-Mem 上，TRP 在多任务与少样本设置中表现有竞争力，并在长时程和上下文依赖任务上取得显著提升，同时参数量明显少于大型生成式基线。执行时扰动实验表明，任务对时间上下文需求越高，策略对持久携带状态的依赖越强；携带扰动训练还能显著提升对携带状态损坏和视觉损坏的鲁棒性。

### 四、结论（Conclusion）
TRP 表明持久时间状态与递归潜细化之间存在强协同：携带状态的收益高度依赖单步内计算量，且性能提升不能仅由参数规模解释。该工作为参数高效的视觉运动策略提供了兼顾上下文保持与计算复用的递归式行为克隆方案。

### 五、方法论与关键技术细节
关键实现点包括：以当前观测和上一控制步传播的高/低层潜状态为输入，使用共享模块进行多次递归更新后解码动作序列；训练中显式扰动携带状态以提升鲁棒性；消融显示持久状态收益与单步递归计算量强相关。摘要未给出具体网络尺寸、递归次数、损失权重、扰动强度及逐基准数值，需查阅全文复现；潜在局限是递归步数与共享模块设计会带来推理计算与调参约束。
