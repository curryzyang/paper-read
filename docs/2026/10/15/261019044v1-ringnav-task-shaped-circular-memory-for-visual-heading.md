# RingNav: Task-Shaped Circular Memory for Visual Heading

- 区域：精读区
- 排名：9
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Naitri Rajyaguru, Aryan Tajne, Stephen Jardim, Cornelia Fermuller, Yiannis Aloimonos
- 机构：University of Maryland, College Park
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.19044v1) · [PDF](https://arxiv.org/pdf/2610.19044v1)

## TLDR
RingNav is a 10.6k-parameter visual heading estimator that uses task-shaped circular memory on \(S^1\) by learning only the turn between consecutive images, improving heading accuracy, enabling exact identity and sequence-reversal behavior, transferring zero-shot to real drones, and running in real time on ultra-low-power edge hardware.

## Abstract
Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the turn between consecutive images, while heading is composed directly on the circle. On the TartanAir Visual SLAM Challenge, RingNav reduces mean absolute turn error by \(27\%\) and accumulated heading error over $4$ sec by \(15\%\) relative to a similarly sized learned-memory model. The structured update also gives exactly zero turn for identical frames and exact cancellation under sequence reversal. Without fine-tuning, RingNav transfers to real-world drone experiments and continues estimating heading under severe visual degradation. RingNav runs at $27.3$Hz on Raspberry Pi Zero 2W and can be deployed on an ultra-low power GAP8 processor at $33.4$Hz.


## 精读解读（中文）
### 一、研究动机
小型机器人计算与内存受限，但视觉导航系统常维护超出任务所需的状态；作者提出任务塑形记忆，即在任务已知状态结构时固定状态及其更新规则，只学习观测如何改变状态。本文聚焦视觉航向，其状态是一维周期变量，天然位于圆环 S^1 上，因此不应让网络学习隐含的持久状态。RingNav 试图验证固定圆形记忆与更新能否以极小模型实现鲁棒航向估计。

### 二、技术方案（Method）
输入为相邻两张320x320 RGB图像，共享卷积编码器将按时间顺序拼接的图像对编码为24维特征，再经两层MLP和门控标量头得到有序预测；对正向和反向图像对分别推理，取半差作为反对称视觉转角估计。持久状态为S^1上的二维单位向量，用固定旋转矩阵R(Δψ)更新并重投影，航向由atan2读出，状态更新无可学习参数。训练使用24帧窗口、步长从{1,2}采样，损失包括4倍相邻转角循环误差、0.1倍多尺度路径积分损失（horizon 2/4/8）、分支监督和对称分量惩罚；推理时因果地逐帧配对前一帧，更新S^1状态。

### 三、结果（Result）
在TartanAir Visual SLAM Challenge上，RingNav相对同规模学习记忆模型将平均绝对转角误差降低27%，4秒累积航向误差降低15%。结构化更新保证相同帧输出严格为零转角，序列反转时转角严格反号并可精确抵消。无需微调即可迁移到真实Crazyflie飞行数据，在严重视觉退化下仍能估计航向；模型仅10.6k参数，在Raspberry Pi Zero 2W上27.3Hz、GAP8上33.4Hz运行。评估还覆盖CompTest、HDH-Bench（196条轨迹、四个未训练渲染场景）及35条Crazyflie序列共18,974个图像转换。

### 四、结论（Conclusion）
结果表明，将航向的持久记忆直接约束到S^1并固定其旋转更新，是面向资源受限机器人实现轻量视觉航向估计的有效任务塑形设计。学习只需承担图像间视觉转角的估计，从而带来更小状态、更好泛化和边缘部署可行性，并保持对重复、退化或缺失视觉输入的鲁棒性。该工作也为其他具有已知任务状态流形的导航问题提供了可检验的设计范式，但本文实验仅覆盖S^1航向。

### 五、方法论与关键技术细节
关键实现包括：图像归一化后按通道拼接，编码器为四层3x3步长2无偏置卷积，通道数8/12/16/24，各接BN和ReLU，全局平均池化后接32维隐藏/输出MLP；门控头用A、B、a、b、w_o生成标量。反对称性由半差投影构造，辅助L_br与L_sym仅正则化投影前的有序预测；S^1状态仅存2个FP32（8字节），R∈SO(2)后仅做有限精度归一化，无学习状态转移。训练数据含104条序列（80条TartanAir和24条渲染轨迹），验证8条TartanAir，评估含16条CompTest、196条HDH-Bench和35条Crazyflie；总损失权重为4、0.1、1、0.5。推理因果、无需未来帧、地图、关键帧或学习式隐状态转移；局限是仅实验验证了S^1航向，正反向图像因拼接需分别前向计算，且未扩展到完整VO/SLAM状态。
