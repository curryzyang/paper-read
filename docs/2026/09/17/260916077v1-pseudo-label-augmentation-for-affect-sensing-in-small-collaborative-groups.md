# Pseudo-Label Augmentation for Affect Sensing in Small Collaborative Groups

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Meisam Jamshidi Seikavandi, Tanya Ignatenko, Fabricio Batista Narcizo, Paolo Burelli, Jesper Bünsow Boldt, Andrew Burke Dittberner
- 机构：IT University of Copenhagen, GN Hearing
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16077v1) · [PDF](https://arxiv.org/pdf/2609.16077v1)

## TLDR
This paper studies pseudo-label augmentation for sparse physiological affect sensing in small collaborative groups, finding that while augmentation improves known-team VAD prediction, Big Five personality similarity mainly acts as a same-team filter rather than a fine-grained trust signal, with cross-subject transfer encouraging but strict unseen-group transfer still limited.

## Abstract
Physiological affect sensing in naturalistic group interaction is often limited by sparse labels rather than sensor data: wearable devices produce many time windows, while self-reports are collected only a few times per session. Using GroupAffect-4, a four-person collaborative dataset with wearable physiology, eye tracking, Big Five personality, and post-task VAD labels, we study pseudo-label augmentation for affect sensing under sparse supervision. We compare no augmentation, Gaussian Process pseudo-labelling, personality-aware trust weighting, and joint personality-plus-confidence weighting within a shared target-construction pipeline. Results show that pseudo-label augmentation improves over the labelled-only baseline in the known-team setting. However, the narrow range of Big Five cosine similarities (0.91-0.99) makes fine-grained personality weighting ineffective; personality similarity functions mainly as a same-team filter rather than a calibrated trust signal. With smoothing, augmented SVM variants are effectively tied on Valence and Arousal, while the joint personality-plus-confidence variant gives the highest Dominance score. Cross-subject LOSO transfer remains encouraging, especially for Arousal, whereas strict session-isolated LOGO removes the augmentation benefit. Given only 10 groups, LOGO should be interpreted as a conservative lower bound on unseen-group transfer. Overall, the results suggest that pseudo-label augmentation can make better use of sparsely labelled collaborative affect data, while personality information is most useful as a within-team selection mechanism.
