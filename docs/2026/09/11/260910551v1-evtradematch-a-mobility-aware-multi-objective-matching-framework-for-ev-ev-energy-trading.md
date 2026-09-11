# EVTradeMatch: A Mobility-Aware Multi-Objective Matching Framework for EV--EV Energy Trading

- 区域：速读区
- 排名：6
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Md. Mahfujur Rahman, Alistair Barros, Raja Jurdak, Darshika Koggalahewa
- 机构：Queensland University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10551v1) · [PDF](https://arxiv.org/pdf/2609.10551v1)

## TLDR
EVTradeMatch is a prediction-guided multi-objective optimization framework that formulates mobility-aware EV–EV energy trading as a constrained MILP solved with a tailored NSGA-II to jointly maximize matching coverage, transferred energy, and charging-node suitability while minimizing mobility cost, outperforming proximity- and auction-based baselines.

## Abstract
Peer-to-peer energy trading among electric vehicles (EVs) can improve charging flexibility under limited charging infrastructure, but effective EV--EV trading requires coordinated provider--consumer matching under journey-specific conditions. This paper proposes EVTradeMatch, a prediction-guided multi-objective optimization framework for mobility-aware EV--EV energy trading. Building on the EVNextTrade study, a prior learning-to-rank model for charging-node recommendation, we define charging-node suitability as a prediction-derived score reflecting the appropriateness of assigning a provider--consumer pair to a candidate charging node based on mobility, energy, and contextual trading features. This score is used as a guidance signal and as an explicit optimization objective rather than as a hard selection rule. The EV--EV matching problem is formulated as a multi-objective mixed-integer linear program that maximizes matching coverage, transferred energy, and charging-node suitability while minimizing mobility cost under spatial, temporal, one-to-one matching, and charging-node capacity constraints. To approximate Pareto-efficient solutions in wide-area dynamic settings, we develop a tailored non-dominated sorting genetic algorithm II (NSGA-II). Experimental results show that EVTradeMatch improves transferred energy by 74.2--82.8% and charging-node suitability by 8.3--84.4% compared with proximity- and auction-based state-of-the-art methods, while improving matching coverage by 3.74--25.07 percentage points. Balanced NSGA-II solutions achieve 53.07$\pm$0.76% matching coverage and transfer 1701.94$\pm$17.03 kWh, with higher mobility cost as an explicit trade-off against travel-minimizing methods. Pareto-front analysis shows that the framework supports flexible selection among high-coverage, high-energy, low-mobility-cost, and high-suitability solutions according to operational priorities.
