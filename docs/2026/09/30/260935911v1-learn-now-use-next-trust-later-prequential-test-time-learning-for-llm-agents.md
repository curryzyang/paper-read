# Learn Now, Use Next, Trust Later: Prequential Test-Time Learning for LLM Agents

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Tong Zhao, Reed Li, Yuyang Hu, Yutao Zhu, Haijin Liang, Haibo Shi, Yu Lu, Zhicheng Dou
- 机构：Renmin University of China, Tencent
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35911v1) · [PDF](https://arxiv.org/pdf/2609.35911v1)

## TLDR
StepLearn is a nonparametric test-time learning framework for LLM agents that converts individual transitions into hypotheses for immediate next-step guidance while requiring prospective validation across later episodes before persistent reuse, improving success on WebArena-Lite and ALFWorld without updating model parameters.

## Abstract
Adapting large language model agents during deployment requires not only retaining past experience, but also turning new observations into timely guidance. Many test-time learning methods, however, acquire knowledge from completed episodes. Feedback from an ongoing interaction may therefore not be distilled into knowledge soon enough to help the next decision. Acquiring knowledge at the granularity of individual transitions could reduce this delay, but raises a separate challenge: a rule that is useful within one episode may not be reliable enough to guide future episodes. Waiting for validation can forfeit immediate benefits, whereas unrestricted reuse can propagate accidental or misattributed guidance. We introduce StepLearn, a nonparametric framework that separates immediate use from persistent trust. It turns informative transitions into hypotheses that can guide the next step, while requiring prospective validation before reuse across episodes. Their predicted effects are checked against subsequent observations outside the source episodes, and only sufficiently supported hypotheses become available for persistent guidance. This process updates external knowledge while keeping all model parameters fixed. Over five rounds on WebArena-Lite and ALFWorld, StepLearn achieves average success rates of 59.9% and 84.0% with GPT-5-mini, and 57.8% and 88.1% with Qwen3.5-35B-A3B, respectively. It outperforms EvoTest, the strongest baseline, by 2.2-12.7 percentage points across the four settings. Learning dynamics further shows that these gains are not restricted to the final repetition, with advantages already present on first task attempts in most settings.


## 精读解读（中文）
### 一、研究动机
现有LLM智能体测试时学习多依赖完整回合或轨迹来更新参数或外部知识，导致正在进行的交互反馈难以及时转化为下一步决策的指导；若改以单步转移粒度获取知识，又会面临局部规则即时有用但跨回合可信度不足的矛盾，等待验证会丧失即时收益，不加约束复用则可能传播偶然或错误归因的指导。

### 二、技术方案（Method）
StepLearn将交互转移τ_t=(o_t,a_t,o_{t+1},r_t)作为学习单元，用确定性检测器在导航或结果变化、显式报错、奖励变化、终止反馈或连续无进展时触发采集，并由辅助学习器L_ψ单次生成结构化假设k=(c_k,p_k,φ_k^+,φ_k^-,σ_k,u_k,S_k)，其中条件、自然语言策略、正负可观测效果谓词、作用域、动作类型和源回合集合共同定义可检验知识。每个有效假设同时产生运行时副本用于当前回合从t+1步起即时检索，以及持久候选副本进入候选记忆；运行时记忆在回合边界清空，候选与已验证记忆跨回合保留。动作选择阶段，智能体按环境或网站边界以及页面类型、任务模式、进度线索从运行时与已验证记忆中检索可选指导G_t，并以π_θ(a_t|H_t,G_t)行动，模型参数θ与辅助学习器参数ψ全程冻结。前瞻验证阶段，在演员选定a_t后按作用域和动作类型匹配候选，排除源回合S_k和已有结论回合D_k，冻结其效果谓词再执行动作，由确定性适配器把转移映射为结构化证据z_t，评估得到+1支持、-1反证或⊥未决；累计n_k与n_k^+，当n_k^+≥m且n_k^+≥ρn_k时提升到已验证记忆，反证累积后可撤出检索但保留身份。

### 三、结果（Result）
在WebArena-Lite与ALFWorld各五轮持续评测中，StepLearn配合GPT-5-mini平均成功率为59.9%与84.0%，配合本地Qwen3.5-35B-A3B为57.8%与88.1%，四个设置均超过最强基线EvoTest达2.2至12.7个百分点。消融显示逐步采集、即时复用和记忆保留各自有贡献，且小辅助学习器也能取得有竞争力的表现，辅助学习调用仅占约5.5%。学习动态表明优势不只在最终轮次，在多数设置的首轮任务尝试中已出现。

### 四、结论（Conclusion）
StepLearn把即时使用与持久信任解耦，证明以转移级可检验假设驱动的前瞻式测试时学习能在不更新模型参数的前提下，将当前交互经验及时用于下一步并只在后续非源回合验证后跨回合复用。该范式为部署期LLM智能体提供了兼顾响应速度与可靠性的外部知识演化方案，并在浏览器操作与具身任务规划上显示出稳定增益。

### 五、方法论与关键技术细节
评测数据为WebArena-Lite中排除4个Wikipedia任务和6个多网站任务后的155个任务（Shopping、Shopping Admin、GitLab、Map、Reddit）与ALFWorld valid_unseen的134个任务（Look、Pick、Clean、Cool、Heat、Two），对比基线包括Static、Memory、Reflexion、JitRL、AWM、EvoTest，本地模型另比SFT与TTRL，WebArena每回合最多25步并经BrowserGym交互，在线方法按任务五回合连续流评估并报告跨回合平均成功率。实现上无梯度更新或训练损失，知识项由辅助学习器生成，效果谓词由确定性适配器基于结构化证据进行受限比较而非生成可执行代码，检索受环境和网站边界约束，合并同义假设时保持候选身份并扩展源集合但不增加验证支持。关键超参为提升门槛m≥1与经验精度ρ∈(0,1]，候选验证每回合对每项至多产生一个结论且排除源回合，未决试验不计入支持或反证计数，终止反馈可解决延迟反馈但中间零奖励不等于失败。局限性在于持久记忆和候选会随交互累积、依赖作用域和动作类型匹配、稀疏或延迟反馈可能推迟提升，且只有通过前瞻验证的知识才可持久复用，可能牺牲某些即时有效但证据不足的局部规则。
