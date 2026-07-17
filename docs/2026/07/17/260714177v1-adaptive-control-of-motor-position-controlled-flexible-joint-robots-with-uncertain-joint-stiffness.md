# Adaptive Control of Motor-Position-Controlled Flexible Joint Robots with Uncertain Joint Stiffness

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Annika Kirner, Grazia Zambella, Igor Kovacevic, Hannes Höppner, Jee-Hwan Ryu, Christian Ott
- 机构：Korea Advanced Institute of Science & Technology, Berliner Hochschule für Technik, TU Wien
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14177v1) · [PDF](https://arxiv.org/pdf/2607.14177v1)

## TLDR
This paper presents an adaptive control method for motor-position-controlled flexible joint robots that estimates uncertain nonlinear joint stiffness online using an implicit control law and a control-input-dependent regressor, with robustness to motor position controller errors and experimental validation.

## Abstract
Model-based control of flexible joint robots with position-controlled actuators relies on accurate knowledge of the joint compliance. In practice, precise stiffness models are often unavailable as the properties of physical elastic elements vary with operating conditions and slowly change over time due to wear and aging. To improve model-based control of these systems, we propose an adaptive control approach in this work, which updates an estimate of the uncertain, nonlinear torque-deflection relation of each joint. As opposed to classical adaptive control approaches for non-elastic robots, we rely on an implicit control law and a control-input-dependent regressor matrix to account for the uncertain joint stiffness. We analyze robustness of the approach against errors induced by the motor position controller. Experimental results on a flexible joint with nonlinear stiffness characteristics demonstrate the effectiveness of the proposed approach.


## 精读解读（中文）
### 一、研究动机
在电机位置控制的柔性关节机器人中，模型基控制依赖精确的关节刚度模型，但实际中刚度因操作条件变化、磨损和老化而缓慢改变，导致控制性能下降。为解决这一问题，本文提出一种自适应控制方法，在线更新每个关节的不确定非线性扭矩-变形关系估计。

### 二、技术方案（Method）
针对n自由度柔性关节机器人，连杆侧动力学为M(q)ddq + C(q,dq)dq + g(q) = ψ(θ_d - q + e_θ)，其中θ_d为电机命令位置。假设弹性扭矩ψ可分解为已知回归矩阵Y(θ_d - q)与常参数向量k的乘积：ψ = Y k。基于Slotine和Li的刚性机器人自适应控制器，定义滑模变量s = de + K_p e，期望扭矩τ_d = M(q)ddq_r + C(q,dq)dq_r + g(q) - K_s s。然后通过隐式控制律求解θ_d：Y(θ_d - q) k_hat = τ_d，其中k_hat是k的在线估计。参数更新律根据李雅普诺夫设计，使跟踪误差收敛。对于线性回归和特殊立方回归，隐式控制律有解析解。此外，分析了电机位置控制器误差e_θ非零时的鲁棒性，基于L2和小增益定理给出稳定性条件。

### 三、结果（Result）
在具有非线性刚度特性的柔性关节实验台上进行验证，结果表明所提自适应控制器能够有效提高连杆侧轨迹跟踪性能，相比无自适应情况，跟踪误差显著减小。鲁棒性分析显示，当电机位置控制器误差在一定界限内时，系统仍能保持稳定。

### 四、结论（Conclusion）
提出了一种针对电机位置控制柔性关节机器人的自适应控制器，能够在线适应不确定的非线性关节刚度。该方法通过隐式控制律和输入相关回归矩阵处理刚度不确定性，实验验证了其在非线性刚度关节上的有效性，为实际应用中应对刚度变化提供了可行的方案。

### 五、方法论与关键技术细节
关键点包括：1) 基于回归矩阵的参数化假设，需要根据机械设计选取足够丰富的基函数来近似真实扭矩-变形关系；2) 控制律隐式求解，对于线性情况可显式反解，对于立方情况可用Cardano公式解析求解；3) 参数更新律无显式损失函数，通过李雅普诺夫方法推导确保收敛；4) 增益矩阵K_p和K_s(t)需正定且K_s(t)连续有界；5) 鲁棒性分析假设电机位置误差足够小且内环控制器时间尺度足够快；6) 局限性包括依赖已知回归结构、未考虑惯量不确定性、以及参数常数的假设，实际中可能需要近似。
