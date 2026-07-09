# UASPL: Uncertainty-Aware Self-Paced Learning with Evidential Neural Networks

- 区域：速读区
- 排名：4
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Yifan Zhang, Yuxin Hu, Zhuobin Hao, Xiaozhuan Gao, Lipeng Pan
- 机构：Northwest A&F University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06638v1) · [PDF](https://arxiv.org/pdf/2607.06638v1)

## TLDR
UASPL introduces a novel uncertainty-aware self-paced learning framework that integrates evidential neural networks into sample selection, improving classification performance, interpretability, and generality over traditional SPL methods by prioritizing reliably simple samples based on predictive uncertainty rather than loss alone.

## Abstract
Self-paced learning (SPL) is an effective learning paradigm that simulates the human learning process by progressing from easy to difficult samples based on the value of the loss function during the learning process. It has shown great potential in improving model performance and training efficiency. However, the prediction results of samples with smaller loss values are not necessarily reliable, indicating that such samples are not always simple samples for the model. Hence, this article proposes an uncertainty-aware self-paced learning based on evidential neural networks, termed UASPL, which integrates predictive reliability into sample selection through a general loss function within the Subjective Logic framework. This loss function incorporates uncertainty estimation and can be extended to different variants of SPL. Moreover, this loss function couples a sample selection preference, thereby ensuring the interpretability of the sample selection process. Finally, the experimental results on multiple datasets show that UASPL outperforms other SPL methods in terms of classification performance, interpretability, and generality. The source code is available at: https://github.com/treelife979/UASPL.
