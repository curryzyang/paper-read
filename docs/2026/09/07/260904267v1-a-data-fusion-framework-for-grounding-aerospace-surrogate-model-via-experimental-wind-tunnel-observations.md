# A Data Fusion Framework for Grounding Aerospace Surrogate Model via Experimental Wind-Tunnel Observations

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Nitin Nagesh Kulkarni, Dheeraj Vemula, Yin Yu, Peter Lyu, Juan J. Alonso
- 机构：Luminary AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04267v1) · [PDF](https://arxiv.org/pdf/2609.04267v1)

## TLDR
A data fusion framework trains a lightweight correction head on wind-tunnel PSP measurements to learn and correct the systematic discrepancies between a frozen CFD-trained Geotransolver surrogate and experimental surface-pressure fields, substantially improving agreement with measured aerodynamics at held-out transonic conditions while preserving the surrogate's generalization and efficiency.

## Abstract
Aerodynamic surrogate models trained on high-fidelity CFD data reproduce numerical predictions of both scalar outputs and entire fields accurately, yet their predictive fidelity is limited by systematic discrepancies between CFD and experimental observations. We present an experimentally grounded correction framework that adapts a CFD-trained deep learning surrogate using wind-tunnel PSP measurements. A Geotransolver surrogate trained on 2,300 high-fidelity CFD simulations of the NASA CRM wing-body configuration, spanning geometric variation, Mach 0.70-0.85, and angles of attack 0 to 4 degrees, reproduces the CFD integrated aerodynamic forces and pitching moment to R2 > 0.99 but does not match the experimental data. To incorporate experimental information without retraining the surrogate, a correction network is trained on spatially registered PSP measurements at two freestream Mach numbers (0.70 and 0.85) across the same angle-of-attack range, learning the discrepancy between the surrogate-predicted and experimentally measured surface-pressure distributions. At Mach 0.85 the correction substantially improves agreement with PSP, particularly at the wing suction peak, shock location, and subsequent pressure recovery, reducing both the magnitude of the prediction error and the fraction of wetted surface on which it exceeds 0.05 in Cp, and it does so from a limited experimental dataset without modifying the pretrained surrogate parameters. On held-out angles of attack the grounded surrogate agrees with measurement to within 2.3-2.7% of the measured Cp range, and outperforms direct interpolation between the measured conditions at every state tested. Experimental measurements can therefore ground a large-scale simulation-trained surrogate by learning systematic CFD-to-experiment discrepancies while preserving its generalization capability and computational efficiency.


## 精读解读（中文）
### 一、研究动机
高保真CFD训练的航空代理模型虽能精确复现数值预测，但其预测精度受限于CFD与风洞实验之间存在的系统性偏差。由于实验数据昂贵且覆盖工况有限，仅靠实验无法独立训练深度学习代理模型，因此需要一种数据融合框架，在保留CFD广覆盖优势的同时，利用少量风洞PSP测量数据对预训练的仿真代理模型进行实验接地校正，以缩小数值与物理系统之间的差距。

### 二、技术方案（Method）
提出一种两阶段数据融合框架。第一阶段，使用包含2300个高保真CFD仿真（NASA CRM翼身组合体，几何参数变化，马赫数0.70-0.85，攻角0-4度）的SHIFT-Wing数据集预训练Geotransolver代理模型，输入表面几何和流动条件，输出表面压力场，模型采用几何感知特征提取层和GALE注意力块。第二阶段冻结预训练Geotransolver参数，提取其潜在逐单元表示，与归一化流动条件拼接后输入轻量级MLP校正头；校正头在空间配准的PSP测量数据（马赫0.70和0.85，各9个攻角，其中1.5度和3.0度作为留出测试）上训练，学习CFD预测与实验测量之间的表面压力分布偏差。训练流程为：先固定主干网络，仅更新校正头参数，最终得到接地后的代理模型。推理时，输入几何和流动条件，经冻结主干和校正头输出实验校正的表面压力。

### 三、结果（Result）
基线Geotransolver代理模型在CFD集成气动力（升力、阻力、俯仰力矩）上R2>0.99，但无法匹配实验PSP数据。在马赫0.85条件下，校正后模型显著改善与PSP的一致性，尤其在翼尖吸力峰、激波位置和压力恢复区域，降低了预测误差幅值和Cp误差超过0.05的湿表面积比例。在留出的四个状态（马赫0.70/0.85，攻角1.5/3.0度）下，接地代理模型与PSP的归一化误差为2.3%-2.7%（MAE/测量Cp范围），R2为0.922-0.966；相比原始插值基线（R2 0.655-0.743）和注册后插值基线（R2 0.756-0.874），接地代理在每个测试状态均更优，最大提升出现在马赫0.85、攻角3.0度（插值R2=0.756，接地代理R2=0.952，提升0.196）。

### 四、结论（Conclusion）
研究表明，少量实验数据能够有效接地大规模仿真训练的代理模型，通过学习CFD到实验的系统性偏差，同时保留原模型的泛化能力和计算效率。该方法无需重训完整代理模型即可显著降低预测误差，优于直接插值实验数据，为仿真与实验的闭环连接提供了可行途径。校正向未测量流动包线之外的迁移程度仍待未来研究。

### 五、方法论与关键技术细节
数据集方面：CFD训练集为SHIFT-Wing，含2262个RANS解（马赫0.70和0.85各约1130/1132），几何由七参数（展弦比7.5-11、四分之一弦后掠角25-37.5度等）经拉丁超立方采样变化，气流角0-4度，侧滑角固定为0，雷诺数不恒定（约10^7量级）；PSP实验数据为NASA CRM风洞测量，每个马赫数9个攻角。数值设置：CFD使用Luminary Cloud求解器，可压缩定常RANS，SA湍流模型，自适应加密四面体网格约3000万单元，残差阈值1e-8，最大15000步，高度35000英尺。校正过程需将PSP数据从原生结构化网格配准到CFD表面网格。损失函数未明确给出，但通过最小化校正头预测与PSP测量压力系数之间的误差实现。超参数细节未完全公开，但校正头为轻量MLP。局限性：校正学习的是综合效应，不区分气动弹性、转捩、湍流模型、设施条件等具体误差源；校正向测量包线之外的迁移能力未知。
