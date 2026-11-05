# Objective-Conditioned Active Preference Learning for Multi-Objective Alignment

- 区域：速读区
- 排名：7
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Duc Anh Vu, Thong Nguyen, Hoang Pham, Ponhvoan Srey, Luu Anh Tuan
- 机构：National University of Singapore, VinUniversity, Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05506v1) · [PDF](https://arxiv.org/pdf/2611.05506v1)

## TLDR
OGC-DPO is an active preference learning framework for multi-objective LLM alignment that treats each (response pair, objective) as a separate query and selects those most expanding objective-specific gradient coverage via the policy’s own implicit gradient, improving alignment under fixed annotation cost while showing that informative preference conflicts can be useful rather than harmful.

## Abstract
Aligning large language models (LLMs) with several objectives, such as helpfulness, harmlessness, and honesty, typically relies on preference judgment for each objective, growing the annotation cost linearly with the number of objectives. Active preference learning can reduce this cost by selecting the comparisons whose labels are expected to change the policy most. Existing remedies either lack an objective-aware query selection mechanism for the multi-objective setting or regard conflicting preferences as harmful, therefore excluding them from the training data. We introduce OGC-DPO (Objective-conditioned Gradient Coverage DPO), an active learning framework that treats each (response pair, objective) combination as a separate query and measures its informativeness through the policy's own implicit gradient, without relying on an external reward model. OGC-DPO then selects the queries that most expand each objective's gradient coverage. Empirical experiments across varying numbers of objectives demonstrate the effectiveness of OGC-DPO over existing active preference learning methods under the same annotation cost. Further analysis demonstrates that informative conflicts, rather than being uniformly harmful, provide a useful policy training signal.
