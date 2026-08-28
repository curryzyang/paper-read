# Cross-Platform Benchmark of Neural 3D Reconstruction for Autonomous Laboratory Robots

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yongho Kim, Mengjiao Han, Victor Mateevitsi, Silvio Rizzi, Michael E. Papka, Nicola Ferrier
- 机构：University of Illinois Chicago, Argonne National Laboratory, Northwestern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26383v1) · [PDF](https://arxiv.org/pdf/2608.26383v1)

## TLDR
This paper benchmarks neural 3D reconstruction methods (NeRF, 3D Gaussian Splatting, and SAM3D) across compute platforms from edge devices to HPC nodes, finding that Gaussian Splatting offers better rendering quality at higher GPU cost, onboard compute is insufficient for interactive per-scene optimization, and SAM3D is fast but less accurate—motivating a tiered reconstruction pipeline for autonomous laboratory robots.

## Abstract
Autonomous robots performing laboratory tasks depend on 3D reconstruction pipelines that can turn raw camera streams into actionable object representations within the latency budget of a physical control loop. Neural 3D reconstruction methods have demonstrated high-quality view synthesis, but their real-time viability across the compute platforms on which laboratory robots actually run remains poorly characterized. In this work, we present a systematic compute-platform benchmark of neural 3D reconstruction methods, evaluating NeRF and 3D Gaussian Splatting training and rendering on GPU-enabled computing devices ranging from single-board computers to server-class nodes, and place Meta's SAM3D single-image reconstruction on the same axes to quantify its latency and fidelity gap relative to per-scene optimization. Our results show that Gaussian Splatting yields higher rendering quality than NeRF at greater GPU cost, and that onboard compute is insufficient for full per-scene optimization at interactive rates. Our preliminary assessment on SAM3D indicates that it delivers plausible object geometry within seconds, but with detail mismatches that can compromise downstream manipulation. Together, these findings motivate tiered pipelines in which lightweight feed-forward reconstruction sustains the real-time perception-and-tracking loop for laboratory robots, while heavier neural reconstruction is scheduled selectively on suitable compute.
