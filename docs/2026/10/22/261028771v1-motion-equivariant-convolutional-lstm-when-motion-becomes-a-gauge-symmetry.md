# Motion Equivariant Convolutional LSTM: When Motion Becomes a Gauge Symmetry

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Vahid Hosseinzadeh, T. Anderson Keller, Michael Puthawala
- 机构：Cusp AI, Harvard University, South Dakota State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28771v1) · [PDF](https://arxiv.org/pdf/2610.28771v1)

## TLDR
The paper introduces MELSTM, a convolutional LSTM that treats motion as a time-local gauge symmetry and estimates time-varying velocities as a gauge field to transport its memory, making it provably equivariant to arbitrary motion and outperforming ConvLSTM and flow-equivariant models on future-frame prediction, motion-only classification, and action recognition.

## Abstract
Objects move, cameras pan, and weather drifts with the wind: much of what changes in sequential data is motion. Motion changes where things are, not what they are, and is therefore a symmetry of the data. Yet standard recurrent networks are not equivariant to it: their memory stays put while the input moves on. Flow equivariant recurrent networks first brought this symmetry into sequence models, for motions of constant velocity, or flows, by enumerating a bank of velocities. We extend this idea in three directions: from simple recurrent networks to convolutional LSTMs, from flows to motions whose velocity changes in time, and from enumerating velocities to estimating them. Treating a sequence as a field over time, we show that motion becomes a gauge symmetry: a global symmetry made local in time. Built on this view, our motion equivariant convolutional LSTM (MELSTM) uses its velocity model as the gauge field and is provably equivariant to every motion. Across future-frame prediction, classification of digits visible only through their motion, and action recognition under camera shake, MELSTM outperforms a convolutional LSTM and its flow equivariant counterpart with the same number of parameters: it is more accurate, generalizes to longer horizons and to unseen motions, and carries a fraction of the flow equivariant model's state.


## 精读解读（中文）
### 一、研究动机
序列数据中大量变化源于运动：物体移动、相机平移或抖动、天气漂移。运动改变的是位置而非内容，因此应视为数据的对称性；但标准循环网络的内存停原地，输入运动时隐藏状态不随之传输，导致拖影。已有流等变循环网络只处理常速度流，并通过枚举速度副本实现，状态大、速度离散且变速时历史会丢失。

### 二、技术方案（Method）
作者把序列视为时间上的场，将运动建模为随时间变化的群作用，把全局对称性在时间上局部化后视为规范对称性；MELSTM在卷积LSTM中引入速度模型，读取序列并在每步输出李代数元素u_t，生成传输算子T_t，将隐藏状态和细胞状态从前一步传输到下一步。速度模型可为可训练或免参数模块，其等变条件是按规范联络规律变换；对多物体局部运动，模型用少量槽位分别传输，并通过槽位跟踪用自身隐藏状态匹配当前帧来估计各槽速度，避免显式帧间对应。

### 三、结果（Result）
在Moving MNIST未来帧预测、仅通过运动可见的数字分类以及相机抖动下KTH动作识别三个任务上，MELSTM在参数量与ConvLSTM和流等变对照相同的情况下均更准确；它是唯一在运动统计变化时性能不下降的模型，并能泛化到更长预测时域和未见运动。Moving MNIST上训练每epoch约比流等变模型快6倍，外推到训练时域的8.5倍时误差低37倍，且所需状态仅为流等变模型的一小部分。

### 四、结论（Conclusion）
论文表明仅靠权重约束不足以让卷积LSTM获得流或一般运动等变，因为流等变仅对应测度零的核集合，时空核在非零时间延迟下会被迫在空间上恒定；真正需要的是让记忆随输入运动而传输。以估计速度生成规范传输的MELSTM可证明对所有运动等变，并能通过槽位叠加扩展到局部多运动场景，说明运动等变性是提升序列模型泛化与效率的有效归纳偏置。

### 五、方法论与关键技术细节
关键实现是把速度模型视为规范场，传输算子实现平行传输，速度在输入被运动ψ变换时须满足u_t变为ψ_t u_t ψ_t^{-1}+dotψ_t ψ_t^{-1}，这是保证定理成立的核心约束。与FERNN枚举速度格点副本不同，MELSTM估计连续速度，避免状态随速度库膨胀并支持时变速度；槽位跟踪在隐藏状态内完成分割和速度估计，无需解帧间对应。局限性包括依赖李群运动结构与速度模型满足规范变换，局部运动用少量槽位近似表示，理论等变性与实际离散实现之间仍需数值近似。
