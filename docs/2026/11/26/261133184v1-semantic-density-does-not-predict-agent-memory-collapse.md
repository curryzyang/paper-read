# Semantic Density Does Not Predict Agent-Memory Collapse

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Saksham Gupta, Yash Choudhary, Arpit Upadhyay
- 机构：Independent Researcher, Vasuki Inc., Piramal Finance
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33184v1) · [PDF](https://arxiv.org/pdf/2611.33184v1)

## TLDR
**TLDR:** Across 805 memory snapshots and long-horizon runs, memory-store statistics—especially global semantic density—do not reliably predict when LLM-agent memory will collapse, local crowding signals do not transfer consistently, and the main observed failure is unbounded whole-store prompting exceeding model input capacity, which token growth predicts directly.

## Abstract
Persistent textual memory can improve LLM agents, but repeated updates can erode task performance. We ask whether memory-store statistics warn before held-out accuracy declines. We registered mean pairwise cosine similarity ($ρ$) and 13 additional geometry, retrieval, and graph statistics on 805 snapshots from 13 memory methods across ALFWorld, AppWorld, ScienceWorld, WebShop, and two ARC-AGI settings. These methods store trajectories, rules, workflows, strategies, or linked records, using selective retrieval or whole-store prompting. No such statistic reliably predicted early signs of task accuracy decline, and $ρ$ had zero median lead. With the checkpoint after peak accuracy as a secondary decline point, measures of highly similar pairs and nearest-neighbor crowding changed earlier but did not consistently outperform stored-item count. We trained classifiers on this corpus and applied them unchanged to PropWorld runs of up to 5,000 crafting tasks. They falsely flagged 56.9% of checkpoints from size-limited stores with stable accuracy and detected only 18% of checkpoints after task success fell to zero. Thus, global semantic density did not provide a reliable warning, while local crowding did not transfer consistently across memory designs. In these long-horizon runs, size-limited stores remained stable, while the sole failure arose when unbounded whole-store prompting exceeded model input capacity, which token growth predicted directly.
