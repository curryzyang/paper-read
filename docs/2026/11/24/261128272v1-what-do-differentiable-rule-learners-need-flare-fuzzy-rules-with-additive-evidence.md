# What Do Differentiable Rule Learners Need? FLARE: Fuzzy Rules with Additive Evidence

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Javier Fumanal-Idocin, Javier Andreu-Perez
- 机构：University of Essex
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28272v1) · [PDF](https://arxiv.org/pdf/2611.28272v1)

## TLDR
This paper shows that rule weighting, rather than complex rule learning, drives most of the performance of differentiable rule learners, and introduces FLARE, a differentiable fuzzy rule learner with additive rule evidence and a learned categorical encoding that matches random forests on tabular benchmarks and outperforms existing rule learners.

## Abstract
Rule learners are used where transparency and accountability are required, because they give practitioners patterns they can read. Learning rules is a discrete problem, so neurosymbolic pipelines that use rules as explanations rely on relaxations such as the straight-through estimator. However, these differentiable rule learners often lag behind both classical rule learners and black-box classifiers in terms of performance. We study which parts of a rule-based classifier affect performance, and how well gradient-based training learns each of them. We found that most of the performance comes from how the rules are weighted: random rules with learned weights are already more accurate than every published differentiable rule learner we tested. Based on our results, we propose FLARE (Fuzzy Learned-Antecedent Rule Evidence), a differentiable rule learner that learns simple rules that combine to make the final decision. We also propose a learned encoding for variables with thousands of categories. We test FLARE on tabular data, using 42 datasets of OpenML-CC18 and the 38 classification tasks of TabArena. On CC18, FLARE exceeds the compared rule learners by 7.69 to 12.38 macro-F1 points and performs comparably to random forests, while remaining 1.00 to 1.11 points below tuned gradient-boosted trees. On TabArena it ranks at the same level as random forests and ahead of the other rule learners. As the concept-to-label head of a concept bottleneck model, FLARE is the best rule-based head in five of six settings. On graphs, it is competitive on PubMed and EMOGI but falls behind graph neural networks on Cora and Citeseer. Our code is available at https://github.com/Fuminides/FLARE
