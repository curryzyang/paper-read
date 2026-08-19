# Forward Pass Domain Adaptation (Without Cross-Layer Backpropagation)

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Rivaan Patil, Simon Dennis, Hao Guo, Kevin Shabahang
- 机构：University of Melbourne, i14, University of California, Santa Cruz
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14563v1) · [PDF](https://arxiv.org/pdf/2608.14563v1)

## TLDR
Forward-Pass-Only MLP training (FPO) adapts large language models to domain data using only a forward pass and output-layer error signals—no cross-layer backpropagation—delivering 2.7–3.2× higher throughput and ~40% lower peak memory than standard fine-tuning while keeping off-domain benchmarks within seed noise.

## Abstract
Forward-Pass-Only MLP training (FPO) adapts large language models without a backward pass through the model body, achieving 2.7--3.2x the throughput of standard fine-tuning at ~40% less peak training memory, while leaving off-domain benchmarks within seed-noise of baseline, a property that full-network fine-tuning does not reliably reproduce. FPO rests on a single empirical observation: at late layers of a transformer, the output-layer prediction error approximates the true gradient with cosine similarity 0.47--0.59 across six public models we survey. We introduce a two-minute diagnostic that quantifies this approximation per layer for any model, identifying where late-layer adaptation is viable. Informed by the diagnostic, FPO computes a single error signal at the output and applies it to each target layer. No signal is propagated between layers, and no autograd graph is constructed at any point. We evaluate FPO on three model families (OLMo-2-7B, Qwen3-8B, Falcon3-7B). Across all three, FPO produces in-domain perplexity improvement and leaves MMLU, ARC-Challenge, HellaSwag, and Winogrande within seed-noise of baseline. Localizing SFT to FPO's target layers to enter this regime is also feasible, but at 2.2x the wall-clock cost of FPO.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
