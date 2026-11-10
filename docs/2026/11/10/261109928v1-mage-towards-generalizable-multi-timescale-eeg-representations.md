# MAGE: Towards Generalizable Multi-timescale EEG Representations

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Tuan-Kiet Doan, Van-Chien Nguyen, Trung-Hieu Tran, Quang-Hung Pham, Ngoc-Son Vu, Huy Phan, Phi Le Nguyen, Duc-Han Le, Nikola Simidjievski, Van-Tam Nguyen
- 机构：Institut Polytechnique de Paris, German Research Center for Artificial Intelligence (DFKI), Université de Technologie de Troyes, Hanoi University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.09928v1) · [PDF](https://arxiv.org/pdf/2611.09928v1)

## TLDR
MAGE is a multi-timescale EEG foundation model that uses multi-timescale tokenization, attention, and a trainable aggregator to dynamically adapt and fuse representations across temporal scales, consistently outperforming existing EEG foundation models with fewer parameters.

## Abstract
Electroencephalography (EEG) data plays an important role in understanding human brain activity, with various major applications. While current approaches, which largely build on EEG foundation models, have demonstrated strong performance across datasets and tasks, they typically rely on a fixed temporal scale. This design choice limits their ability to capture characteristics of neural dynamic behavior, often spanning across multiple timescales, which are naturally captured in EEG recordings. To address this limitation, we propose MAGE (\textbf{Multi-timescale Adaptive Generalization for EEG}), a foundation model that dynamically adapts to capture and integrate information across different timescales. Specifically, MAGE combines two key mechanisms: (i) a novel multi-timescale attention mechanism, capable of learning representations across multiple temporal scales and (ii) a trainable aggregation module, that dynamically identifies and adapts to the most informative timescale of the input signal. Experimental results across seven datasets demonstrate that MAGE consistently outperforms existing EEG foundation models while using substantially fewer parameters. Moreover, our results support the hypothesis that different downstream tasks benefit from distinct temporal scales. All source code will be released.
