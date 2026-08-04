# Progressive$^2$: A Teacher-Student Progressive Co-Evolving Knowledge Distillation Method for Substantial Model Compression

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Tiancong Cheng, Ying Zhang, Zhiwen Yu, Yifang Yin, Bin Guo
- 机构：Northwestern Polytechnical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00129v1) · [PDF](https://arxiv.org/pdf/2608.00129v1)

## TLDR
Progressive² is a knowledge distillation method that bridges large teacher-student capacity gaps for substantial model compression by progressively strengthening the teacher's layer-wise knowledge and gradually shrinking the student network in a co-evolving curriculum.

## Abstract
Knowledge distillation (KD) is a widely utilized technique for transferring knowledge from a large model (the teacher) to a smaller model (the student). Owing to its flexibility and broad applicability, KD has been extensively applied in the compression of server-side models to meet the Quality of Service (QoS) requirements of client users. Despite significant advancements, the performance of distillation is substantially compromised when a large disparity exists between the capabilities of the server and the requirements of the client. To alleviate this problem, we propose a novel distillation approach, named Progressive$^2$, which operates through the combination of a progressively stronger teacher and a progressively smaller student. On the side of the teacher, rather than involving all layers simultaneously, we progressively select additional layers for distillation following a raw-to-rich semantic progression, establishing a systematic learning curriculum. Furthermore, we design a teacher-side multi-feature fusion adapter for the teacher to improve training stability, which is theoretically supported by the framework of Lipschitz continuity. On the side of the student, rather than directly training a tiny model, we gradually reduce the size of the network to facilitate an iterative co-evolution with the teacher. Progressive$^2$ serves as a flexible framework; the progressive strategy of the teacher can be deployed independently to achieve an optimal balance between accuracy and training efficiency, while the joint integration of the teacher and the student yields further improvements in overall performance.
