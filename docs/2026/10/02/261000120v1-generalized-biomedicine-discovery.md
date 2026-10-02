# Generalized Biomedicine Discovery

- 区域：速读区
- 排名：10
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Luyao Tang, Yingkai Yang, Hanqi Chen, Jiewei Zheng, Chaoqi Chen, Cheng Chen
- 机构：Shenzhen University, Xiamen University, The University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00120v1) · [PDF](https://arxiv.org/pdf/2610.00120v1)

## TLDR
The paper introduces Generalized Biomedicine Discovery (GBD), a unified benchmark for open-world medical image discovery under long-tailed, normal-dominant, and hierarchical conditions, and proposes SCAN, a cognition-inspired plug-in that suppresses expected patterns, amplifies surprising deviations, and integrates them to improve novel concept discovery while preserving known clinical knowledge.

## Abstract
In real-world clinical practice, medical images face open-world shifts: (i) long-tailed rare diseases, (ii) subtle lesions dominated by normal anatomy, and (iii) hierarchical taxonomies. Yet most open-world paradigms assume flat, balanced label spaces, leaving these biomedical demands unresolved. We introduce Generalized Biomedicine Discovery (GBD) and a unified benchmark spanning long-tail, anomaly, and taxonomy-aware discovery. Our key insight is that dominant known patterns form a visual manifold that masks subtle novelty. Inspired by expert diagnosis, we propose SCAN (Surprise-evoked Complementary AccommodatioN), which follows a cognition-inspired perceptual progression: it applies predictive suppression to filter expected norms, triggers surprise-evoked salience to highlight unexpected deviations, and performs complementary accommodation to integrate these shifts into global representations. Extensive experiments show that SCAN improves novel concept discovery while generally preserving established clinical knowledge, and it plugs into existing architectures to better navigate the known-unknown trade-off in medical imaging. Code is available at https://github.com/lytang63/generalized-biomedicine-discovery.
