# Typed Temporal Interaction Features for Simulation-Backed Forecasting of Open-Source Game Release Incidents

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Shayma Alkobaisi, Anas Ali
- 机构：United Arab Emirates University, National University of Modern Languages
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31647v1) · [PDF](https://arxiv.org/pdf/2609.31647v1)

## TLDR
This paper presents GAMEQUALGRAPH-Pilot, a simulation-backed typed temporal interaction pipeline for forecasting open-source game release incidents, but its evaluation mainly supports protocol reproducibility rather than real-world deployment because it does not significantly outperform a static heterogeneous baseline.

## Abstract
Open-source video-game quality depends on inter-actions among code, assets, configuration, tests, contributors, and issue workflows, yet conventional defect predictors usually flatten or omit these relations. We investigate release-level forecasting of a quality incident within thirty days using GAMEQUALGRAPH-Pilot, a typed temporal feature pipeline with calibrated risk estimates and effort-aware ranking. Because the accessible OS-SGameBench materials do not provide manually audited release dates and outbreak labels, the executed evaluation is explicitly simulation-backed rather than an empirical claim about real games. Five seeded worlds each contain 120 projects and 24 releases, with project-disjoint validation and future cross-project testing. The pilot obtains an AUPRC of 0.520, AUROC of 0.673, Brier score of 0.207, and 29.68% effort-aware recall at a twenty-percent testing budget. Its closest local comparator, Static-Hetero-Reimpl, reaches 0.522 AUPRC; the -0.002 difference is not statistically significant after Holm correction. Inference requires 0.023 milliseconds per release in the measured environment. Ablations and controlled missingness, drift, engine, project-size, alert-threshold, and attribution analyses expose where typed interactions help and where they fail. Results support the reproducibility of the proposed protocol, not deployment effectiveness. Real OSSGameBench release reconstruction, stratified label audits, and official graph-model comparisons remain mandatory before journal submission or operational use in practice. This boundary protects research integrity and supports credible evaluation.
