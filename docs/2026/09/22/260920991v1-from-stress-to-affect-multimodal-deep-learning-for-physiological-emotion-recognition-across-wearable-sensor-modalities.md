# From Stress to Affect: Multimodal Deep Learning for Physiological Emotion Recognition Across Wearable Sensor Modalities

- 区域：速读区
- 排名：15
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Desta Haileselassie Hagos, Saurav Keshari Aryal, Legand L. Burge
- 机构：Howard University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20991v1) · [PDF](https://arxiv.org/pdf/2609.20991v1)

## TLDR
This paper comparatively evaluates bidirectional LSTM, TCN, and Transformer models for physiological emotion recognition on WESAD and EmoWear across wrist-only, chest-only, and multimodal wearable sensing, finding that multimodal inputs consistently perform best, that no single architecture is universally superior (Transformer leads on WESAD while LSTM leads on EmoWear), and that 4 Hz offers a practical accuracy-efficiency trade-off.

## Abstract
Physiological emotion recognition using wearable sensors has important applications in mental health monitoring, affective computing, and human-computer interaction. However, existing studies typically evaluate a single model, sensing configuration, or dataset, limiting our understanding of how these factors influence recognition performance. We present a comparative study of temporal deep learning architectures for physiological emotion recognition using two multimodal wearable datasets: WESAD and EmoWear. Bidirectional long short-term memory (LSTM), temporal convolutional network (TCN), and Transformer models are evaluated under wrist-only, chest-only, and multimodal sensing configurations using participant-independent leave-one-subject-out cross-validation (LOSO-CV). We also investigate soft-voting ensembles, sensor ablation, sampling frequency, and gradient-based saliency. The Transformer achieved the highest multimodal accuracy on WESAD (99.02% +/- 0.51%), whereas the LSTM achieved the best multimodal accuracy on EmoWear for both arousal (91.80% +/- 1.06%) and valence (89.96% +/- 0.36%). These results show that relative architecture performance depends on dataset characteristics rather than one architecture being uniformly superior. Multimodal sensing consistently outperformed wrist-only and chest-only configurations across both datasets. Sampling-frequency analysis showed that 4 Hz provides a practical operating point, with performance comparable to higher frequencies at substantially lower training cost. These findings provide guidance for selecting architectures, sensing modalities, and sampling frequencies for wearable physiological emotion recognition.
