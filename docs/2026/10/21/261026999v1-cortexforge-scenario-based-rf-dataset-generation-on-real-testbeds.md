# CorteXforge: Scenario-Based RF Dataset Generation on Real Testbeds

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Andréa Joly, Leonardo S Cardoso, Jean-Marie Gorce
- 机构：INSA Lyon, Inria
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26999v1) · [PDF](https://arxiv.org/pdf/2610.26999v1)

## TLDR
CorteXforge is a scenario-based framework that automatically translates high-level RF scenarios into synchronized over-the-air experiments on programmable SDR testbeds to generate realistic, reproducible, fully annotated SigMF datasets, validated via the ModForge modulation-classification dataset, which reveals a synthetic-to-real performance gap and shows that synthetic pretraining aids adaptation to OTA data.

## Abstract
Deep learning for radio frequency (RF) signal analysis relies on large annotated datasets, yet synthetic datasets trade physical realism for controllability, while uncontrolled over-theair measurements offer realism but limited reproducibility. We present CorteXforge, a scenario-based framework for generating realistic and reproducible RF datasets on programmable software defined radio (SDR) testbeds. High-level RF scenarios are automatically translated into synchronized experiments executed on the SLICES-RI/CorteXlab platform, producing fully annotated Signal Metadata Format (SIGMF) datasets that capture hardware impairments and propagation effects. We validate CorteXforge through automatic modulation classification using ModForge, an over-the-air (OTA) dataset generated with the framework. Cross-domain experiments reveal a synthetic-to-real performance gap and show that synthetic pretraining remains beneficial for adaptation to OTA data. CorteXforge provides a practical foundation for reproducible RF dataset generation and future research on domain generalization.
