# Constructed Reality, Contested Priors: Decoupling and the Architecture of Cognitive Relapse Under the Free Energy Principle

- 区域：精读区
- 排名：2
- 匹配度：3.1/10
- 来源：arxiv
- 作者：MD Ibrahim Hossain Ridoy
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11958v1) · [PDF](https://arxiv.org/pdf/2607.11958v1)

## TLDR
Using a variational autoencoder with a recurrent latent predictor as a computational proxy for free energy minimization, this paper demonstrates that a predictive system's representational capacity and default generative behavior decouple, and that default output can undergo "cognitive relapse"—partial reversion toward a baseline environment despite continued training on a target—establishing that resistance to adopting a new reality as a default prior is a structural property with distinct failure modes irreducible to learning speed.

## Abstract
Under the free energy principle, a predictive system does not observe reality directly; it maintains a generative model of the world and experiences that model's best current hypothesis. Can a synthetic environment be made consistent enough that a predictive system's own inference machinery adopts it as this default hypothesis, permanently displacing the environment that first shaped it? We call this state ontological inversion. Because inducing and monitoring such a transition in a nervous system is neither ethical nor technically feasible, we study the underlying computational problem through a controlled proxy: a convolutional variational autoencoder paired with a recurrent latent predictor, whose evidence lower bound objective is mathematically identical, up to sign, to variational free energy itself. The network is trained first on a baseline visual domain, then on a mixed stream in which a swept rehearsal ratio r controls how much baseline content persists during transition to a target domain. Representational capacity, what the latent space can discriminate, is tracked separately from default behavior, what the system generates when left unconstrained. Across a full sweep of 90 runs, the two diverge sharply: representational accuracy stays near ceiling, 0.97 to 0.998, regardless of r, while default behavior spans nearly the system's entire range depending on r alone, a decoupling of learning from acceptance. More strikingly, at intermediate r the system's default output rises toward the target domain, then partially reverts toward the baseline while training continues unchanged, a structural failure we term cognitive relapse. Resistance to reality-adoption is not reducible to learning speed; it is a structural property with its own distinct failure modes, established here as a computational existence proof and nothing further.


## 精读解读（中文）
### 一、研究动机
自由能原理下，系统体验的是自身生成模型而非直接现实；这引出一个极端可能性：能否用合成环境永久取代系统原本的生成先验？此问题称为本体论倒置，但无法直接在生物神经系统中测试，故本文通过计算代理研究学习与接受之间的结构性解耦及认知复发现象。

### 二、技术方案（Method）
使用卷积变分自编码器（VAE）和循环潜在预测器（GRU）组成的V+M模型。数据：基线域为MNIST，目标域为FashionMNIST。训练分两阶段：阶段1仅在基线域上训练至早停；阶段2从阶段1最佳检查点继续，在混合数据流上训练15个epoch，每个批次按排练比例r（0~0.8）混合基线与目标数据。关键指标：表示能力通过线性探测分类器在潜在空间上区分两域的准确率（w_proxy）度量；默认行为通过GRU自由运行生成图像的域分类概率（dmn_proxy）度量。交叉15个随机种子，共90次运行。

### 三、结果（Result）
表示能力始终接近满分（0.97~0.998），与r无关；默认行为强烈依赖于r：r=0时dmn_proxy立即>0.9，r增加则初始跃迁变慢；在中间r（0.2-0.6）时，dmn_proxy先向目标域上升（多数接近0.9），然后部分回撤至基线，表现为认知复发。这揭示了学习与接受的结构性解耦，且认知复发不能由学习速度解释。

### 四、结论（Conclusion）
认知刚性不是单一的学习速度问题，而是至少包含两个独立故障模式：解耦（表示能力与默认行为分离）和复发（已达成的默认偏移在持续接触基线时部分逆转）。本研究提供了计算存在证明，表明自由能原理下的生成系统可能具有此类结构性质。

### 五、方法论与关键技术细节
关键细节包括：1）数据为MNIST和FashionMNIST，均为简单灰度图像，便于可控实验；2）先验：VAE的KL项使用标准正态先验；3）损失：VAE损失为二元交叉熵重构+KL散度，GRU损失为MSE预测误差，两者联合优化但梯度不相交；4）超参：潜在维度32，GRU隐藏单元256，学习率1e-3，批大小128；5）复杂度：总参数量572,769，可在单GPU上训练；6）约束：排练比r直接控制基线数据在混合流中的持续出现，无其他正则化；局限性：代理模型无皮质层级、睡眠巩固等生物机制，结果仅限计算层面，不可直接推广至生物脑。
