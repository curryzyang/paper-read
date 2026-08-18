# CutClean: Neural Network Pruning for Privacy-Preserving Inference

- 区域：速读区
- 排名：8
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Leonardo Magliolo, Vito Paolo Pastore, Giuseppe Valenzise, Enzo Tartaglione
- 机构：Institut Polytechnique de Paris, Istituto Italiano di Tecnologia, Universite Paris-Saclay, University of Genoa
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.13773v1) · [PDF](https://arxiv.org/pdf/2608.13773v1)

## TLDR
CutClean is a privacy-aware structured pruning method that uses auxiliary linear privacy heads to measure and minimize private information leakage in neural networks while increasing sparsity and preserving target task accuracy.

## Abstract
Neural networks are increasingly deployed in high-stakes applications with growing privacy leakage concerns. We show that this privacy leakage can occur even in the absence of representation imbalances that lead to traditional dataset biases. This poses significant privacy risks when deploying models that process sensitive attributes. In this context, we propose CutClean, a privacy-aware pruning method that allows to reduce privacy information flow through the network, while increasing its sparsity. Our approach employs auxiliary linear privacy heads placed at each network's block to quantify information leakage, and further applies increasing levels of sparsity to remove the private attribute leakage, measured in terms of the accuracy of the privacy head attached to the last block. Experiments on synthetic and real-world datasets demonstrate that our approach effectively minimizes private information flow while achieving high sparsity rates and preserving classification target accuracy.
