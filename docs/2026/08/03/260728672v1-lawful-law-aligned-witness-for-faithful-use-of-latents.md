# LAWFUL: Law-Aligned Witness for Faithful Use of Latents

- 区域：精读区
- 排名：6
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Kevin Chen, Kenneth W. Parker, Anish Arora
- 机构：The Ohio State University, Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28672v1) · [PDF](https://arxiv.org/pdf/2607.28672v1)

## TLDR
LAWFUL introduces a physics-grounded interpretability framework that closes key gaps in verifying whether neural networks faithfully learn and internally use continuous physical laws, demonstrated by confirming a Mocap2Radar transformer's adherence to the Doppler frequency law across its domain of validity.

## Abstract
When a neural network predicts a physical system accurately, has it learned the governing law as formal, structured knowledge, and if so, does the network's internal computation actually use that representation throughout the law's domain of validity? We identify four interpretability gaps that limit answering these questions for {\em physics laws over continuous variables}: the absence of a coverage-aware causal-consistency measure over continuous counterfactuals; of a domain-of-validity test for the identified circuit; of a verification of the law's invariants and forbidden behaviors; and of a quantification of how a derived physical quantity flows through the circuit. We develop a foundational framework, LAWFUL, that closes the first two and lays groundwork for the remaining two, and illustrate it on the Mocap2Radar transformer, validating whether it learns and internally uses the Doppler frequency law $f(t) = \frac{2 v(t)}λ$ from motion-capture and radar data in which neither $f(t)$ nor $v(t)$ appears.


## 精读解读（中文）
### 一、研究动机
神经网络在预测物理系统时，其内部是否真正学到了形式化、结构化的物理定律，并且在定律的有效域内因果地使用该表示，这是一个关键的可解释性问题。现有方法存在四个空白：缺乏覆盖连续反事实族的因果一致性度量、缺乏对已识别电路的定律有效域测试、缺乏对定律不变量和禁止行为的验证、缺乏对导出物理量在电路中流动的量化。LAWFUL旨在弥合这些空白，为物理定律的机制可解释性提供基础框架。

### 二、技术方案（Method）
LAWFUL框架将学习模型f与物理模型g对齐。首先定义输入桥B将原始输入映射到物理空间Ω，输出桥D_f和D_g将两个模型输出投影到共享可观测空间Z。然后构建物理有意义的连续反事实扰动族P={p_α}，对每个评估输入x^(i)生成扰动输入x'^(i,α)使得B(x'^(i,α))=p_α(B(x^(i)))。定义物理一致性得分M_P(f,g)=Φ(z_f,z_g)，其中z_f和z_g分别包含基线和扰动下的桥接输出，Φ为设计选择（如误差或相似度）。为识别物理一致电路，将f视为计算图，使用激活修补：充分性配置patch^{x'}_{C}(x)将扰动仅路由到子图C，必要性配置patch^{x'}_{V\C}(x)将扰动路由到除C外的所有组件，计算修补后的得分相对未修补基线M0的偏差Δ_suf(C)和Δ_nec(C)。子图C若满足Δ_suf(C)≤(1-τ)M0且Δ_nec(C)≥τM0则称为τ-物理一致电路，并取最小子图。实例化于MoCap2Radar transformer：学习模型是空间transformer（对53个标记）和时间transformer（对帧）组成的序列到序列模型，输入为MoCap窗口x∈R^{M×L×3}，输出dB尺度微多普勒谱；物理模型对每个标记独立应用多普勒频率定律g(v_rad)=2v_rad/λ。训练数据中不出现f(t)和v(t)，模型仍能泛化到分布外目标。

### 三、结果（Result）
在MoCap2Radar任务上，LAWFUL成功验证了transformer内部确实学习并使用了多普勒频率定律f(t)=2v(t)/λ，尽管f和v均未出现在训练数据中。框架识别出一个物理一致电路，该电路恢复了约91%的物理一致性得分（原文为“recovers 91\...”），并且表现出对切向速度的不变性，即符合多普勒定律中径向速度决定频率、切向速度不影响频率的约束。模型在训练分布之外（如随机游走）仍然保持一致性，表明其推广到定律有效域而非仅经验分布。

### 四、结论（Conclusion）
LAWFUL提供了一个统一的正式框架，通过覆盖连续反事实的物理一致性得分和电路域有效域测试，弥合了物理定律机制可解释性的关键空白。该框架不仅能验证网络是否学习并内部使用物理定律，还能识别负责该行为的电路，并为验证定律不变量和量化物理量流动奠定基础。结论是：模型在预测物理系统时，其内部确实可以形式化地表征物理定律并在整个有效域内因果使用，LAWFUL为这种忠实性提供了可测量的证据。

### 五、方法论与关键技术细节
关键细节包括：数据采用53个反射标记的MoCap轨迹与Bumblebee雷达测量配对，训练输入为重叠STFT窗口（长度L），输出为K个多普勒频率bin的dB谱。输入桥B从MoCap轨迹提取每个标记的径向速度（物理空间Ω），输出桥D将预测谱和物理模型输出投影到共享可观测空间（如多普勒频率）。扰动族P选择径向速度扰动和切向速度扰动，分别测试速度-频率关系和切向不变性。一致性得分Φ采用点误差或相似度度量，取较大值表示更一致，上界为f完全匹配g的理想响应。电路识别使用激活修补，阈值τ∈(0,1)控制充分性和必要性偏差，需M0>0。框架的局限性：扰动族A为无限集时需通过采样、插值或信号重建近似；输入桥B的选择决定所测物理变量；输出桥Z的选择决定测试的物理方面；电路识别依赖扰动族，不同P可能识别不同子图。此外，不变量验证和信号流量化仅部分实现，是未来工作。
