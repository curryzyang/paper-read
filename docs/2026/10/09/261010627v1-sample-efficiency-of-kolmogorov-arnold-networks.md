# Sample-Efficiency of Kolmogorov-Arnold Networks

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Kevin Riehl, Shaimaa K. El-Baklish, Fan Wu, Anastasios Kouvelas
- 机构：ETH Zürich
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10627v1) · [PDF](https://arxiv.org/pdf/2610.10627v1)

## TLDR
Kolmogorov–Arnold Networks can match MLP performance with roughly 40% fewer samples—and show up to 50% relative training improvements—in Feynman regression and Gymnasium reinforcement learning benchmarks, highlighting their potential for more sample-efficient control learning.

## Abstract
Deep reinforcement learning has achieved substantial performance gains over classical control approaches. Yet, a central challenge to learning in real-world applications is acquiring costly samples. Kolmogorov-Arnold Networks are a recently proposed architecture that can learn physical relationships in control problems effectively, with significantly higher parameter efficiency and interpretability when compared to Multi-Layer-Perceptron architectures. In this work, we systematically study sample-efficiency using computational experiments, covering the Feynman dataset and the Gymnasium RL benchmark. The results show that similar performance can be achieved with 40% fewer samples using the Kolmogorov-Arnold architecture, and that relative performance improvements up to 50% occur during the training process. The observed gains are robust to varying levels of noise in rewards. These results highlight the potential of the Kolmogorov-Arnold architectures for more sample-efficient reinforcement learning. Code: https://github.com/DerKevinRiehl/neurips26_kan_training


## 精读解读（中文）
### 一、研究动机
深度强化学习在控制中潜力巨大，但真实应用的核心瓶颈是样本效率，因为每次交互都昂贵且安全关键场景难以承受大量试错。KAN 相比 MLP 具有更高参数效率和可解释性，但已有低数据与 RL 证据相互矛盾，尚不清楚在可比实验预算下 KAN 是否真正提升样本效率。本文因此系统评估 KAN 在物理关系学习和 RL 控制中的样本效率。

### 二、技术方案（Method）
方法上先在 Feynman 数据集上用 27 个无单位物理方程做监督回归，训练集规模设为 10 到 1000、测试集固定 1000，并每个设置用 20 个随机种子重复，比较 KAN 与 MLP 在相同优化器、损失、更新步数、批大小和种子下的 NRMSE 等指标。随后在 Gymnasium Classic Control 的 Acrobot、CartPole、MountainCar、MountainCarContinuous 和 Pendulum 上用 PPO 做在线 RL，将 actor 和 critic 同时替换为 KAN 或同时替换为 MLP，并覆盖离散与连续动作空间。模型比较包括 MLP 的 ReLU/Sigmoid 激活和 KAN 的 B-spline、Gaussian RBF、BSRBF 等边函数，通过网格搜索与参数匹配控制复杂度，还加入不同强度高斯奖励噪声测试鲁棒性。评估使用学习曲线、达到目标性能所需样本数、样本减少比例、误差-样本曲线面积以及参数数量和墙钟时间等。

### 三、结果（Result）
Feynman 实验显示 KAN 在约 50 个训练样本后出现清晰的低样本交叉优势，最佳 KAN 家族将平均 NRMSE 从 50 样本时的 0.200 降至 0.163，并在 1000 样本时从 0.127 降至 0.060，相对提升从 13.9% 起且训练中最高可达 50%。Gymnasium 控制任务复现了类似模式，KAN 相对优势在早期至中期训练达到约 41.6% 的峰值，整体上可用约 40% 更少样本达到相近性能。加入高斯奖励噪声会增大方差，但 KAN 与 MLP 的定性比较关系在不同噪声尺度下保持一致，说明增益并非干净奖励反馈的假象。

### 四、结论（Conclusion）
结论是 KAN 在任务具有平滑低维结构时能显著提升样本效率，尤其是在仿真、测量或硬件试验昂贵的早期和中期训练阶段。该优势并非所有任务一致，当两类架构获得大量样本后最终回报往往接近，因此 KAN 更适合低数据控制场景。实际部署可先在稀缺样本阶段用 KAN 训练，再在推理成本成为瓶颈时蒸馏到更便宜的 MLP。

### 五、方法论与关键技术细节
关键实现细节包括：Feynman 数据按方程采样并拒绝非有限值后重采样，输入用训练集标准化，测试集不参与模型选择或归一化；KAN 后端包括 EfficientKAN 的 B-spline、FastKAN 的 Gaussian RBF 以及 BSRBF-KAN 混合边函数，MLP 对照使用 ReLU 与 Sigmoid；主要指标为 NRMSE，并辅以 RMSE、MAE、相对 L2 和 R2，聚合时按种子平均并报告标准误或标准差。RL 部分 PPO 中 KAN 或 MLP 完整替换 actor-critic，KAN 隐藏维度扫描包含 [2]、[4]、[8]、[4,4]、[8,8]、[16,16]，连续动作使用对角高斯加 tanh 压缩且可训练 log 标准差初始化为 0。局限在于效果强依赖环境，最终回报常趋于接近，奖励噪声增大方差，理论样本复杂度假设与 RL 的噪声、自举和策略变化不同，且已有低数据研究显示带个体可学习激活的 MLP 在某些小样本场景可优于 KAN，KAN 组件并非可无条件替换。
