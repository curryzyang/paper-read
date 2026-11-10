# Coordinated Mixed-Precision KV Cache Quantization for Efficient LLM-based Multi-agent Systems

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Weizhong Huang, Jinchao Zhang, Xiawu Zheng
- 机构：Tencent Inc., Xiamen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10096v1) · [PDF](https://arxiv.org/pdf/2611.10096v1)

## TLDR
CoMixKV is a coordinated mixed-precision KV-cache quantization framework that uses online attention-error sensitivity estimates to jointly allocate bit-widths across simultaneously resident LLM agents under a shared memory budget, improving accuracy while reducing memory and inference cost versus independent quantization baselines.

## Abstract
LLM-based multi-agent systems solve complex tasks through collaboration, but their growing, simultaneously resident key-value (KV) caches create a memory bottleneck. Applying single-model quantization policies independently ignores differences in agents' precision needs, potentially degrading collective reasoning. We introduce Coordinated Mixed-Precision KV Cache Quantization (CoMixKV), which combines online sensitivity estimation with joint agent-layer bit-width allocation under a shared memory budget. To our knowledge, CoMixKV is the first mixed-precision KV-cache quantization framework to jointly allocate precision across simultaneously resident agent caches under such a budget. The estimator derives sensitivity from a local attention-error bound using recent queries, keys, and values, without calibration data, trial quantization, or additional model passes. A shared controller combines these scores with remaining quantizable capacity and byte-level storage costs to minimize total estimated error. Allocations are refreshed as agents start or finish and new observations become available. Selected widths apply only to newly quantized blocks; recent states retain native precision and previously quantized blocks remain unchanged. Across four benchmarks and three LLM backbones at average 2-bit, 3-bit, and 4-bit settings, CoMixKV achieves strong accuracy against the evaluated quantization baselines. At the average 3-bit setting on Gemma-4-31B-it, it achieves 68.35% average accuracy, exceeding the strongest quantized baseline by 0.59%. On Qwen3-32B, it reduces peak KV-cache memory by 32.08% and achieves a 1.38x inference speedup over FullKV.
