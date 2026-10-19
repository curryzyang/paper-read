# Predicting Privileged Information Effectiveness for On-Policy Self-Distillation

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Kaijian Zou, Emiliano Penaloza, MohammadHossein Rezaei, Anisha Gunjal, Mohit Raghavendra, Lu Wang, Yunzhong He, Anas Mahmoud
- 机构：Scale AI, University of Michigan, Mila
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22512v1) · [PDF](https://arxiv.org/pdf/2610.22512v1)

## TLDR
A systematic study of privileged information (PI) in on-policy self-distillation shows that information-dense trajectories and PI from more capable generators yield larger gains, while error-step KL contrast can predict and select effective PI before training and effective PI also complements GRPO.

## Abstract
On-policy self-distillation (OPSD) enables large language models (LLMs) to learn from privileged information (PI) without a separate teacher model. However, prior work largely treats PI as a fixed design choice, leaving the effects of its content and construction poorly understood. This challenge is particularly important in multi-turn agentic settings, where trajectories contain actions, observations, and reasoning that can be transformed into PI in many ways. We systematically evaluate 16 PI configurations across three multi-turn agentic benchmarks and three student models that vary in scale and reasoning mode. We find that PI effectiveness depends on its content, generation source, and the student model. Information-dense trajectories and PI produced by more capable generators generally yield larger gains, whereas thinking models benefit less consistently. To assess PI before training, we compare PI utility with two KL-based metrics: sampled-token reverse KL ($D$) and error-step KL contrast ($Δd^{-}_{\mathrm{err}}$). The KL-based metrics track post-training performance more consistently than PI utility, which can be distorted by information leakage. Empirically, selecting each task's PI by $Δd^{-}_{\mathrm{err}}$ also improves post-training performance over random selection, most when the PI candidates differ widely. Finally, effective PI remains beneficial when combined with GRPO, allowing the combined objective to outperform a strong GRPO baseline. Overall, our results provide practical guidance for constructing and evaluating PI in OPSD training.


## 精读解读（中文）
### 一、研究动机
OPSD 可以让大语言模型在不单独引入教师模型的情况下，从特权信息（PI）中学习，但已有工作通常把 PI 当作固定设计选择，较少系统理解 PI 的内容与构造方式如何影响多轮智能体任务中的训练效果。尤其轨迹中包含动作、环境观察和推理，可被转换成多种 PI，因此亟需回答何种 PI 更有效、能否在训练前评估 PI 质量，以及有效 PI 能否与 GRPO 等强化学习目标结合。

### 二、技术方案（Method）
论文在 ALFWorld、AppWorld 和 τ²-retail 三个多轮智能体基准上，使用 Qwen3-4B-Instruct、Qwen3-4B-Thinking 和 Qwen3-30B-A3B-Instruct 三种学生模型，系统评估 16 种 PI 配置，包括仅动作、动作加观察、动作加推理、动作加观察加推理四类参考轨迹，以及 Summary、Skill、Checklist 三类提示，并比较 GLM-5.2、Qwen3.7-Plus 与学生自生成等来源。训练采用 OPSD：学生采样轨迹后，以同一模型在 PI 条件下的策略作为停止梯度的教师，最小化学生到 PI 条件教师的反向 KL，并在 SkyRL 中实现，以 pass@1 的最佳三检查点窗口评估。为在训练前评估 PI，作者比较 PI utility、采样 token 反向 KL D 和误差步骤 KL 对比 Δd⁻err，后者用 judge 标注失败轨迹中的错误步骤，并以同任务、同步骤位置的匹配基线校正后衡量 PI 对错误 token 的抑制强度。离线指标在训练或开发任务上计算，与最终评估集分离。

### 三、结果（Result）
结果显示，信息密集的轨迹型 PI 通常优于压缩提示，给 Instruct 学生加入环境观察常带来额外收益，但给 Thinking 模型加入教师推理可能反而损害性能；Skill 提示因包含错误分析和可复用策略，往往是最强提示格式。更强大的生成器通常产生更有效的 PI，尤其对提示格式影响明显，GLM-5.2 在 4B-Instruct 的 21 次比较中赢下 20 次，ALFWorld 提示上领先可达 36.0 分，而轨迹格式差距在 3.2 分以内。离线指标方面，KL 类指标比 PI utility 更稳定地跟踪训练后表现，PI utility 会受信息泄漏扭曲；按 Δd⁻err 为每个任务选择 PI 优于随机选择，且在候选 PI 差异较大时提升更明显。最后，将有效 PI 的 OPSD 与 GRPO 结合后，组合目标可超过强 GRPO 基线。

### 四、结论（Conclusion）
OPSD 中 PI 的有效性取决于 PI 内容、格式、生成来源和学生模型，不能把 PI 视为固定设计；面向多轮智能体任务，应优先考虑信息密集且能解释错误与策略的 PI，并谨慎为已具较强推理能力的 Thinking 模型增加教师推理。训练前可用误差步骤 KL 对比 Δd⁻err 进行 PI 候选筛选，它比 PI utility 更可靠，并能指导逐任务选择；有效 PI 还可与 GRPO 结合，形成优于强 GRPO 基线的训练方案。

### 五、方法论与关键技术细节
关键实现包括：以成功参考轨迹构造四类轨迹 PI，并用 GLM-5.2、Qwen3.7-Plus 或学生自身生成 Summary、Skill、Checklist 提示；OPSD 损失为学生采样轨迹上的 token 级反向 KL，教师分布停止梯度，训练与评估覆盖三个基准和三种 Qwen3 模型。离线诊断中，D 用学生采样 token 的对数概率比绝对值衡量 PI 引起的概率偏移，Δd⁻err 则先计算错误步骤的正向抑制量，再减去同任务同绝对步骤位置的基线，并要求 judge 标注失败轨迹中的错误步骤。局限在于 PI utility 可能受信息泄漏影响，采样 token 反向 KL 可能给无益偏移较大值且不刻画方向，研究范围限于特定基准、模型和 PI 构造，Thinking 模型在 τ² 上已有较高 pass@4（88.9），额外 PI 的增益空间和干扰风险需谨慎解读。
