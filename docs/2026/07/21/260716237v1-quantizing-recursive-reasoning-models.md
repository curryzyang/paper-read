# Quantizing Recursive Reasoning Models

- 区域：精读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Thorir Mar Ingolfsson, Wajeeha Tahir, Anna Tegon, Lionnus Kesting, Gamze İslamoğlu, Luca Benini
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16237v1) · [PDF](https://arxiv.org/pdf/2607.16237v1)

## TLDR
The paper identifies that the catastrophic degradation of recursive reasoning models under 4-bit quantization is caused by per-tensor activation scaling, and demonstrates that per-block scaling (MXInt4) fully restores accuracy, with robustness maintained across varying recursion depths and architectures.

## Abstract
Recursive reasoning models solve hard puzzles by applying compact, weight-tied blocks over many refinement steps. Because these blocks are reused many times, quantizing them creates a unique dynamical problem: the quantization error is incurred at every step. While 8-bit quantization (integer or float) preserves accuracy, moving to a per-tensor 4-bit format causes a systematic bias to accumulate. The ensuing drift catastrophically degrades exact-solution accuracy on Sudoku from 84.1% to 0.0% (only ~25% of cells correct). In this work, we show that this collapse is caused by activation-scaling granularity rather than bit-width or number format. Crucially, moving to per-block scaling completely restores the transition. To implement this, we apply MXInt4, a blockwise integer activation format, to recursive reasoning models. It is competitive with blockwise float formats on our tasks, while keeping integer elements and power-of-two block scales. Finally, recursion depth and reuse modulate quantization sensitivity, with the deepest architecture we test (the EqR equilibrium model) the most sensitive. Yet blockwise scaling overcomes this vulnerability, staying robust across these architectures and transferring to the open-ended ARC-AGI benchmark.


## 精读解读（中文）
### 一、研究动机
递归推理模型通过复用紧凑的权值共享块多次迭代求解难题，但低比特量化（如4位）会导致系统性偏差累积，使数独精确求解准确率从84.1%骤降至0.0%，因此需探究量化失效原因并设计能恢复精度的量化方案。

### 二、技术方案（Method）
本文采用MXInt4逐块整数激活格式对递归推理模型进行量化。模型以谜题（如数独）为输入，通过权值共享的递归推理块执行多步迭代优化。量化过程中，激活值以逐块粒度进行缩放（每块使用2的幂次缩放因子），并保持整数元素格式，替代传统的逐张量缩放。整个流程为后训练量化，无需微调模型参数，仅在推理时应用量化操作。

### 三、结果（Result）
在数独任务上，8位量化保持84.1%准确率，而每张量4位量化导致准确率崩溃至0.0%（仅约25%单元格正确）。采用MXInt4逐块缩放后，准确率完全恢复至接近浮点水平，与逐块浮点格式（如MXFP4）性能相当。在EqR平衡模型等更深架构上，逐块缩放依然稳健，并成功迁移至开放式的ARC-AGI基准。

### 四、结论（Conclusion）
递归推理模型量化失败的根本原因是激活缩放粒度不足，而非位宽或数值格式；采用逐块缩放（如MXInt4）可完全恢复低比特量化的准确率，且对于深度递归模型尤为有效，为递归推理模型的高效部署提供了可行方案。

### 五、方法论与关键技术细节
关键细节包括：(1) MXInt4格式元素为整数，块缩放因子为2的幂次，便于硬件实现；(2) 递归深度和复用次数调节量化敏感性，EqR模型（深度最大）最敏感；(3) 实验仅在数独和ARC-AGI基准上进行，未涵盖其他领域；(4) 量化方式为后训练量化，无需微调；(5) 局限性：仅验证了特定递归架构和任务，通用性需进一步验证。
