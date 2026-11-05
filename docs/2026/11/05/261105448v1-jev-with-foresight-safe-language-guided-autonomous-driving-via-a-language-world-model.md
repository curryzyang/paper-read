# Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model

- 区域：精读区
- 排名：4
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Yansong Qu, Jiancong Chen, Samuel Labi
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05448v1) · [PDF](https://arxiv.org/pdf/2611.05448v1)

## TLDR
Jev-AD pairs a fast typed decision model with a language world model that foresees each candidate action’s near-future consequences, enabling safe, language-guided autonomous driving with far fewer collisions and high passenger-intent success.

## Abstract
Large language models understand passengers' driving commands, but as driving agents they reason in generated text for seconds and must infer each action's consequences implicitly from the scene. We present Jev-AD, which pairs Jev, a typed decision model that answers predefined questions with probabilities, not generated text, with a language world model that predicts for every candidate action how nearby vehicles move over the next two seconds. Code turns these predictions into foreseen consequences, which Jev compares instead of inferring them from coordinates. In simulated highway merging (500 car-episodes), this foresight lowers the same decision model's collision rate from 26.0% to 2.4% at 0.25 seconds per decision, and Jev-AD achieves the passenger's intent in 93% of free-form command trials. In 500 replayed real-world NGSIM episodes, foresight lowers the collision rate from 48.2% to 2.8%, and the world model, learned from this traffic, foresees 93% of dangerous actions. Project page: https://ys-qu.github.io/jev-ad-website.


## 精读解读（中文）
### 一、研究动机
大语言模型能理解乘客的自由语言驾驶指令，但作为驾驶智能体时往往需要生成文本链式推理，耗时可达秒级，而且只能从场景坐标中隐式推断每个动作的后果，在汇入等密集交互中容易失效。因此需要一种既快又安全的语言引导驾驶框架，让决策模型显式比较候选动作的预见后果，而不是依赖缓慢文本推理或隐式推断。

### 二、技术方案（Method）
Jev-AD 用类型化决策模型 Jev 先将自由语言指令一次性落地为四个概率化问题：是否明确要求撞击/伤人/违法、是否与驾驶无关、激进度评分以及请求的机动类型，并按预设阈值拒绝、暂缓、忽略或执行；每个决策步再让 Jev 在 Left、Idle、Right、Faster、Slower 中选择一个动作。语言世界模型以 Qwen2.5-0.5B 加 LoRA r=16 为骨干，输入自车及最多 8 辆近邻车最近四帧、速度航向加速度、AV 设定速度/目标车道和自车/他车最近三次动作等文本，控制头在自车候选动作和他车动作嵌入条件下预测最多 9 辆车未来 2 秒内 10 个关键帧的加速度与转角，意图头预测他车动作，插值到 20Hz 后用运动学自行车模型积分成轨迹。每次决策对全部候选动作查询一次世界模型，对每个自车动作执行一步后接 Idle 三步，并考虑他车概率不低于 0.2 的动作，保留最严重结果；代码计算是否/何时碰撞、最小 TTC、最终车道与速度、是否完成汇入，并转成短语后果。Jev 的决策输入包含已落地指令、简短场景描述和每个动作的预见后果，指令要求在有安全选项时避免 Collision 或 Danger，并选择最符合乘客意图的安全动作。

### 三、结果（Result）
在 500 个仿真高速公路汇入 car-episode 中，同一决策模型加入预见后碰撞率从 26.0% 降到 2.4%，每次决策约 0.25 秒；在自由语言指令试验中，Jev-AD 有 93% 达成乘客意图。在 500 个回放的真实 NGSIM episode 中，预见使碰撞率从 48.2% 降到 2.8%，且从该交通数据学习的世界模型能预见 93% 的危险动作。

### 四、结论（Conclusion）
结果表明，将快速类型化决策模型与语言世界模型结合，用代码把预测转成可比较的碰撞、TTC、车道和速度后果，可以在语言引导驾驶中显著提升安全性并保持实时性。作者强调起主要作用的是预见本身而非预测器形式，但当前验证仍限于仿真与真实数据回放，并依赖 AV 间共享设定点和历史动作等协作假设。

### 五、方法论与关键技术细节
实验覆盖 highway-env/KoMA 的汇入、三车道汇入和环岛场景，以及 US-101 与 I-80 的 NGSIM 回放数据，仿真中其他车采用 IDM/MOBIL，NGSIM 按车辆 ID 划分训练/验证/测试。关键超参包括 0.5 秒决策周期、2 秒预测时域、10 个关键帧、20Hz 轨迹积分、最多 9 辆车、他车动作概率阈值 0.2、TTC 小于 1.5 秒记为 Danger，以及指令不安全概率 0.8 拒绝、0.2 至 0.8 暂缓、离题概率 0.5 忽略，这些阈值在评估前固定。Jev 单次约 0.13 秒，整体约 0.25 秒/决策，满足 0.5 秒决策周期；数值计算如间距、相对速度和 TTC 由代码完成而非语言模型。局限在于他车当前动作未知且只按概率枚举，AV 间假设可共享设定点和历史动作，实验为仿真和回放而非真实车辆部署，场景与动作空间也受 highway-env 元动作限制。
