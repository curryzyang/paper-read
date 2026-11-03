# Quantization of Large Models with Weight Outliers and Sparsity

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Leonidas Tsigkounakis, Abraham Jaeger Mountain, Yilang Zhang, Georgios B. Giannakis
- 机构：University of Minnesota, Morgan Stanley
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00286v1) · [PDF](https://arxiv.org/pdf/2611.00286v1)

## TLDR
The paper proposes a calibration-free post-training quantization method that decomposes large-model weights into a quantized matrix, a sparse component for outlier rows, and a low-rank component, using simulated annealing to search for a decomposition that reduces 4-bit quantization error and improves LLM performance with minimal memory overhead.

## Abstract
Post-training quantization (PTQ) reduces the memory burden of large model deployment by casting the high precision trained weights to fewer bits. While this promotes memory-efficient inference, it also incurs quantization error that impairs model performance. To compensate for quantization error, the present contribution decomposes the original trained weights into a quantized matrix, a low-rank component, and a sparse matrix that accounts for outlier rows in the weights. Due to analytical intractability and the discrete structure of the decomposition, a simulated annealing search is employed to explore candidate decompositions while avoiding poor local minima. Numerical tests demonstrate the effectiveness of this approach across a broad suite of large language models, including Llama 3.2 1B, Llama 3.2 3B, Llama 3.1 8B, and Qwen2.5 7B, evaluated on natural language generation benchmarks using 4-bit NF4 and FP4 quantizers. The novel method can markedly outperform direct quantization while incurring minimal memory overhead.
