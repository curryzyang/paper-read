# REACT: A Fully Spiking State-Space Model for Real-Time Event-Driven Temporal Perception

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Geoffroy Keime, Nicolas Cuperlier, Benoit R. Cottereau
- 机构：CNRS, ENSEA, Université de Toulouse, CY Cergy Paris Université
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19204v1) · [PDF](https://arxiv.org/pdf/2609.19204v1)

## TLDR
REACT is a fully spiking, event-by-event state-space model that uses a complex-valued spiking neuron driven by physical inter-event intervals to process raw event-camera streams without temporal accumulation, enabling low-latency, continuously updated temporal perception such as time-to-collision estimation and gesture recognition.

## Abstract
Robotic systems operating in dynamic environments require visual perception that evolves continuously with the incoming sensory stream. Event cameras provide microsecond temporal resolution and asynchronous sensing, but most learning-based methods accumulate events into frames or temporal bins, introducing an integration delay that can limit fast reaction. Here we propose REACT, a fully spiking state-space model for event-driven temporal perception that processes raw events one by one, without temporal accumulation. REACT uses a complex-valued spiking neuron, C-SiLIF, whose continuous-time dynamics are driven by the physical inter-event interval, allowing its internal state to evolve at the temporal resolution of individual events. We evaluate REACT on gesture recognition and time-to-collision (TTC) estimation from full-field event streams, without a target bounding box or localization input. On EvTTC, REACT achieves a 9.59% relative TTC error with 4.6 ms end-to-end inference latency, within 0.15 percentage points of the best learned method while requiring no target prior. At the dataset's mean approach speed, this latency corresponds to only 4 cm of vehicle motion, compared with 1 m for the fastest competing learned method. REACT further supports anytime TTC prediction, zero-shot transfer to a different driving sequence, and INT8 quantization, reducing the estimated energy consumption from 18.5 to 2.8 mJ per 32,768 events. These results show that event-driven spiking state-space dynamics can provide low-latency, continuously updated temporal perception for reactive robotic systems.


## 精读解读（中文）
### 一、研究动机
动态环境中的机器人需要随事件流连续演化的低延迟视觉感知。事件相机具有微秒级时间分辨率和异步感知能力，但多数学习方法把事件累积成帧或时间箱后再推理，引入积分延迟并破坏原生时间结构。本文旨在让模型直接逐个处理原始事件，在事件到达时更新状态，以保留细粒度时序并支持快速反应。

### 二、技术方案（Method）
REACT把每个事件(t,x,y,p)编码为空间通道索引j=p*HW+y*W+x和物理事件间隔Δt，经可学习嵌入E与LayerNorm得到token；核心C-SiLIF为每通道一个复数状态的线性时不变状态空间神经元，其动力学为du/dt=Λu+bx，Λ=-e^{λ_re}+iλ_im，离散化时用δ_k=e^ρ·Δt_k，α_k=exp(Λδ_k)，状态更新u_k=α_k·u_{k-1}+b·z_k，脉冲s_k=Θ(2Re(u_k)-θ)，且脉冲不重置状态。网络主体为2个残差块、128通道，每块沿时间维独立更新C-SiLIF并做通道混合线性层，块间用掩码均值池化并按实际时间累加事件间隔；训练时用Hillis-Steele前缀扫描并行计算，部署时严格逐事件顺序推理。手势识别任务用交叉熵和标签平滑；TTC任务回归η=1/TTC，读出logη的均值μ和对数方差s，用高斯负对数似然训练，预测TTC_hat=e^{-μ}。评估包括DVS128 Gesture和EvTTC，其中EvTTC直接使用全视场事件流且不提供目标框，坐标下采样后输入。

### 三、结果（Result）
在EvTTC上，REACT取得9.59%的相对TTC误差和4.6 ms端到端推理延迟，仅比最佳学习型方法差0.15个百分点，且不需要目标先验。按数据集平均接近速度，4.6 ms延迟仅对应车辆移动约4 cm，而最快竞争学习方法约为1 m。REACT还支持任意时刻TTC预测、零样本迁移到不同驾驶序列以及INT8量化，估计能耗从18.5 mJ降至2.8 mJ每32,768个事件。在手势识别上，它以更小的状态空间组件保持了有竞争力的准确率（摘要未给出具体数值）。

### 四、结论（Conclusion）
全脉冲状态空间动力学可以直接在事件时间尺度上持续更新，为反应式机器人提供低延迟、连续更新的时序感知。无需时间累积或目标框即可完成全视场TTC估计，并具备任意时刻预测、零样本迁移和神经形态部署的能效潜力。结果表明，事件驱动的脉冲状态空间模型适合TTC等实时时序感知任务。

### 五、方法论与关键技术细节
关键实现细节包括：事件间隔Δt作为连续物理量进入离散化，而非时间箱索引；C-SiLIF无脉冲重置使状态递归保持线性，|α_k|<1由构造保证稳定性，脉冲非线性仅作读出；初始化采用S4D-Lin，e^{λ_re}=0.5、λ_im=π/s，e^ρ按10^-3至10^-1对数均匀采样，b_re~U(0,1)、b_im=0；代理梯度为宽度2的arctan。DVS128 Gesture使用131,072事件窗口、池化因子32，增强含时间偏斜、逐事件时间/空间抖动、随机丢事件、roll/rotation/scaling和事件CutMix，不做水平翻转；EvTTC无目标框、全视场、事件坐标8倍下采样，TTC用η=1/TTC和高斯NLL，评价含e_TTC及MiD_w，后者在[0,3)、[3,6)、[6,10)秒区间按0.5、0.3、0.1加权。局限与约束包括：EvTTC不池化导致每事件能耗较高，能耗为估计值，INT8量化效果和完整训练超参在摘要/预览中未全部给出，部署为严格逐事件顺序推理。
