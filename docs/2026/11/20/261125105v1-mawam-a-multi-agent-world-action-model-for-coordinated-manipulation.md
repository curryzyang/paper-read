# MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Xianzhe Fan, Chi-Pin Huang, Fu-En Yang, Jing Wang, Yecheng Wu, Yu-Cheng Chou, Johan Bjorck, Linxi "Jim" Fan, Jan Kautz, Yu-Chiang Frank Wang, Zhiding Yu, Hengshuang Zhao, Zhiqi Li
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25105v1) · [PDF](https://arxiv.org/pdf/2611.25105v1)

## TLDR
MAWAM is a multi-agent world-action model that jointly predicts all robots’ future views and executable action chunks via cross-agent attention, enabling coordinated manipulation and achieving 67.8% real-robot and 90.3% simulated average success.

## Abstract
Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the highest success on all three real-robot tasks (laundry-bag collection, bath-towel folding, and umbrella handover), with 67.8% mean success, 18.9 percentage points above MA-VLA trained on the same demonstrations and cameras. In simulation, MAWAM reaches 90.3% mean success on eight tasks with teams of up to four arms. Ablations show that cross-agent attention and team-stage future-video supervision both improve coordinated control: without attention, a four-arm relay falls from 95.0% to 39.0%, and without this supervision, Place Food falls from 78.0% to 47.0%.


## 精读解读（中文）
### 一、研究动机
多机器人协同操作中，任一机器人的动作都会改变队友所处的物理世界，因此仅预测各自动作而忽略彼此造成的未来观测变化，难以实现真正协调。现有基于单机器人的世界-动作模型或视觉-语言-动作策略缺乏对团队联合未来的显式建模，导致在交接、折叠、收集等需要紧密配合的任务中成功率受限。作者因此提出同时生成“团队动作”与“团队共同创造的物理未来”的多智能体世界-动作模型。

### 二、技术方案（Method）
MAWAM 以预训练的单机器人世界-动作模型为骨干，输入为各机器人当前观测（多相机视图）与任务条件，将每个机器人的未来视图 token 与可执行动作 chunk token 放入同一去噪序列，通过跨智能体注意力在所有机器人的动作与未来视图 token 之间联合去噪，单次采样即同时输出各机器人的未来视图和动作块。模型为每个机器人保留独立的控制接口以输出各自动作，同时在训练中引入团队阶段（team-stage）的未来视频监督，使联合预测不仅拟合动作标签，也约束团队共同造成的视觉未来。推理时从噪声出发联合迭代去噪，得到各机器人可直接执行的动作 chunk，并在执行中按观测更新继续预测。

### 三、结果（Result）
在三项真实机器人任务（收集洗衣袋、折叠浴巾、雨伞交接）上，MAWAM 全部取得最高成功率，平均成功率 67.8%，比在相同示教数据与相同相机配置下训练的 MA-VLA 高 18.9 个百分点。仿真中在多达四只机械臂的八个任务上平均成功率达 90.3%。消融显示跨智能体注意力与团队阶段未来视频监督都对协同控制有实质贡献：去掉注意力后四臂接力任务从 95.0% 降到 39.0%，去掉该监督后 Place Food 从 78.0% 降到 47.0%。

### 四、结论（Conclusion）
结果说明，把多机器人动作与联合未来观测放在统一生成过程中建模，并借助跨智能体注意力共享彼此意图，是提升协同操作成功率的有效途径；团队层面的未来视频监督提供了额外的物理一致性约束，二者缺一都会显著削弱多臂协调能力。该工作表明世界-动作模型可从单机器人自然扩展到多智能体团队，并保持各机器人独立的控制接口。

### 五、方法论与关键技术细节
方法复用预训练单机器人世界-动作骨干以降低数据需求，训练数据为与 MA-VLA 完全相同的多相机示教，保证对比公平；核心实现是动作 token 与未来视图 token 的联合去噪加跨智能体注意力，并以团队阶段未来视频预测作为辅助监督，各机器人保持独立动作解码头。需要关注的是联合去噪的序列长度与注意力复杂度随机器人数增加而增长，实验覆盖最多四臂、真实任务仅三项，向更多智能体、更长时域与异构机器人团队的扩展性及对示教规模与相机配置的敏感性仍需进一步验证。
