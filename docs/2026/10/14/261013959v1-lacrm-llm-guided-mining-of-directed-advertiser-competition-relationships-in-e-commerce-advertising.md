# LACRM: LLM-Guided Mining of Directed Advertiser Competition Relationships in E-Commerce Advertising

- 区域：速读区
- 排名：14
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Xiang Shi, Yitian Kou, Bing Li, Shengsheng Niu, Chun Gan, Linghui Meng, Jie He, Zhangang Lin, Ching Law
- 机构：JD.com, East China Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.13959v1) · [PDF](https://arxiv.org/pdf/2610.13959v1)

## TLDR
LACRM is an LLM-driven framework that mines directed, weighted advertiser competition graphs in e-commerce advertising via role-separated profiling, asymmetric multi-route retrieval, and listwise behavioral ranking, improving offline retrieval and raising production ad revenue by 1.73% for bidding and 1.14% for incentive allocation.

## Abstract
In e-commerce advertising, ad platforms typically fail to model the externalities among advertisers when making optimization decisions: an advertiser's actual performance is largely shaped by rivals competing for the same users; these rivals typically operate in overlapping product categories and at comparable budget scales. However, capturing this rivalry as an explicit, reusable signal is challenging because it is directed, multi-faceted, and partially observable. Existing paradigms such as interaction graphs, taxonomy rules, and single-embedding models do not fully capture these properties. In this paper, we propose LACRM (LLM-driven Advertiser Competition Relationship Mining), a novel framework that constructs directed competition graphs with continuous edge intensities via a three-stage pipeline. LACRM moves beyond symmetric similarity through LLM-driven role-separated profiling, which enables asymmetric multi-route retrieval to uncover both realized and latent rivals. The framework further incorporates listwise learning-to-rank aligned with temporal auction behavior to accurately model directed competition intensity. In offline retrieval experiments on an industrial benchmark, LACRM outperforms strong directed GNN baselines and ablation variants. Multi-LLM and human studies provide complementary evidence that the recovered latent rivals reflect meaningful market competition rather than merely model-generated artifacts. In production A/B tests, LACRM-guided bidding and incentive allocation increase advertising revenue by 1.73% and 1.14%, respectively. The results demonstrate the practical value of explicit competition modeling in large-scale advertising systems.
