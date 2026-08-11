# Latent Fact-Checking: Detecting Misinformation through Activation Engineering

- 区域：速读区
- 排名：8
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Pedro Barcelos, Otávio Parraga, Marcelo M. Mussi, Lucas M. Fraga, Lucas S. Kupssinskü, Rodrigo C. Barros
- 机构：PUCRS
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06417v2) · [PDF](https://arxiv.org/pdf/2608.06417v2)

## TLDR
TLDR: This paper introduces an activation-engineering-based misinformation detector that extracts a "falsehood direction" from contrastive truthful/false statement activations and classifies unseen claims by projecting their last-token representations onto it, showing that truthfulness is linearly separable across 11 language models and matching or beating prompting baselines without fine-tuning or external evidence retrieval.

## Abstract
The proliferation of misinformation online has driven demand for scalable detection systems. While most existing approaches rely on surface-level linguistic features or external knowledge retrieval, we examine truthfulness as a geometric property of a language model's representation space. We introduce a misinformation detection framework grounded in activation engineering, which leverages the latent geometry of transformer models. Our approach elicits a misinformation direction in the residual stream by contrasting activations from paired truthful and false statements, following the difference-in-means principle of Contrastive Activation Addition (CAA). At inference time, the last-token activation of an unseen claim is projected onto this direction, and the projected representation is fed to an Multilayer Perceptron (MLP) for classification. The procedure requires no fine-tuning of the backbone model, no external evidence retrieval, and no task-specific supervision beyond the contrastive pairs used to estimate the direction. We evaluate the method across 11 models from the Gemma, Llama, and Qwen families, ranging from 270M to 12B parameters, on three fact-checking benchmarks: AVeriTeC, LIAR, and FACTors. The falsehood direction is recoverable across model scales and architectural families, and last-token projection matches or surpasses zero-shot and few-shot prompting baselines on LIAR and FACTors, with the largest gains observed for smaller models. Performance on AVeriTeC is more limited, which we attribute to its evidence-grounded labeling scheme. These findings provide evidence that truthfulness is a structured, linearly separable concept in the latent space of pretrained language models, and point toward interpretability-driven misinformation detection as a practical complement to retrieval-based pipelines. The code is available on https://github.com/Malta-Lab/LaFaCt.
