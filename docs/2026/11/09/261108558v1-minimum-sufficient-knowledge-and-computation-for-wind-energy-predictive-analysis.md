# Minimum-Sufficient Knowledge and Computation for Wind Energy Predictive Analysis

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Purbak Sengupta, Aparna S. varde, Emil Jørgensen Njor
- 机构：University of Southern Denmark
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08558v1) · [PDF](https://arxiv.org/pdf/2611.08558v1)

## TLDR
The paper introduces Minimum-Sufficient Knowledge and Computation (MSKC), showing that adaptively routing to the cheapest sufficient knowledge/computation path at each state can match always-on knowledge injection for wind ramp-event prediction while cutting knowledge calls by 64%.

## Abstract
Resource-constrained cyber-physical decision systems often apply fixed sensing, knowledge, and computational pipelines despite state-dependent information needs. We introduce Minimum-Sufficient Knowledge and Computation (MSKC), a resource-aware computing principle: select the least-costly route meeting decision-risk and deployment constraints, escalating only when cheaper routes are insufficient. As proof of concept, we isolate adaptive knowledge routing, the decision underlying Knowledge-Guided Machine Learning (KGML), which conventionally injects external knowledge unconditionally rather than only where needed. We instantiate this for wind ramp-event predictive analysis, an edge-oriented decision-support task, evaluating local, relational, and physics-informed routes with a state-aware gate on publicly available real data from two wind farms. We establish conditions for feasibility preservation, cost dominance, and strict expected savings over always-on routing. At a 35.9% relational-knowledge injection rate, adaptive routing is statistically indistinguishable from always-on injection on the reported metrics while reducing knowledge calls by 64%, supporting sustainable, Green-IT-aligned deployment. These results support MSKC's premise that uniformly maximal intelligence is unnecessary. This offers intelligent data analysis for big data streams: the analysis itself decides, per state, how much knowledge and computation the data warrant.
