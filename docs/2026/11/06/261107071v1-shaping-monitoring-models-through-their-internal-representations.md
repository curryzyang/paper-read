# Shaping & Monitoring Models through their Internal Representations

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Thomas Fel, Matthew Kowal, Matt Feiszli, Satchel Grant, Andrew Lee, Chris Earls, Fatih Dinc, Vasudev Shyam, Usha Bhalla, Leon Bergen, Siddharth Boppana, Ching Fang, Michael Byun, Tristan Gallent, Nicholas Wang, Tal Haklay, Dron Hazra, Neehar Kondapaneni, Connor Watts, Ryan Panwar, Thomas Dooms, Jack Merullo, Atticus Geiger, Ekdeep Singh Lubana, Thomas McGrath, Owen Lewis
- 机构：Goodfire
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07071v1) · [PDF](https://arxiv.org/pdf/2611.07071v1)

## TLDR
The paper proposes **Mechanistic Shaping**, a unified framework that uses internal representations during training to control which concepts a model expresses or relies on—reducing targeted behaviors while preserving task performance and largely maintaining monitorability across domains, scales, and training paradigms.

## Abstract
We propose Mechanistic Shaping, a unified framework for shaping models through their internal representations. Mechanistic Shaping is applied during training so that models follow specifications (rules) about which concepts they express, measured via their outputs or internal representations (e.g., no harmful content), and also which concepts they rely on, i.e., what they use to make their decisions (e.g., not a candidate's gender when screening a résumé). Across multiple domains (vision, medical imaging, language), scales (up to 32B parameters), and training paradigms (classification, SFT, DPO, GRPO), we find that Mechanistic Shaping substantially reduces targeted behaviors while preserving task performance. Since training against a representation can also modify it, we ask whether shaped concepts remain monitorable, a question that depends on the class of monitors considered. We therefore introduce a hierarchy of such classes, which separates a concept that escapes one probe from a concept that is truly gone. We characterize three geometric mechanisms of circumvention: the concept can drift away from the monitor, be erased from the layer, or persist in higher-order statistics as a nonlinear encoding, which we explain through a product-code construction. Although other mechanisms may arise in different settings or at larger scales, these three account for all of our observations, and each can be detected by a matching monitor. In practice, we find that shaped concepts largely remain monitorable: refitted linear probes recover the concept in most settings, and the original probe remains reliable whenever gradients do not flow through it. Taken together, these results point to the potential of using interpretability as a tool for training, and call for a correspondingly rigorous science of interpretability-based training.
