# Calibrated Partial Resets: Preventing Policy Collapse in Continual Reinforcement Learning

- 区域：精读区
- 排名：9
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Luc McCutcheon, Evangelos Chatzaroulas, Saber Fallah
- 机构：University of Surrey
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24996v1) · [PDF](https://arxiv.org/pdf/2607.24996v1)

## TLDR
Calibrated Partial Resets (CPR) prevents policy collapse in continual reinforcement learning by periodically pulling low-utility neurons toward their initialization with a continuous strength scaled by each neuron's utility, avoiding the brittleness of binary resets and outperforming prior methods.

## Abstract
Neural networks are hindered by accumulating dormant neurons and loss of expressivity throughout training, particularly in non-stationary data settings, such as continual supervised and reinforcement learning. Recently, neuron resets have been used to maintain gradient flow and restore plasticity. However, full unit reinitialization often sacrifices peak performance and can destabilize training, leading to policy collapse.
  To preserve plasticity without destabilizing training, we propose Calibrated Partial Resets (CPR), an optimizer that periodically pulls low-utility neurons toward their initialization, with pull strength scaled by each neuron's utility. Unlike binary reset methods, partial resets avoid brittleness; unlike uniform decay, calibrated utility-scaling concentrates adjustment on the units that need it most.
  Among compared methods, only CPR avoids policy collapse over 400M training steps in SlipperyAnt, and it outperforms prior decay and reset-based methods on Continual MetaWorld and Continual MinAtar benchmarks. Ablations reveal a tunable trade-off between plasticity and peak performance, highlighting utility-scaled reinitialization as a promising direction for continual learning.


## 精读解读（中文）
### 一、研究动机
神经网络在非平稳训练（如持续强化学习）中会积累休眠神经元并失去表达能力，现有神经重置方法通过完全重新初始化低效用单元来恢复塑性，但全有或全无的干预方式引入突变参数变化，导致训练不稳定甚至策略崩溃。为此，需要一种既能保持塑性又不会破坏稳定性的选择性且平滑的优化方法。

### 二、技术方案（Method）
提出校准部分重置（CPR）优化器，其核心是每f步将神经元的权重部分拉向初始化值。具体技术方案：(1) 效用估计：使用批数据中传入权重的梯度幅度的层归一化指数移动平均（EMA）作为每个神经元的效用得分；(2) 重置机制：计算每个神经元的重置系数 r_i^l = ρ * φ(u_i^l)，其中 φ 是通过 logistic sigmoid 函数定义的单调递减形状函数（固定 κ=16），ρ 是最大重置比例（<1），使低效用神经元接受强重置，高效用神经元仅受微弱扰动；(3) 权重更新：传入权重按 (1-r) 缩放并加上 r 乘以初始化分布采样，传出权重按 (1-r) 缩放；(4) 流程：在每次基础优化器更新后计算效用EMA，每隔f步执行一次CPR操作，并重置EMA至均值1。

### 三、结果（Result）
在400M步的长时域SlipperyAnt任务中，CPR是唯一在所有15个种子上均未出现策略崩溃的方法（零崩溃），而现有二进制重置方法（如CBP、ReDo）和衰减方法均发生崩溃；在SlipperyHumanoid、Continual MetaWorld和Continual MinAtar基准上，CPR的IQM平均回合回报显著优于先前方法。消融实验表明，CPR能通过调整重置强度ρ和形状函数κ控制塑性-稳定性权衡，且在κ∈[2,20]范围内表现鲁棒。

### 四、结论（Conclusion）
CPR通过部分、效用校准的重置机制，避免了二进制重置的突变不稳定性和均匀衰减的无差别调整，在长期持续强化学习中有效防止策略崩溃并提升最终性能。该工作揭示了效用缩放的重初始化作为持续学习中有前景的方向，并提供了通过调整重置强度实现塑性-稳定性权衡的可控框架。

### 五、方法论与关键技术细节
关键方法与实现细节：(1) 效用度量采用梯度幅度的EMA，相比激活或输出权重更稳定且可扩展；(2) 层归一化使效用均值恒为1，确保跨层可比；(3) 形状函数φ设计为以效用均值为中心的S形曲线，默认κ=16逼近阶梯但保留连续性；(4) 重置强度ρ∈(0,1]是主要超参数，需按任务手工设定；(5) 局限性：CPR依赖初始化分布（如Kaiming），且需周期性重置效用EMA，在极长训练中仍需调度重置频率f；对小批量梯度噪声敏感，但在RL高并发环境（2048环境）下表现稳定。
