# Do Tabular Foundation Models Still Need Feature Engineering?

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Yifan WU, Pinjun Dong, Jiran Tao, Binyan Jiang
- 机构：The Hong Kong Polytechnic University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13202v1) · [PDF](https://arxiv.org/pdf/2609.13202v1)

## TLDR
A controlled study of TabPFN and TabICL shows that generic feature engineering becomes largely unnecessary for stronger tabular foundation models, with gains concentrated in earlier generations, while providing additional task-relevant in-context examples from related datasets still improves performance.

## Abstract
Feature engineering has long been a cornerstone of tabular machine learning. Tabular foundation models (TFMs) are pretrained on a wide range of tabular datasets and applied via in-context learning. Their rise raises a natural question: does manual feature construction still matter as these models become more capable? To answer this, we perform a controlled study across several versions of two major TFM families, testing a wide range of existing feature engineering techniques on benchmark datasets from TabArena. We find a consistent pattern: feature engineering gains are concentrated in earlier model generations and become negligible for the strongest models. These results suggest that stronger TFMs depend less on explicitly engineered input representations. In a complementary experiment, however, adding in-context information from related datasets still improves performance. Our findings indicate a shift in the source of performance gains for stronger TFMs: re-representing existing inputs becomes less effective, while providing additional task-relevant context remains beneficial.
