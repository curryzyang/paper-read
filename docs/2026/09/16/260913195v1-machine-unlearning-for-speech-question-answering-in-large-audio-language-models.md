# Machine Unlearning for Speech Question Answering in Large Audio-Language Models

- 区域：速读区
- 排名：8
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Zhe Liu
- 机构：Meta Platforms, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13195v1) · [PDF](https://arxiv.org/pdf/2609.13195v1)

## TLDR
This paper presents and evaluates machine unlearning strategies for speech question answering in large audio-language models, showing that gradient ascent, task arithmetic, and alignment-based refusal fine-tuning can reduce private information leakage by up to 80% while largely preserving non-private speech QA and general audio understanding performance.

## Abstract
Large Audio-Language Models (LALMs) have recently shown strong capabilities in speech understanding and question answering (QA), but they also inherit privacy risks from large-scale training data, including the unintended memorization of sensitive information. In this work, we study machine unlearning for speech QA in LALMs, a setting that is more challenging than prior work on text-based Large Language Models (LLMs) or Automatic Speech Recognition (ASR) due to the tight coupling between acoustic perception and factual knowledge. We present and evaluate multiple unlearning strategies, including gradient ascent, task arithmetic, and alignment-based fine-tuning methods that enforce safe refusal responses, to remove private knowledge while still preserving performance on core capabilities. Through extensive experiments on speech QA datasets, we show that these unlearning methods can reduce the privacy leakage rate by up to 80% while maintaining near-neutral performance on non-private speech QA and general speech understanding benchmarks.
