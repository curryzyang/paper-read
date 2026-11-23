# Parasite Features: Causal Abstraction Through Spurious Pathways

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Denis Sutter, Qing Yao, Sasha Boguraev, Julian Minder, Antonio Di Maio, Thomas Hofmann, Kyle Mahowald, Tiago Pimentel
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26711v1) · [PDF](https://arxiv.org/pdf/2611.26711v1)

## TLDR
This paper shows that causal-abstraction interpretability methods such as Distributed Alignment Search can falsely identify “parasite features” by exploiting spurious pathways that combine feature-discriminating and output-steering directions, making it appear that a model implements a feature when it does not.

## Abstract
Causal Abstraction defines a notion of \emph{equivalence} between a neural network and an algorithm, thus serving as a powerful framework for mechanistic interpretability. In this paper, however, we show the existence of a class of \emph{spurious features} which straightforwardly pass such equivalence tests. Suppose there are two directions in a model's representation space where: (i) one discriminates the input based on some feature, and (ii) the other steers the model towards a certain output. Interpretability methods based on Causal Abstraction (e.g., Distributed Alignment Search) can \emph{spuriously} simulate these directions' combined behavior by leveraging pathways passing through them, giving the impression that the model implements this feature. In such cases, we say the method discovered a \defn{parasite feature}. Experimentally, we show that Distributed Alignment Search finds parasite features using linear alignment maps in two tasks: syntactic agreement and two-digit addition. Our paper highlights an important consideration for Causal Abstraction and contributes to the ongoing debate about best practices for mechanistic interpretability.
