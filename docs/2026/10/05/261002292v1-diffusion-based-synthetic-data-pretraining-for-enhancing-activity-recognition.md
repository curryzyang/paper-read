# Diffusion-Based Synthetic Data Pretraining for Enhancing Activity Recognition

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：E. Riveros, D. Vega-Oliveros, A. Soriano-Vargas, A. Rocha
- 机构：State University of Campinas, Universidad de Ingeniería y Tecnología, Federal University of São Paulo
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02292v1) · [PDF](https://arxiv.org/pdf/2610.02292v1)

## TLDR
This paper proposes a two-stage pipeline that pre-trains a CABiGRU activity-recognition model on diffusion-generated synthetic smartwatch sensor data and then fine-tunes it on real data, achieving 90.6% balanced accuracy for eating/drinking recognition under class imbalance.

## Abstract
Human activity recognition (HAR) is increasingly important for healthcare, well-being, and daily monitoring ap- plications, for which detecting alimentary activities such as eating and drinking can provide actionable insight into dietary habits and chronic disease management. HAR systems, however, often underperform on subtle and underrepresented classes, limiting their utility in real-world dietary monitoring. This work builds upon CABiGRU, a convolutional architecture with Bidirectional GRU layers, multi-head attention, and residual connections, designed to capture discriminative temporal patterns from smart- watch accelerometer, gyroscope, and magnetometer data. To improve CaBiGRU's generalization and reduce underfitting in the minority class, we leverage synthetic sensor data windows using a diffusion model and adopt a two-stage training strategy: pre-training CABiGRU on synthetic data, followed by fine-tuning on the real-world data. On the DEO (drinking/eating/other) dataset, the proposed pipeline achieves a balanced accuracy of 90.6%, improving over a strong supervised baseline and showing the benefits of diffusion-based synthetic pre-training for recognizing alimentary activities and representing a step forward dealing with unbalanced classes. These results suggest that combining diffusion-generated data with targeted fine-tuning enhances robust recognition of dietary behaviors, supporting more reliable deployment in healthcare and nutrition-monitoring settings.
