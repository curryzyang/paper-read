# Observational Policy Ranking for SMB Financial Guidance from Multi-Action Accounting Logs

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Shrutendra Harsola, Vignesh Subrahmaniam, Vikas Raturi, Kamalika Das, Xiang Gao, Kratika Gupta, Ruocheng Guo, Padmaja Jonnalagedda, Ananya Pramod, Sricharan Kumar
- 机构：Intuit
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10050v1) · [PDF](https://arxiv.org/pdf/2608.10050v1)

## TLDR
This paper introduces Covariate-Adjusted Residual Policy Learning (CAR-PL) to rank 34 ledger-derived business-change categories from observational multi-action accounting logs for SMB financial guidance, showing KPI-specific policy leaders—CAR-PL for Gross Profit, T-Learner for Revenue, and a contextual value model for Quick Ratio—across 85,078 company-month records from 7,505 firms.

## Abstract
Small and medium-sized businesses need timely financial guidance, yet historical accounting logs record self-selected and often co-occurring business changes rather than randomized recommendations. We formulate this setting as observational policy ranking: from pre-decision financial information, a policy selects one of 34 ledger-derived business-change categories for a target financial KPI. Using 85,078 company-month observations from 7,505 firms, we introduce Covariate-Adjusted Residual Policy Learning (CAR-PL), an action-wise R-learner that operates directly on multi-hot logs and regularizes selection by observational support. We compare CAR-PL with an uplift T-Learner, a conservative contextual value model, a zero-shot LLM, and non-personalized references on company-disjoint held-out firms under a shared model-assisted scoring rule. CAR-PL has the highest Gross Profit point estimate (0.084), the T-Learner has the highest Revenue point estimate (0.085), and the contextual value model has the highest Quick Ratio point estimate (0.062). CAR-PL and the T-Learner are not statistically separated on either growth KPI in matched company-clustered comparisons, while CAR-PL selects 33-34 categories and produces less concentrated selections across the catalog. Outcome-model-only scoring retains the same KPI-level point-estimate leader or top pair, and category rankings remain similar when the all-zero treatment reference is replaced by the most common training co-action pattern. These findings support objective-specific ranking of SMB financial guidance from multi-action accounting logs.
