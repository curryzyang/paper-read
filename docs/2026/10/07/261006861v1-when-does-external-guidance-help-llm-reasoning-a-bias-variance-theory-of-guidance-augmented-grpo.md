# When Does External Guidance Help LLM Reasoning? A Bias-Variance Theory of Guidance-Augmented GRPO

- 区域：精读区
- 排名：4
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Sofia Torres, Gabriel Almeida, Carter Adams, Camila Rocha
- 机构：Federal University of Bahia
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06861v1) · [PDF](https://arxiv.org/pdf/2610.06861v1)

## TLDR
This paper develops a bias-variance theory for guidance-augmented GRPO, showing that external guidance helps LLM reasoning only when its distribution shift is small relative to policy-gradient variance, and derives the optimal guidance weight with convergence and minimax lower bounds that unify methods like LUFFY, ExPO, PAPO, and TAPO.

## Abstract
Reinforcement learning with verifiable rewards (RLVR) has become the dominant paradigm for eliciting multi-step reasoning in large language models, and a recent wave of methods (LUFFY, ExPO, PAPO, TAPO) further augments RL with \emph{external guidance} - expert traces, self-explanations, or retrieved thought patterns. Although each method reports empirical gains, none provides convergence rates, bias bounds, or an optimal weighting rule for the guidance signal. We close this gap with \emph{Guidance-Augmented GRPO} (GA-GRPO), a unified theoretical framework that casts external guidance as a stochastic guidance operator G re-writing the question distribution, and analyses the resulting policy-gradient estimator as a biased on-policy estimator whose bias is bounded by the total-variation guidance divergence delta\_G between the guidance-augmented sampling distribution and the policy's own distribution. The framework subsumes vanilla GRPO, LUFFY, ExPO, PAPO, and TAPO as special cases obtained by particular choices of G. Under smoothness and bounded-divergence assumptions we prove that GA-GRPO converges at rate O(1/sqrt(T)) to an O(delta sqrt(T))-neighbourhood of the GRPO stationary point, derive the closed-form MSE-optimal guidance weight lambda-star(T, delta, sigma\_0 squared) = sigma\_0 squared / (sigma\_0 squared + R\_max squared delta squared T), and prove a matching minimax lower bound showing the Omega(delta squared T) bias term is unavoidable. Experiments on Qwen2.5-Math-7B-Base across nine math and OOD benchmarks confirm that optimal-weight GA-GRPO matches or surpasses TAPO, LUFFY, ExPO, and vanilla GRPO while requiring 31\% fewer GPU-hours, and eight analysis experiments validate each theoretical prediction.


## 精读解读（中文）
### 一、研究动机
外部引导（专家轨迹、自解释、检索思维模式等）在 RLVR 中被广泛用于提升 LLM 多步推理，但 LUFFY、ExPO、PAPO、TAPO 等方法只报告经验增益，缺少收敛率、偏差界与最优权重规则，导致实践者无法预判引导何时有益、何时有害，也无法避免昂贵的网格调参。本文旨在建立统一的理论框架，回答外部引导在何种条件下可证明地帮助 GRPO 式推理训练，以及如何按偏差—方差权衡最优地使用引导信号。

### 二、技术方案（Method）
将 LLM 自回归推理建模为有限时域 MDP：问题 q 从 P(Q) 采样，策略 πθ 生成 rollout o，验证奖励 R(o|q)∈[0,Rmax]，并用组相对优势 A 构造 GRPO 目标。核心是引入随机引导算子 G: Q→Δ(Q)，把问题 q 重写为引导增强问题 g(q)，得到引导增强采样分布 πθ^G(o|q)=E_{g∼G(·|q)}[πθ(o|g(q))]，并以总变分引导散度 δ_G=sup_q D_TV(πθ^G,πθ) 刻画分布偏移；由此得到的策略梯度估计器是有偏 on-policy 估计器，偏差由 δ_G 控制。vanilla GRPO、LUFFY、ExPO、PAPO、TAPO 分别对应恒等、轨迹注入、自解释、感知反馈和模式检索等具体 G。训练流程为对问题施加 G 生成增强样本、按组采样 rollout 并计算可验证奖励与组相对优势、以权重 λ 混合引导信号并更新策略；在平滑性与有界散度假设下推导 MSE 最优引导权重 λ*(T,δ,σ0^2)=σ0^2/(σ0^2+Rmax^2 δ^2 T)，并证明收敛率与匹配的 minimax 下界。

### 三、结果（Result）
理论上，GA-GRPO 以 O(1/√T) 速率收敛到 GRPO 稳定点的 O(δ√T) 邻域，且 Ω(δ^2 T) 偏差项不可消除；最优权重随训练步数 T 衰减，其闭式解由初始方差 σ0^2、引导散度 δ 和奖励上界 Rmax 决定。实验在 Qwen2.5-Math-7B-Base 上覆盖 MATH-500、AIME 2024、AMC、Minerva Math、OlympiadBench、GSM8K、GPQA-Diamond、ARC-C、MMLU-Pro 九个数学与 OOD 基准，最优权重 GA-GRPO 匹配或超过 TAPO、LUFFY、ExPO 与 vanilla GRPO，同时减少 31% GPU 小时。八项分析实验进一步验证了理论预测：当 δ^2 T≪σ0^2 时引导有益，训练后期偏差累积且方差收缩时引导可能有害，最优引导权重随训练步数下降。

### 四、结论（Conclusion）
GA-GRPO 给出了外部引导增强 GRPO 的首个统一偏差—方差理论，说明引导本质上是在早期以偏差换方差、提升探索效率，但偏差会随训练累积，因此最优使用方式是让引导权重随 T 衰减。该框架将 TAPO、LUFFY、ExPO、PAPO 和 vanilla GRPO 纳入同一视角，并提供了可操作的权重选择规则与收敛保证。其核心实践结论是：外部引导并非总有益，只有当引导散度相对当前策略方差足够小且处于训练早期时，才应较强地使用，并需按 λ*(T,δ,σ0^2) 逐步退火。

### 五、方法论与关键技术细节
关键实现与假设包括：有限时域 MDP、问题分布 P(Q)、验证奖励 R∈[0,Rmax]、组相对优势与组采样；引导算子 G 为随机核，δ_G 用总变分距离定义并在 [0,1] 内有界；理论依赖平滑性与有界散度假设，收敛到稳定点的邻域而非精确稳定点，且 minimax 下界表明偏差不可避免。最优权重 λ* 依赖 σ0^2、δ、Rmax 与 T，大 T 时近似按 1/T 衰减；方法无需修改验证奖励，但引导质量 κ 和 δ 会影响收益。局限在于理论假设可能不完全匹配真实 LLM 训练的非凸性与复杂引导，实验主要在 Qwen2.5-Math-7B-Base 和九个基准上验证，跨模型、跨任务与在线估计 δ 的稳健性仍需进一步检验。
