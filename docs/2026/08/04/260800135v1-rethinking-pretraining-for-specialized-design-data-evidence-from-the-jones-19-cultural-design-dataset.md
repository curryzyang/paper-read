# Rethinking Pretraining for Specialized Design Data: Evidence from the JONES-19 Cultural Design Dataset

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Alexandros Haridis, Charles Zhou
- 机构：Harvard University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00135v1) · [PDF](https://arxiv.org/pdf/2608.00135v1)

## TLDR
On a small, specialized cultural design dataset (JONES-19), ImageNet pretraining boosts CNN classification accuracy, but training from scratch with multi-crop augmentation largely recovers those gains, suggesting that curated, high-quality domain-specific data can rival massive general-purpose pretraining.

## Abstract
Design and architectural archives encode expert human knowledge in graphical formats, providing a critical testbed for design-inspired Machine Learning (ML) challenges absent with typical computer vision benchmarks. Building on JONES-19, a small-size image dataset based on The Grammar of Ornament (London, 1857), we evaluate the discriminative performance of Convolutional Neural Networks (CNNs) in two model training strategies: (a) ImageNet pretraining for domain-general "visual common sense," and (b) learning from scratch on the design data in JONES-19. We find that while domain-general priors improve discriminative performance, learning from scratch augmented with repeated local sampling (multi-crop) effectively recovers these gains. For highly structured design data, local design-driven representations provide sufficient foundation for learning, challenging a reliance on massive general-purpose pretraining. These findings suggest that in specialized design domains, careful curation of smaller high-quality datasets that capture empirical and formal design principles may prove more effective and informative on the nature of a particular design domain than prioritizing large-scale data collection.
