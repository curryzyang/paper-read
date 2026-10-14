# SemTree: Judge-Aware Semantic Decision Trees for Inspectable and Repairable Rule Decisions

- 区域：速读区
- 排名：15
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Jincheng Gao, Wei Ding, Shuo Sun
- 机构：Xiamen University, The Hong Kong University of Science and Technology (Guangzhou)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13999v1) · [PDF](https://arxiv.org/pdf/2610.13999v1)

## TLDR
SemTree turns rule decisions into judge-aware semantic decision trees of natural-language Yes/No/Unknown questions, making each decision’s reasoning path inspectable and allowing targeted node-level repairs that improve accuracy and judge training.

## Abstract
Rule decisions such as content moderation, advertising compliance, and eligibility checks combine several conditions, exemptions, and missing-information cases, and an error can be fixed only once the failing condition is known. We introduce SemTree, a framework that represents a rule decision as a semantic decision tree: each node is a natural-language question with explicit Yes/No/Unknown criteria, a pluggable semantic judge answers it, and the branching structure is compiled on the answers that this judge actually gives. The executed path is the reasoning behind every decision, so errors are repaired where they occur: a reviewer corrects a single node and replays the rule, corrected nodes become training labels for the judge, and a tool-using LLM editor revises questions and subtrees while observing execution results. On all 8,276 ShARC test cases, a tree executed by a hosted judge reaches 67.70% accuracy with 2.99 questions per case, on par with asking the same judge for the final label (68.23%); an earlier tree compiled for a different judge scores 47.87% when executed by this judge, while a new tree compiled on this judge's answers to a 12-question initial pool already scores 64.39%. Node-level repair raises BANKING77 accuracy from 82.04% to 86.16%, an explicit exemption node cuts the false positives of a Chinese e-commerce moderation clause from 24 to 5, and a trained editor raises the development accuracy of edited trees from 64.47% to 73.35%.
