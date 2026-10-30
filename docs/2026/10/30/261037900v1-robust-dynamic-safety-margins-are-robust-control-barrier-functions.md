# Robust Dynamic Safety Margins are Robust Control Barrier Functions

- 区域：精读区
- 排名：1
- 匹配度：6.3/10
- 来源：arxiv
- 作者：Victor Freire, Saber Jafarpour, Marco M. Nicotra
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37900v1) · [PDF](https://arxiv.org/pdf/2610.37900v1)

## TLDR
TLDR: This paper shows that dynamic safety margins can serve as robust control barrier functions—via input-to-state stability or contractivity—and derives closed-form robust DSM-based CBFs for linear systems, with simulations demonstrating improved disturbance rejection over nominal DSM-CBF baselines.

## Abstract
This paper establishes robustness properties for control barrier functions (CBFs) constructed using dynamic safety margins (DSMs). We show that DSMs can act as robust CBFs by leveraging input-to-state stability for Lyapunov-based constructions, and contractivity for trajectory-prediction-based approaches. Additionally, we derive closed-form DSM-based robust CBFs (RDSM-RCBFs) specifically for linear systems. Simulations highlight the improved robustness of the proposed RDSM-RCBFs compared to nominal DSM-CBF baselines.


## 精读解读（中文）
### 一、研究动机
控制屏障函数可用于安全控制器设计，但鲁棒控制屏障函数的构造方法仍然缺乏；现有备份CBF和动态安全裕度方法虽有构造性优势，却主要针对名义系统或计算负担较重。本文旨在研究动态安全裕度在外部有界扰动下的鲁棒性，并建立其与鲁棒控制屏障函数之间的理论联系。

### 二、技术方案（Method）
考虑控制与扰动仿射系统，扰动属于紧凸集且控制输入受凸紧集约束，在预稳定反馈下定义状态-参考增强空间中的鲁棒动态安全裕度。作者先利用Nagumo定理和MFCQ把鲁棒控制不变性转化为约束函数的切锥条件，再证明RDSM在该增强空间中构成RCBF，并据此构造RDSM-RCBF安全滤波器以在线筛选鲁棒安全输入。RDSM的构造给出两条路径：基于输入-状态稳定Lyapunov函数，以及基于预稳定系统轨迹预测及其收缩性；对线性系统和小面体约束进一步导出闭式RDSM-RCBF。

### 三、结果（Result）
论文证明动态安全裕度在增强状态-参考空间中可作为鲁棒控制屏障函数，并为基于Lyapunov和基于轨迹预测的两类DSM分别建立ISS与收缩性依据。对线性系统，作者得到闭式RDSM-RCBF表达式，并指出相应的安全滤波优化问题具有持续可行性。仿真结果表明，所提出的RDSM-RCBF相较名义DSM-CBF基线具有更好的扰动抑制与鲁棒安全性。

### 四、结论（Conclusion）
RDSM为构造鲁棒CBF提供了一条结构化途径，将预稳定控制、动态安全裕度和增强空间安全滤波统一起来。该框架既能覆盖Lyapunov型设计，也能覆盖轨迹预测型设计，并在线性系统中简化为可计算的闭式形式；但其保证依赖有界扰动、模型结构和约束 qualification 等假设。

### 五、方法论与关键技术细节
关键细节包括：采用最坏情况扰动抑制哲学而非允许安全集扩张的ISSf；以约束函数超水平集描述安全集并要求MFCQ以保证切锥的简洁表达；RDSM定义在系统状态与参考拼接的增强空间，安全滤波器需要持续可行性；扰动集需紧凸且含零，控制集为凸紧集；两类构造分别依赖ISS Lyapunov函数或轨迹预测的收缩性，线性小面体约束情形可闭式化；潜在局限是轨迹预测型方法的计算负担、最坏情况设计的保守性以及理论保证对模型和假设的依赖。
