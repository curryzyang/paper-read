# Data-DPO: Direct Preference Optimization for Target Model Data Selection in LLM Post-Training

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Peng Sun, Yi Yang, Antong Zhang, Chunxiao Li, Yanbo Wang, Dianbo Liu, xin chen, Kai Yu, Lu Chen, Tianfan Fu
- 机构：Fudan University, Nanjing University, Suzhou Laboratory, Shanghai Jiao Tong University, Brown University, North University of China, National University of Singapore
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16926v1) · [PDF](https://arxiv.org/pdf/2608.16926v1)

## TLDR
Data-DPO introduces a target-model-aware data selection method for SFT that uses one-step probing to derive pairwise data preferences, trains a lightweight reward model on them, and combines preference, quality, and diversity to select training subsets that consistently outperform existing baselines and even full-data training on Vision-Flan and LLaVA-CoT.

## Abstract
Data selection in supervised fine-tuning aims to select a small set of effective samples from large-scale candidate data, reducing training cost while preserving model performance. However, existing methods usually treat data value as a relatively static property, and pay limited attention to the compatibility between data and the capability distribution of the target model. To address this issue, we propose Data-DPO, a target model-oriented SFT data selection method. Data-DPO observes the local training feedback of the target model on different samples through one-step probing, transforms activation differences among samples into pairwise data preferences, and trains a lightweight reward model to learn target-model-aware data preferences. In the final selection stage, Data-DPO further combines target model preference, external quality scores, and marginal diversity to construct a more stable and effective training subset. Experimental results on Vision-Flan and LLaVA-CoT show that Data-DPO consistently outperforms existing data selection baselines under multiple data budgets and stably surpasses full data training performance.
