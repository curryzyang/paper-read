# Convergence Properties of PF-Exec: Homogeneous Structure, Anchored Closed Form, and Gain Dynamics

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Hanzhang Jia, Liheng Zeng, Yiran Li, Yi Gao, Bo Ma
- 机构：Zhejiang Gongshang University, University of Sussex, Shanghai Shuyuan Information Technology Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17488v1) · [PDF](https://arxiv.org/pdf/2611.17488v1)

## TLDR
This paper provides a layered convergence analysis of PF-Exec, showing that demand-proportional bandwidth allocation yields closed-form equal-load targets and feasibility bounds, the damped softmax association admits a fixed point, and the one-dimensional gain iteration is globally bounded with geometric convergence or bounded oscillations/cycles depending on the gain, thereby guaranteeing stable execution through closed-form recovery directions and bounded adaptive gains without requiring a global Euclidean contraction assumption.

## Abstract
This paper establishes a layered mathematical char acterisation of PF-Exec, the algorithm of the companion system paper. Demand-proportional bandwidth allocation yields an exact first-order homogeneous decomposition, from which the equal-load bandwidth target and its feasibility bound follow in closed form. The logarithmic knee view preserves strict load order and shares its global optimum with the Jain fairness index, while the demand-weighted centroid minimises the position potential. The damped softmax association block possesses a fixed point on the product of simplices. The truncated one-dimensional gain iteration admits a complete characterisation, with geomet ric convergence below the critical gain, initial-value-dependent bounded oscillation at it, and a family of bounded two-state cycles above it. A global invariant error ball and an explicit tracking recursion complete the execution guarantee. A numerical audit confirms the structural identities on every measured state and quantifies the local amplification of the coupled association and resource dynamics. Together, the results explain how closed form recovery directions and bounded adaptive gains provide stable execution without requiring a global Euclidean contraction assumption.
