# Not All Agreement Counts as Corroboration: Provenance-Conserving Multi-View Fusion for Typed Action Admission in Human-Robot Collaboration

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Zekai Jin, Hanrong Zhang, Yihong Tang, Fei Hu, Zhen Dong, Yi Shao
- 机构：McGill University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01662v1) · [PDF](https://arxiv.org/pdf/2609.01662v1)

## TLDR
PACT is a provenance-conserving multi-view fusion method for human-robot collaboration that treats evidence countability as a relational variable—counting agreement as corroboration only when outputs come from separately countable origins—and uses a coordinatewise meet within and accumulation across provenance-defined units to enable typed action admission (hold/confirm/fallback), preventing repeated inferences from inflating evidence while improving selective action admission and risk coverage in embodied settings.

## Abstract
For embodied systems, predictive agreement alone does not determine whether evidence warrants action; evidential origin matters. Repeated inference over one observation can multiply agreement without adding evidence, while source-local values do not reveal whether outputs have separately countable origins. PACT treats evidence countability as a relational variable for provenance-conserving fusion and typed action admission. A supplied provenance partition defines countable units. PACT retains coordinatewise support shared within each unit, accumulates only across units, and maps unmet release conditions to hold, confirm, or fallback. Under the stated assumptions, source-local values cannot identify countability; the coordinatewise meet is the greatest budget satisfying singleton fidelity and insertion non-amplification, with coarsening monotonicity and fixed-partition stability. Across 31,200 evaluations in 48 scene clusters, PACT attains a common-support normalized risk-coverage area (ncsAURC) of 0.0861. Excluding the constructed adversarial-consensus arm, provenance-partition aggregation reduces ncsAURC by 0.0557 relative to singleton aggregation, while the corroboration contrast vanishes. On complete-source records, native scores favor PACT, but a common posterior-peak score narrows its difference from nested Dirichlet and favors product fusion. Reassigning provenance over unchanged predictions moves evidence budgets as predicted. In offline human-robot collaboration, eightfold within-camera duplication leaves 720 typed responses per checkpoint unchanged; camera-grouped PACT admits 47 of 57 Qwen3-VL-32B reference-consistent candidates with no observed reference-inconsistent admission in 60 episodes. PACT separates computational from evidential multiplicity: agreement constitutes corroboration only when provenance permits separate accumulation.
