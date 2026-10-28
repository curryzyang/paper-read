# Distributed LLM Inference via Communication-Efficient Speculative Decoding

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Joohyun Shin, Byeonghyeon Park, Keumseo Ryum, Joonhyuk Kang
- 机构：Korea Advanced Institute of Science and Technology (KAIST)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35957v1) · [PDF](https://arxiv.org/pdf/2610.35957v1)

## TLDR
DISCO is a communication-efficient distributed speculative decoding framework that places a replica of the draft small language model on the server to eliminate vocabulary-scale distribution transfer, enabling only token indices and scalar probabilities to be exchanged while preserving exact target sampling and improving decoding speedup under bandwidth constraints.

## Abstract
Distributed speculative decoding has emerged as a promising approach for device--server collaborative large language model (LLM) inference, but its decoding speedup is often limited by the vocabulary-scale communication overhead. In existing distributed speculative decoding methods, exact rejection sampling requires transmitting full token distributions over the LLM vocabulary between the device and the server, which becomes costly in bandwidth-constrained environments. To address this issue, we propose DISCO, a communication-efficient framework for distributed speculative decoding, that eliminates vocabulary-scale distribution transfer while preserving the exact target distribution. DISCO achieves this by introducing a server-side replica of the draft small language model (SLM), which enables the server to locally obtain the draft-side distribution required for rejection sampling. As a result, DISCO exchanges only drafted token indices and scalar probability values between the device and the server. Experimental results on multiple datasets show that DISCO consistently achieves higher decoding speedup than existing distributed speculative decoding methods, particularly under stringent bandwidth constraints.
