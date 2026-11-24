# FoGConcept: Identifying Interpretable Movement Concepts for Freezing-of-Gait Detection from Multi-Scale IMU Signals

- 区域：速读区
- 排名：10
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Chuntian Chi, John Clapham, GinaMari Blackwell, Leslie Cloud, Ingrid Pretzer-Aboff, Yanfu Zhang, Huajie Shao, Gang Zhou
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28262v1) · [PDF](https://arxiv.org/pdf/2611.28262v1)

## TLDR
FoGConcept is a mechanism-based interpretability framework that discovers nine stable, expert-recognizable movement concepts from multi-scale IMU signals to explain and accurately detect freezing of gait in Parkinson’s disease, achieving a 94.2% F1 score.

## Abstract
Freezing of gait (FoG) is a disabling motor symptom of Parkinson's disease, characterized by an episodic inability to initiate or sustain effective stepping. Current inertial measurement unit (IMU)-based models can detect FoG accurately, but they fail to explain their predictions in terms of human-understandable movement concepts. A major contribution of this work is to identify nine human-understandable movement concepts encoded by a multi-scale FoG model, including gait initiation, rhythmic bilateral gait, trembling in place, shuffling steps, and pivot turns. These concepts recur across subjects, are functionally linked to the model's FoG decisions, and exhibit emergent specialization across short and long temporal contexts. Repeating the concept-discovery procedure on a new FoG dataset, wider temporal contexts, and a deeper backbone recovers the same comparatively stable set of movement concepts. Accordingly, we propose FoGConcept, a mechanism-based interpretability framework for learning movement concepts from multi-scale IMU signals. Domain experts independently recognize 88.9% of the identified concepts, while the proposed model achieves an F1 score of 94.2% for FoG detection. Our findings show that accurate FoG detection can be understood through human-recognizable movement patterns, providing new insight into what a detection model learns to distinguish FoG from non-FoG movement.
