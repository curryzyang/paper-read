# A Vehicle-Integrated Approach to Digital Twin Deployment for Bridges Through Drive-By Sensing

- 区域：精读区
- 排名：3
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Zihao Liu, Daigo Kawabe, Jiaji Wang, Chul-Woo Kim, Mehrisadat Makki Alamdari
- 机构：Kyoto University, KyoCenseo Inc., The University of Hong Kong, University of New South Wales
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08822v1) · [PDF](https://arxiv.org/pdf/2610.08822v1)

## TLDR
The paper proposes a vehicle-integrated digital twin framework that combines Fourier Neural Operator surrogates and machine learning to convert drive-by vehicle vibration data into scalable, continuous bridge and road condition monitoring, validated through multi-site field trials in Australia and Japan.

## Abstract
Ageing bridge infrastructure is a growing global concern, yet conventional Structural Health Monitoring (SHM) systems are costly and difficult to scale, and routine visual inspections remain subjective. Drive-by, or indirect, bridge inspection, in which a sensorised vehicle recovers structural information from vehicle-bridge interaction (VBI) and vehicle-road interaction (VRI) responses, offers a scalable alternative. However, key challenges remain unresolved, including separating bridge responses from road roughness, detecting damage under normal traffic, and generalising across diverse bridge types. This paper presents a vehicle-integrated digital twin framework that unifies physics-based modelling and machine learning for continuous monitoring of bridge and road conditions. The framework comprises three pillars. First, surrogate models of VBI and VRI are constructed using a Fourier Neural Operator that learns function-to-function mappings from operating conditions to vehicle responses. Trained on both simulated and field data, these surrogates deliver millisecond-scale inference, replacing computationally intensive full-order analyses. Second, the design of a custom electric inspection vehicle, its sensor layout, and signal processing chain are optimised through Bayesian optimisation to maximise bridge information yield while suppressing road and vehicle noise. Unsupervised damage-assessment pipelines based on adversarial autoencoders, matrix profiles, and transformer architectures have been developed and validated to process the resulting vehicle data. Third, the complete workflow is validated through coordinated multi-site field trials in Australia and Japan, covering a range of bridge types, traffic conditions, and environmental settings.


## 精读解读（中文）
### 一、研究动机
全球桥梁老化使传统结构健康监测成本高、难扩展，而目视巡检主观且易漏早期损伤；drive-by或间接检测利用装有传感器的车辆从车桥相互作用与车路相互作用响应中反演结构信息，具备可扩展潜力，但仍需解决从路面粗糙度和车辆动力学中分离桥梁响应、正常交通下损伤检测以及跨桥型泛化等问题。将drive-by测量转化为桥梁状态本质上是对耦合车桥系统的反问题，而全阶有限元VBI仿真过慢，因此需要可随每次过桥快速更新的数字孪生。

### 二、技术方案（Method）
本文提出车辆集成数字孪生框架，包含三类支柱：用Fourier Neural Operator构建VBI/VRI代理模型，学习从运营条件到车辆响应的函数到函数映射，并用仿真与现场数据训练以实现毫秒级推理；通过Bayesian优化设计定制电动检测车、传感器布局和信号处理链，以最大化桥梁信息量并抑制路面与车辆噪声，同时用对抗自编码器、matrix profile和transformer等无监督损伤评估流程处理车辆数据；最后在澳大利亚和日本多站点现场试验中验证完整工作流。具体到Old Ada Bridge案例，建立29根构件的钢桁架有限元模型，损伤表示为单根构件杨氏模量折减，结构状态为29维severity向量；两轴车以恒定速度在固定路面谱上过桥，FNO以频谱参数化直接作用于响应频域；正向任务将29个severity作为常量输入通道并输出两轴整段过桥响应，且在损伤与健康响应残差上训练；反向任务以轴响应为输入，通过两个输出头返回损伤构件与severity；训练集为1160次仿真过桥、每构件40次、severity范围0.10至0.60，划分986训练、58验证、116测试。

### 三、结果（Result）
在116条留出过桥样本上，正向FNO预测的车辆响应与全阶有限元结果高度吻合，计算成本仅为有限元的一小部分，且精度随训练集增大持续提升，说明当前受数据量而非模型容量限制。反向配置在102/116条过桥中正确识别损伤构件，severity估计平均绝对误差为0.03；失败案例多将损伤误判为同一弦杆内相邻构件，但severity估计仍较准确，作者将其归因于相邻弦杆构件对车辆响应影响相近导致可区分性不足而非不可观测。Old Ada Bridge部分为数值算例，摘要还报告了在澳大利亚和日本开展多站点现场试验以覆盖不同桥型、交通和环境条件。

### 四、结论（Conclusion）
该神经算子数字孪生可在drive-by配置下同时执行正向响应预测和反向损伤识别，移动车辆作为覆盖全跨的传感器能捕捉包括近支座构件在内的损伤效应，而固定单点传感器难以做到。整体上FNO方法在车致过桥检测中表现良好，但本文Old Ada Bridge结果仍属数值案例研究，后续需用现场数据验证；摘要层面则强调该车辆集成框架可通过多站点试验向连续桥梁与路面状态监测部署。

### 五、方法论与关键技术细节
关键实现细节包括：测试桥为日本Old Ada Bridge，简支钢桁架，主跨59.2m、宽3.6m，1959年建、2012年退役，先前已有5种人工损伤场景的环境与车致振动基准数据；有限元模型含29根构件，分为下弦、上弦、竖杆和斜杆4组，损伤为单根构件杨氏模量折减，severity取0.10至0.60，状态为29维有限向量而非连续损伤场；仿真中两轴车恒速、固定路面谱过桥以控制差异仅来自结构状态；FNO在频域学习算子，正向输入为常量severity通道、输出为两轴响应，训练目标是损伤与健康响应残差，反向输入为轴响应并用双头输出构件与severity；数据为1160次仿真过桥、每构件40次，划分986/58/116；全阶FE单次过桥约需1分钟，FNO推理为毫秒级；局限是相邻同弦构件响应差异小导致误识别，且Old Ada Bridge部分为数值验证，摘要所述Bayesian优化车辆与传感器、无监督对抗自编码器、matrix profile、transformer及澳日现场试验的详细指标未在预览中给出。
