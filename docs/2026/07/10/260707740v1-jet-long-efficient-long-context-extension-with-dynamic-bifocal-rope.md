# Jet-Long: Efficient Long-Context Extension with Dynamic Bifocal RoPE

- 区域：精读区
- 排名：10
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Haozhan Tang, Zerui Wang, Yuxian Gu, Song Han, Han Cai
- 机构：NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07740v1) · [PDF](https://arxiv.org/pdf/2607.07740v1)

## TLDR
Jet-Long introduces a tuning-free, zero-shot context extension method using dynamic bifocal RoPE that adaptively rescales a remote window based on sequence length, preserving short-context fidelity while achieving superior long-context performance and efficiency.

## Abstract
Modern LLMs are increasingly deployed in long-context applications such as retrieval-augmented generation, repository-level coding, and agentic workflows whose accumulated reasoning and tool traces routinely push the input an order of magnitude past the pretraining window, making zero-shot context extension the dominant deployment path for open-weight checkpoints. Most existing zero-shot methods fix a single rescaling factor up front, so an aggressive factor sacrifices short-context fidelity while a conservative one breaks down at long contexts. We propose Jet-Long, a tuning-free zero-shot method that pairs a local RoPE-faithful window with a long-range window whose rescaling factor adapts dynamically to the current sequence length, recovering the base model exactly at short inputs while extrapolating cleanly at long ones. An inclusion-exclusion attention merge and an on-the-fly RoPE correction rotation make the bifocal construction essentially free at inference; fused into a single CuTe kernel, long-context prefill reaches up to $1.39\times$ FA2 throughput on H100 (approaching the Hopper-only FA4), and single-batch generation incurs $\le 4\%$ overhead at every length. On Qwen3-1.7B/4B/8B up to 128K context, Jet-Long leads RULER by $+4.79$/$+2.18$/$+2.03$~pp over the strongest baseline at 1.7B/4B/8B, achieves the best overall accuracy on HELMET-RAG (a benchmark identified by HELMET as the most efficient predictor of downstream long-context performance) and attains the lowest PG-19 perplexity. Jet-Long also generalizes to hybrid attention architectures such as Jet-Nemotron for further long-context improvement without retraining, and remains hyperparameter-resilient for ease of deployment.


## 精读解读（中文）
### 一、研究动机
现代大语言模型在检索增强生成、仓库级代码理解和多步智能体工作流等长上下文应用中，输入长度常常超过预训练窗口，驱动零样本上下文扩展成为主流部署方式。现有零样本方法大多固定单一缩放因子，激进因子牺牲短上下文保真度，保守因子则在长上下文时失效。因此需要一种无需微调、能动态适应序列长度的方法，在短输入时精确恢复基模型行为，在长输入时干净外推。

### 二、技术方案（Method）
Jet-Long是一种无需调优的双焦点旋转位置编码方法。它包含一个保持经典RoPE的局部窗口（大小w0）和一个远程窗口，远程窗口的重缩放因子动态依赖于当前序列长度L：定义组大小G = max(1, ceil(L / w_pretrained))，远程位置映射为f(x) = floor(x / G)。推理时，通过包含-排除注意力合并将三个FlashAttention调用（全远程、局部仅RoPE、局部仅重映射）组合，并用LogSumExp稳定；生成时通过实时RoPE校正旋转实现，KV缓存保持不变。整个计算融合为单个CuTe核，长上下文预填充可达1.39倍FA2吞吐量（接近仅Hopper的FA4），单批生成开销不超过4%。

### 三、结果（Result）
在Qwen3-1.7B/4B/8B模型上测试至128K上下文，Jet-Long在RULER基准上比最强基线分别高出+4.79/+2.18/+2.03个百分点；在HELMET-RAG（被HELMET识别为最有效下游长上下文性能预测的基准）上取得最佳或并列最佳总体准确率；在PG-19上达到最低困惑度。该方法还泛化至混合注意力架构（如Jet-Nemotron），无需重新训练即可进一步提升长上下文性能，且超参数鲁棒。

### 四、结论（Conclusion）
Jet-Long通过动态双焦点RoPE解决了固定缩放因子的保真度-外推权衡，无需微调即可在短上下文精确恢复基模型、在长上下文干净外推。推理时的高效融合实现几乎零开销，并在多个模型和基准上超越现有零样本方法。该方法适用于纯RoPE和混合注意力架构，为无需训练的长上下文部署提供了实用且高效的解决方案。

### 五、方法论与关键技术细节
方法关键点：动态组大小G=max(1, ceil(L/w_pretrained))确保每个远程旋转角度落在预训练网格上，最大化位置分辨率；包含-排除注意力合并通过三个FlashAttention调用实现，配合LogSumExp稳定；生成时KV缓存不变，通过实时RoPE校正旋转进行解耦；融合CuTe核使预填充接近FA4吞吐量（H100上1.28-1.39× FA2）。超参数仅w0（局部窗口大小），实验表明其选择鲁棒。局限：离散分组在极端长上下文下可能引入轻微量化误差，但动态分组已最小化压缩。数据基于Qwen3 (1.7B/4B/8B)和Jet-Nemotron架构，无训练损失或长上下文数据需求。
