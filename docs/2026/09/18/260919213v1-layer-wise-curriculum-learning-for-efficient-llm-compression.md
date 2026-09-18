# Layer-wise Curriculum Learning for Efficient LLM Compression

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Donggeon Lee, Dooyeon Na, Seungmin Oh, Jongbin Ryu
- 机构：Ajou University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19213v1) · [PDF](https://arxiv.org/pdf/2609.19213v1)

## TLDR
The paper introduces layer-wise curriculum learning with feature caching and multi-threading for LLM compression, progressively focusing optimization on deeper error-prone layers to achieve state-of-the-art performance while cutting GPU memory and training time by over 50%.

## Abstract
In this paper, we introduce layer-wise curriculum learning for efficient LLM compression. The proposed method facilitates the knowledge transfer from the teacher model to the student model, utilizing a curriculum learning approach that begins with easier optimization tasks and progressively tackles harder ones. In order to adopt the layer-wise learning in LLM compression, we partition the whole model into multiple segments consisting of layers, thereby enabling more computationally efficient knowledge transfer for LLMs. Based on our theoretical analysis of cumulative error phenomenon, layer-wise curriculum learning accelerates convergence while stabilizing the knowledge transfer process. In addition, we present a feature caching method with a multi-threading strategy to efficiently address feature misalignment across layers, maximizing GPU utilization. Consequently, our method exhibits advanced model compression performance, as well as high computational efficiency in terms of minimized memory usage and short training hours. Experiments on multiple datasets show that the proposed method achieves state-of-the-art performance while reducing GPU memory usage and training hours by more than 50\% on BERT and GPT-2. Moreover, it outperforms the other pruning methods on LLaMA-family and Qwen models under the same training hours, with a lower GPU memory footprint.
