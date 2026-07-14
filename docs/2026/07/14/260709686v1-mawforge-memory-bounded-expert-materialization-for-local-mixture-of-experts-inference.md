# MawForge: Memory-Bounded Expert Materialization for Local Mixture-of-Experts Inference

- 区域：精读区
- 排名：7
- 匹配度：2.4/10
- 来源：arxiv
- 作者：Craig Opie
- 机构：Holocron Security, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09686v1) · [PDF](https://arxiv.org/pdf/2607.09686v1)

## TLDR
MawForge enables memory-bounded local inference of large sparse Mixture-of-Experts models on constrained unified-memory machines by storing the full model on disk, keeping common tensors resident, and materializing expert tensors into a bounded execution cache on demand, but it is effective as a measurement substrate rather than a cache-maximization policy, with performance depending on balancing expert reuse, resident footprint, KV-cache size, quantization, route locality, and memory pressure.

## Abstract
Sparse Mixture-of-Experts (MoE) language models separate total parameter count from per-token active computation, but local inference systems often still require the full model, key-value cache, runtime buffers, and operatingsystem headroom to fit in fast memory. MawForge tests a different systems hypothesis: local MoE serving can be made practical on constrained unified-memory machines by storing the full model on disk, keeping common tensors resident, and materializing routed expert tensors into a bounded execution cache on demand. The central finding is that MawForge is effective as a bounded execution mechanism and measurement substrate for local MoE inference, but not as a cache-maximization policy. Performance depends on balancing expert reuse against resident footprint, KV-cache size, quantization, route locality, and macOS memory pressure.


## 精读解读（中文）
### 一、研究动机
本地MoE推理系统常要求完整模型参数、KV缓存和运行时缓冲区全部驻留快速内存，但在受限统一内存设备上难以满足。MawForge提出一个不同的系统假设：将完整模型存储在磁盘，仅使公共张量常驻，路由专家张量按需物化到有界执行缓存中，从而在内存受限的机器上实现实用化本地MoE服务。

### 二、技术方案（Method）
MawForge采用split-pack架构：首先将GGUF模型拆分为公共张量和按层、按专家划分的确定性块，并生成索引文件。运行时，加载公共张量并分配有界槽位，根据路由器的需求从磁盘物化专家块到缓存，更新路由到槽的元数据。暴露OpenAI兼容端点，报告TTFT、解码速率、缓存命中率等指标。执行前进行静态预算检查，计算下界 L = C + E(p) + K(n) 并拒绝超出预算的组合。实验在MacBook Pro M5 Pro 24GB统一内存上进行，目标18 GiB，使用三个模型：Gemma 4 26B A4B Q8_0 (25GB)、Qwen3.6 35B A3B Q8_0 (34GB)、Qwen3.6 35B A3B Q4_K_M (20GB)。评估两个上下文长度（4K, 32K）、五个缓存设置（15%,25%,35%,50%,65%）、四个提示类别，每单元5次重复，共600行非推测解码生成96个token。

### 三、结果（Result）
所有540个静态可行的生成行成功完成，未触发内存保护。较大专家缓存一致提高命中率并减少物化字节，但吞吐量非单调：Qwen Q8在所有上下文和提示类下最优为15%缓存（如4K代码12.09 tok/s，45%时降至1.83 tok/s）；Gemma Q8在4K下最优为35%缓存（8.18 tok/s），65%时吞吐下降。静态规划拒绝了30个独特组合中的3个（Gemma Q8 32K 50%/65%和Qwen Q4 32K 90%）。直接完整加载Gemma Q8 32K导致系统内存使用达99.19%被保护终止。推测解码（MTP horizon 4, threshold 0.5）未改善性能（非推测5.49 tok/s vs 推测5.00 tok/s）。

### 四、结论（Conclusion）
MawForge作为有界执行机制和测量基座在测试条件下有效，能够在大内存预算内服务大型GGUF MoE模型，但并非缓存最大化策略。性能取决于专家重用与驻留占用、KV缓存大小、量化、路由局部性和macOS内存压力的平衡；缓存大小非单调增加可能降低吞吐量。

### 五、方法论与关键技术细节
split-pack表示包含每个专家块的张量类型、层、专家ID、偏移量、字节数、拓扑和摘要，索引文件确保可复现。静态预算下界公式 L = C + E(p) + K(n) 用于计划拒绝。非单调吞吐模型 T(p) = tokens / (compute + materialization + pressure_penalty(F))，其中压力惩罚在缓存过大时起主导作用。推测解码增加额外物化开销，因验证批可能触及更广专家集。实验未收集所有macOS内存字段（如system_ram, tracked_metal），仅报告进程RSS和包装器采样。局限：仅单一机器、短序列（96 tokens）、非推测解码为主，结论有限。
