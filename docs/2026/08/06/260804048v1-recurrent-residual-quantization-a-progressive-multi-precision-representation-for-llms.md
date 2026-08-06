# Recurrent Residual Quantization: A Progressive Multi-Precision Representation for LLMs

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yu Luo, Bo Dong, Wenhua Cheng, Haihao Shen
- 机构：Intel
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04048v1) · [PDF](https://arxiv.org/pdf/2608.04048v1)

## TLDR
RRQ is a calibration-free post-training quantization framework that represents LLM weights as a low-bit base plus progressive quantized residual stages, enabling 2-, 4-, 6-, and 8-bit models from a single checkpoint with faster construction and competitive accuracy at higher precisions.

## Abstract
Serving large language models (LLMs) under diverse deployment constraints requires flexible trade-offs between accuracy, memory footprint, and throughput. However, conventional quantization methods typically require a separate checkpoint for each target bit-width. We introduce Recurrent Residual Quantization (RRQ), a post-training quantization (PTQ) framework that represents weights as a low-bit quantized base together with a sequence of quantized residual corrections, enabling multiple effective precisions from a single checkpoint. Starting from a 2-bit model obtained via post-training quantization (PTQ) or round-to-nearest (RTN), RRQ progressively adds lightweight 2-bit residuals generated via RTN to construct 4-, 6-, and 8-bit representations. The method is calibration-free and avoids joint multi-bit optimization. In our Qwen3-8B setup, the full all-RTN 2-/4-/6-/8-bit package is constructed in 1,293 seconds, 3.3 times faster than the measured MatGPTQ construction. Experiments on six recent LLMs show competitive accuracy at 6 and 8 bits, with model-dependent behavior at 4 bits. The code will be made publicly available upon publication.


## 精读解读（中文）
### 一、研究动机
现有LLM量化通常为每个目标位宽生成独立检查点，难以在内存、吞吐和精度之间灵活切换；多精度方法如MatGPTQ采用嵌套整数位切片，所有精度耦合在同一比特层级里，且难以复用已有低比特检查点。RRQ提出将权重表示为低比特量化基座加一系列量化残差修正，用单一检查点支持2/4/6/8比特，同时保留PTQ的灵活性和对已有量化检查点的可重用性。

### 二、技术方案（Method）
RRQ以全精度权重为输入，也可直接加载已有低比特检查点作为基座；若没有基座，则先用RTN对每个分组执行仿射量化（尺度/零点）得到2比特基座Q0，并令残差R0为原始权重减去基座反量化结果。随后递归地对R_{k-1}用RTN做2比特量化Q_k，存储该残差阶段的码、尺度和零点，反量化得到修正项，再更新残差R_k=R_{k-1}-hat R_k；重复三个残差阶段后，2/4/6/8比特分别对应基座前缀加上0/1/2/3个残差修正项。整个构建免校准、无需Hessian或联合多比特优化；推理时按前缀逐级累加基座和残差GEMM输出即可得到对应有效精度的结果。

### 三、结果（Result）
在Qwen3-8B案例中，全RTN的2/4/6/8比特RRQ包构建耗时1293秒，比实测MatGPTQ构建快约3.3倍。在六个近期LLM上，RRQ在6比特和8比特达到接近BF16的精度，并与现有单检查点多精度方法相当；4比特精度则呈现模型依赖行为，部分模型上表现不稳定。

### 四、结论（Conclusion）
RRQ通过递归残差量化提供了一种单检查点、可渐进扩展的多精度LLM权重表示，能够复用已有低比特模型并以极低构建开销生成更高精度版本。其适用性由权重的局部离群程度决定：离群值主导分组动态范围时残差修正显著有效，分布较平坦时直接固定比特量化可能更优，因此4比特效果依模型而异。

### 五、方法论与关键技术细节
关键实现细节包括：采用分组仿射零点量化，基座与三个残差阶段均用2比特RTN，因此前缀2/4/6/8比特天然可部署；基座和残差阶段格式可以异构，但实验只评估整数低比特阶段。分析采用Peak-to-Mean Ratio（PMR）刻画组内局部动态范围，示例Qwen3-14B在group size 128下平均张量最大PMR为27.826。理想化离群阈值近似为K>r(2^{n1+1}-1)，说明残差量化仅在离群幅度足够大时更优。局限是4比特表现模型相关，且完整构建需要全精度权重计算残差；若以已有低比特检查点为基座则只需执行残差阶段，可进一步节省开销。
