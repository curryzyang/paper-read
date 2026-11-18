# Regularized Score Centering

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Hao Bai, Chenlu Ye, Xuanchang Zhang, Aviral Kumar, Tong Zhang
- 机构：CMU, UIUC
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21791v1) · [PDF](https://arxiv.org/pdf/2611.21791v1)

## TLDR
Regularized Score Centering (RSC) stabilizes asynchronous, off-policy reinforcement learning by adding a reverse-KL penalty to score centering—optionally with truncated importance sampling—to keep the learner close to the behavior policy, improving sample efficiency and achieving top performance on mathematical reasoning and diverse agentic benchmarks.

## Abstract
Asynchronous reinforcement learning increases training throughput, but data from stale policies and numerical mismatch between training and inference can destabilize learning. To stabilize off-policy learning, score centering (SC) removes the effect of reward baselines on the expected update. Our gradient diagnostics show less extreme gradients with SC than with importance sampling (IS), but SC can still fail when the learner moves far from the behavior policy that generated the data. To limit this policy mismatch, we introduce Regularized Score Centering (RSC), which adds a reverse Kullback-Leibler (KL) penalty to encourage the learner's next-token distribution to stay close to the behavior policy's next-token distribution. RSC works with or without truncated importance sampling (TIS), which caps token importance weights. Our theoretical analysis supports this approach, showing that KL regularization improves convergence guarantees. We evaluate dense and mixture-of-experts models on mathematical reasoning and agentic tasks, including online shopping, tool use, games, and fully asynchronous software engineering. RSC with TIS substantially improves sample efficiency across all agentic benchmarks, attaining higher training rewards with the same number of sampled responses. In final evaluations, it achieves top performance across all six agentic tasks, improving by 14.3% on AppWorld and reaching 9.9 times the strongest baseline's score on BabyAI.


## 精读解读（中文）
### 一、研究动机
异步强化学习虽能提升训练吞吐，但陈旧策略数据以及训练与推理的数值不匹配会造成离策略学习不稳定。重要性采样（IS）虽可修正分布差异，却容易产生极端梯度；分数中心化（SC）能移除奖励基线对期望更新的影响，但当学习器远离生成数据的行为策略时仍会失效。因此需要一种既能保留 SC 的基线校正、又能限制策略偏移的稳定化方法。

### 二、技术方案（Method）
RSC 在 SC 的 token 级目标上加入反向 KL 正则：在每个历史处约束学习器与行为策略的下一 token 分布，目标由行为策略下的 token 优势项与 β·KL(πθ||μ) 组成，μ 在求导时固定并按采样策略刷新。其更新先对加权分数减去行为策略下的条件均值以完成中心化，条件均值用同一历史采样的辅助动作进行 Monte Carlo 估计；可与截断重要性采样（TIS）结合，对 token 重要性权重按上下界裁剪，SC 无 IS 可视为裁剪区间退化为 1 的特例。训练数据来自异步或周期性刷新的行为策略，方法不增加环境交互，只改变 token 级损失与权重计算。

### 三、结果（Result）
梯度诊断显示完整 IS 会产生极端梯度，SC 能显著降低梯度幅度，但策略偏移较大时仍会失败。理论分析表明 KL 正则可改善收敛保证，反复拟合正则化目标后，最终策略单次响应的奖励可接近初始策略 best-of-N 采样的奖励。实验覆盖稠密与 MoE 模型、数学推理及购物、工具使用、游戏和全异步软件工程等任务；RSC+TIS 在所有 agentic benchmark 上提升样本效率，并在六个 agentic 任务最终评测中全部取得最佳，AppWorld 提升 14.3%，BabyAI 达到最强基线的 9.9 倍。

### 四、结论（Conclusion）
RSC 可视为 SC+KL（可选 TIS）的方法族，在保留分数中心化对奖励基线偏差校正的同时，用反向 KL 控制学习器相对行为策略的漂移。该设计对异步 RL、策略陈旧和训练-推理不匹配场景具有实际稳定化价值，并得到收敛性理论支持。

### 五、方法论与关键技术细节
关键实现包括 token 级反向 KL 以行为策略为参考、β≥0 控制正则强度、TIS 使用 c_low≤1≤c_high 的裁剪有效重要性比，以及用辅助动作估计中心化条件均值；行为策略在周期刷新或异步批次中按样本对应并固定求导。实验涉及稠密/MoE 模型、数学推理与多类 agentic 任务，强调相同采样响应数下的样本效率比较。局限在于中心化依赖 Monte Carlo 辅助动作估计质量，TIS 裁剪会引入偏差，且正则效果依赖行为策略参考的合理维护。
