# GPUSimBench: Towards Scalable and Reliable GPU-Accelerated Simulators in Embodied AI

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Huzhenyu Zhang, Shenghai Yuan, Wenrui Yan, Li Ma, Hengjie Li, Jingcheng Pang, Dmitry Yudin
- 机构：Nanyang Technological University, AXXX, Shanghai AI Laboratory, MIRAI, Nanjing University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13059v1) · [PDF](https://arxiv.org/pdf/2607.13059v1)

## TLDR
GPUSimBench exposes hidden scalability, physical consistency, and non-determinism trade-offs in GPU-accelerated robotic simulators to enable more reliable and reproducible robot learning.

## Abstract
Data-driven embodied AI is rapidly transitioning into a paradigm that scales training through massively parallel simulation, where GPU-accelerated simulators serve as the foundational data infrastructure. However, as computational throughput scales, the underlying trade-offs between parallel efficiency, physical fidelity, and execution determinism remain largely unexamined, hindering the development of reliable robot learning. In this paper, we expose the hidden limits of mainstream GPU-based robotic simulators (e.g., Isaac Lab, Genesis) by introducing GPUSimBench, which focuses on scalability, physical consistency, and computational determinism. First, GPUSimBench establishes a physical grounding evaluation with a controlled inclined-plane task, quantifying the distributional alignment between simulated dynamics and their real-world counterparts. Second, we benchmark parallel scalability by measuring throughput and memory footprints across scaling environment counts. Crucially, beyond standard performance metrics, we unveil and quantify the inherent non-determinism introduced by GPU-batched execution, characterized by significant run-to-run and inter-environment variability even under identical initial conditions. Finally, we identify four empirical regimes of stochasticity within current simulator stacks, highlighting that unbounded scaling can compromise reproducibility without explicit constraints.
