# Physically Constrained Federated Additive Models for O-RAN SLA-Risk Prediction

- 区域：速读区
- 排名：4
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Aubida A. Al-Hameed, Mohammed M. H. Qazzaz, Maryam Hafeez, Syed A. Zaidi
- 机构：Ninevah University, University of Leeds
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21665v1) · [PDF](https://arxiv.org/pdf/2607.21665v1)

## TLDR
This paper proposes Monotone FedNAM, a federated additive model that enforces physical monotonicity constraints on key performance indicators with known directional effects to ensure auditable and physically valid SLA-risk predictions across distributed O-RAN base stations while preserving data privacy.

## Abstract
Proactive service assurance in O-RAN requires predicting per-slice SLA violations before they occur. The prediction model must be auditable by operators and must train across base stations without pooling per-slice KPIs, which are commercially sensitive because slices are leased to individual tenants. Neural additive models (NAMs) offer auditability because each KPI contributes through a visible shape function. However, visibility alone does not guarantee physical validity. On the ColO-RAN testbed dataset, unconstrained NAMs learn effects that contradict wireless physics, for example predicting higher risk when channel quality improves. This failure appears under both local and centralized training, and non-IID federated averaging worsens it. We present Monotone FedNAM, a federated additive model in which KPIs with unambiguous physical direction are represented as monotone splines whose constraints survive FedAvg aggregation by construction, while contestable KPIs remain unconstrained. The model trains and operates as a Non-RT RIC rApp and is compact enough for deployment as a Near-RT RIC xApp. Monotone FedNAM eliminates all monotonicity violations, raises constrained shape consistency from 0.71 to 1.00, generalizes to an unseen scheduling policy, and reduces uplink traffic by 65%, at a cost of 0.04 to 0.07 AUC. These results show that physically constrained federated additive models can support auditable SLA risk inference for multi-tenant O-RAN service assurance
