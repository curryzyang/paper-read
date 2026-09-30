# Graph neural networks for sampling-invariant embeddings of organized signal sets

- 区域：精读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Martin Bauw, Santiago Velasco-Forero, Jesus Angulo
- 机构：PSL University, Université Paris-Saclay
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35934v1) · [PDF](https://arxiv.org/pdf/2609.35934v1)

## TLDR
This paper investigates graph neural network encoders that project heterogeneously sampled organized signal sets into fixed-size, sampling-invariant, waveform-aware embeddings for discrimination, evaluated on synthetic complex-valued radiofrequency signals.

## Abstract
Sensor networks and radars can deliver signals as organized sets, e.g. ordered signals, signals describing range cells within a grid or signals perceived as graph nodes. Within such sets, individual signals may be characterized by distinct sampling parameters. This paper investigates organized signal sets neural network encoders. In the context of this work, the purpose of such encoders is to project heterogeneously sampled signal sets into an arbitrary fixed-size vectors space. This new representation space is designed so that signal sets can be processed as vectors rid of sampling differences to allow for arbitrary topology-aware processing with no signal processing constraints. Within this representation space designed to reduce the influence of heterogeneous sampling parameters, the relevance of signal sets representations is evaluated by considering signal sets discrimination potential with a focus on waveforms separation. The encoding and embeddings discrimination experiments conducted rely exclusively on synthetic complex-valued radiofrequency signals.


## 精读解读（中文）
### 一、研究动机
传感器网络和雷达会以有组织集合的形式给出信号，例如有序信号、距离单元网格中的信号或被视为图节点的信号，且集合内单个信号可能具有不同采样参数。本文研究有组织信号集合的神经网络编码器，目标是把异构采样信号集合投影到任意固定大小的向量空间，从而消除采样差异并以向量形式支持任意拓扑感知处理。该表示空间通过信号集合区分潜力评估，重点考察波形分离能力。

### 二、技术方案（Method）
将 P 个 M 维复信号 Z 与邻接矩阵 A 输入图神经网络 Φ，信号实际长度 M'≤M 并零填充到 M，批量输入 G∈C^{B×P×M}，输出嵌入 E∈R^{B×N}。提出的编码器为三层 GCN，均值池化得到 128 维信号集合嵌入，采用链状图且有向边指向中心节点，并以 NT-Xent 对比损失训练，正对为同标签信号集合，使用余弦相似度和温度 τ。基线包括忽略拓扑的 1D 自编码器、图自编码器，以及无学习得 raw_spectrum 的 320 维傅里叶特征和 raw_dsp 的 44 维统计信号特征，下游用决策树分类头，并用 silhouette、KNN 及 PCA、t-SNE、UMAP 评估潜在空间。

### 三、结果（Result）
在潜在表示空间分类中，GCN 编码器在 Train+ 上训练 60 epoch 后取得最佳信号集合模板分类表现，GCN 基线紧随其后，而 1D 自编码器训练 40 epoch 后表现较差并低于谱和统计特征。测试集混淆矩阵显示线性下扫频 chirp 与二次下扫频 chirp 间存在有限混淆，且仍难以区分集合内波形顺序，例如 chirp3_noise2 与 noise2_chirp3、chirpup2_fsk3 与 fsk3_chirpup2 混淆。raw_spectrum 和 raw_dsp 基线意外地难以击败，在某些未展示模板下系统性地优于训练神经编码器。

### 四、结论（Conclusion）
本文表明图神经网络适合编码有组织信号集合以用于下游判别，所提编码器在合成条件下产生对异构采样参数稳健的判别表示。考虑图结构使表示对集合内顺序敏感，适用于传感器网络和雷达单元邻域处理。实验也重申谱与统计特征作为嵌入的相对竞争力。未来将考虑更大更复杂信号集合、真实数据、更多波形，并以分类和异常检测评估嵌入，同时指出对训练未见波形的泛化仍具挑战，需研究图拓扑和注意力机制。

### 五、方法论与关键技术细节
数据为合成复基带射频信号，含 19 个五节点模板，每集合 5 个信号，受加性白高斯噪声污染并零填充到 M=4096；Train 与 Train+ 各 100000 个集合，Val 与 Test 各 10000 个集合，每个信号独立抽长度和采样率，SNR 每集合共享，训练、验证、测试参数池互斥，Train+ 扩展了采样与噪声参数。GCN 为三层、128 维、2.33M 参数；AE 为 1D 卷积、128 维瓶颈、1.28M 参数，GAE 未能取得实质可分性；NT-Xent 使用余弦相似度和温度 τ，AE 使用长度掩码 MSE。评估用 silhouette、KNN 和降维可视化，决策树分类，神经网络指标在三 seed 上平均；局限包括集合内顺序识别困难、无学习特征竞争力强以及未见波形泛化难。
