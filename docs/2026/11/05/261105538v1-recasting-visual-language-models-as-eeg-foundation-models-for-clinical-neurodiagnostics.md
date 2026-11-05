# Recasting Visual Language Models as EEG Foundation Models for Clinical Neurodiagnostics

- 区域：速读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Xin Zhou, Elena Sergeeva, Nan Bi, Wenyu Song, Lijun Yin, Hao Deng
- 机构：Harvard Medical School, Brigham and Women's Hospital, Massachusetts General Hospital, Binghamton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05538v1) · [PDF](https://arxiv.org/pdf/2611.05538v1)

## TLDR
Generalist vision-language models can serve as effective EEG foundation models for clinical neurodiagnostics, matching or outperforming EEG-specific foundation models on several tasks while showing stronger few-shot adaptability and model-size scaling without large-scale EEG pretraining.

## Abstract
Historically automated electroencephalography (EEG) systems was done using task-specific supervised models trained on purposely annotated data. A more recent modeling paradigm relies on creating a unified representation, or a 'foundation model', for multiple modality-specific tasks through large-scale domain-specific pretraining on the unannotated EEG signal. The quality of this unified representation directly depends on the availability of the modality-specific datasets. At the same time, generalist Vision Language Models (VLMs) exhibit broad few-shot learning capacities as well as good fine-tuning adaptability to different visual and language tasks. Can VLMs learn how to read and interpret EEG visually, emulating to a degree the way human clinicians inspect the EEG patterns? In this work we make a case that they can: we show that generalist VLMs without large-scale EEG pretraining perform competitively across a collection of clinical neuro-diagnostic tasks, can adapt to different tasks in a few-shot learning setting better than specialist foundation models, and exhibit better performance with model scaling when modality-specific models fail to exhibit.
