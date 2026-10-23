# GANet: A Lightweight Group Attention Network for Plant Disease Identification on Embedded Systems

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Anubhab Tripathi, Bibek Das, Asfak Ali, Sheli Shinha Chaudhuri
- 机构：Jadavpur University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30225v1) · [PDF](https://arxiv.org/pdf/2610.30225v1)

## TLDR
GANet is a 0.001M-parameter lightweight group-equivariant attention network that identifies 38 plant disease types with 99.99% accuracy on PlantVillage and enables real-time edge deployment at 5–11 FPS on Raspberry Pi 4B and Jetson Nano.

## Abstract
Global warming and climate change are major catalysts for plant diseases, significantly affecting food production worldwide. Addressing this issue requires continuous monitoring and early detection of plant diseases. While recent advancements in deep learning offer potential solutions, most models demand high processing power and struggle to perform efficiently on low-end electronic hardware. Furthermore, many existing works focus on specific crop diseases, limiting their broader applicability. This paper presents a lightweight Group Equivariance Attention Network (GANet) designed for the prediction and monitoring of 38 types of plant diseases. GANet introduces a novel Group Attention block and Group-Wise Feature Fusion block, making it both sparse and efficient. With only 0.001M parameters, the model achieves an impressive 99.99% accuracy on the PlantVillage dataset. Additionally, GANet is optimized for deployment on edge devices such as the Raspberry Pi 4b and Jetson Nano, where it reaches 5 FPS and 11 FPS, respectively, demonstrating its potential for real-time plant disease monitoring on low-power devices.
