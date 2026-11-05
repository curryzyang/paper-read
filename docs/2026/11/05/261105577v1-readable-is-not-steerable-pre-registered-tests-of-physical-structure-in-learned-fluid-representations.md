# Readable Is Not Steerable: Pre-Registered Tests of Physical Structure in Learned Fluid Representations

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Manvendra Modgil
- 机构：Modint Intelligence
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05577v1) · [PDF](https://arxiv.org/pdf/2611.05577v1)

## TLDR
Across three pre-registered studies on 2D decaying Navier–Stokes flow, the paper finds that physical quantities may be readable from learned latent representations but are not reliably steerable, showing that what a latent contains and what can be controlled through it are distinct properties.

## Abstract
Self-supervised world models are often said to organize their latents around physical quantities. We test this on 2D decaying Navier-Stokes flow in three pre-registered studies, each tested once on held-out data. In Study 1, a joint-embedding predictive architecture (JEPA) trained to predict the flow fails the pre-registered criteria for organizing its latent around fluid quantities better than an untrained network of the same architecture (not supported); a JEPA trained on non-physical linear dynamics and a static invariance model that never sees time do as well or better. In Study 2, plain autoencoders that render the field make enstrophy prominent in their slowest unsupervised latent directions (best r 0.80-0.86 vs 0.38 untrained; fresh seeds, sealed data). Adding VICReg lowers this prominence in every comparison, though not by the pre-registered margin for vorticity, while raising the autoencoders' linear decodability (partially supported). In Study 3, we build steerable directions ("dials") by routing: the decoder gets overall scale only through a small conditioning code, while its other pathway carries a degraded copy of spectral shape. Label-free rules find a loudness dial in all 8 trained models and a shape dial in 3 of 5 fresh seeds on sealed data, against a pre-registered bar of 4; neither control shows a shape dial (partially supported). Across the studies, what a latent contains and what can be controlled through it come apart. In exploration, a supervised direction reading spectral shape almost perfectly moved nothing when steered. During the build, the loudness dial had to be found by its effect on the output (closest to a pure rescaling), not by data variance; for shape, a variance rule and an effect-constrained rule each worked in 3 of 5 seeds. The program used about 70 logged hours on one consumer GPU; all pre-registrations, deviations, code and outputs are public.


## 精读解读（中文）
### 一、研究动机
自监督世界模型常被认为会把潜空间组织成物理量，但线性可解码或与守恒量相关并不等于模型真正表示或可控制该物理量。论文在二维衰减 Navier-Stokes 流上预注册三项研究，区分可解码性、显著性和可操控性，并用对照实验检验“潜空间组织围绕物理”这一说法。

### 二、技术方案（Method）
数据为周期域 64×64 二维不可压衰减 Navier-Stokes 涡量流，伪谱求解器、2/3 去混叠、Lawson 四阶 Runge-Kutta、CFL 0.3、float64，按轨迹划分训练/验证/测试；编码器为带循环填充、GELU、Kaiming 初始化且无归一化的小卷积网络，输出 8×8×128 特征并池化为 128 维潜变量。研究 1 训练 JEPA 在潜空间预测流场，以 EMA 目标和 VICReg 式方差-协方差正则防塌缩，并设非物理线性动力学 JEPA、静态不变模型和未训练网络对照；研究 2 训练重建流场的普通自编码器及加 VICReg 版本，考察最慢无监督方向与 enstrophy 的相关。研究 3 通过路由构造可操控“旋钮”：解码器仅经小条件码获得整体尺度，另一通路只携带退化的谱形状，并用 FiLM 条件调制；操控评估沿方向 d 解码 z+ασ_d d，α 从 -2 到 +2 步长 0.5，测幅值 logE 与形状 log(Z/E)，判据包括效应≥0.2 log 单位、单调 Spearman≥0.9、重编码相关≥0.9 且增益 0.5–2、帧特异性、谱现实性及形状选择性阈值。每项确认性研究先提交假设、规则和分析代码，冻结脚本一次性打开封存测试集，并记录偏差、代码、输出与检查点哈希。

### 三、结果（Result）
研究 1 中，预测流场的 JEPA 未达到预注册标准，未能比同架构未训练网络更好地围绕流体量组织潜空间；非物理线性动力学 JEPA 和从未见时间的静态不变模型表现相当或更好，假设不支持。研究 2 中，普通自编码器使 enstrophy 在最慢无监督方向中显著，最佳 |r| 为 0.80–0.86，未训练对照仅 0.38；加入 VICReg 在每次比较中都降低该显著性，但涡量降幅未达预注册边际，同时提高线性可解码性，结论为部分支持。研究 3 中，无标签规则在全部 8 个训练模型找到响度旋钮，在封存数据的 5 个新种子中 3 个找到形状旋钮，低于预注册门槛 4，两个对照均未出现形状旋钮，结论为部分支持。探索中还发现，能近乎完美读出谱形状的监督方向在操控时几乎不改变输出；整个项目约在一张消费级 GPU 上记录 70 小时计算。

### 四、结论（Conclusion）
三项预注册研究表明，潜变量“包含什么”和“能通过它控制什么”是分离的性质：可读、可解码甚至显著，并不保证可操控。作者据此提出“可读不等于可操控”，并强调需要干预式评估和严格对照，而不能仅凭线性探针或慢方向相关推断模型学到了物理结构。

### 五、方法论与关键技术细节
关键实现包括：2D 周期衰减流、单一模拟器与初始条件分布、按轨迹而非帧划分、结构探针需偏回归掉时间与初始条件族；显著性用 z-score 潜变量、32 主成分和轨迹内/间广义特征问题找最慢方向，并以轨迹平均投影与 log 初始 enstrophy 的最大 |r| 衡量。操控判据要求效应、单调性、重编码一致性、帧特异性和谱包络现实性同时满足，形状选择性 σ_shape 对形状旋钮≥0.7、响度旋钮≤0.2；响度旋钮须按输出效应而非数据方差识别。局限性是范围窄：仅 64×64 二维周期衰减流、一个模拟器、小卷积编码器，结果不宣称可迁移到三维流、更大模型或其他数据；显著性不等于模型知道守恒，探针可解码也不等于模型使用该信息。预注册、偏差、代码和输出公开，但研究 1 测试集为协议性单次使用而非代码封存，部分探索性分析与事后解读需按标签区分。
