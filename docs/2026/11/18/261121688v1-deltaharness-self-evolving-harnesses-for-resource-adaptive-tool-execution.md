# DeltaHarness: Self-Evolving Harnesses for Resource-Adaptive Tool Execution

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Lecheng Yan, Jianze Lin, Xicheng Han, Xiantao Xu, Wenxi Li, Chenyang Lyu
- 机构：Zhejiang University, Dmall Inc., East China Normal University, University of Science and Technology of China, Beijing Normal University, Alibaba Group
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21688v1) · [PDF](https://arxiv.org/pdf/2611.21688v1)

## TLDR
DeltaHarness is an execution-guided policy-search method that self-evolves tool-execution harnesses by using cold-start runtime measurements to adapt dispatch, revise physical plans, and select informative experiments, thereby reducing latency under varying resources.

## Abstract
Tool-using agents rely on execution harnesses to organize and schedule tool operations. The same task and resource description can conceal runtime conditions that reverse the latency ordering of valid execution plans. Resolving this uncertainty requires firsthand execution in the target setting. We introduce DeltaHarness, an execution-guided policy-search method that adapts agent harnesses from cold-start measurements. Its QHI loop uses the observed response to update runtime dispatch, revise physical plans, and select experiments for later proposals. An independent confirmation panel controls policy replacement. With fixed dispatch, a revised materialization policy reduces complete-delivery latency by 30.0% on one video-editing task across three fresh pairs. On held-out tasks, the evolved policies reduce latency by 8.2% relative to the best fixed plan in one seed and by 4.6% relative to the initial proposal in another.
