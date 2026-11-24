# Failure Modes and Data-Efficient Remedies for Transformer-Based Prediction of Viscoplastic Flows

- 区域：精读区
- 排名：6
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Maedeh Saberi, Hugo Franca, Maziyar Jalaal, Safa Jamali
- 机构：University of Amsterdam, Northeastern University, University of Cambridge
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28267v1) · [PDF](https://arxiv.org/pdf/2611.28267v1)

## TLDR
This paper systematically identifies the failure modes of the transformer-based RheOFormer surrogate for steady Bingham channel flows—particularly in plug-dominated and out-of-distribution regimes—and shows that logarithmic velocity representations, gradient-aware losses, and a few strategically selected training cases substantially improve accuracy and data efficiency.

## Abstract
Fast and accurate prediction of viscoplastic flows remains a challenge in computational rheology due to yield surfaces, discontinuous gradients, and strongly nonlinear transitions between yielded and unyielded regions. Transformer-based neural operators such as RheOFormer have recently shown strong potential for surrogate modeling of non-Newtonian flows. However, their applicability to viscoplastic systems and their efficacy in recovering realistic flows remain poorly understood. In this work, we present the first systematic investigation of RheOFormer applied to steady Bingham channel flow. By isolating the problem to a simple geometry and constitutive model, we examine how dataset structure, numerical value range, and input representation govern the model's ability to interpolate and extrapolate within the parameter space. The data regimes in which RheOFormer remains accurate and those in which errors emerge are identified, particularly for plug-dominated flows and for conditions outside the velocity scales or flow structures represented during training. Upon identifying these failure modes, targeted enhancements to the input representation and loss formulation are introduced to better predict low-gradient plug regions. Logarithmic velocity representations and gradient-aware loss formulations substantially improve accuracy in challenging regimes where the baseline formulation fails. In addition, extrapolation errors are reduced by augmenting the training set with only a few strategically selected cases spanning the missing physical regimes. Finally, a single partially developed snapshot suffices for an accurate steady-state prediction, and the model outperforms simply copying its input throughout flow development. These results highlight the importance of appropriate field representation and parameter-space coverage for data-efficient neural-operator prediction of viscoplastic flows.


## 精读解读（中文）
### 一、研究动机
黏塑性流动的屈服面、梯度间断以及屈服区与非屈服塞流区之间的强非线性转变，使高保真数值模拟和快速代理预测都很困难；Transformer类神经算子RheOFormer已在非牛顿流中显示潜力，但其对黏塑性系统是否适用、何时失效以及如何以少量数据补救仍缺乏系统认识。本文因此以稳态Bingham槽道流为可控基准，剥离几何和本构复杂性，专门考察数据集结构、数值范围和输入表示如何支配插值与外推能力。

### 二、技术方案（Method）
以二维压力驱动Bingham槽道流为数据来源，用Basilisk求解器生成由Re、Bi和固定无量纲压力梯度Kbar=10定义的数据集：Re取0.01至1的9个值，每个Re对应21个从0到8Re均匀分布的Bi；模型输入为早期若干时刻的速度场快照及空间坐标，目标为稳态速度场，且不显式输入Re或Bi。RheOFormer先用前馈嵌入将快照投影到潜空间，经带残差连接和层归一化的多头自注意力编码全局空间耦合，再由随机傅里叶特征坐标嵌入和交叉注意力解码到任意空间网格，最终输出稳态ux。训练比较四种输入表示：原始ux、ux加横向梯度∂ux/∂y、ux加对数梯度log|∂ux/∂y|、以及对输入和目标均取log|ux|；损失采用相对L2损失，并进一步测试联合速度与梯度误差的Sobolev型梯度感知损失。基线使用前5个Δt=0.03的快照（t=0至0.12），训练后稳态预测通过一次前向完成，不积分后续瞬态。

### 三、结果（Result）
基线RheOFormer在训练参数范围内可较好插值，但在塞流主导的低梯度区域会系统性低估平台速度，并在训练未覆盖的速度尺度或流动结构上出现外推误差。采用对数速度表示和梯度感知/Sobolev损失可显著改善这些困难区域中塞流速度与屈服—非屈服过渡的预测；仅加入少量策略性选取、覆盖缺失物理区域的锚点案例，就能明显降低外推误差。时间输入实验表明，单个部分发展阶段的快照已足以获得较准确的稳态预测，且模型优于简单复制最后输入这一平凡预测器。

### 四、结论（Conclusion）
研究表明，对黏塑性流的神经算子代理而言，速度场的数值表示和训练参数空间覆盖与网络架构同等关键；合适的对数变换、梯度信息融入损失以及少量锚点数据，可把基线失效区转化为可接受甚至准确的预测区。该工作为数据高效、可解释地构建屈服应力流体代理模型提供了系统诊断框架，并强调需针对塞流低梯度和外推尺度分别设计表示与采样策略。

### 五、方法论与关键技术细节
关键实现细节包括：数据为二维稳态Bingham槽道流，具有已知精确稳态解和固定平直屈服面，速度场刻意保持未归一化以暴露速度尺度外推失败；对数变换使用log(|·|+δ)，δ=1e-8以避免壁面、静止初始场和塞流内部奇异性，但所有误差均在物理速度场上计算以便跨表示比较。损失以批内相对L2为主并加小常数ε防止除零，Sobolev损失中的预测梯度在训练时数值计算且与真值梯度采用同一差分格式。模型依赖自注意力的全局非局部交互、残差与层归一化、傅里叶特征坐标解码；基线超参为5帧输入、Δt=0.03、单输出稳态场，且不提供Re/Bi标签。局限性在于基准限于简单几何和Bingham本构、仅评估稳态单场预测，外推补救依赖锚点案例选择，梯度计算和表示变换也引入额外数值约束。
