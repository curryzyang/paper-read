# Ultra-Low-Energy Open-Circuit Fault Diagnosis for Three-Phase Inverters

- 区域：速读区
- 排名：1
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Xiaoyi Lei, Fanfu Wu, Yunting Liu
- 机构：The Pennsylvania State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.25037v1) · [PDF](https://arxiv.org/pdf/2607.25037v1)

## TLDR
The paper proposes an event-driven neuromorphic framework using a spiking neural network converted from a CNN to achieve ultra-low-energy (11 μJ per diagnosis, a 382× reduction vs. GPU-based CNN) and 100% accurate open-circuit fault diagnosis for three-phase inverters by exploiting the sparsity of current-vector trajectory matrices.

## Abstract
Embedded fault diagnosis in three-phase inverters must satisfy the sub-watt power budget of converter control hardware, but conventional convolutional neural network (CNN)-based methods require dense multiply-accumulate operations and impose substantial inference energy. This work proposes an event-driven neuromorphic framework for energy-efficient open-circuit (OC) fault diagnosis. A CNN trained on current-vector trajectory matrices is converted into a spiking neural network (SNN) and evaluated using the NengoLoihi framework with Loihi-based neuromorphic energy estimation. By exploiting the sparse structure of trajectory matrices, the SNN activates computation only in informative regions instead of processing the full feature map densely. Experiments on a three-phase inverter platform show that the proposed method achieves 11 microjoules per diagnosis, corresponding to a 382 times inference-energy reduction compared with a GPU-based CNN, while maintaining 100% diagnostic accuracy. Robustness is further validated under unbalanced loading, current amplitude step changes, and injected measurement noise.
