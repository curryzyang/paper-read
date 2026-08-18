# hint$^2$: Hierarchical World Models for Inference-Time Temporal Logic Guidance

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Moritz Zoellner, Anastasios Manganaris, Ahmed H. Qureshi, Rohan Paleja
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13678v1) · [PDF](https://arxiv.org/pdf/2608.13678v1)

## TLDR
hint² uses hierarchical world models—a high-level model for LTL automaton progress and a low-level model for local safety—to guide short-horizon diffusion policies at inference time toward satisfying complex temporal logic specifications.

## Abstract
A central goal of robot learning is to enable robots to execute rich instructions specified at runtime. Large-scale language-conditioned policies have made substantial progress toward this goal, yet still struggle with temporal structure and safety constraints. Linear Temporal Logic (LTL) provides a powerful language to express complex, non-Markovian instructions. However, guiding learned manipulation policies toward LTL satisfaction remains challenging because modern policies generate short-horizon action chunks and replan in closed loop, while almost all LTL specifications are evaluated over long-horizon trajectories. In this paper, we introduce hint$^2$, a method for guiding short-horizon policies toward satisfying complex LTL specifications at inference time using hierarchical world models. Our key idea is to derive two separate guidance objectives using each world model's abstraction level. A high-level model predicts future action-induced transitions in task-relevant atomic propositions to guide progress through the LTL automaton, while a low-level dynamics model predicts immediate state evolution for accurate local safety guidance. Our results show that hint$^2$ overcomes the limitations of current LTL-guided diffusion methods, outperforms existing inference-time steering methods in CALVIN, and successfully completes instructions with complex liveness and safety constraints more elegantly than language-conditioned alternatives. Finally, we demonstrate that hint$^2$ can handle complex instructions on a real UR5e manipulator.


## 精读解读（中文）
### 一、研究动机
现代语言条件策略虽能执行运行时指令，但难以处理具有时间结构和安全约束的长时序任务。线性时序逻辑可以表达复杂非马尔可夫指令，但现有LTL引导方法要么在训练时条件化受限于数据扩展，要么在推理时引导需要全轨迹预测，面临复合误差和短视策略与长时规格之间的地平线不匹配问题。因此需要一种在不修改预训练策略的前提下，推理时引导短视策略满足LTL规格的方法。

### 二、技术方案（Method）
提出hint^2，使用分层世界模型在推理时引导短视扩散策略。高电平世界模型以当前状态和短视动作块为输入，预测未来N个不同标签序列中每个原子命题的边际概率，结合LTL公式对应的确定性Büchi自动机，在stutter-invariant假设下精确计算自动机状态分布，并利用自动机势向量构造引导目标以推动朝向接受状态前进。低电平世界模型预测短期状态演化，用于计算STL鲁棒性梯度，为安全约束提供局部精确引导。推理时从无条件扩散策略采样动作块，将两个引导目标的梯度加权联合用于选择或偏置动作块，使执行轨迹满足LTL规格。

### 三、结果（Result）
在CALVIN环境中，hint^2克服了现有LTL引导扩散方法只能处理短时安全过滤的局限，优于现有推理时引导方法。相比语言条件策略，hint^2能够更优雅地完成具有复杂活性和安全约束的长时序指令，并在真实UR5e机械臂上验证了其对复杂指令的可行性与泛化能力。

### 四、结论（Conclusion）
hint^2通过引入规格诱导的自动机抽象作为高电平规划层，结合低电平动力学模型，有效弥合了短视策略与长时LTL规格之间的地平线鸿沟。该方法无需重新训练策略或修改训练时条件，即可在推理时将任意LTL规格（活性和安全性）注入预训练扩散策略，为一般化机器人策略提供了一种可扩展的时序逻辑引导框架。

### 五、方法论与关键技术细节
关键点包括：LTL公式被转换为决定性Büchi自动机，并定义自动机势向量v_q = max_{q'∈F} γ^{d(q,q')} 用于衡量到接受状态的最短距离；高电平模型假设各原子命题独立以计算符号概率，且依赖环境相关stutter-invariance条件（同一标签重复不改变自动机状态）从而消除段时长影响；低电平模型使用STL鲁棒性梯度处理需要精确几何的安全约束。推理时采用类似分类器引导的梯度加权方式，从非条件扩散策略中采样动作块。局限性包括：高电平模型需要预训练以预测命题转移，低电平模型对复合误差仍敏感，且方法依赖环境标签函数和LTL公式的可翻译性（限定于recurrence类）。
