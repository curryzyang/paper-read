# When Do Options Help? Policy Necrosis and Redundant Coverage in Option-Critic

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Bingyun Liu, Yuheng Jing
- 机构：Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05508v1) · [PDF](https://arxiv.org/pdf/2609.05508v1)

## TLDR
The paper shows that option-critic's performance gains from adding options come not from temporal abstraction but from redundant coverage that reduces the chance all options fail in the same state, while its learned termination rule is vacuous or harmful and the real failure is "policy necrosis" in intra-option policies, which restoring lower-level exploration can repair with a single option.

## Abstract
Option-critic learns options: sub-policies together with a learned rule for when each one hands control back. Its headline result is that performance improves as options are added. We explain that result, with theory and experiment. First, the termination rule option-critic learns by maximising return contributes nothing. When the termination test and the policy that picks options read the same values, the test fires at every step, so the learned rule is identical to always terminating. When that policy explores and the test does not, as in option-critic itself, the rule can block the exploration; there are instances where it suffers $Ω(T)$ regret while always terminating holds to $O(\log T)$. Forcing termination at every step leaves the option-count curve intact. Second, the policy inside an option barely explores at all, so a state locks onto the first action that looked good and never updates again. We name this policy necrosis, give a state-level test for it, and find three fifths of states necrotic in a typical option. Restoring exploration repairs those states, and one option then solves the task. Third, extra options improve no option; what falls is the chance that all of them fail in the same state, from $59\\%$ to $4\\%$, and performance follows that joint quantity.
