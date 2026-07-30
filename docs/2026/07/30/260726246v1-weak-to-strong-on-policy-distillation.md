# Weak-to-Strong On-Policy Distillation

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Fangxu Yu, Zinan Lin, Xiaodong Liu, Weijia Xu, Michael Xu, Tianyi Zhou, Jianfeng Gao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26246v1) · [PDF](https://arxiv.org/pdf/2607.26246v1)

## TLDR
W2S-OPD introduces a simple and effective framework that improves a strong student model by distilling from multiple weaker models via a contrast-based proxy teacher, enabling the student to outperform even the weak teachers on math and code benchmarks.

## Abstract
On-policy distillation (OPD), which aligns a student with the teacher's token-level distribution on the student's own rollouts, is an effective paradigm for transferring capabilities across LLMs. Prevailing approaches assume a teacher at least as capable as the student: they either distill a larger model into a smaller one, which fails at the frontier where no larger teacher exists, or consolidate multiple domain experts trained from a shared base, which requires costly training at the student's scale. We introduce Weak-to-Strong On-Policy Distillation (W2S-OPD), a simple yet effective OPD framework that improves the strong student by distilling from multiple weak models. W2S-OPD constructs a proxy teacher in logit space from a contrast pair of a positive and a negative model, both smaller than the student and cheap to obtain. Their logit difference isolates the capability direction, which is added to the student's own base model, yielding a proxy teacher that couples this direction while staying distributionally adjacent to the student. The student then distills it by minimizing the per-token reverse KL on its own rollouts. We instantiate the contrast pair as i) a post-RL expert against its pre-RL initialization, isolating the skill RL instills, ii) a larger against a smaller base model, isolating the capability from scale, and iii) a small base model with correct versus wrong hints, isolating the instance-level direction toward the solution. Across four math and three code benchmarks, W2S-OPD outperforms OPD, enables the student to surpass the domain teacher, and keeps improving the student even when every supervision source is weaker. Analysis shows different contrasts yield distinct signals: the post-RL and hint contrasts emphasize reasoning frameworks, while the scale contrast emphasizes the solving procedure. Our code will be available at https://github.com/Yu-Fangxu/W2S-OPD.


## 精读解读（中文）
### 一、研究动机
现有基于策略的蒸馏（OPD）方法假设教师至少与学生能力相当，因此在缺乏更大教师的前沿场景下失效；同时，从共享基础模型训练多个领域专家并蒸馏的方法成本高昂。为解决此问题，我们提出弱到强策略蒸馏（W2S-OPD），旨在利用多个弱模型（即比学生更小的模型）通过对比蒸馏来增强强学生，从而突破教师必须更强的限制并降低资源开销。

### 二、技术方案（Method）
W2S-OPD在logit空间中构建一个代理教师，该教师由一对正负模型（均小于学生）的logit差值构成，此差值隔离了特定能力方向，并与学生自身基座模型的logit相加，得到分布上接近学生且耦合了该方向的代理教师。学生通过最小化自身rollout上的逐token逆向KL散度来蒸馏该代理教师。具体实例化三种对比对：（1）后强化学习（RL）专家与其RL前初始化，隔离RL注入的技能；（2）大基座模型与小基座模型，隔离规模带来的能力；（3）小基座模型分别使用正确提示和错误提示，隔离解法的实例级方向。训练过程中，学生模型在自生成数据上以代理教师为目标进行离线蒸馏。

### 三、结果（Result）
在四个数学基准和三个代码基准上，W2S-OPD一致优于传统OPD方法，且使学生模型超越其领域教师（如更小的专家模型）。即使在所有监督源（正负模型）均弱于学生的情况下，W2S-OPD仍能持续提升学生性能。不同对比对产生不同的信号：后RL和提示对比强调推理框架，规模对比强调解题过程。

### 四、结论（Conclusion）
W2S-OPD通过从多个弱模型构造代理教师，实现了对强学生的有效蒸馏，克服了传统策略蒸馏对教师-学生能力梯度的依赖。该框架不仅降低了蒸馏成本，还证明了弱监督信号也能通过对比机制增强强模型，为模型能力持续提升提供了新路径。

### 五、方法论与关键技术细节
关键细节包括：代理教师构建在logit空间而非输出分布上，通过正负模型logit差捕捉定向能力；蒸馏损失采用逐token逆向KL散度以保持分布匹配；对比对的选择需要确保正负模型差异集中于目标能力（如RL效果、规模、实例解法），且负模型不引入有害偏差；复杂度方面，正负模型远小于学生，计算开销低；局限性在于对比对的工程构造需要领域知识，且代理教师的质量依赖于对比对的有效性。
