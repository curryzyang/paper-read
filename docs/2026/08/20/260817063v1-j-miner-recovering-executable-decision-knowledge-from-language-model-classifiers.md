# J-Miner: Recovering Executable Decision Knowledge from Language-Model Classifiers

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Yunfan Gao, Xinyi Huang, Tao Sheng, Haorui Song, Yun Xiong, Haofen Wang
- 机构：Fudan University, Tongji University, Meituan
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17063v1) · [PDF](https://arxiv.org/pdf/2608.17063v1)

## TLDR
J-Miner extracts explicit, executable decision rules from fine-tuned language-model classifiers by mining vocabulary-aligned internal concepts, closely reproducing their decisions and enabling transfer to a much smaller standalone model.

## Abstract
Large language models can be fine-tuned into specialized classifiers that perform well across diverse text tasks and make complex judgments, but they typically expose only final labels, leaving the decision knowledge acquired through fine-tuning implicit within the model. We study how to mine this internal decision knowledge from a fine-tuned classifier and encode it in an executable representation that can be inspected, validated, and reused beyond the source classifier. We introduce J-Miner, which mines text-level named concepts by aggregating vocabulary-aligned internal signals across layers and token positions, and uses the classifier's own predictions to learn executable decision rules over them. This process distills local internal readouts into an explicit classifier-level knowledge representation. Across multiple classification tasks, J-Miner rules reproduce up to 98.3\% of source-classifier decisions and achieve 6.0--29.5 percentage points higher behavioral fidelity than equally compact rules learned from input words. Further analysis shows that the named concepts reflect internal semantic evidence associated with task decisions, while the learned rules consolidate these distributed signals into inspectable decision structures. The resulting decision knowledge also transfers to lightweight standalone students: using about 1/24 as many parameters as the source classifiers, they reconstruct and execute the representation from raw text while retaining 99.8\% of the source classifiers' mean task accuracy. These findings show that task-specific decision knowledge can be faithfully represented in an explicit, executable form and reused beyond the classifier in which it was learned.
