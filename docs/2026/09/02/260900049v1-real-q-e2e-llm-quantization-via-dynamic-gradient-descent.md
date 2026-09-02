# REAL-Q: E2E LLM Quantization via Dynamic Gradient Descent

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Qian Zhang, Yaoming Li, Zhewen Tan, Yanshu Wang, Heng Lu, Kun Su, Zongwei Lv, Wenhan Yu, Yongge Ma, Yinjun Han, Ruikuang Liu, Tong Yang
- 机构：ZTE Corporation, Peking University, Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00049v1) · [PDF](https://arxiv.org/pdf/2609.00049v1)

## TLDR
REAL-Q improves LLM post-training quantization by replacing static, layer-local second-order solvers with an end-to-end aligned surrogate (aggregated Fisher MSE) refined via fine-grained dynamic block-wise gradient descent, reducing KL divergence by up to ~49% over prior methods on LLaMA-3.1 and Qwen3 models.

## Abstract
Post-training quantization (PTQ) is essential for deploying large language models (LLMs) under strict resource constraints. State-of-the-art PTQ methods quantize each layer with a single closed-form second-order solver: to remain analytically tractable, they heavily approximate the global loss (dropping cross-channel coupling, pooling output rows into groups), and they then freeze the resulting Hessian across the entire layer, with no way to refresh it as the loss landscape shifts column by column--a phenomenon we call information misalignment. We propose REAL-Q (Real-time E2E-loss Aligned LLM Quantization), a novel PTQ paradigm that breaks this compromise: instead of diluting the objective for the sake of analytic tractability, REAL-Q targets an end-to-end-aligned surrogate of the global loss and refines it via fine-grained, dynamic Block-wise Gradient Descent applied after every column block (128 columns). By coupling this fine-grained correction with a sliding window mechanism for smooth cross-layer transitions, REAL-Q effectively mitigates error propagation across the network. On LLaMA-3.1 (8B and 70B) and Qwen3 (0.6B-32B) at W4A16, REAL-Q reduces end-to-end KL divergence by up to ~49% relative to state-of-the-art globally-guided methods.


## 精读解读（中文）
### 一、研究动机
GPTQ类后训练量化方法为了保持闭式二阶求解可解析，不得不严重近似全局损失，丢弃跨通道耦合并将输出行分组；同时冻结的Hessian在整个层内不随逐列量化造成的损失地形变化而更新，形成论文所称的信息错位。REAL-Q旨在打破分析可解性与保真度之间的折中，用动态、细粒度、端到端对齐的梯度校正降低跨层误差传播。

### 二、技术方案（Method）
REAL-Q在逐层逐列量化管线中引入粗到细的优化层次。输入为校准集token及当前transformer block输出y_t；先从全精度模型输出分布中采样标签，计算NLL梯度g_t=∇_{y_t}L_NLL，并按块聚合完整的Fisher矩阵F=(1/T)Σg_tg_t^T，再以block输出扰动Δy_t的二次型L_Fisher=1/(2T)ΣΔy_t^T F Δy_t作为替代端到端KL的损失。量化时保留GPTQ风格的列扫描合解析补偿作为粗更新；在W4A16下按128列组成一个列块，每完成一个列块，就以当前block输出上的Fisher损失为目标，用Adam执行一步动态Block-GD，梯度针对真实的当前部分量化状态在线重算，从而修正静态Hessian漏掉的累积误差；Adam对角预条件隐式提供二阶信息。为避免相邻transformer block间目标突变，使用loss sliding window对相邻block的Fisher损失做连续插值，并将反向传播限制在至多两个相邻block内。

### 三、结果（Result）
在LLaMA-3.1（8B和70B）与Qwen3（0.6B–32B）的W4A16设置下，REAL-Q在所有评测模型上都取得最低的端到端KL散度；相比当前最强的全局引导类方法（如GuidedQuant），WikiText-2上的KL最多降低约49%。论文同时报告困惑度与zero-shot准确率作为次级指标，REAL-Q在输出分布保持方面的优势保持一致。

### 四、结论（Conclusion）
REAL-Q表明，无需将优化目标压缩到可解析二阶求解器也能实现高保真LLM量化。通过完整的聚合Fisher矩阵作为端到端对齐的损失代理，配合每128列后的动态Adam块级梯度校正与滑动窗口，静态近似和冻结Hessian导致的信息错位与误差传播可被有效缓解。该范式说明在PTQ中将解析式粗校正与动态一阶精修结合，是更优且可扩展的量化策略。

### 五、方法论与关键技术细节
REAL-Q在每个transformer block上离线聚合一整张d×d Fisher矩阵，不保留逐token Hessian，也不引入输出行分组这类启发式超参；Fisher-Hessian等式要求从全精度模型输出分布p中采样目标标签并计算NLL梯度的外积，均值场解耦的近似误差可写为元素级协方差之和。超参上列块大小取128列，每个列块后仅执行单步Adam，梯度在线重算；与GuidedQuant对比时其分组数N_g=4，而REAL-Q保留全跨通道耦合。实验统一采用W4A16 per-row量化并采纳QuaRot旋转预处理，KL在WikiText-2上报告；反向传播限制在至多两个相邻block内以避免全模型回传。局限是Fisher替代损失并非精确全局KL，均值场项丢弃逐token Hessian与输出扰动间的相关性，且Block-GD需要在线前向/反向传播，实际开销高于单次闭式求解；Adam对角预条件只能隐式逼近二阶信息，不能替代精确Hessian。
