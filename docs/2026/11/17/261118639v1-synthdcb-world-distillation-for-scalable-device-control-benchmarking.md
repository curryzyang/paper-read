# SynthDCB: World Distillation for Scalable Device Control Benchmarking

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Zichen Zhu, Dingye Liu, Nan Jiang, Danyang Zhang, Hang Zheng, Shijie Zheng, Situo Zhang, Kunyao Lan, Yingzi Ma, Sheng Jiang, Lu Chen, Kai Yu
- 机构：Nanyang Technological University, Jiangsu Key Lab of Language Computing, Shanghai Jiao Tong University, Shanghai Innovation Institution, University of Wisconsin–Madison, AISpeech Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18639v1) · [PDF](https://arxiv.org/pdf/2611.18639v1)

## TLDR
SynthDCB is a scalable device-control benchmark that uses “world distillation” to convert device-behavior knowledge into modular executable worlds and validated tasks across Home, Car, and Phone domains, enabling efficient, extensible, and verifiable evaluation of agents’ environment awareness and control capabilities.

## Abstract
Scaling device-control evaluation requires scaling both the worlds agents interact with and the tasks they must solve. We introduce SynthDCB, a scalable benchmark for environment awareness and device control built through world distillation. World distillation transforms knowledge of device behaviors, interaction constraints, and environmental effects into modular executable components, which are composed into interactive worlds with explicit states, actions, and temporal dynamics. A unified capability representation connects tool discovery, world execution, and task synthesis, allowing new capabilities to enter evaluation through a shared construction pipeline. SynthDCB instantiates Home, Car, and Phone domains with 114 device classes, 1,166 functions, and 95 events, supporting five task families with 32 subtypes. The stateful design enables task validation and agent evaluation through state correctness and tool-call traces. We evaluate seven models on 2,560 test tasks; the best achieves 68.2% Pass@1. Error analysis reveals challenges in answer delivery, feasibility diagnosis, and temporal coordination. Construction experiments demonstrate scalability across domains and token efficiency: world distillation reduces token consumption by 0.9-66.0% and 46.2-92.5% relative to Codex with low and xhigh reasoning effort, respectively, while achieving broader capability coverage. SynthDCB makes executable world construction the basis of scalable device-control benchmarking, connecting an expanding space of capabilities and interactions to verifiable agent evaluation.
