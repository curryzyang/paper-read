# Scaling Closed-Loop Feature Channel Configuration with LLMs

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Tolgay Atinc Uzun, Radu Timofte, Dmitry Ignatov
- 机构：University of Würzburg
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20516v1) · [PDF](https://arxiv.org/pdf/2607.20516v1)

## TLDR
Scaling closed-loop LLM-based channel configuration search to 250 candidates per cycle confirms a positive accuracy trend, improves parameter efficiency (best model: 36.76% accuracy with 11.8M parameters vs. 31.44% with 166.5M), and reveals architectural regularities such as frequent non-power-of-two channel widths and structured allocation patterns.

## Abstract
Promising initial results in closed-loop large-language-model-based channel-configuration search demonstrated that neural-network widths can be optimized directly through executable code generation and accuracy feedback. However, those results were obtained from a relatively sparse set of valid evaluations, leaving open whether the observed optimization behavior transfers to a denser sampling regime and whether additional architectural regularities emerge when more generated networks are evaluated. To test this, the same search setting is scaled to 250 candidate networks per fine-tuning cycle. The analysis covers 2000 generated candidates from 8 complete cycles, yielding 462 verified CIFAR-100 evaluations after task and metadata filtering. Per-cycle mean accuracy exhibits a positive linear trend with slope 9.87e-4 (p=0.043), while the high-performing frontier improves more strongly: the best observed accuracy increases from 0.3144 to 0.3676, and both the top-5 and top-10 cycle-level means exhibit positive trends. The scaled run also reveals improved parameter efficiency. The best model reaches 0.3676 with 11.8M parameters, compared with an early high-performing model at 0.3144 with 166.5M parameters. Beyond accuracy, the larger sample exposes architectural regularities that were difficult to assess from sparse observations. Non-power-of-two channel widths occur in 41.8% of verified candidates, and the strongest models share structured channel-allocation patterns characterized by moderate early widths and expanded middle or later blocks. These findings indicate that the channel-search signal observed in the initial study transfers
