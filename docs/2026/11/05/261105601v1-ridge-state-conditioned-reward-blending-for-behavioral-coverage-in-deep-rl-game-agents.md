# RIDGE: State-Conditioned Reward Blending for Behavioral Coverage in Deep RL Game Agents

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：AL Muqshith Mohammed Shifan, Kevin Christopher Chua, Ali Neshati, Loutfouz Zaman, Cristiano Politowski
- 机构：Ontario Tech University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05601v1) · [PDF](https://arxiv.org/pdf/2611.05601v1)

## TLDR
RIDGE enables a single PPO game agent to cover multiple playstyle personas by smoothly blending persona rewards using state-conditioned weights while a multi-head critic keeps each persona’s value learning stationary, avoiding the instability of mid-episode reward switching.

## Abstract
A deep RL agent trained on a fixed persona reward plays one way: an Explorer keeps exploring while starving, a Survivor hoards on an empty map. Since each persona fixes its own reward, automated playtesting trains N agents for N styles. Changing reward composition mid-episode runs into the switching-stability dilemma: PPO degrades under non-stationary rewards. We present RIDGE, a single-agent architecture that sidesteps the dilemma with two design choices: a state-conditioned blender that computes softmax-normalized sigmoid weights from slow-moving state variables, and a multi-head critic that trains one value head per persona on its own stationary signal. On Crafter with four personas, one \ridge agent acquires both branches of the wood-tier crafting/combat split that no fixed-persona baseline solves jointly, and a sharpness ablation confirms state-conditioning drives the gain. We position these results as demonstrations of the blending mechanism's dynamics across n=3 seeds per condition; larger multi-seed sweeps remain future work.


## 精读解读（中文）
### 一、研究动机
固定人格奖励训练的深度强化学习智能体只会表现单一行为，自动玩法测试需为N种风格训练N个智能体，且难以覆盖同一回合内随状态变化的行为切换；而在回合中改变奖励组合又会触发切换稳定性困境，使PPO因奖励非平稳而退化。RIDGE旨在用单智能体实现状态条件化的奖励混合，从而兼顾多风格行为覆盖与训练稳定性。

### 二、技术方案（Method）
在Crafter上为Explorer、Survivor、Craftsman、Warrior定义可解释的人格奖励，并由状态条件混合器从新地块、生命体征最小值、制作进度、敌人接近度等慢变状态特征计算各人格Sigmoid激活，经偏置、尺度与全局锐度α得到归一化混合权重，聚合奖励为各人格奖励的加权和。策略网络共享编码器，critic采用每人格一个价值头的多头结构，各头用GAE在各自平稳的人格回报上训练；策略更新使用按混合权重组合的混合优势代入PPO裁剪目标，价值头以逐头MSE损失训练。训练流程为采集rollout、逐时刻计算权重与人格奖励、计算各人格回报与优势、混合优势后做K轮PPO优化与价值头更新；实验设α=1.0四头RIDGE、四个单头固定人格基线及α∈{0.0,0.5,1.5,2.0}消融，统一1M环境步和相同PPO/Adam超参，每条件n=3种子。

### 三、结果（Result）
在Crafter的木材层级分叉上，RIDGE单个智能体同时取得Wood Pickaxe 0.32和Wood Sword 0.26，而Craftsman为0.70/0.16、Warrior为0.12/0.79，说明专家基线只在自身分支强、RIDGE能跨分支覆盖且在本分支低于专家，体现覆盖—专精权衡；三者均能到达共同前置Place Table（RIDGE 0.75、Craftsman 0.90、Warrior 0.88）。RIDGE还在Wake Up上达到0.66，远高于Explorer/Craftsman的0.15和Warrior的0.01。锐度消融显示α=0的均匀混合（无状态条件）比状态条件变体低约30%–50%，α=1.5/2.0略优于1.0但差异在种子波动范围内；RIDGE价值损失约0.04，接近最稳定的Explorer，低于Craftsman/Warrior，而Survivor-only为0.3–0.5。

### 四、结论（Conclusion）
结果表明，状态条件化的平滑奖励混合与多头critic可绕开切换稳定性困境，使单一智能体在同一训练过程中获得跨分支制作/战斗覆盖和生命体征管理行为，且增益主要来自状态条件化而非仅使用四个人格奖励。多头critic通过让每个价值头学习平稳的人格信号，保持了与最稳定专家相当的价值学习稳定性。作者将n=3种子的结果定位为混合机制动态的演示而非确定性结论，后续需更大规模多种子扫描，且Crafter绝对分数受编码器和基线设置差异影响不宜直接横向比较。

### 五、方法论与关键技术细节
关键实现细节包括：四个可读的人格奖励分别奖励新地块、生命/饥饿/口渴/能量维持及阈值下悬崖惩罚、制作成就、战斗成就，制作/战斗奖励按科技树深度缩放；混合器权重为sigmoid(α k^i(σ_t^i−b^i))后按人格求和归一化，α→0退化为均匀混合、α→∞接近硬argmax；每个价值头以各自人格回报的GAE和MSE训练，策略使用混合优势。实验在Crafter标准1M环境步下用PyTorch PPO，条件间共享编码器、Adam、rollout长度、batch大小、GAE系数、PPO clip和熵奖励，仅改变奖励信号、锐度与critic头数，每条件n=3种子。局限性是种子预算小、结果属初步演示、状态条件区间内的最优α尚需更多种子确定，且Crafter成就沿科技树顺序依赖，深层成就低成功率反映整条前置链；代码、数据和检查点已公开。
