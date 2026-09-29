# NanoForecast v0.5: Competitive Time Series Forecasting Through Training Pipeline Optimization

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Gautam Kishore
- 机构：Eulogik
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31669v1) · [PDF](https://arxiv.org/pdf/2609.31669v1)

## TLDR
NanoForecast v0.5 shows that fixing three training-pipeline issues—loss-scope handling, tensor shape alignment, and wider augmentation—without changing its 6.5M-parameter architecture cuts MASE by 43.8% and enables it to beat or compete with much larger forecasters like TimesFM (200M parameters) on several benchmarks while remaining CPU-deployable.

## Abstract
We present NanoForecast v0.5, a 6.5M-parameter forecaster that competes with models 31x its size (TimesFM, 200M parameters) after training pipeline fixes and no architecture change. Retraining the v0.3 architecture with corrected loss-scope handling, tensor shape alignment, and wider augmentation coverage cuts overall Mean Absolute Scaled Error by 43.8% under one fixed protocol (MASE 3.030 to 1.704) on the same data and compute budget. NanoForecast v0.5 beats TimesFM on all three ETT datasets (MASE 0.676/1.110/0.287 vs. 0.705/1.360/0.545) and on exchange rate (4.317 vs. 4.383); TimesFM keeps a clear lead on the high-cardinality electricity and traffic sets. Against PatchTST (15M+ parameters, official configuration), v0.5 wins all three ETT sets. Training takes about 12 hours on a single cloud GPU (NVIDIA T4, Google Colab) and inference needs no GPU (measurements in this paper are on an Apple M4 CPU). We release all code, pretrained checkpoints, and evaluation framework under Apache 2.0 at https://github.com/eulogik/NanoForecast


## 精读解读（中文）
### 一、研究动机
大型时序基础模型（TimesFM 200M、Chronos 710M、PatchTST 15M+）精度高但训练和推理依赖 GPU，难以在消费级硬件与边缘设备部署。作者目标是在不改架构的前提下，让 6.5M 参数的小模型保持可部署性并尽量缩小与大规模模型的精度差距。其切入点是发现并修复训练管线中的三个静默缺陷。

### 二、技术方案（Method）
沿用 NanoForecast v0.3 的 6.5M 参数架构，仅改训练管线：输入采用窗口级鲁棒归一化 median/IQR（epsilon=0.1）、非重叠 patch size 8、频率嵌入；8 层混合网络由 LongConv、DeltaNet 线性 RNN 和 SwiGLU 门控 MLP 经 per-window 软路由组成，输出点预测、单调分位数、趋势/季节/残差分解与异常分数；训练时 200 epochs、batch 128、OneCycleLR（base 3e-5、peak 3e-4、10% warmup），并在循环内做 jitter、随机缩放、平移、掩码、时间反转增强。关键修复包括：在 loss 前把预测和目标截断到 H=48，horizon key 仅在 multi_horizon 开启时附加；分位数分支也在截断后再算 loss；增强覆盖从 scale/shift/jitter 扩展到五类。评估使用 context 512、H=48、非重叠测试窗，MASE 用季节朴素法在训练段做分母，点预测取 pinball 训练的中位数 p50。

### 三、结果（Result）
同一数据与算力下，仅修复训练管线把整体 MASE 从 3.030 降到 1.704，降幅 43.8%。在 6.5M 参数下，v0.5 在三个 ETT 数据集上均优于 TimesFM（ETTh1 0.676 vs 0.705、ETTh2 1.110 vs 1.360、ETTm1 0.287 vs 0.545），在 Exchange Rate 上也优于 TimesFM（4.317 vs 4.383），并在三个 ETT 集上全部胜过官方配置的 PatchTST（15M+）。但 TimesFM 在 Electricity 和 Traffic 两个高基数数据集上仍保持明显领先。训练约 12 小时于单张 NVIDIA T4（Google Colab），推理无需 GPU，Apple M4 CPU 上单次预测约 19.5 ms，ONNX Runtime 下约 10.7 ms，ONNX 导出 FP32 27.9MB、INT8 9.2MB。

### 四、结论（Conclusion）
论文的结论是，训练管线的正确性、损失截断、张量形状对齐和增强覆盖可带来超过架构改动的收益，使 6.5M 小模型在部分标准基准上达到 31 倍参数模型的竞争力。该工作强调可部署性：CPU 推理、ONNX/Docker 与状态化流式推理，而不仅是基准分数。作者同时指出其优势并非全面，TimesFM 在高基数电力/交通数据上仍领先，且对比受限于可在统一协议下端到端运行的基线。代码、预训练权重和评估框架以 Apache 2.0 发布。

### 五、方法论与关键技术细节
细节上，模型为单变量预测，context C=512、horizon H=48，d_model=96、L=8、patch=8、总参数 6.5M；DeltaNet 每层维护矩阵状态 W_t，支持跨 predict 调用的流式推理，流式更新一次前向约 19.1 ms，与全量推理 19.5 ms 接近。分位数水平为 0.1/0.25/0.5/0.75/0.9，通过 p50 加非负 softplus 偏移保证单调；MASE 分母按小时 s=24、15 分钟 s=96、日频 s=7 的季节朴素误差计算。训练用 200 epochs、batch 128、OneCycleLR、base 3e-5、peak 3e-4、10% warmup，v0.3 与 v0.5 共用同一数据、算力和架构，唯一差异是管线修复，因此消融可归因。局限是只评估 H=48、单变量与固定协议，Chronos-T5-large 和 Timer 因硬件推理不可行未纳入主表，且未显示在小规模数据外仍全面超越大规模基础模型。
