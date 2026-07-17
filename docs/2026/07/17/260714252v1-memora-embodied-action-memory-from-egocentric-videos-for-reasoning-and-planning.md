# MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Zihao Yu, Xiu Yuan, Chongjie Zhang
- 机构：Washington University in St. Louis
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14252v1) · [PDF](https://arxiv.org/pdf/2607.14252v1)

## TLDR
MEMORA introduces a typed memory lifecycle with online editing and offline consolidation that improves robot planning and memory assessment by up to 20.5% over baselines, using egocentric video to build persistent, actionable embodied memory.

## Abstract
Long-horizon robot planning requires more than predicting what actions will do next; it also requires memory of the embodied experience that makes future goals interpretable. People do not plan from the present scene alone: they draw on remembered places, object-state changes, prior procedures, and regularities revealed through repeated action. We formulate Embodied Action Memory (EAM) as the capability to form, maintain, and use such experience as a persistent memory state for later decisions. MEMORA realizes EAM with a formation-consolidation-retrieval lifecycle and four typed stores: Environment Memory, Entity Memory, Activity Memory, and Inferred Knowledge. Online editing maintains object identities and state histories as new observations arrive; offline consolidation abstracts repeated experience into reusable procedures and participant-specific regularities. MEMORA-Bench evaluates this lifecycle on 45 hours of EPIC-KITCHENS-100 extension video across 18 participants through memory-grounded planning, including previously unseen goals, and a complementary memory-assessment task. Across four open-weight language models, full MEMORA--combining editing, typed stores, and consolidation--achieves the strongest aggregate results among the evaluated memory conditions. It improves memory-assessment accuracy by up to 20.5 points over the strongest controlled baseline and improves out-of-distribution Robot-Grounded Plan score by up to 16.6% relative. A qualitative two-task robot deployment study further illustrates how memory-grounded language plans can interface with downstream control, while the overall results show that editable, consolidated memory can supply remembered context for robot planning. Project page: https://yuzihaowashu.github.io/MEMORA/
