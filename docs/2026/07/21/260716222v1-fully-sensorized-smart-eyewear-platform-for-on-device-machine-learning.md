# Fully-sensorized smart-eyewear platform for on-device Machine Learning

- 区域：速读区
- 排名：5
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Andrea Giudici, Christian Veronesi, Pietro Bartoli, Mario Caliò, Aurelio Teliti, Giacomo Gervasoni, Diana Trojaniello, Franco Zappa
- 机构：Politecnico di Milano, EssilorLuxottica
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16222v1) · [PDF](https://arxiv.org/pdf/2607.16222v1)

## TLDR
This paper presents ARGO, a fully sensorized smart-eyewear platform that achieves on-device machine learning for real-time urban obstacle recognition through a holistic co-design of hardware, firmware, and AI, leveraging an STM32N6 microcontroller with an integrated NPU to run an optimized YOLOv11 model with high efficiency and privacy.

## Abstract
This paper presents ARGO, a smart eyewear platform designed to bridge ergonomic comfort, high computational throughput, and energy efficiency. Unlike cloud-dependent solutions, ARGO leverages the STM32N6 microcontroller and its integrated Neural Processing Unit (NPU) to enable on-device machine learning, minimizing latency and preserving user privacy through local data processing. The primary contribution lies in the holistic co-design of hardware, firmware, and artificial intelligence, centered on the deployment of an optimized YOLOv11 model for real-time urban obstacle recognition. To ensure compatibility with the target NPU, we introduce Head-wise Parallel Attention (HPA), an architectural refinement that enables efficient accelerator execution while preserving the original computational logic. The model is trained on the Walking On The Road (WOTR) dataset, and the final deployed configuration achieves an mAP50-95 of 24 under strict memory constraints, with a memory footprint of only 2.483 MB. The platform integrates a multimodal sensor suite, RGB cameras, Time-of-Flight sensors, microphones, and ambient sensors, and delivers 10 FPS at a continuous autonomy of ~113 minutes on a 200 mAh battery. These results demonstrate the feasibility of a high-performance, privacy-preserving, and socially acceptable assistive device, and highlight how competitive edge AI solutions increasingly demand tightly integrated, multidisciplinary co-design approaches.
