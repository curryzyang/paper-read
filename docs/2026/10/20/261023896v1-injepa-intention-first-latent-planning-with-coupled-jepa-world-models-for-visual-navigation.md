# InJePA: Intention-First Latent Planning with Coupled JEPA World Models for Visual Navigation

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Siming Zhou, Bowen Ma, Ruiran Du, Pengcheng Zheng, Sheng Zheng, Dongshen Han, Zhijie Li, Wei Dong, Fan Mo, Chaoning Zhang
- 机构：University of Electronic Science and Technology of China, Xi'an University of Architecture and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23896v1) · [PDF](https://arxiv.org/pdf/2610.23896v1)

## TLDR
InJePA is an intention-first visual navigation framework that couples goal-conditioned and action-conditioned JEPA world models in a shared latent space, using predicted action consequences to iteratively guide latent intention generation and action inference in a closed loop.

## Abstract
Visual navigation requires goal directed planning informed by predictions of environment dynamics. Representative navigation world model methods propose complete action candidates before predicting consequences for selection or search updates. For each candidate, predictions primarily evaluate proposed actions rather than guide its stepwise construction. To this end, we propose InJepa, an intention first planning paradigm centered on latent states. A goal conditioned JEPA proposes latent intentions, and an action conditioned JEPA continually predicts future latent states. Both operate in a shared latent space to align their predictive representations. Within each candidate, predicted consequences feed into the next intention proposal and action inference, forming a closed loop of intention, action, and consequence. This extends the world model's role beyond evaluation to leading candidate construction through latent intentions. We evaluate InJepa through closed loop image goal navigation in Habitat MP3D. The results show effective multistep navigation through intention guided action generation and consequence feedback. Experiments across encoders further support applicability across visual representations. These findings support latent intentions as the central planning object and show that world models can directly guide plan construction through coordinated reasoning about intentions and consequences. Code is available at https://github.com/zhuxun132/InJepa.
