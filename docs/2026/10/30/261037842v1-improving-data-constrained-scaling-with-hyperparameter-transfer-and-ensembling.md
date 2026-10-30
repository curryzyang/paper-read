# Improving Data-Constrained Scaling with Hyperparameter Transfer and Ensembling

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Ethan Baron, Shmuel Berman, Anirudh Satheesh, Akshay Vegesna, Samip Dahal, Andrew Gordon Wilson
- 机构：New York University, Q Labs, Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37842v1) · [PDF](https://arxiv.org/pdf/2610.37842v1)

## TLDR
This paper improves data-constrained scaling by transferring hyperparameters across scale and incorporating ensembling into scaling laws, yielding substantially lower validation loss and monotonic gains with compute compared with prior data-constrained recipes.

## Abstract
As growing compute budgets outpace the growth of high-quality training data, large language models must be trained with both compute and data constraints in mind. Unfortunately, existing prescriptions for data-constrained scaling suffer from two important limitations. First, past works hold key hyperparameters such as weight decay fixed with scale, despite the fact that optimal hyperparameters vary wildly with model size and number of epochs. Second, past works neglect ensembling, a promising axis for scaling under data constraints. As a surprising consequence, prior prescriptions can lead to loss that increases with compute budget. We address both limitations by fitting power laws that prescribe how to transfer hyperparameters with scale and scaling laws that prescribe how to allocate compute with ensembling. Training on 100M tokens from FineWeb, our recipe reduces validation loss by over 0.15 nats compared to prior recipes, a 14% decrease in perplexity, and achieves monotonic improvements with compute through ensembling. These gains are achieved using prescriptions fit to smaller runs and validated at up to 12$\times$ larger compute budgets.
