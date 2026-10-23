# Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jona Joy
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30197v1) · [PDF](https://arxiv.org/pdf/2610.30197v1)

## TLDR
Alpha is a fault-injection framework for LLM-driven embodied manipulation that, through matched comparison against a scripted oracle, shows physical, kinematic, and perceptual faults affect both planners equally while the LLM’s performance gap is caused entirely by planner-output corruption at the JSON serialization/validation interface rather than by a reasoning deficit.

## Abstract
Large language models (LLMs) are increasingly integrated into embodied robotic planning, yet standard benchmarks primarily evaluate end-to-end task completion in nominal environments, obscuring failure origins across the execution stack. We present Alpha, a systematic fault-injection and robustness-evaluation framework for LLM-driven manipulation in simulation. Alpha injects calibrated faults across perception (sensor lag), actuation (grip slip), kinematics (unreachable targets), and planning (planner-output corruption), alongside concurrent conditions. To separate physical vulnerabilities from planner sensitivities, we introduce a matched methodology pairing an LLM agent (Llama-3 via Ollama) against a deterministic Scripted Oracle planner across a balanced 150-episode matrix under identical seeds, geometries, and safety criteria. Across the matrix, the Oracle achieves 64.0% (48/75) success while the LLM achieves 44.0% (33/75) (paired McNemar p = 3.01 x 10^-4). Crucially, excluding planner-output corruption, performance across all physical and kinematic conditions is identical: 55.0% (33/60) for both planners with zero discordant pairs (McNemar p = 1.00). This demonstrates that physical actuator slip, kinematic reach boundaries, and perceptual staleness affect deterministic controllers and LLM planners equivalently. The performance gap is driven entirely by planner-output corruption (100% Oracle vs. 0% LLM), isolating the prompt-to-JSON serialization and validation interface rather than a cognitive reasoning deficit. We also audit 169 historical pilot attempts for transparency.


## 精读解读（中文）
### 一、研究动机
现有具身操作基准多评估名义环境下的端到端完成率，难以定位感知、规划、运动学与执行各层的故障来源；LLM 规划器的失败也缺少与确定性基线在相同条件下的反事实对照。Alpha 旨在通过系统故障注入和匹配评测，把物理/环境脆弱性与规划器接口敏感性分开。

### 二、技术方案（Method）
Alpha 在 PyBullet 仿真中构建 Brain/Body 执行链，通过 ChaosRoboticsWrapper 在四个边界注入校准故障：感知传感器滞后 F1、执行抓握滑移 F2、运动学不可达 IK 目标 F3、规划输出 JSON 损坏 F4，并设置 F1+F2 并发条件；故障强度由 I∈{0.33,0.66,1.00} 参数化。评测采用 150 个平衡 episode（LLM 与 Scripted Oracle 各 75），二者共享随机种子、场景几何、物理参数和安全阈值；LLM 为 Ollama 上的 Llama-3，Oracle 直接生成无碰撞抓放轨迹并绕过 JSON 序列化。执行中每步以 240 Hz 安全监控接触力、工作空间和去重事件，记录遥测并统计成功率、校验拒绝和事件。

### 三、结果（Result）
全矩阵 Oracle 成功率 64.0%（48/75），LLM 44.0%（33/75），配对 McNemar p=3.01×10^-4。排除 F4 后，两者在所有物理/运动学/感知条件上完全一致，均为 55.0%（33/60），不一致对为零，McNemar p=1.00；性能差距完全来自规划输出损坏条件下 Oracle 100% 对 LLM 0%。

### 四、结论（Conclusion）
物理执行滑移、运动学可达边界和感知陈旧对确定性控制器与 LLM 规划器影响等价，LLM 的主要脆弱点不是认知推理缺陷，而是 prompt 到 JSON 的序列化与校验接口。因此具身 LLM 评测应报告分层故障归因，并优先增强结构化输出解析、校验失败恢复与安全降级，而非仅优化端到端成功率。

### 五、方法论与关键技术细节
关键实现包括 3000 N 暴力接触阈值、工作空间 x∈[0.15,0.95] m、y∈[-0.45,0.55] m、z∈[0.55,1.25] m，以及 15 个仿真步（约 0.0625 s）的事件去重窗口；F1 因初始历史缓冲仅 0.500 s 而强度饱和，空间陈旧约 0.025 m，F3 偏移 0.03+0.27I 且放置误差可 >0.17 m，F4 以 P=0.20+0.80I 注入并使 Pydantic 校验失败后中止为空计划。方法在 PyBullet DIRECT 仿真、单一 Llama-3/Ollama 与 150 episode 小矩阵上验证，未训练模型，存在仿真到现实、样本规模和 F1 饱和等局限；另审计了 169 次历史 pilot 尝试以降低丢弃偏差。
