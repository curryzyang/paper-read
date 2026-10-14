# PreSO: Privileged Representation Isolation for On-Policy Self-Distillation

- 区域：精读区
- 排名：5
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Yuhang Yang, Mingxuan Xia, Chao Ye, Shuai Zhu, Shouqing Yang, Haobo Wang, Shenzhi Yang, Zhengqing Zang, Chenglong Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14001v1) · [PDF](https://arxiv.org/pdf/2610.14001v1)

## TLDR
PreSO improves on-policy self-distillation by using compact hints and projecting privileged representation shifts onto a low-rank subspace of cross-problem recurring structure, yielding consistent accuracy gains on competition-level mathematics benchmarks across Qwen3 models.

## Abstract
On-policy self-distillation (OPSD) uses a self-teacher conditioned on privileged information to turn the sparse outcome signal of reinforcement learning with verifiable rewards (RLVR) into dense token-level supervision. Yet the teacher's advantage may depend on information unavailable to the student at inference, raising a central question: which privileged changes are worth distilling? We use cross-problem recurrence as an empirical cue for potentially reusable guidance. Comparing the representation shifts induced by full solutions and compact hints, we find that hint-induced shifts are more concentrated and directionally consistent across problems, and yield more sustained downstream gains despite revealing less information. Motivated by this association, we propose Privileged Representation Isolation for On-Policy Self-Distillation (PreSO). At the source, PreSO uses compact hints to limit the solution-specific detail entering the privileged shift. At the target, it estimates a leading low-rank subspace from shifts pooled across related problems, projects the privilege-induced correction onto this subspace, and adds it to the student's unprivileged representation to form the representation-level distillation target. The selected subspace serves as an operational proxy for recurring structure, rather than a guaranteed separation of transferable and instance-specific information. On five competition-level mathematics benchmarks, PreSO consistently outperforms strong baselines across Qwen3-1.7B, 4B, and 8B, improving average accuracy over the base model by 6.8, 9.0, and 10.0 points. Beyond peak accuracy, PreSO attains the highest final-checkpoint average at every model scale, with improvements that persist through the end of training.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
