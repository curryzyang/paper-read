# Scaling Trusted Autonomy: Towards Generally Capable Verifiable Robots

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Benedict Quartey
- 机构：Brown University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00158v1) · [PDF](https://arxiv.org/pdf/2611.00158v1)

## TLDR
This thesis proposes a neurosymbolic framework that combines foundation-model-driven perception and learned visuomotor skills with explicit symbolic planning and evolving 3D scene representations to enable generally capable robots whose interpretations, actions, and world models can be verified and trusted.

## Abstract
Robots powered by foundation models are increasingly able to interpret open-ended language, recognize unfamiliar objects, and operate across diverse environments. Yet broader capability does not establish that a robot has understood a request, that its actions will produce the intended effects, or that its internal representation still corresponds to reality. Classical symbolic planning provides explicit structure for composition and verification, but traditionally depends on hand-engineered skills and representations. Learned policies can broaden the robot's repertoire, but provide weak guarantees about what will happen and why. This thesis argues that scaling trusted autonomy requires a neurosymbolic approach that unifies the generality of learned models with symbolic structure for robust robot behavior. It explores three complementary directions. First, LIMP uses foundation models and spatial reasoning to ground natural-language instructions in explicit task constraints and instruction-specific semantic maps, enabling task-and-motion planning while exposing the robot's interpretation for inspection. Second, REALM maintains an editable, photorealistic 3D Gaussian scene, predicts the consequences of planned manipulation, and locally reconciles the scene so that subsequent instructions obtain their grounding and planning geometry from an updated state. Third, PACTS learns visuomotor skills that jointly generate action trajectories and predictions of their symbolic effects, supporting skill composition, progress monitoring, and recovery through replanning. Together, these contributions preserve explicit structure for reasoning and verification while broadening how it is obtained, providing a foundation for generally capable robots whose behavior can be assessed under the assumptions of their models.


## 精读解读（中文）
### 一、研究动机
基础模型驱动的机器人已能理解开放式语言、识别陌生物体并跨环境作业，但能力的提升并不等于机器人真的理解了指令、动作会产生预期效果、内部表示仍与现实一致，由此形成“能力与保障”之间的缺口。经典符号规划提供了可组合、可验证的显式结构，但其应用长期依赖人工构造的技能与表示；学习策略虽能扩展技能库，却对“会发生什么、为什么”给出很弱的保证。因此论文主张，规模化可信自主需要神经符号路线，把学习模型的泛化性与符号结构的可检验性统一起来，并围绕意图、动作、世界三个接口组织研究。

### 二、技术方案（Method）
论文提出三个互补模块。LIMP 用基础模型与空间推理把自然语言指令转换为显式任务约束（含时序逻辑式的行为规约）与指令特定的语义地图，再交给任务与运动规划（TAMP）求解，使机器人对指令的解释可被外部检查。REALM 维护一个可编辑、照片级真实的 3D 高斯场景表示，对被规划的抓取、放置等操作预测其后果，并在执行后用新观测对高斯场景做局部一致性校正，使后续指令的落地与规划几何来自更新后的状态。PACTS 学习视觉运动技能，同时输出动作轨迹与对这些动作符号效果的预测，从而支持技能组合、执行进度监控以及失败后的重规划恢复。整体流程为：输入语言指令与感知观测，中间生成显式符号与几何表示，输出可被规划器检验的动作序列，形成“解释—规划—执行—校正”的闭环。

### 三、结果（Result）
论文报告的核心发现是三条路线都能在保留显式结构的前提下扩展可处理的任务范围：LIMP 能把开放式指令转成可检查的约束与指令特定语义地图，并直接支撑 TAMP 在含新物体、新指称的场景中完成规划；REALM 通过执行后的局部场景校正，使后续指令的落地不再依赖过时或静态的地图，从而在多步操作中维持世界表示与现实的一致性；PACTS 的符号效果预测可用于判断技能是否达成前置、后置条件，实现技能组合、进度监控与基于重规划的错误恢复。全文预览未给出具体数值指标，各章的量化对比与消融结果应以正文实验为准。

### 四、结论（Conclusion）
论文结论是，可信自主的关键并不在于用更强大的黑箱替换符号结构，而在于保留用于推理与验证的显式结构，同时拓宽其获取方式：形式化推理在模型内部给出性质保证，经验评估检验语言落地、控制与状态预测同真实环境的一致性，二者结合才能说明行为在何种假设下可信。该框架为“行为可被评估”的通用机器人提供了方法论基础。

### 五、方法论与关键技术细节
关键实现细节包括：以时序逻辑等形式化规约承载顺序、避让等约束并作为规划目标；语义地图按指令按需构建，避免预设封闭世界假设；世界模型采用可编辑的 3D 高斯泼溅表示，并做局部而非全局重建以控制开销；技能端联合预测动作轨迹与符号效果，并以闭环滚动方式监控进度。局限在于：所有保证都以动作模型与世界模型的假设为前提，若规约误解指令或模型转移与实际不符则结论失效；学习策略仍受演示数据覆盖范围与分布偏移制约；高斯场景的保真度、局部校正的触发条件与计算成本，以及向真实机器人的迁移都是实际约束。
