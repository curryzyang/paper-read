# H$^2$EDL: Hyper Evidential Deep Learning for Hierarchical Classification

- 区域：速读区
- 排名：8
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Yuanye Liu, Xiahai Zhuang
- 机构：Fudan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18185v1) · [PDF](https://arxiv.org/pdf/2608.18185v1)

## TLDR
H²EDL introduces a tractable hyper-evidential deep learning framework that places local Dirichlet opinions at each branching node of a label taxonomy, inducing a valid tree-structured hyper-opinion which jointly provides hierarchically consistent predictions and location-aware uncertainty, reducing calibration error by about half over cross-entropy baselines on hierarchical fine-grained benchmarks.

## Abstract
Fine-grained recognition often involves hierarchical label spaces, where a model may be confident about a coarse semantic concept while remaining uncertain among its descendant classes. Such structured ambiguity requires uncertainty representations that capture both fine-grained classes and intermediate concepts. However, existing tools each capture only half of it: flat evidential classifiers quantify total ignorance with a single vacuity on the leaf frame, and hierarchical classifiers propagate point probabilities with no notion of evidence. Hyper-opinions would unify the two, but their general form is exponential in the label count, and existing hyper-evidential networks either require composite labels to be supplied in the training data or read them off an unstructured weight pattern, with no principled notion of which composites deserve mass. We observe that the taxonomy itself is the missing hyperdomain. Its subtrees and leaf singletons form a linear-size focal family, and one local Dirichlet opinion per branching node induces every composite mass in closed form. The resulting model, H$^2$EDL, can be interpreted in two complementary ways using the same set of parameters. From a prediction perspective, it functions as a hierarchical classifier that preserves consistency across different levels of the label tree. From a probabilistic perspective, it defines a valid tree-structured hyper-opinion, where the mass assigned to each node represents the belief that reaches that node but does not provide sufficient confidence to further specialize into its descendants. On FGVC-Aircraft and DERM12345, H$^2$EDL reduces calibration error by approximately half compared with cross-entropy baselines, with the improvement becoming more pronounced at deeper hierarchy levels and under larger training budgets.
