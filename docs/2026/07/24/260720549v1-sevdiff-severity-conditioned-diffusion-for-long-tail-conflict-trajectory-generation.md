# SevDiff: Severity-Conditioned Diffusion for Long-Tail Conflict Trajectory Generation

- 区域：精读区
- 排名：4
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Eni Solomon Laughter
- 机构：Chang’an University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20549v1) · [PDF](https://arxiv.org/pdf/2607.20549v1)

## TLDR
SevDiff is a severity-conditioned diffusion model that generates vehicle interaction trajectories at a requested Time-to-Collision value, achieving 100% hit-rate for low TTC targets, enabling precise generation of rare conflict events for ADAS stress-testing.

## Abstract
Trajectory datasets used in ADAS evaluation are heavily biased toward routine driving; genuine vehicle-to-vehicle conflict events are rare, and the rarer the event, the higher the cost when an ADAS system fails to handle it. Existing generative approaches address this imbalance by conditioning on scene-level properties - spatial goals, agent structure, or natural-language adversarial objectives - but none can accept a target Time-to-Collision (TTC) value as input and be held to producing it within a measurable error. This paper introduces SevDiff, a severity-conditioned denoising diffusion probabilistic model (DDPM) that accepts a requested minimum TTC value as a scalar conditioning signal and generates paired vehicle interaction trajectories whose realized conflict severity matches the request, evaluated through a hit-rate metric. Trained on 468 interaction windows extracted from the UTE SQM-W-1 expressway weaving-section dataset (1,041 vehicles, 822,691 observations after smoothing), SevDiff achieves 100% hit-rate within +/-0.5 s for TTC targets of 0.5-1.5 s and 97-99% at 2.0-2.5 s, with graceful degradation to 39% at TTC = 5.0 s. Generated kinematic features are physically plausible, with a maximum out-of-range rate of 4.7% across 12 features and no negative speed or gap values in more than 96.5% of samples. The hit-rate degradation pattern is physically interpretable as the strength of the conditioning signal relative to the training prior, making it a precision characterization of the generator rather than a pass/fail result.


## 精读解读（中文）
### 一、研究动机
现有ADAS评估轨迹数据集严重偏向常规驾驶，真实冲突事件稀少，且越罕见的事件系统失败成本越高。现有生成方法虽能通过场景级属性（空间目标、代理结构、语言对抗目标）缓解不平衡，但无法接受目标TTC值作为输入并产生可控误差内的场景。因此，需要一种能够直接根据用户指定的最小TTC值生成对应严重性轨迹的模型。

### 二、技术方案（Method）
提出SevDiff，一个严重性条件去噪扩散概率模型（DDPM），以目标最小TTC值标量作为条件信号，生成配对车辆交互轨迹。数据来自UTE SQM-W-1高速交织区数据集（1041辆车，822691个观测），经Savitzky-Golay滤波平滑后，提取468个交互窗口，每个窗口用12维运动学特征向量表示（包括跟随车车速均值和标准差、头车车速均值和标准差、车间时距均值/最小值/标准差、窗口内最大和平均逆TTC（ITTC）、相对速度均值、交互时长、归一化窗口长度）。采用始终可定义的ITTC（当跟随车不接近时为0）作为严重性标签，对每个窗口取峰值ITTC进行严重性分箱（TTC 0.5-5.0 s，半宽±0.25 s），共10个等级。模型为DDPM，在12维特征空间上正向扩散300步（线性噪声调度），条件信号通过正弦位置编码与扩散步数编码求和后注入去噪网络。去噪网络为四层MLP（SiLU激活，256隐藏单元），训练时使用逆频率加权采样使各严重性分箱贡献均衡，优化噪声预测目标。推理时从纯噪声出发，逐步去噪生成符合条件的目标样本。评估采用命中率指标：生成轨迹的最小TTC落在目标值±δ内（δ=0.5 s）的样本占比。

### 三、结果（Result）
在TTC目标0.5-1.5 s范围内，命中率（±0.5 s）达到100%；在2.0-2.5 s时命中率为97-99%；但在5.0 s时降至39%。生成轨迹的运动学特征物理合理：12个特征的最大越界率为4.7%，超过96.5%的样本无负速度或间隙值。

### 四、结论（Conclusion）
SevDiff首次实现了对扩散模型进行数值代理安全度量（SSM）的精确条件控制，并通过命中率直接评估生成精度。命中率随目标TTC增大而下降的模式是可解释的——条件信号强度相对于训练先验中心变弱，这成为生成器精度的表征而非通过/失败判定。该方法为ADAS测试中长尾冲突场景的受控生成提供了实用工具。

### 五、方法论与关键技术细节
关键点包括：(1)采用逆TTC（ITTC）而非标准TTC，确保所有交互窗口都有定义的标签；(2)数据预处理通过Savitzky-Golay滤波（速度窗长7帧，横向距离窗长11帧，阶数3）消除噪声，速度平均变化仅0.011 m/s；(3)使用极值理论（POT）确定严重性分箱上限为TTC=5 s；(4)训练采用逆频率加权采样以缓解长尾分布；(5)条件信号直接是输出特征之一（ITTC），避免了潜在空间编码的模糊性；(6)模型仅用468个交互窗口即达到高命中率，但局限性在于对常规TTC（>3 s）命中率下降，且结果可能依赖特定道路几何（交织区）。(7)最大超出率4.7%表明物理合理性仍有改进空间。
