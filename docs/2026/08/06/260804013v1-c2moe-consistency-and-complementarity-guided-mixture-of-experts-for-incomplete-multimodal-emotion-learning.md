# C$^2$MOE: Consistency and Complementarity-guided Mixture of Experts for Incomplete Multimodal Emotion Learning

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Yuntao Shou, Tao Meng, Wei Ai, Keqin Li
- 机构：Central South University of Forestry and Technology, State University of New York, New Paltz
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04013v1) · [PDF](https://arxiv.org/pdf/2608.04013v1)

## TLDR
C²MOE is a consistency and complementarity-guided mixture-of-experts framework that tackles incomplete multimodal emotion recognition by decoupling shared and modality-unique information via information-theoretic objectives and adaptive expert fusion, consistently outperforming state-of-the-art methods under missing-modality conditions.

## Abstract
Recent advances in Multimodal Emotion Recognition in Conversations (MERC) highlight its reliance on complete multimodal inputs. However, real-world data often suffer from missing modalities due to transmission errors or user behavior, severely degrading model performance. Existing methods enhance robustness via cross-modal consistency learning but largely ignore modality complementarity, leading to biased reconstructions. To address this limitation, we propose C$2$MOE, a novel Consistency and Complementarity-guided Mixture of Experts framework for incomplete multimodal emotion learning. Our approach unifies representation learning and missing modality imputation within a principled information-theoretic framework. Specifically, multimodal knowledge is factorized into consistency and complementarity components via interaction-aware experts. Consistency is captured by maximizing cross-modal predictability, while complementarity is preserved by maximizing conditional entropy between modalities. Building upon this decomposition, C$2$MOE introduces a dual-branch prediction mechanism for robust imputation under missing modalities. The consistency branch aligns imputed features with the joint distribution by minimizing uncertainty, and the complementarity branch exploits modality-unique cues via entropy maximization. Finally, C$2$MOE employs a learnable reweighting module that dynamically assigns importance scores to each expert's output, yielding a robust and adaptive fusion for imputation. Extensive experiments on multiple MERC benchmarks demonstrate that C$2$MOE consistently surpasses state-of-the-art methods across various missing-modality settings, validating its robustness and generalization.
