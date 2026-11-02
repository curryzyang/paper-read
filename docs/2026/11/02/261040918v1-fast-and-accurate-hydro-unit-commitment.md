# Fast and Accurate Hydro Unit Commitment

- 区域：速读区
- 排名：14
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Shaked Regev, Evan J. R. Brody
- 机构：Oak Ridge National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40918v1) · [PDF](https://arxiv.org/pdf/2610.40918v1)

## TLDR
The paper introduces a greedy heuristic for hydro unit commitment that achieves solution quality comparable to the leading commercial solver Hexaly while being up to 10,000× faster and scaling log-linearly, enabling scheduling of 1,792 generators for an entire year in about 20 seconds.

## Abstract
We introduce a fast novel algorithm to commit hydro-generators. We show that our algorithm can commit 56 generators for 200 days 10,000 times faster than Hexaly, the leading commercial solver for scheduling problems, without sacrificing solution quality. Our method can commit 1792 generators for an entire year in approximately 20 seconds on commodity hardware. Hexaly is unable to solve problems of this size in reasonable time. We attain this runtime improvement by introducing a greedy-heuristic tailored for hydro units. We provide a direction for a possible proof that the error our solver makes decreases with the problem size. This is supported by our experimental results. We prove that our solver's runtime scales log-linearly in the number of generators and time periods.
