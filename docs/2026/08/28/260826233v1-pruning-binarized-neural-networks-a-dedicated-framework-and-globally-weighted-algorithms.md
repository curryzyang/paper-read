# Pruning Binarized Neural Networks: A Dedicated Framework and Globally Weighted Algorithms

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Roan Rubiales, Jean Pierre David
- 机构：Polytechnique Montreal
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26233v1) · [PDF](https://arxiv.org/pdf/2608.26233v1)

## TLDR
The paper proposes a PyTorch framework and a novel globally weighted pruning method for binarized neural networks that significantly improves the accuracy-versus-pruning-rate trade-off, achieving 70% pruning on VGG11 without accuracy loss.

## Abstract
Extreme compression of deep neural networks, up to full binarization, dramatically reduces memory footprint and arithmetic complexity, facilitating deployment on constrained edge hardware with field-programmable gate arrays (FPGAs) and microcontrollers. Although combining binarization with pruning promises additional efficiency gains, existing pruning strategies are ill-suited to binarized representations and rarely translate into meaningful hardware savings. We introduce a PyTorch-based, research-oriented framework that incorporates freezing and pruning mechanisms for designing and optimizing binarized neural networks. The framework enables rapid and reproducible evaluation of state-of-the-art approaches and the fast prototyping of new ones. Leveraging this framework, we propose a novel pruning method that accounts for the relative importance of learned parameters across abstraction levels. Such a global weighting mechanism consistently achieves a superior trade-off between model accuracy and pruning rate, achieving a 70% pruning rate on VGG11 with constant accuracy, while state-of-the-art results reach only 41% in the binarized setting.
