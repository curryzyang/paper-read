# ARC-2: Continuous Compliance Through Delta Management

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Tord Johan Eide, Einar Holt
- 机构：Wybe Labs Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21811v1) · [PDF](https://arxiv.org/pdf/2611.21811v1)

## TLDR
ARC-2 introduces Delta Management, a continuous post-deployment governance framework that defines compliance as the measured distance between an autonomous system’s current operational state and its certified baseline region, extending ARC with worst-case/outlier-quarantined CRAB governance, a layered trigger taxonomy, graduated authority withdrawal versus physical shutdown, and environmental-delta-triggered recertification or ODD revision to support lifecycle compliance obligations such as EU AI Act Article 72(2).

## Abstract
ARC 1 introduced a three-layer governance architecture for autonomous systems comprising model safety validation, cognitive certification (CRAB), and operational authorization (LEA). However, it did not address how compliance should be maintained after deployment.
  This paper introduces Delta Management, a continuous governance framework that measures deviations between a system's current operational state and its certified baseline, defined as a region rather than a fixed point. Compliance is assessed through continuous monitoring instead of static certification.
  Four extensions are proposed. First, CRAB evaluation incorporates the worst verified behavioral deviations, with isolated outliers quarantined pending confirmation to prevent unjustified restrictions. Second, a layered trigger taxonomy distinguishes hard safety violations, critical single-dimension failures, correlated multi-system degradation, and risk-weighted composite indicators, each triggering proportionate responses. Third, a graduated safe transition protocol separates withdrawal of operational authorization from physical shutdown, consistent with established safety standards and EU AI Act requirements. Fourth, environmental delta is introduced as a distinct baseline validity condition: environmental drift beyond the certified Operational Design Domain (ODD) triggers recertification or ODD revision rather than automatic authority contraction.
  Together, these extensions transform ARC from a deployment-time certification architecture into a continuous framework for monitoring, evaluating, and enforcing compliance throughout the operational lifecycle of autonomous systems. The framework addresses the continuous compliance obligations established by EU AI Act Article 72(2).
