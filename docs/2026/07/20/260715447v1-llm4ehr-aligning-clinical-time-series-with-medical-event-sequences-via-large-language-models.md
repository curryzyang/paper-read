# LLM4EHR: Aligning Clinical Time Series with Medical Event Sequences via Large Language Models

- 区域：速读区
- 排名：9
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Jingteng Li, Alexander Capstick, Louise Rigny, Iona Biggart, Neil J Sebire, Payam Barnaghi
- 机构：UK Dementia Research Institute, University College London, Great Ormond Street Hospital, Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15447v1) · [PDF](https://arxiv.org/pdf/2607.15447v1)

## TLDR
LLM4EHR introduces a clinical foundation model that temporally aligns electronic health record (EHR) events and time series via a contrastive learning objective guided by a domain-adapted large language model, improving downstream task performance and cross-dataset transferability.

## Abstract
Recent research in clinical machine learning, focusing on outcome predictions in intensive care unit (ICU), has shifted from bespoke supervised models to foundation models, utilising modern representation learning methods. Here, foundation models are pre-trained on mixtures of complex clinical data modalities, useful for various downstream tasks. Existing works often utilise Electronic Health Records (EHR) to provide rich and diverse patient observations to train clinical foundation models. However, existing methods do not sufficiently explore the shared temporal structures between clinical events and time series (TS) observations recorded in EHRs. This limitation potentially leads to less robust and adaptive clinical foundation models, resulting in reduced performance on downstream tasks. To fully exploit this temporal structure, we propose LLM4EHR, a new clinical foundation model trained on ICU EHR data. Combining domain adapted large language models with a transformer TS encoder, we pre-trained LLM4EHR by temporally aligning the EHR events and TS. For this, we propose a regularised contrastive objective to learn robust EHR TS representations conditioned on EHR event embeddings produced by the domain adapted LLM. Supported by an ablation study, we find that learnt EHR TS embeddings from LLM4EHR improve performance on various downstream clinical tasks with competitive performance. Further, we empirically demonstrate that LLM4EHR learns transferable clinical TS embeddings that can be deployed to new cohorts via k-shot adaptation. These findings provide a step towards building more generalisable and performant clinical foundation models.
