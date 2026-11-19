# Biologically-Inspired Spike Encoding and Optimization for Spiking Neural Networks

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ayaan Qayyum, Bruce Yi Bu, Zicong Li, Jingfeng Zhou
- 机构：Columbia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23242v1) · [PDF](https://arxiv.org/pdf/2611.23242v1)

## TLDR
Biologically inspired spike encoders—especially DoG and delta modulation—combined with Rouser adaptive-threshold surrogate gradients and K-FAC optimization improve spiking neural network accuracy and parameter efficiency on MNIST/Fashion-MNIST while producing sparser spike trains than rate coding.

## Abstract
Spiking Neural Networks (SNNs) offer theoretical energy-efficiency advantages over conventional deep networks, but realizing these advantages on vision tasks requires sparse spike representations that naive rate-coding methods fail to provide. We combine biologically motivated spike-encoding schemes with two training improvements: Rouser adaptive-threshold surrogate gradients and Kronecker-Factored Approximate Curvature (K-FAC) second-order optimization. The spike encoding schemes experimented with are rate coding, latency coding, DVS-style delta modulation, and Difference-of-Gaussians (DoG) filtering. Experiments on MNIST and Fashion-MNIST demonstrate that biologically inspired encoders yield the largest accuracy gains in capacity-constrained regimes and serve as an effective parameter-efficiency lever. DoG and delta modulation encoders produce significantly sparser spike trains than rate coding. K-FAC yields modest but consistent accuracy improvements over Adam-trained baselines, and Rouser's learnable per-neuron thresholds improve Fashion-MNIST accuracy from 87.37% to 88.13% by enabling homeostatic firing-rate regulation. Biologically grounded pre-processing methods can help close the accuracy gap between SNNs and non-spiking baselines without increasing model size.


## 精读解读（中文）
### 一、研究动机
脉冲神经网络（SNN）理论上比常规深度网络更节能，但在视觉任务上要兑现这一优势，需要稀疏的脉冲表示，而朴素的率编码会产生密集脉冲、削弱能效优势。论文关注的核心问题是：能否通过生物学启发的输入脉冲编码与训练优化，在不增加模型尺寸的情况下缩小SNN与非脉冲基线的精度差距，并提升参数效率。

### 二、技术方案（Method）
研究在MNIST和Fashion-MNIST归一化图像上比较四种编码器：率编码、延迟编码、DVS式差分调制和DoG中心-周围滤波编码，其中差分与DoG采用ON/OFF双极性整流，使有效输入维度D'翻倍。下游为三层SpikingMLP，输入经SparseLinear映射到256和128维隐藏层、再线性投影到类别数，每层接LIF神经元；LIF采用β=0.9、固定阈值1和减法重置，默认全连接，权重用Kaiming均匀初始化并按fan-in缩放。训练使用替代梯度，基线为snntorch快速Sigmoid替代导数（k=25）；Rouser将阈值变为每神经元可学习参数，并对膜电位和阈值分别赋予形状相同、符号相反的替代梯度，通过阈值学习率更新。读出支持脉冲计数、膜电位求和和末时刻膜电位三种模式，并对比Adam与K-FAC二阶优化。

### 三、结果（Result）
实验表明，生物启发编码器在容量受限的小网络中带来最大精度增益，编码器选择可在匹配精度下最多节省约8倍可训练参数；DoG和差分调制编码产生的脉冲串显著比率编码更稀疏。K-FAC相对Adam基线带来 modest 但一致的精度提升；Rouser的可学习逐神经元阈值通过稳态放电率调节，将Fashion-MNIST精度从87.37%提升到88.13%。MNIST上常规SNN已接近饱和（≥98%），因此Fashion-MNIST更能暴露朴素率编码SNN的弱点。

### 四、结论（Conclusion）
生物学 grounded 的预处理与编码方法能够在不增加模型尺寸的前提下，帮助SNN缩小与非脉冲基线的精度差距，并提升参数效率与脉冲稀疏性。可学习阈值和二阶优化是较小但一致的训练侧增益，说明输入编码是SNN视觉任务中独立且重要的优化面。

### 五、方法论与关键技术细节
关键先验包括视网膜中心-周围DoG滤波对应自然图像1/f^2冗余抑制、ON/OFF双通道在零均值信号下可提升每脉冲Fisher信息、微眼跳启发帧差/DVS式差分编码；实现超参为T=25、β=0.9、阈值1、快速Sigmoid k=25、隐藏层256/128、默认连接概率1.0。DoG和差分编码的双极性使首层参数翻倍，K-FAC带来曲率近似开销，Rouser仅增加每神经元一个阈值参数但对阈值学习率敏感。局限是仅在MNIST/Fashion-MNIST和小型MLP上验证，尚未覆盖复杂视觉任务、真实神经形态硬件能耗及更大规模网络。
