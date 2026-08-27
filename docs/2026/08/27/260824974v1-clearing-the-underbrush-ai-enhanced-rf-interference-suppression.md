# Clearing the Underbrush: AI-Enhanced RF Interference Suppression

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Rahul Jain, Pierre Trepagnier, Rick Gentile, Joey Botero, Alexia Schulz
- 机构：MIT Lincoln Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24974v1) · [PDF](https://arxiv.org/pdf/2608.24974v1)

## TLDR
This paper presents an AI-enhanced RF interference suppression approach that augments an autoregressive transformer with a Finite Scalar Quantization tokenizer, achieving lower latency and improved interference rejection compared to traditional and prior AI-based methods for recovering digitally modulated signals.

## Abstract
AI-based structured interference rejection has grown more popular because deep learning approaches can outperform traditional methods by jointly considering the signal of interest (SOI) and the signal mixture (SOI plus interference). This work builds on a previous AI-enabled approach utilizing autoregressive transformer-based models by adding a Finite Scalar Quantization (FSQ) tokenizer layer which aims to improve the interference rejection performance while keeping overall latency to a minimum. Additionally, we experiment with other inference optimization techniques with the goal of speeding up inference without much accuracy loss. We explore this space with an experiment where the SOI is a digitally modulated radio frequency (RF) signal and the structured interference is a digital television signal, an extremely common type of Orthogonal Frequency-Division Multiplexing (OFDM) transmission. Our results achieve low latency and increased interference rejection over traditional techniques and prior work with other AI-enabled methods. We demonstrate the benefits of the AI-enabled approaches via audio metrics such as Perceptual Evaluation of Speech Quality (PESQ). Additionally, we explore a variety of applications and detail how our interference rejection algorithm may be used in operationally-relevant scenarios.
