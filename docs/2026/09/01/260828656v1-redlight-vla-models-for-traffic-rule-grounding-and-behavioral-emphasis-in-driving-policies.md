# RedLight-VLA: Models for traffic-rule grounding and behavioral emphasis in driving policies

- 区域：精读区
- 排名：1
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Bala Murali Manoghar Sai Sudhakar, Sourab Bapu Sridhar, Sandipan Das, Rahul Ahuja, Meda Lazar, Ashish Garg, Pratik Likhar, Senthil Yogamani
- 机构：Qualcomm Technologies, Inc., USA, Arriver System Software S.r.l., Romania, Qualcomm Auto Ltd Sweden Filial, Sweden, Qualcomm India Private Limited, India
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28656v1) · [PDF](https://arxiv.org/pdf/2608.28656v1)

## TLDR
RedLight-VLA improves behavior-cloned Vision-Language-Action driving policies at signalized intersections by combining trajectory-derived behavioral reweighting with parallel auxiliary heads for traffic-light and stop-line grounding, reducing red-light overshoot, stop-line velocity error, and displacement errors.

## Abstract
Behavior-cloned Vision-Language-Action (VLA) driving policies struggle with rare rule-governed maneuvers at signalized intersections. Braking and launching examples contribute little to averaged trajectory loss, while fused representations lack explicit supervision for the governing traffic-light and stop-line state. We present RedLight-VLA, a training objective that uses expert futures and automatically generated perception targets without additional manual rule annotation. First, trajectory-derived behavioral reweighting (BR) emphasizes rare deceleration and acceleration using rotation-invariant longitudinal dynamics and a scale-preserving reduction that exactly recovers the baseline when disabled. Second, parallel auxiliary (AUX) heads ground traffic-light and stop-line state in continuous post-fusion rule tokens, without autoregressive language generation or changes to the trajectory decoder. We evaluate on a curated set of 20 s sequences with a 5 s prediction horizon. Controlled variants share the same backbone, training data, decoder, and evaluation population. Against an otherwise identical VLA baseline, RedLight-VLA reduces red-light stop-line overshoot from 7.3% to6.8%, reduces stop-line velocity error by 12.7%, and improves 3 s trafficlight-sliced ADE/FDE from 0.274/0.964 m to 0.247/0.897 m. Green-light false stops increase from 3.2% to 3.9%; however, combining BR with AUX supervision mitigates the larger increase observed for AUX alone (4.0%). The combined model also improves non-traffic-light ADE/FDE from 0.268/0.956 m to 0.241/0.876 m and outperforms either mechanism alone on all four sliced displacement measures.


## 精读解读（中文）
### 一、研究动机
行为克隆的视觉-语言-动作（VLA）驾驶策略在信号交叉口的罕见规则控制操作中表现不佳，因为制动和起步样本对平均轨迹损失的贡献很小，且融合表示缺乏对交通灯和停车线状态的显式监督。

### 二、技术方案（Method）
提出RedLight-VLA训练目标，包含两个关键模块：一是基于轨迹导出的行为重加权（BR），利用旋转不变的纵向动力学和尺度保持的缩减方式强调罕见的减速和加速样本，并在禁用时精确恢复基线；二是并行辅助头（AUX），在连续的后融合规则token上监督交通灯和停车线状态，无需自回归语言生成或修改轨迹解码器。模型在20秒序列、5秒预测horizon的精选数据集上评估，受控变体共享相同骨干、训练数据、解码器和评估集。

### 三、结果（Result）
与完全相同的VLA基线相比，RedLight-VLA将红灯停车线过冲从7.3%降至6.8%，停车线速度误差降低12.7%，3秒交通灯分片的ADE/FDE从0.274/0.964米改善到0.247/0.897米。绿灯误停从3.2%升至3.9%，但BR与AUX结合缓解了单独AUX带来的更大上升（4.0%）。组合模型还改善了非交通灯ADE/FDE从0.268/0.956米到0.241/0.876米，并在所有四项分片位移指标上优于任一单独机制。

### 四、结论（Conclusion）
RedLight-VLA通过行为重加权和并行辅助监督有效增强了驾驶策略对交通规则的grounding和行为侧重，在红灯场景显著减少过冲和速度误差，同时保持整体轨迹预测性能提升，是无需额外人工规则标注的可扩展方案。

### 五、方法论与关键技术细节
关键点包括：BR使用旋转不变纵向动力学进行重加权，且设计为可关闭以恢复基线；AUX头直接利用连续后融合规则token，避免离散语言生成；评估关注20秒序列和5秒预测horizon，使用交通灯分片指标；控制变量保证公平对比；局限性是绿灯误停略有增加，需BR与AUX联合抑制，且评测集为精选场景而非全量开放道路。
