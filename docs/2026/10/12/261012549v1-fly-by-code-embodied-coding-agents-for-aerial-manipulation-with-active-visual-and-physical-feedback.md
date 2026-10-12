# Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Jaewoo Lee, Jeongyeon Seo, Sihyun Cho, Gyeongrak Choe, Yutong Wang, Bavin Saravanan, Jia-Bin Huang, Furong Huang, Sebastian Scherer, Guanya Shi, H. Jin Kim, Seungjae Lee, Dongjae Lee
- 机构：Seoul National University, University of Maryland, College Park, Carnegie Mellon University, All Purpose AI, Kyung Hee University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12549v1) · [PDF](https://arxiv.org/pdf/2610.12549v1)

## TLDR
Fly-by-Code introduces Active Feedback, a post-execution “View and Probe” diagnostic stage in which embodied coding agents generate executable programs to actively acquire missing visual or physical evidence in simulation, improving aerial manipulation success and enabling transfer to real-world hardware.

## Abstract
Embodied coding agents construct robot policies from natural-language instructions by generating executable programs and refining them from execution feedback. This refinement assumes that execution feedback reveals whether the task succeeded and, after a failure, provides sufficient evidence to guide program revision. Aerial manipulation violates this assumption in two ways. Payload constraints restrict onboard camera coverage and leave task-critical outcomes outside the robot's view (partial observability), while strong dynamic coupling and limited control margins make physical interactions fragile (limited interaction robustness) and leave failure causes unresolved. Re-examining the same feedback cannot recover observations that were never collected or separate failure causes that the available evidence does not distinguish. To acquire this missing evidence, we introduce Active Feedback (AF), an active "View and Probe" framework. When execution feedback leaves unresolved questions, the agent synthesizes a separate diagnostic program that runs in simulation to inspect unseen outcomes from informative viewpoints (View) or test hypotheses about failure causes through targeted physical interactions (Probe). Across six simulated aerial manipulation tasks with 60 trials per condition, AF reduces false completion declarations from 25 to 5 and raises final task success from 31.7% to 75% compared with terminal feedback under the same coding-agent configuration and task-execution limit. Using shared robot APIs, task programs refined with AF in simulation run on a physical aerial manipulator without task-program source-code modification and complete multi-stage manipulation tasks in the real world. These results show that executable diagnosis fills gaps in execution feedback for embodied coding agents, improving both completion assessment and program refinement in aerial manipulation.


## 精读解读（中文）
### 一、研究动机
具身编码智能体通过生成可执行程序并依据执行反馈迭代修正来构建机器人策略，但这一范式隐含假设反馈能揭示任务是否成功、并在失败后提供足以指导修改的证据。空中操作从两方面打破该假设：载荷限制压缩机上相机视野，使关键结果落在视野之外（部分可观测，造成“结果观测缺失”）；强动态耦合与有限控制裕度使物理交互脆弱，失败原因难以区分（交互鲁棒性受限，造成“失败原因未决”）。重复检视同一批反馈无法找回从未采集的观测，也无法区分现有证据无法分辨的失败原因，因此必须主动获取新证据。

### 二、技术方案（Method）
Fly-by-Code 在仿真程序精炼循环中引入 Active Feedback（AF）这一显式的“执行后诊断阶段”。输入是自然语言任务指令、执行日志、终端观测与语义地图摘要；智能体先写出调用共享机器人 API 的任务程序并执行，环境在诊断前已记录任务得分。随后智能体针对本次尝试的具体不确定性，编写一个独立的诊断程序（同一套 API，如 look、get_observation、goto_pose、open_gripper、release_and_hold、report），执行两类诊断动作：View 即飞行到能回答特定问题的信息性视角（必要时用语义地图查询定位物体），返回图像及智能体自写的检视说明与分割深度测量等控制台输出；Probe 即执行以信息价值而非任务进度为目标的定向物理交互（如不同接触点的推、门铰链测试、尝试举升以探测载荷能力）并测量响应。诊断程序从任务程序留下的状态出发，可定位到失败发生的那一步而无需重放。最后智能体综合诊断证据与原始执行日志，输出 FINISH 或 REGENERATE；环境重置物理状态但诊断信息保留在上下文中，用于下一轮任务程序修正。整个流程在同一提示词下跨任务通用，诊断程序按每次尝试单独合成。

### 三、结果（Result）
在六个仿真空中操作任务、每种条件 60 次试验的设定下，相同编码智能体配置与相同任务执行次数上限下，AF 将虚假完成声明从 25 次降至 5 次，将最终任务成功率从 31.7% 提升至 75%。案例层面，2-Objects Pick-and-place 中任务程序报告两件工具均已放置，View 诊断从俯视与地面附近视角发现工具实际掉落，智能体据此拒绝成功声明并选择 REGENERATE；Align 任务中连续推动使纸箱持续旋转，Probe 比较六个接触点的推动响应，下一版任务程序把测量结果转化为推-响应模型来选取接触位置。由于仿真与硬件共享任务级 API，经 AF 在仿真中精炼的任务程序无需修改源码即可部署到实体空中机械臂，并在初始位姿与朝向波动的条件下重复完成 2-Objects Pick-and-place 与 Cabinet 两阶段（含多阶段）操作任务。

### 四、结论（Conclusion）
结果表明，可执行诊断能够填补具身编码智能体执行反馈中的证据空缺，同时改善完成判定与程序修正：AF 用一次性的诊断程序把“无法从既有反馈回答的问题”转化为可执行的主动观测或物理探测，显著降低误报成功并提升最终成功率，且仿真精炼的程序可零源码修改地迁移到真实空中机械臂，验证了该范式的 sim-to-real 可用性。

### 五、方法论与关键技术细节
实现基于 Isaac Lab、在 AM-Bench 上扩展的六个任务，仿真体为全向空中机械臂，共享执行后端负责碰撞感知的全身运动规划并跟踪生成轨迹；智能体与诊断程序共用同一套高层机器人 API 与同一提示词，但因任务得分已在诊断前记录、且下一轮尝试前环境重置，诊断动作不计入任务收益，从而允许 Probe 执行诸如超载举升这类任务执行中不应做的动作。诊断证据以图像+智能体自写检视笔记+控制台测量（如分割深度物体位置、接触响应）形式回流到上下文，支持 View 与 Probe 在同一程序内组合。关键约束与局限：诊断在仿真中进行（真实世界仅做零修改部署验证），依赖语义地图与深度分割等感知模块质量，效果受仿真动力学与真实差异影响，未给出诊断程序生成的Token/时间开销、超参或复杂度分析。
