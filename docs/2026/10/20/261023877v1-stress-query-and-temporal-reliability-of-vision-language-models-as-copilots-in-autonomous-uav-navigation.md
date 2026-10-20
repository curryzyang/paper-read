# Stress-Query and Temporal Reliability of Vision-Language Models as copilots in Autonomous UAV Navigation

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Hiago Sodre, Sebastian Barcelona, Vincent Sandin, Pablo Moraes, Andre S. Kelbouscas, Ricardo B. Grando
- 机构：Technological University of Uruguay
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23877v1) · [PDF](https://arxiv.org/pdf/2610.23877v1)

## TLDR
This paper benchmarks vision-language models as asynchronous UAV navigation copilots under stress and shows that mid-weight architectures best balance inference latency and reasoning accuracy, avoiding lightweight hallucinations and heavyweight trajectory overcorrections across hardware profiles.

## Abstract
Integrating Vision-Language Models (VLMs) into autonomous UAV navigation enables high-level semantic reasoning but introduces critical temporal bottlenecks that can destabilize flight control. This paper presents a systematic benchmark that evaluates the operational trade-offs among model scale, hardware constraints, and flight reliability. By subjecting the system to extensive stress tests on both a high-performance workstation and a constrained integrated-graphics laptop, we isolate the kinetic impact of inference latency against reasoning accuracy. Our findings reveal a performance dichotomy: lightweight models struggle with structural hallucinations that break deterministic state machines, while heavyweight models induce trajectory overcorrections due to inference lag. We demonstrate that a mid-weight architecture strikes the optimal balance, successfully rehabilitating navigation in degraded environments without compromising real-time stability across different hardware profiles.


## 精读解读（中文）
### 一、研究动机
将视觉语言模型引入无人机自主导航可提供高层语义推理，但模型推理延迟会破坏实时控制回路，导致轨迹偏差甚至碰撞；现有研究缺乏对模型规模、硬件约束与飞行可靠性之间定量权衡的系统评测。本文旨在识别VLM作为无人机副驾驶时的时序可靠性边界，并回答多大模型规模能在语义恢复与实时稳定之间取得最优平衡。

### 二、技术方案（Method）
论文构建PX4 Autopilot、ROS 2 Humble与Gazebo Harmonic的高保真SITL测试台，采用快慢解耦的混合FSM-VLM架构：30-50 Hz确定性有限状态机用OpenCV提取线条和门等快速视觉基元并经MAVROS发送速度设定点，异步VLM经Ollama在本地接收周期相机帧并仅输出预定义JSON模式。系统对格式错误和逻辑错误分别校验，失败输出被FSM丢弃，并在推理等待期触发自适应降速和延迟感知回溯。实验比较Moondream 1.8B、LLaVA-LLaMA3 8B与LLaMA 3.2 Vision 11B，在RTX 4070 Ti 12GB高性能工作站和RTX 4050 6GB受限笔记本上运行；以Mission 1为基线，将异步查询间隔从5 s到30 s分档，每条件重复5次，每模型配置共30次自主飞行，并记录推理延迟、最大轨迹误差、JSON格式稳定性和任务成功率，同时用TRB=e_max/v_UAV量化可恢复时间边界，室内走廊取e_max约2.5 m、v_UAV约0.5 m/s，得到TRB约5 s。

### 三、结果（Result）
实验显示明显的性能二分：轻量Moondream在边缘端平均延迟约2.39 s、最大误差约0.75 m，但格式稳定性仅约16.5%，结构化幻觉会破坏确定性状态机；重型LLaMA 3.2 11B在云端延迟约3.31 s、格式稳定性100%、最大误差约0.80 m，但在边缘端延迟约31.4 s、最大误差约35.19 m，远超约5 s的TRB并引发轨迹过修正或碰撞。中量级LLaVA-LLaMA3 8B在云端延迟约3.28 s、格式稳定性约99.5%，在语义恢复与实时性之间表现最均衡；但边缘端约11.54 s的延迟和约14.56 m误差说明其部署仍受TRB约束。

### 四、结论（Conclusion）
论文证明VLM用于无人机闭环导航时，时序延迟而非单纯语义精度是决定系统生存性的首要因素；过轻模型因结构化幻觉破坏FSM，过重模型因推理滞后造成轨迹过修正，中量级架构在可用算力下能兼顾语义恢复与实时稳定。作者据此提出以TRB为平台和场景相关的部署判据，要求推理延迟低于可恢复边界，并为不同硬件配置下的VLM规模选择提供经验蓝图。

### 五、方法论与关键技术细节
关键方法细节包括：以JSON模式作为VLM与FSM之间的严格结构契约，将失败分为格式错误和逻辑错误并直接丢弃无效输出；通过异步查询、自适应降速和延迟感知回溯缓解推理窗口内的位置漂移；用TRB=e_max/v_UAV把空间可恢复性与推理延迟联系起来，实验中TRB约5 s，因此边缘端11B的31 s延迟必然越界。评测覆盖Mission 1至多阶段任务及Full Run，查询间隔5-30 s、每条件5次重复，主要指标为平均延迟、最大误差、格式稳定性和成功率。局限在于TRB依赖具体平台和场景，e_max与速度近似常数，结果主要来自SITL仿真而非真实飞行，任务矩阵和硬件配置有限，且量化与VRAM瓶颈会显著影响边缘延迟。
