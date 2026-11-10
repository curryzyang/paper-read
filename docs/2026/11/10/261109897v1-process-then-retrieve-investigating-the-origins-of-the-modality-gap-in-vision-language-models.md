# Process then Retrieve: Investigating the Origins of the Modality Gap in Vision-Language Models

- 区域：速读区
- 排名：14
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Arpita Shanbhag, Julia Tran, Dhruv Mandala, Ayda Sultan
- 机构：Algoverse
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.09897v1) · [PDF](https://arxiv.org/pdf/2611.09897v1)

## TLDR
The paper shows that the vision-language modality gap arises because visually pre-encoded, semantically dense vision tokens enter the model before lower-density text tokens, causing early layers to process text first and integrate vision later—an asymmetry confirmed by replacing vision tokens with semantically similar text embeddings, which increases early cross-modal attention.

## Abstract
Understanding the origins of the modality gap in vision language models remains a significant challenge. This work investigates whether differences in information density between modality specific tokens at the embedding layer contribute to this imbalance. We show that text tokens enter the model with much lower semantic density than visual tokens, driving early layers to focus on processing text representations before combining them with vision. Through mechanistic analysis, we demonstrate that replacing vision token positions with their semantically closest text token counterparts elicits increased attention to those positions in early layers. These findings provide a foundation for addressing the modality gap and provide insight to improve multimodal reasoning in VLM architectures.
