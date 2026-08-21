# GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction

- 区域：精读区
- 排名：3
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ziyang Cheng, Tianshu Tang, Jinxin Lan, Xinze Chen, Yuhan Gong, Zhichao Liu, Changzhong Wu, Yahao Mao, Zongyan Deng, Mingxuan Ma, Huasen Xi, Yilong Liu, Yutong Wu, Xiaofeng Wang, Yang Wang, Yun Ye, Guan Huang, Xiaojie Jin, Zheng Zhu, Jiwen Lu
- 机构：Tsinghua University, University of Chinese Academy of Sciences, GigaAI, Chinese Academy of Sciences, University of Shanghai for Science and Technology, Beijing Jiaotong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18234v1) · [PDF](https://arxiv.org/pdf/2608.18234v1)

## TLDR
GigaBrain-WBC-0.5 is a humanoid whole-body control policy trained as a causal Behavior World Model that jointly predicts its next action, state, and latent command distribution, enabling robust terrain/object interaction, online rejection of implausible commands, and fall recovery within a single controller.

## Abstract
Whole-body motion tracking policies turn a humanoid into a robust control interface: the teleoperator---or an upstream model---only supplies a coarse movement intent, while the low-level policy keeps the robot balanced and physically feasible. Existing trackers deliver this interface only on flat ground: trained in empty scenes, they never learn how contact with terrain and objects reshapes their dynamics, and they attempt to teach the policy to balance under any command by continually enlarging the reference-motion corpus, which stops working once feasible behaviors become environment-dependent. We present GigaBrain-WBC-0.5, the first Behavior World Model (BWM) for humanoid whole-body control. Rather than a purely reactive tracker, we train a causal Transformer to jointly predict its next action, next state, and the distribution over its next latent behavior command, so the network that acts also models how the environment shapes what it can do next. An automatic terrain-annotation pipeline recovers full 3D contact geometry from retargeted motion, enabling terrain annotation at the scale of existing motion datasets. The predicted distribution is reused at deployment to detect implausible commands online and retract them onto learned behaviors, so the robot attempts tasks in a "best-effort" manner. The result is a unified policy that takes real-time command, interacts with environment, and stays robust to implausible commands, falls, and disturbances. GigaBrain-WBC-0.5 achieves the highest success rate across all four regimes among three large-scale tracker baselines: 81.3% on terrain interaction (4.3x the strongest baseline), 83.1% under implausible commands, and 99.3% fall recovery (16.8x the strongest baseline). Hardware trials show robust interaction under missing supports and disturbances; the Unitree G1 checkpoint transfers to the Maker L01 robot with simple fine-tuning.


## 精读解读（中文）
### 一、研究动机
现有全身运动跟踪策略只在平坦地面上有效，训练于空场景，无法学习地形与物体接触对动力学的重塑；同时通过不断扩大参考运动库来保证任意指令下平衡的做法，在可行行为依赖环境时失效。因此需要一种能同时建模环境如何塑造可能行为、并在线处理不合理指令与跌倒的鲁棒全身控制方案。

### 二、技术方案（Method）
提出GigaBrain-WBC-0.5，即首个用于人形全身控制的行为世界模型（BWM）。训练一个因果Transformer，在每个控制步联合输出下一动作、下一本体状态以及下一潜在行为命令的混合分布；该网络既执行动作又建模当前环境允许的行为。配合自动地形标注流程，从重定向运动轨迹恢复完整3D接触几何，实现与现有运动数据集规模相当的地形配对语料。部署时利用预测的命令分布在线检测不合理指令，并将其投影到最接近可执行行为上，形成无状态闭式滤波器，无需独立分类器或回退控制器。

### 三、结果（Result）
在四个测试场景中，GigaBrain-WBC-0.5均取得最高成功率：地形交互81.3%（为最强基线的4.3倍），不合理指令下83.1%，跌倒恢复99.3%（为最强基线的16.8倍）。硬件实验显示在缺失支撑和外部扰动下仍能鲁棒交互，且Unitree G1模型通过简单微调即可迁移至Maker L01机器人。

### 四、结论（Conclusion）
行为世界模型将环境交互、在线指令过滤与跌倒恢复统一在一个策略中，使机器人既能实时响应操作员粗略意图，又能以“尽力而为”方式处理不可行指令和跌倒，显著优于现有大规模跟踪器基线，证明了建模自身未来行为比单纯扩大参考数据更有效。

### 五、方法论与关键技术细节
关键设计包括：联合预测动作、下一状态与下一命令分布，使策略内化接触动力学；自动地形标注输出真3D几何而非2.5D高程图，支持桌椅箱体等空间结构；在线滤波器为无状态闭式解，仅含一个运行时安全半径超参，可权衡精度与鲁棒性；训练不使用逐链接触标签或特权状态，命令通道为操作员可在线提供的参考窗口；局限性可能包括对复杂动态物体或极高难度地形的泛化仍需验证，且训练数据规模与多样性依赖现有运动数据集。
