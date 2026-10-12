# CASTER: Formalizing Zero-Shot Manipulation from Synthetic Videos as Constrained Optimization

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Yinlong Dai, Homanga Bharadhwaj, Dylan P. Losey
- 机构：Virginia Tech, Johns Hopkins University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12567v1) · [PDF](https://arxiv.org/pdf/2610.12567v1)

## TLDR
CASTER formalizes zero-shot robot manipulation from synthetic videos as a constrained optimization problem that refines video-derived object trajectories in a digital twin to enforce physical feasibility and semantic consistency, improving average task success by 34.1% over the best baseline.

## Abstract
Prior research on learning from humans often requires real human demonstrations. But advances in video generation models offer a new paradigm: we can now prompt these generators to make synthetic videos of the task. On the plus side, these synthetic videos take place in the robot's current environment, and do not require actual human teaching. However, while the generated videos appear to show plausible motions, they lack both physical consistency and robot grounding, and thus the robot cannot directly roll out the trajectory shown by the video. In this paper we seek to formalize the process of going from synthetic video generation to real-world robot trajectories for zero-shot manipulation tasks. We recognize that this problem is an instance of constrained optimization. The object trajectories extracted from the synthetic video provide an initial guess at the correct motion, and the robot must refine these trajectories (for instance, within a digital twin) while enforcing physical feasibility and semantic consistency. Our optimization-based formalism provides insights into the video generation properties necessary for success. Specifically, we show that the video generation must probabilistically seed the search within a semantic basin of attraction where the trajectory can be locally modified without losing its task alignment. Our analysis further reveals that state-of-the-art approaches can be viewed as instances of our unified formalism with key simplifications. In our experiments we remove these simplifications to more closely match the underlying optimization, leading to more robust zero-shot trajectories from synthetic videos and improving average task success by 34.1% compared to the best-performing baseline. See videos at our project website: https://collab.me.vt.edu/CASTER


## 精读解读（中文）
### 一、研究动机
现有从人类学习操作常需真实人类演示，数据采集昂贵；视频生成模型可在推理时根据任务和机器人当前环境生成合成视频，无需人类教学。但合成视频虽视觉合理，却缺乏物理一致性和机器人接地，无法直接作为轨迹执行。因此需要形式化从合成视频生成到真实机器人零样本操作轨迹的问题。

### 二、技术方案（Method）
CASTER将问题建模为约束优化：输入自然语言任务τ和初始视觉观测o，调用冻结的图文条件视频生成模型q_vid采样合成人类视频v，并用跟踪器f_track将视频映射为物体轨迹，作为待优化物体运动的初始猜测。优化变量是机器人动作轨迹ξ_a及其诱导的系统轨迹ξ，目标是使物体轨迹经任务特征映射φ后的差异最小化；约束为语义成功谓词G_τ(ξ)=1的概率不低于1-ε_sem，且物理可行集F_R内轨迹的概率不低于1-ε_phys。实现上在数字孪生中细化轨迹，提取并加权任务关键特征而非匹配每个路点，迭代满足碰撞避免、可达性、关节/速度限制和接触要求，最后输出可执行机器人动作。

### 三、结果（Result）
理论分析表明，要使零样本迁移成功，视频生成必须概率性地将搜索种子落在语义吸引盆内，使轨迹可局部修改而不丢失任务对齐；多合成视频可帮助播种搜索并识别任务关键特征。现有最先进方法可视为该统一形式化在不同简化假设下的实例。CASTER通过移除这些简化更接近底层优化，实验报告更鲁棒的合成视频零样本轨迹，平均任务成功率相比最佳基线提升34.1%。

### 四、结论（Conclusion）
该工作把从合成视频生成到真实机器人轨迹的零样本操作统一为约束优化，明确区分语义一致性与物理可行性，并给出视频生成模型需满足的可迁移条件。基于该形式化的CASTER通过任务特征对齐和数字孪生约束优化，提升了合成视频驱动操作的鲁棒性与成功率，并为分析和设计相关方法提供通用框架。

### 五、方法论与关键技术细节
细节包括：设定为零样本桌面操作，固定桌面工作区、静态相机、任务物体至少部分可观测，状态由物体状态s_o和机器人状态s_r组成，动作为关节位置变化与夹爪开合，轨迹含时域T内状态和动作。视频生成器q_vid被视为黑盒且冻结，不能微调、无梯度或内部表示，不提供显式几何/接触/运动学信息；f_track被假设能准确提取物体轨迹。损失采用φ映射后的物体轨迹特征距离，φ可实例化为相对轨迹或任务关键特征，ε_sem与ε_phys为语义和物理约束的容忍概率；物理可行集涵盖可达性、关节/速度限制、碰撞避免及必要接触。主要局限是依赖视频生成落入语义吸引盆、f_track准确性和数字孪生保真度，且假设固定工作区与有限时域，未给出显式复杂度数值。
