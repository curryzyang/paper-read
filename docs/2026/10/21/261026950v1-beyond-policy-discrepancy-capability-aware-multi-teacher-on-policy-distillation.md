# Beyond Policy Discrepancy: Capability-Aware Multi-Teacher On-Policy Distillation

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Xuanfeng Yang, Le Gui, Jiaming Wang, Xuan Zhang
- 机构：Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26950v1) · [PDF](https://arxiv.org/pdf/2610.26950v1)

## TLDR
CA-MOPD improves multi-teacher on-policy distillation by initializing the student from merged RL specialists and allocating teacher supervision based on verifier-estimated capability gaps rather than policy discrepancy, achieving a 32.22 average score across mathematics, code, and instruction-following benchmarks.

## Abstract
Multi-teacher on-policy distillation (MOPD) integrates domain specialists into a shared student, but determining how strongly each teacher should supervise remains challenging. Existing discrepancy-based allocation can assign strong supervision even when the student already matches or exceeds the teacher's task performance, since behavioral mismatch does not necessarily imply a remaining capability deficit. We propose Capability-Aware Multi-Teacher On-Policy Distillation (CA-MOPD), which combines specialist merging with capability-guided allocation to account for what the student has already learned. CA-MOPD first merges reinforcement-learning specialists into a strong student initialization, then uses verifier-estimated teacher--student capability gaps to adjust domain-level distillation strength. Supervision decreases as capability gaps close and increases when estimated student capability regresses, while dense token-level guidance remains provided by the teachers. Across six benchmarks spanning mathematics, code generation, and instruction following, CA-MOPD achieves an average score of 32.22, outperforming naive MOPD, Open-MOPD, and the merged initialization by 0.86, 0.83, and 0.74 points, respectively. Controlled comparisons further support the benefits of merged initialization and capability-gap guidance under matched training budgets.


## 精读解读（中文）
### 一、研究动机
多教师在线策略蒸馏需要把数学、代码和指令遵循等领域专家整合进一个共享学生模型，但现有方法主要按教师与学生之间的策略差异分配监督强度，而行为分布不匹配并不必然意味着教师仍有任务级能力优势，学生可能在合并专家后已经追平甚至超过教师。论文因此主张从“剩余可迁移能力”而非单纯策略差异出发分配蒸馏强度。

### 二、技术方案（Method）
CA-MOPD首先用Task Arithmetic将共享MixSFT基座上的多个RL专家合并为学生初始化，合并系数取α_d=1；随后在留出校准集上用领域验证器估计各教师能力T_d，并估计合并学生的初始能力C_d^(0)与历史最佳C_d^★。训练中复用学生已有在线rollout的验证器分数，以指数滑动平均更新学生能力C_d^(k)，计算有符号能力差g_d=T_d−C_d和正剩余空间H_d=[g_d]_+，用剩余空间比例r_d=H_d/H_d^(0)生成headroom因子，并在检测到能力回退时用guard因子提高监督；最终能力因子与token-share平衡因子b_d=q_d/s_d相乘，经全局缩放F=max_j f_j归一化为每token权重w_d，对原有稠密OPD信号做sg[w_d A]加权并用token归一化PPO目标优化。

### 三、结果（Result）
在数学、代码生成和指令遵循六个基准上，CA-MOPD取得平均32.22，分别比Naive MOPD的31.36、Open-MOPD的31.39和ParamMerge-TA初始化的31.48高0.86、0.83和0.74分。它在该平均指标上最高，并在AIME24、AIME25和IFBench上领先，其中相对Open-MOPD在AIME24提升2.19分、在IFBench提升3.34分；但LiveCodeBench v5/v6相对合并初始化有所下降。消融显示ParamMerge-TA初始化本身把平均分从24.92提高到31.48，而相同200步预算下从合并初始化训练到32.22，优于从MixSFT训练得到的31.53。

### 四、结论（Conclusion）
论文的核心结论是策略差异不能替代能力缺口，MOPD应按验证器估计的剩余教师优势和能力回退风险动态分配领域监督。将RL专家合并作为强初始化，再叠加能力引导的域级权重，可在匹配训练预算下提升多领域聚合性能；但收益并非各领域均匀提升，代码性能下降说明存在跨域能力权衡。

### 五、方法论与关键技术细节
实验使用SmolLM3-3B的MixSFT检查点及Open-MOPD发布的数学、代码、指令遵循三个RL专家，主模型从三专家Task Arithmetic合并初始化并训练200个外层步，六个基准为AIME24、AIME25、LiveCodeBench v5/v6、IFEval、IFBench，采用等权平均。方法关键点包括固定教师能力参考T_d、学生能力EMA跟踪、历史最佳C_d^★、headroom比例幂次与clip、回退阈值τ与有界guard、token-share平衡q_d/s_d、全局缩放F=max_j f_j，以及保持教师token级稠密监督不变而只改域级优化压力。局限与约束包括能力估计依赖领域验证器和校准集，控制器超参及附录细节未在正文给出，结果集中在单一3B模型和三类领域，且代码能力相对合并初始化下降，表明并非一致改进。
