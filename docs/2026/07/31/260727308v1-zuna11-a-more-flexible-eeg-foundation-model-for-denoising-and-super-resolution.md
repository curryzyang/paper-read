# ZUNA1.1: A more flexible EEG foundation model for Denoising and Super-resolution

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Christopher Warner, Jonas Mago, JR Huml, Beren Millidge
- 机构：Zyphra
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27308v1) · [PDF](https://arxiv.org/pdf/2607.27308v1)

## TLDR
ZUNA1.1 is a 380M-parameter EEG diffusion autoencoder that flexibly reconstructs variable-length (up to 30s) and arbitrarily sampled/missing channel data, matching or exceeding its predecessor ZUNA1 while substantially outperforming standard methods like spherical spline interpolation.

## Abstract
We introduce ZUNA1.1, a 380M-parameter diffusion autoencoder for flexible EEG signal reconstruction. ZUNA1.1 is capable of reconstructing variable length sequences of up to 30s, with an arbitrary number of EEG channels at arbitrary scalp locations, and can reconstruct arbitrary temporal intervals within channels in addition to reconstructing entire channels. We demonstrate that ZUNA1.1 performs at least on par with our earlier ZUNA1 model, while being far more flexible and capable of handling a wide range of reconstruction tasks. ZUNA1.1 continues to substantially outperform standard EEG denoising and reconstruction methods such as spherical spline interpolation, which is ubiquitously deployed in the MNE package. The ZUNA1.1 model is released open source under the permissive Apache 2.0 license.


## 精读解读（中文）
### 一、研究动机
现有EEG基础模型ZUNA1仅支持固定5秒窗口，且训练时的随机通道丢弃模式与真实场景中常见的突发性、空间相关或消费级头戴设备稀疏布局等损坏模式不匹配，导致部署到实际流程时存在明显局限。为了修复任意长度（0.5-30秒）、任意位置通道及通道内任意时间区间的损坏EEG信号，本文提出更灵活的ZUNA1.1。

### 二、技术方案（Method）
ZUNA1.1是一个380M参数的Transformer编码器-解码器扩散自编码器，采用4D-RoPE位置编码以支持任意通道数量和头皮位置；训练时随机裁剪0.5-30秒窗口，通过flex attention和样本感知掩码将变长样本打包批量训练，并采用每窗口z-score归一化、高通+陷波与带通两种滤波变体进行隐式增广。预处理阶段为每条记录计算每通道每秒的质量矩阵（结合方差、峰峰值、平坦度三个指标），并在加载时按阈值筛选通道；训练采用八种通道丢弃方案的混合（包括全通道随机、随机均匀、全时段时间块、相关通道时间块、标准/随机蒙太奇、脑区、消费级设备布局），分三阶段调整权重，并加入sandwich norm和QK-norm提升稳定性，同时移除自适应损失加权。损失函数为解码器上的rectified-flow损失加编码器辅助MMD正则，训练语料扩至约350万通道小时并显著增加训练步数。

### 三、结果（Result）
在四个数据集上按头皮区域进行通道重建评估（NMSE），ZUNA1.1在多数区域与ZUNA1相当或更优，且显著优于MNE中常用的球面样条插值。它支持最长30秒变长序列、任意数量/位置通道、以及通道内任意时间区间的重建；在保持380M参数和Apache 2.0开源协议下，性能至少不逊于ZUNA1，同时灵活性和任务覆盖范围大幅提升。

### 四、结论（Conclusion）
ZUNA1.1通过变长训练、质量感知预处理和多样化丢弃策略，解决了ZUNA1固定窗口和失效模式单一的问题，成为更灵活、可直接用于EEG去噪与超分辨率的开源基础模型。实验表明其在保持原有重建质量的同时显著优于传统插值方法，适合实际消费级和实验室EEG数据修复场景。

### 五、方法论与关键技术细节
关键细节包括：长度采样采用分段均匀分布（0.5-1s占0.2、1-5s占0.3、5-10s占0.3、10-30s占0.2）；质量矩阵Q由方差评分、峰峰值评分和平坦度评分逐元素取最小值得到，阈值在加载时应用；丢弃训练分三阶段，布局类方案在44万步后退出；早期1.2B参数消融未见显著收益，故保持380M；MMD正则权重被调低以改善下游表示质量；使用flex attention的打包机制需处理样本间掩码，训练窗口以0.125秒为粗时间单位。模型以Apache 2.0协议开源，提供pip install zuna。
