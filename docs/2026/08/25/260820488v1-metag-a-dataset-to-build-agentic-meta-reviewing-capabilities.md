# Metag: A dataset to build agentic meta-reviewing capabilities

- 区域：速读区
- 排名：13
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Anirudh Sundar, Min Chen, Divya Tadimeti, Gemma Zhang, Alice Li, Nigel Boachie Kumankumah, Pavan Uttej Ravva, Sadid Hasan, Somya Chatterjee, Pruthvi Prakash Navada, Xiao Wang, Yue Kang, Sulaiman Vesal, Larry Heck
- 机构：Microsoft, Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20488v1) · [PDF](https://arxiv.org/pdf/2608.20488v1)

## TLDR
Metag is a new dataset of 349 human-annotated action items that link reviewer concerns from OpenReview to specific manuscript diffs, enabling agentic meta-reviewing tools to trace whether and where authors addressed feedback during the review-rebuttal process.

## Abstract
AI tools increasingly support tasks across the scientific research cycle, from experiment design and manuscript preparation to peer review. At the same time, the continuing growth in conference submissions has increased the burden on meta-reviewers, who must synthesize reviewer feedback, author rebuttals, and manuscript revisions. To address this concern, this paper introduces Metag, a dataset to accelerate the development of meta-reviewing agents, specifically to identify changes made to scientific articles during the review-rebuttal process. Each instance contains a reviewer concern, the author's proposed resolution, and the manuscript diffs implementing the stated change. Metag is collected by obtaining manuscript versions from before the review deadline and after acceptance, computing differences between the two documents, and asking human annotators to align these differences with action items from OpenReview discussions. The resulting dataset consists of 349 high-quality action items tied to paper differences and will enable building methods to empower meta reviewers to quickly identify whether authors have addressed reviewer statements and where in the paper those changes have been made, resulting in additional transparency and traceability throughout peer review. The dataset is publicly available at https://github.com/microsoft/Metag-dataset.
