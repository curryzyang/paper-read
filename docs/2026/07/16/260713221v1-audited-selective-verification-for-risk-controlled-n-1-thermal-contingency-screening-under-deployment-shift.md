# Audited Selective Verification for Risk-Controlled N-1 Thermal Contingency Screening under Deployment Shift

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jayakumar Manoharan
- 机构：Electric Power Research Institute (EPRI)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13221v1) · [PDF](https://arxiv.org/pdf/2607.13221v1)

## TLDR
This paper introduces Audited Selective Verification, a risk-budgeted N-1 thermal contingency screening method that uses an online audit of full power flow solves to certify a violation-rate bound for skipped contingencies, providing distribution-free guarantees robust to deployment shift from black-box controllers.

## Abstract
Real-time N-1 contingency screening in an energy management system trades assurance against cost: verifying every credible outage with full power flow is too slow, while fast linear-sensitivity screening gives no statistical guarantee and can silently pass unsafe operating points, especially when a controller drives the system into unfamiliar regimes. This paper introduces Audited Selective Verification, a risk-budgeted screening and triage layer for any controller's output (optimization, model-predictive, or learned). A cheap surrogate proposes which outages to skip; an online audit runs full power flow on a small random sample each window; and a calibrated threshold certifies a thermal-violation-rate bound for the skipped set at a chosen budget and confidence, with a corresponding bound for the unverified trusted subset. Validity rests on real verification and the audit rather than on surrogate accuracy, so it holds under arbitrary deployment shift. It is a risk-budgeted screen, not a replacement for deterministic verification when policy requires checking every credible contingency. On three public transmission systems up to 1354 buses, the realized violation rate stays within budget, standard deterministic and calibrated screens become unsafe under shift, and the method cuts full power-flow studies by 29 to 75 percent per real-time operating point.
