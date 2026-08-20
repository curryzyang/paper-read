# FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences

- 区域：精读区
- 排名：2
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Omar Rayyan, Zhi Li, Max Argus, Yuxin Jiang, Chang Yu, Chenfanfu Jiang, Yuchen Cui
- 机构：University of California, Los Angeles, University of Washington, Allen Institute for AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17027v1) · [PDF](https://arxiv.org/pdf/2608.17027v1)

## TLDR
FetchMan trains visual humanoid loco-manipulation policies entirely in simulation by combining synthetic behavior cloning with Flow-GRPO reinforcement learning, enabling zero-shot deployment on a real Unitree G1 that walks to and grasps objects in unseen scenes at 73.3% success.

## Abstract
Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior to the real world, as is commonly done in locomotion, sidesteps this struggle, so we replicate that recipe for loco-manipulation. In doing so, we find that cloning synthetic demonstrations results in a low performance ceiling no matter the amount of training data. Reinforcement learning breaks through it, and refining the cloned policy with Flow-GRPO on a single sparse reward yields performance that synthetic behavior cloning cannot match. Together, these stages form our end-to-end sim-to-real pipeline spanning more than 150,000 scenes, which we use to train FetchMan. We evaluate it on FetchMan-Bench, a simulation benchmark we release, and deploy it zero-shot on a real Unitree G1, where our single-object reach-and-pick policy walks to and grasps a target across unseen scenes at 73.3% success. Finally, we extend this recipe to multi-object training, a first step toward loco-manipulation generalist policies at this data scale.


## 精读解读（中文）
### 一、研究动机
视觉人形机器人移动操作策略要泛化到新场景和新物体，长期是机器人研究的目标。然而，数据饥渴的算法在桌面操作上收集示范已很困难，对人形机器人还需行走和平衡，示范收集更难。从仿真数据学习并迁移到真实世界，如 locomotion 领域常见做法，可绕过这一困境，因此本文将该范式复制到移动操作任务。作者发现直接克隆合成示范存在性能上限，需要强化学习突破，从而提出端到端仿真到真实世界的训练流程。

### 二、技术方案（Method）
该方法分为三阶段：首先使用带特权信息的脚本化全身控制器在程序化生成的室内场景中滚动生成合成示范数据，场景来自 MolmoSpaces（含 ProcTHOR-10k、Holodeck 等），每个 episode 采样场景、目标物体和机器人起始位姿，通过 A* 路径规划和离散操作阶段（reach/descend/close/lift）控制 Unitree G1 完成到达-抓取任务，并施加域随机化（纹理、光照、相机内外参、表面高度、物体位姿、动作噪声）。其次，用行为克隆（BC）从这些合成示范中训练视觉策略，输入为头部鱼眼图像、腕部 RGB 图像和本体感知向量（基座高度、横滚俯仰、上半身关节位置、夹爪开度），输出15维全身指令（基座线速度/偏航、基座高度、腰部关节、右臂关节、夹爪目标），基座指令由预训练的 SONIC 下半身控制器跟踪。最后，用 Flow-GRPO 在单一稀疏奖励下对克隆策略进行强化学习微调，利用仿真中相同状态的分组 rollout 打破示范性能上限，得到最终策略 FetchMan，并零样本部署到真实 Unitree G1。

### 三、结果（Result）
在包含超过150,000个场景的仿真训练后，FetchMan 在真实 Unitree G1 上对未见场景的单物体到达-抓取任务达到 73.3% 成功率，且无需真实数据或逐场景调参。实验表明克隆合成示范无论如何增加数据量都有性能天花板，而 Flow-GRPO 微调后的策略显著超越合成行为克隆。作者还发布了 FetchMan-Bench 仿真基准，并将该流程扩展到多物体训练，向移动操作通用策略迈出第一步。

### 四、结论（Conclusion）
本文证明仿真数据生成结合行为克隆与 Flow-GRPO 强化学习微调的端到端流程，可训练出能零样本部署到真实人形机器人的视觉移动操作策略。该方法克服了脚本化示范的模仿间隙，在场景多样性和真实泛化上优于纯行为克隆，为人形机器人移动操作提供可扩展的仿真到真实范式。

### 五、方法论与关键技术细节
关键细节包括：采用分层控制，将29维关节力矩压缩为15维全身指令，SONIC 控制器以50Hz跟踪基座指令，上半身和夹爪用PD控制，减少命令空间并保持 sim-to-real 一致性。示范数据中80%为完整到达-抓取，20%为纯抓取（起始于抓取站位）以平衡操纵阶段并随机化初始上肢配置。起点位姿在完整3D物理验证下可贴近支撑面，扩大接近几何分布。域随机化每 episode 独立重采样纹理、光照、相机、表面和物体位姿以及动作噪声。Flow-GRPO 在确定性 ODE 采样器中加入高斯噪声获得逐步似然，实现无需真实交互的强化学习微调。局限性包括：策略在单物体任务上评估，多物体为初步扩展；真实部署成功率仍有提升空间；依赖 MolmoSpaces 场景生成和预训练 SONIC 控制器，对仿真资产质量和控制器性能有一定依赖。
