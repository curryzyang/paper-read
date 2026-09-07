# Quantum-Assisted Memory-Efficient Training for Parameter-Intensive Wi-Fi-Based Human Activity Recognition

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：To Truong An, Jie Zhang, Guolin Yin, Junqing Zhang, Yanjiao Li, Trung Q. Duong, Simon L. Cotton
- 机构：Queen's University Belfast, Memorial University, University of Science and Technology Beijing, University of Liverpool
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04271v1) · [PDF](https://arxiv.org/pdf/2609.04271v1)

## TLDR
Q-MET introduces a quantum-assisted hybrid classical-quantum framework that generates Wi-Fi HAR model parameters with 90–95% fewer trainable parameters and integrates structured pruning during training to achieve 75–85% sparsity with under 2% accuracy loss, making both training and inference memory-efficient.

## Abstract
Wi-Fi-based human activity recognition (HAR) has become an important part of integrated sensing and communications, paving the way for a range of context-aware services. However, most existing Wi-Fi-based HAR systems rely on deep learning (DL) models that are computationally and memory intensive in both training and inference, which poses significant challenges for real-world deployment. Conventional training requires simultaneous updates of millions of parameters, leading to prohibitive memory consumption. In this paper, we propose a novel quantum-assisted memory-efficient training framework (Q-MET) designed to improve efficiency in both training and inference. Q-MET utilizes a hybrid quantum classical neural network to indirectly generate parameters for HAR models, significantly reducing the trainable parameter count compared to direct optimization. To further support the deployment on resource-constrained devices, we integrate structured pruning during the training phase. Experimental results demonstrate that Q-MET achieves a 90% to 95% reduction in trainable parameters compared with conventional backpropagation-based DL training while maintaining or even exceeding classical classification accuracy. Additionally, Q-MET supports lightweight inference through structured pruning, achieving 75% to 85% model sparsity with less than 2% loss in classification accuracy. To the best of our knowledge, this work represents the first quantum-assisted approach to simultaneously tackle memory inefficiencies in both the training and inference stages of HAR systems.
