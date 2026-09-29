# When Does Domain Adaptation Help on Physical Vibration Sensors? A Held-Out-Bearing Study of Neural-Operator and Convolutional Models

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Kumbha Nagaswetha, Rabi Pathak
- 机构：India
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31639v1) · [PDF](https://arxiv.org/pdf/2609.31639v1)

## TLDR
Under a held-out-bearing protocol, bearing-fault domain adaptation is far weaker than standard >99% results suggest, and the physics-informed input representation—order tracking with a Fourier Neural Operator—rather than the alignment method is what determines whether unsupervised adaptation succeeds.

## Abstract
Diagnosing rolling-element bearing faults from vibration is a canonical physical-sensing task and a widely used benchmark for domain adaptation under operating-condition shift. Accuracies above 99 percent are commonly reported, but under evaluation splits that place the same physical bearing in both training and test. We revisit the task under a held-out-bearing protocol, assigning every bearing unit entirely to either the training or the test set, and find that source-only transfer is far weaker than such numbers suggest: on a change of shaft speed it reaches only $0.36$, against a target-supervised ceiling of 0.97. We then study what governs transfer. Treating computed order tracking, a shaft-angle resampling that places fault frequencies at fixed shaft orders independent of running speed, as a controlled change of representation, we find that a Fourier Neural Operator raises source-only transfer from $0.36$ to $0.61$ on the speed shift, where the fault peaks move, while a convolutional network of matched feature dimension stays near chance in both representations. The representation also decides whether unsupervised alignment can work: with the same normalized RBF-MMD loss and no target labels, the operator reaches 0.71 in the frequency domain but 0.95 in the order domain, within 0.02 of the target-supervised ceiling and above $0.86$ on every held-out bearing fold. Once the representation is right, a small label budget adds little. These results indicate that, for this task, the input representation rather than the alignment method decides whether adaptation helps. A second dataset, whose held-out units are fault diameters rather than bearings, shows that the same protocol exposes failures that even a target-supervised model cannot avoid.


## 精读解读（中文）
### 一、研究动机
轴承振动故障诊断的域适应文献常报告超过99%的准确率，但许多评估划分把同一物理轴承的窗口同时放入训练集和测试集，模型可能记住轴承单元身份而非故障类型，因此无法回答未见轴承跨工况时迁移到底有多强。本文要在留出整轴承协议下重估该任务，并分离输入表示与对齐方法各自对迁移成败的作用。

### 二、技术方案（Method）
主数据集Paderborn(PU)以1500 rpm为源，900 rpm及降扭、降径向力为目标，按每类三个物理轴承做三折整轴承留出；次数据集CWRU以最轻载为源、其他负载为目标，并以0.007/0.014/0.021英寸故障直径为留出单元。信号经共振带带通(PU 2–6 kHz，CWRU 2.5–4.5 kHz)、Hilbert包络、2 kHz抽取和归一化得到2000点Hz表示，再按已知名义轴速做计算阶次跟踪，以15转×128点重采样得到1920点阶次表示。模型比较FNO(16通道、两个谱块、保留最低200个Fourier模态)与CNN(四个卷积块)，二者在16维特征层对齐；训练用AdamW、类平衡交叉熵、标签平滑、幅值抖动/加噪和梯度裁剪，在源标签加目标标签比例0到0.30下比较none、CORAL、DANN、线性MMD和归一化RBF-MMD，并以source-only B1和target-supervised oracle为参照，每配置3种子×3折、源域验证选模。

### 三、结果（Result）
PU速度偏移下，FNO的source-only迁移从Hz域0.36提升到阶次域0.61(+0.25，9次配对中8次)，target-supervised上限为0.97；同特征维CNN在两种表示下均接近随机。无目标标签且使用相同归一化RBF-MMD时，FNO在Hz域为0.71、在阶次域达0.95，距oracle仅0.02，且每个留出轴承折均高于0.86；表示合适后小标签预算增益很小。CWRU以故障直径为留出单元时，同一协议暴露了即使目标监督模型也无法避免的失败。

### 四、结论（Conclusion）
结果表明，在该物理振动传感任务中，输入表示而非对齐损失更决定域适应能否奏效；把轴旋转周期性和故障阶次不变性编码进坐标可显著改善跨转速迁移。留出物理单元协议说明窗口级划分会高估实际迁移，而CWRU进一步提示未见故障几何可能构成连目标监督都难以突破的上限。

### 五、方法论与关键技术细节
关键实现点包括PU外圈峰在约3.05阶次、一阶谐波6.1阶次；固定15转导致Hz域与阶次域保留时长不同(25 Hz下0.6 s、15 Hz下1.0 s)，固定200模态下两轴带宽也不同(Hz轴200 Hz、25 Hz轴速阶次轴333 Hz)，文中用带宽和时长匹配对照排除这两点。CWRU先按RMS归一化原始窗并将48 kHz健康记录降至12 kHz，且每类故障仅一条记录、健康按连续段切分，留出保证弱于PU的整轴承留出，源健康类仅5至6个一秒窗。模型参数量FNO约207k(谱权为复数)、CNN约375k，二者仅特征维度匹配而非总参数量匹配；对齐权重在FNO上选择后共享给CNN。阶次跟踪假设测试时已知目标名义轴速，这是固定工况研究中的重要约束。
