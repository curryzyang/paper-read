# RoboPhys-3D: A Comprehensive Embodied World Model Evaluation via 3D Reconstruction

- 区域：速读区
- 排名：10
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Tianyi Wang, Jiazhou Chen, Yiming Xu, Xiangyu Li, Tianyi Zeng, Chih-Hsien Chou, Ning Lu, Liang Peng, Junfeng Jiao, Christian Claudel
- 机构：The University of Texas at Austin, Futurewei Technologies, Inc., Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28718v1) · [PDF](https://arxiv.org/pdf/2608.28718v1)

## TLDR
RoboPhys-3D is a comprehensive 3D-grounded benchmark for embodied world models that evaluates generated rollouts against reconstruction-matched ground truth through a unified 3D reconstruction pipeline, organizing 50 metrics across four levels to disentangle generation-induced errors and introduce task-aligned scores that strongly correlate with human judgment.

## Abstract
Video world models increasingly serve as data engines, action planners, and simulators for embodied AI, but conventional embodied world model (EWM) benchmarks lack a unified 3D-grounded protocol for establishing whether generated rollouts preserve the underlying 3D scene state or translate into executable actions. We introduce RoboPhys-3D, a 3D-grounded EWM benchmark built on RoboTwin 2.0, covering 50 manipulation tasks across four regimes, with 5,000 episodes and 25,000 multi-view ground-truth videos. A defining feature of RoboPhys-3D is that generated and ground-truth videos are processed through the same 3D reconstruction pipeline, enabling reconstruction-induced error to be distinguished from generation-induced error. The RoboPhys-3D benchmark organizes 50 complementary metrics into 18 sub-dimensions across four levels: pixel-level fidelity, 3D geometry consistency, state-level understanding, and task-level completeness. We further introduce Average Full Score, a hierarchical score averaging all 50 metrics for comprehensive evaluation, and RoboPhyscore, a compact task-aligned score averaging the metrics most strongly correlated with task success. Among the four representative video world models, Cosmos 3 achieves the highest RoboPhyscore (0.6330, 92.7% of ground truth), while state- and execution-grounded metrics reveal substantial failures that perceptual and vision-language model-based judgments fail to capture. RoboPhyscore further exhibits strong agreement with human evaluation (Pearson r = 0.9761 and Spearman \r{ho} = 0.8962), demonstrating the importance of grounded, execution-aware evaluation for EWM capability.
