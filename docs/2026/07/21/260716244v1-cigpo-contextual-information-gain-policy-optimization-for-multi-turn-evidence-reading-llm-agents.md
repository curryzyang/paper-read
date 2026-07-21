# CIGPO: Contextual Information-Gain Policy Optimization for Multi-Turn Evidence-Reading LLM Agents

- 区域：精读区
- 排名：2
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Hao Dou
- 机构：Harbin Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16244v1) · [PDF](https://arxiv.org/pdf/2607.16244v1)

## TLDR
CIGPO addresses the training collapse in multi-turn evidence-reading LLM agents caused by zero-advantage lock-in in outcome-only GRPO by injecting per-turn contextual information-gain rewards, achieving a 105% relative F1 improvement on HotpotQA (from 0.252 to 0.518) while maintaining stable reward variance.

## Abstract
Training multi-turn evidence-reading agents with outcome-only reinforcement learning is unstable because intermediate turns receive little direct credit. In HotpotQA experiments with Qwen2.5-3B-Instruct, GRPO initially improves (standard F1 0.430) but subsequently collapses to 100% format-violating outputs. Training-log diagnosis reveals a zero-advantage lock-in mechanism: all sampled trajectories receive the minimum format penalty (-2.0), group-relative advantages vanish, and the policy-gradient loss becomes zero--an optimization deadlock. We propose a variance-injection strategy: by assigning per-turn rewards to intermediate evidence-reading turns, we prevent the group reward distribution from collapsing to a single value--preserving the variation that GRPO's group-relative advantage requires. Contextual Information-Gain Policy Optimization (CIGPO) implements this strategy using the marginal increase in the frozen reference model's log-likelihood of the ground-truth answer as the per-turn signal. With separate normalization of IG and F1 rewards and an IG-weight curriculum, CIGPO reaches a standard F1 of 0.518 on HotpotQA at the 3B scale (from 0.252 base; +105%), compared with 0.430 for the best GRPO checkpoint and 0.000 for the final GRPO checkpoint. CIGPO maintains meaningful reward variance and avoids zero-advantage lock-in throughout training. These results identify reward-variance collapse as a concrete failure mode of outcome-only GRPO and show that turn-level IG rewards can prevent it in this HotpotQA setting.


## 精读解读（中文）
### 一、研究动机
Training multi-turn evidence-reading agents with outcome-only reinforcement learning is unstable because intermediate turns receive little direct credit, leading to optimization deadlock. In HotpotQA experiments with Qwen2.5-3B-Instruct, GRPO initially improves (standard F1 0.430) but subsequently collapses to 100% format-violating outputs due to zero-advantage lock-in, where all sampled trajectories receive minimum format penalty (-2.0), group-relative advantages vanish, and policy-gradient loss becomes zero.

### 二、技术方案（Method）
CIGPO is a lightweight extension of GRPO that injects variance at intermediate turns via reference-based contextual information gain. Given a question q and a closed pool of pre-indexed evidence documents, the agent interacts for up to T turns: at each turn t, it reasons in a <think> block, calls Read[block_id] in a <tool_call> block, and receives evidence content. For each intermediate turn t (< T), the per-turn IG reward is computed as r_t^IG = log p_ref(y* | q, e_{≤t}) - log p_ref(y* | q, e_{<t}) using the frozen reference model (the same as used for KL regularization). The final turn receives F1 reward r_T^F1 = F1(extract_answer(o_T), y*). IG and F1 rewards are normalized separately within each GRPO group (group size N=2) to compute group-relative advantages, with a safety clip of ±50 for IG. A linear curriculum schedules the IG weight from 0.1 to 0.3 over 200 steps, while F1 weight stays at 1.0. Prealigned vectorized computation batches all turn prompts into one forward pass for efficiency (~3× speedup).

### 三、结果（Result）
On HotpotQA test set (1,000 examples), CIGPO reaches a standard F1 of 0.518 (from base 0.252; +105%), compared to 0.430 for the best GRPO checkpoint and 0.000 for the final collapsed GRPO checkpoint. CIGPO maintains meaningful reward variance throughout training and avoids zero-advantage lock-in. Per-turn IG analysis shows mean cumulative IG of 4.06 for correct trajectories vs. 2.10 for wrong trajectories, indicating correlation with successful evidence use.

### 四、结论（Conclusion）
The study identifies reward-variance collapse as a concrete failure mode of outcome-only GRPO in multi-turn evidence reading, and shows that turn-level IG rewards can prevent it in the HotpotQA setting with Qwen2.5-3B-Instruct. CIGPO stabilizes training by ensuring non-zero reward variance across group members, preserving the variation that GRPO's group-relative advantage requires.

### 五、方法论与关键技术细节
Data: HotpotQA training set (1,000 examples) and test set (1,000 examples). Model: Qwen2.5-3B-Instruct (3.09B parameters) trained on 2×24GB GPUs with FSDP and vLLM. Hyperparameters: rollout temperature 0.6, max 3 turns, GRPO group size N=2, PPO mini-batch size 2, learning rate 1e-6, KL coefficient β=0.10, entropy coefficient 0.01, IG curriculum 0.1→0.3, IG safety clip ±50, format penalty -2.0, max sequence length 3072 tokens, training steps 200. IG reward uses frozen reference model log-likelihood of ground-truth answer. Separate group normalization for IG and F1 rewards is essential due to their different scales. Limitations: group size limited to 2 due to hardware; experiments only on Qwen2.5-3B-Instruct and HotpotQA; reference model and IG computation assume accurate ground-truth answer availability; IG values may be noisy for some examples; curriculum parameters not extensively tuned.
