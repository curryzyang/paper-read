# RoboACE: Adversarial Co-Evolution for Robot Self-Improvement

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Delin Zhao, Zhengrong Yue, Junlin He, Yali Wang
- 机构：SIAT
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13034v1) · [PDF](https://arxiv.org/pdf/2611.13034v1)

## TLDR
RoboACE is an adversarial co-evolution framework that jointly revises a curriculum harness—which selects capability-revealing practice—and an execution harness—which learns reusable robot-control improvements—around frozen foundation models, yielding stronger self-improving robot deployments that outperform evaluated controllers and agent systems across LIBERO benchmarks.

## Abstract
Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the search for new weaknesses unchanged. Useful practice depends on the agent's current capabilities, so the procedure that chooses practice must also be revisable. We present RoboACE (Robot Adversarial Co-Evolution), a framework that jointly evolves curriculum and execution harnesses around frozen foundation models. The curriculum harness uses accumulated capability evidence to propose informative challenges, while the execution harness responds with reusable revisions that expand execution capabilities. Alternating updates hold one side fixed as the other changes, and admitted challenges form fixed snapshots for comparing execution revisions. Starting from a compact set of LIBERO practice conditions, the resulting frozen deployment outperforms the evaluated controllers and agent systems across four LIBERO-family panels. On LIBERO-PRO, it reaches 74.0% success, exceeding the initial deployment by 15.0 percentage points and direct execution by its VLA controller by 13.5 points. Case studies document changes to evidence-guided practice selection, drawer-skill grounding, and controller intervention.


## 精读解读（中文）
### 一、研究动机
机器人智能体虽能利用执行反馈改进技能、规划与恢复策略，但固定练习源不会改变对新弱点的搜索；有效练习取决于当前能力，因此选择练习的程序本身也必须可修订，才能形成持续自我改进闭环。

### 二、技术方案（Method）
RoboACE围绕冻结基础模型联合进化课程harness与执行harness：harness包含提示、技能、工具、接口和可读记忆；每轮先固定执行端，课程智能体读取能力画像P_k，保留、替换或新增练习条件，经物理有效性、可达性和Judge一致性准入后形成固定任务快照T_k；随后固定快照，执行智能体用代码技能与π0.5 VLA控制尝试任务，优化器依据结果、轨迹和工具反馈诊断并独立测试候选修订，按成功、回归、复用和成本决定采用Candidate或保留Stable；执行证据经Experience Consolidator汇总为P_{k+1}，Strategic Advisor定期跨轮审查方向。实现使用GPT-6.1 Terra、SAM 3和冻结π0.5，30个练习条件、最多40个内部基准条件、27轮记录，不训练LLM或VLA权重。

### 三、结果（Result）
最终冻结部署在四个LIBERO族面板上优于所评估控制器与智能体系统；相对初始部署，LIBERO提升35.5个百分点、LIBERO-Plus提升30.0、LIBERO-PRO提升15.0、LIBERO-X提升11.0。LIBERO-PRO达到74.0%成功率，比初始部署高15.0个百分点，比同一VLA控制器直接执行高13.5个百分点。案例还记录了证据引导的练习选择、抽屉技能落地和控制器介入的变化。

### 四、结论（Conclusion）
RoboACE给出了一个可运行的机器人自我改进实现：课程选择程序与执行软件都可持久修订，而基础模型权重保持冻结；最终部署在保留LIBERO及三个迁移面板上均取得提升，说明联合对抗进化能带来可复用的系统级收益。研究结果刻画了一条开发轨迹及其部署表现，而非完整官方基准结论。

### 五、方法论与关键技术细节
关键实现细节包括：开发仅使用LIBERO条件，保留LIBERO面板与条件不相交，LIBERO-Plus、LIBERO-PRO和LIBERO-X不参与开发；每面板200条件，每回合8000个20Hz控制步，成功由环境原生谓词判定，超时和基础设施错误计失败。交替更新与准入快照保证课程提案和执行修订可比，准入不预筛VLA难度、也不保证完整可执行解；最终评估不反馈进循环。局限性是结果仅代表单条开发轨迹，四面板为固定子集而非完整官方协议，且未训练或微调LLM或VLA权重。
