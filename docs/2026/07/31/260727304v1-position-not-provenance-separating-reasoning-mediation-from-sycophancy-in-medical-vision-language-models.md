# Position, Not Provenance: Separating Reasoning Mediation from Sycophancy in Medical Vision-Language Models

- 区域：速读区
- 排名：15
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Supratik Bhowal, Subhrajyoti Basu, Aritra Gir Mahanta, Anik Pal Chowdhury
- 机构：Indian Institute of Information Technology, Kalyani, Heritage Institute of Technology, IEM Kolkata, School of UEMK
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27304v1) · [PDF](https://arxiv.org/pdf/2607.27304v1)

## TLDR
Medical vision-language models often generate chain-of-thought reasoning that does not actually drive their predictions, and a new framework, CoT-Mediate, shows that whether such reasoning is faithfully followed depends more on how it is injected—specifically via prefix-forced continuation rather than re-prompting—than on its attributed source, revealing that contextual position, not stated provenance, determines reasoning mediation in medical VLMs.

## Abstract
Medical vision-language models (VLMs) generate chain-of-thought (CoT) reasoning before answering clinical questions, but whether this reasoning causally influences predictions remains unclear. We present CoT-Mediate, a behavioral framework that perturbs a single clinically meaningful attribute within a model's own generated reasoning and measures whether the resulting prediction follows the edited reasoning. Our framework combines a dual-arm protocol comparing re-prompted evidence with prefix-forced continuation, together with a provenance-controlled intervention that varies only the attributed source of identical reasoning to disentangle reasoning mediation from sycophancy. We evaluate LLaVA-Med and MedGemma on 1,000 VQA-RAD samples each. Prefix-forced continuation consistently yields higher mediation faithfulness than re-prompting, while the provenance analysis reveals distinct model-specific deference behaviors. Across both models, removing visual evidence increases reliance on injected reasoning, whereas laterality is the least faithfully tracked clinical attribute. These results show that the mechanism used to inject reasoning substantially affects measured faithfulness and that contextual position, rather than stated provenance, is the primary determinant of whether medical VLMs use their generated reasoning.
