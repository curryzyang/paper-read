# Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Awomo-PhysicalRSI Team, Danjiao Ma, Enhui Ma, Haohan Liu, Heng Jia, Hui Shan, Jianhua Xu, Jiahuan Zhang, Jiangdi Xu, Kaiwen Guo, Kaicheng Yu, Linwei Zhang, Liyang Jin, Maochun Luo, Pengyao Niu, Shiwen Li, Shuangyu Feng, Tong Zhang, Tianheng Wang, Xin Wang, Xiangru Huang, Yongqiang Huang, Zhaozhi Wang, Zijian Ma
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02274v1) · [PDF](https://arxiv.org/pdf/2610.02274v1)

## TLDR
Awomo-SimDataEngine is an agentic, graph-native system that generates simulation-ready interactive assets and image- or text-driven scenes and converts them into replayable robot demonstrations, improving cross-simulator policy training on MuJoCo-based LIBERO-Plus from 77.17% to 89.43% success when co-trained with Isaac Sim data.

## Abstract
Generating useful robot-training data requires more than visually plausiblescenes: objects must support interaction, placements must remain physicallyvalid, and tasks must admit repeatable execution. We present\textbf{Awomo-SimDataEngine}, an agentic system that connects asset and scenegeneration to robot demonstration synthesis. Shared asset services providerigid and articulated objects, including structure-grounded part and jointgeneration with ISArt. Scene generation supports two complementary routes:Unravel reconstructs editable scenes from images, while SimForge buildssingle-room and multi-room environments from text. A graph-native harnesscoordinates construction, validation, andbounded repair, routing failures to the responsible module while retainingunaffected scene state. PolicyForge binds validated worlds to tasks and robotembodiments to produce replayable demonstrations. Evaluations cover assetgeometry, scene quality, and downstream policy learning. On MuJoCo-basedLIBERO-Plus, co-training with Isaac Sim demonstrations improves the overallsuccess rate of a World-Action Model (WAM) from $77.17\%$ to $89.43\%$. Goal and spatialsuccess improve by $31.66$ and $6.25$ percentage points, respectively.These results support the utility of the generated data for cross-simulatorpolicy training, with more limited gains on long-horizon tasks.


## 精读解读（中文）
### 一、研究动机
机器人学习需要可交互、物理有效且可重复执行的训练数据，仅有视觉逼真的场景不足，因为网格可能碰撞几何无效、关节错误、放置不稳定或初始状态不可回放。现有资产生成、场景构建和演示合成能力割裂，缺少对物体身份、坐标系、物理表示、任务要求和验证结果的一致依赖管理。Awomo-SimDataEngine 旨在将资产生成、场景生成和机器人演示合成贯通，并通过有界修复提升仿真就绪世界与下游策略训练数据的可用性。

### 二、技术方案（Method）
输入为文本描述、单视图图像和可选任务请求，至少提供文本或图像；资产生成通过检索、图像到3D、专用生成或程序建模获得候选，ISArt 将单物体图像转为纹理部件网格、URDF 运动树及关节原点/轴/范围，经几何-运动规划、结构约束部件生成、智能体关节绑定和仿真验证完成。场景生成有两条路线：Unravel 以免训练 plan-edit-verify 循环逐步移除物体，利用裁剪和掩码、固定相机点图与未编辑锚点对齐、仅在新表面暴露处融合并按像素和移除轮次归属实例，再按逆移除顺序从房间外壳重组，做约束配准、支撑感知沉降和视觉审计；SimForge 从文本规划房间几何与物体布置，支持单房间和多房间。Graph-Native Harness 用执行图跟踪类型化状态、验证证据、责任模块、修复范围、尝试预算和检查点，按阶段依赖使受影响记录失效并把失败路由给责任模块进行有界修复；PolicyForge 将验收世界绑定到任务、机器人 embodiment 和重置规范，用脚本或运动规划教师于 Isaac Sim 执行，输出同步图像、本体感知和动作，保留成功 episode 作为演示，并通过场景/任务变体、物体替换、初始状态和语言增强扩展数据。所有资产分支共享候选验证、规范化变换、碰撞构建、物理增强与来源追踪，世界须通过硬验证和仿真器打包才被接受。

### 三、结果（Result）
ISArt 在60个物体上取得部件几何 CD 0.163，优于 TRELLIS.2+P3-SAM+X-Part 组合基线的0.268；Unravel 在160个物体上将盲评人类资产保真度从4.9提升至8.6。文本场景在179个房间提示和31个多房间提示上按 SceneEval 与 SceneSmith 协议分别评估。基于 MuJoCo 的 LIBERO-Plus 上，用 Isaac Sim 演示做 SimData-Ultra 协同训练，使 World-Action Model 总体成功率从77.17%提升到89.43%，即12.26个百分点，目标与空间泛化分别提升31.66和6.25个百分点；该结果取自13K步预算内按总体成功率选择的最佳检查点，长时程任务增益较小。

### 四、结论（Conclusion）
结果表明 Awomo-SimDataEngine 生成的数据对跨仿真器策略训练有实用价值，最大提升出现在目标泛化。系统把资产结构、图像场景证据、有界修复和经校验的演示合成连成统一工作流，但实验未分离各生成器或增强的独立贡献，也未证明真实世界迁移。长时程任务增益有限，说明需要更丰富的顺序任务监督；世界构建、episode 成功与基准策略成功仍是不同验证结果。

### 五、方法论与关键技术细节
关键实现点包括以文本/单图/任务请求为输入、ISArt 的结构规划优先与运动学校验、Unravel 的移除顺序仅作为局部遮挡证据而非全局支撑或深度顺序、固定相机点图按未编辑锚点对齐与像素级来源记录、SimForge 的文本到单/多房间规划、Graph-Native Harness 的类型化状态与有界重试/检查点/依赖失效机制，以及 PolicyForge 在 Isaac Sim 中生成同步观测与动作并保留成功演示。评测数据规模为60个物体、160个物体、179个房间提示和31个多房间提示，下游预算为13K步并按总体成功率选最佳检查点，LIBERO-Plus 在 MuJoCo 上评测。局限包括未做多视图重建、无法从无约束单图唯一恢复度量几何、单图路线依赖固定相机及局部遮挡顺序、未隔离各组件贡献、未验证真实世界迁移，且 harness 效率或 orchestrator 学习未被独立证明。
