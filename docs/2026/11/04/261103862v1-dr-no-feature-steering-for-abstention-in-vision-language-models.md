# Dr. No: Feature Steering for Abstention in Vision-Language Models

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Farid Hasanov, Riccardo Renzulli, Bahram Zonooz, Mykola Pechenizkiy, Decebal Constantin Mocanu
- 机构：University of Turin, University of Luxembourg, Eindhoven University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03862v1) · [PDF](https://arxiv.org/pdf/2611.03862v1)

## TLDR
Dr. No is a training-free, inference-time feature-steering method that identifies sparse autoencoder features associated with abstention versus commitment and modulates them during the prefill pass of frozen vision-language models to improve the balance between answering and appropriately abstaining, with gains that depend on the source of unanswerability.

## Abstract
Large foundation models often answer even when the available visual or textual evidence is insufficient to support a reliable conclusion. This failure to abstain makes them hard to trust in high-stakes or information-seeking settings, where a confident but unsupported answer can be worse than no answer at all. It also raises a natural question: can the internal mechanisms behind this behaviour be identified and controlled at inference time? We present Dr. No, a feature-steering approach that mines sparse autoencoder (SAE) features associated with abstention and commitment, then modulates a small set of them during the prefill pass, without retraining the base model.
  Dr. No is evaluated on LLaVA-1.6 Mistral 7B across multimodal abstention benchmarks, including UNK-VQA and MM-UPD, and additionally benchmarked on language reasoning tasks using Qwen3.5-2B on AbstentionBench subsets. Against multiple uncertainty-based abstention baselines, feature steering achieves a more favourable balance between correct answering and appropriate abstention than post-hoc rejection methods. The gains are strongest on UNK-VQA and on MM-UPD cases involving image--question or question--answer incompatibility, and transfer most clearly to mathematical reasoning subsets of AbstentionBench. However, performance is more limited on absent-answer detection and retrieval-heavy multi-hop QA, such as MuSiQue. These results suggest that sparse internal features provide lightweight control handles for shaping uncertainty-aware behaviour in foundation models, while also showing that abstention control is source-dependent rather than governed by a single universal signal.
