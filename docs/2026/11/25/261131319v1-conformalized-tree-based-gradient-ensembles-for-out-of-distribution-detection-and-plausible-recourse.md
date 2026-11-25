# Conformalized Tree-Based Gradient Ensembles for Out-of-Distribution Detection and Plausible Recourse

- 区域：速读区
- 排名：8
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Mariam Zakaria Moussa Ali
- 机构：Arab Open University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31319v1) · [PDF](https://arxiv.org/pdf/2611.31319v1)

## TLDR
The paper shows that conformalized out-of-distribution gating of actionability-constrained counterfactual recourse for gradient-boosted tree ensembles reduces implausible/OOD recommendations on tabular credit benchmarks, at the expense of higher recourse cost and lower feasibility, thereby formalizing a cost–feasibility–plausibility trade-off.

## Abstract
Counterfactual recourse provides actionable feature adjustments that reverse unfavourable predictions made by automated decision models. However, when recourse search optimizes purely against classifier confidence or narrow proxy scores over gradient-boosted decision trees (GBDT), search procedures can exploit boundary artifacts and low-density regions---an instance of Goodhart's law---yielding out-of-distribution (OOD) recommendations that appear favourable nominally while lacking manifold plausibility. In this paper, we study conformalized OOD gating coupled with actionability-constrained counterfactual search across two tabular benchmarks: Adult and Give Me Some Credit (GMSC). Calibrating finite-sample anomaly gates (gate_IF, gate_LOF, and the conjunctive gate_ALL) at significance level delta = 0.05 over isolation forest, local outlier factor, and k-nearest-neighbor signals, we audit generated counterfactuals against held-out GMM and OCSVM detectors alongside ablation studies (gen10, gen100, and relax). Across matched recourse pairs where both constrained and unconstrained searches succeed, gate_ALL significantly reduces held-out OCSVM flags on Adult (N=541, Delta flag_OCSVM = -0.0296, p_Holm = 4.0e-4) and lowers both held-out flags on GMSC (N=540, Delta flag_OCSVM = -0.0346, p = 1.0751e-4; Delta flag_GMM = -0.1663, p = 3.5679e-16) while increasing matched recourse cost (Delta cost = +0.3035, p = 1.3365e-5) and narrowing overall feasibility. Our findings formalize the cost--feasibility--plausibility trade-off and demonstrate how conformal OOD gating audits recourse reliability on tabular ensembles.
