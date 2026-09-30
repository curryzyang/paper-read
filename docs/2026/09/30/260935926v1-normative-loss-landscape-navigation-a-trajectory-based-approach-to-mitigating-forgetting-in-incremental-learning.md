# Normative Loss Landscape Navigation: A Trajectory-Based Approach to Mitigating Forgetting in Incremental Learning

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Isabelle Aguilar, Zayn Andre Zainal, Luis Fernando Herbozo Contreras, Zhaojing Huang, Omid Kavehei
- 机构：University of Sydney
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35926v1) · [PDF](https://arxiv.org/pdf/2609.35926v1)

## TLDR
TMLN mitigates catastrophic forgetting in continual learning by framing sequential learning as optimal control over a Riemannian loss landscape and using a memory-efficient diagonal Fisher Information Matrix with trajectory-modulated preconditioning to protect critical parameters without additive penalties.

## Abstract
Continual learning models suffer from catastrophic forgetting when trained sequentially on non-stationary data distributions. Previously, this has been addressed through weight regularization. While preconditioning gradients offer a promising alternative to mitigate forgetting, current approaches are myopic. Conversely, standard regularization methods apply rigid, scalar Euclidean penalties that entirely ignore the underlying Riemannian geometry of the parameter space. To overcome this gap, we propose TMLN (Trajectory-Modulatory Landscape Navigation), a normative navigation policy that formalizes continual learning as an optimal control problem over a curved loss landscape. TMLN utilizes a memory-efficient diagonal empirical Fisher Information Matrix (FIM) to define a localized Riemannian manifold. To compensate for the spatial limitations of the diagonal approximation, TMLN dynamically modulates a preconditioner using the normalized historical trajectory of the network's parameter values. By integrating this trajectory-based preconditioning directly into the gradient update, we actively shield historically critical parameter directions without relying on additive penalties. Empirical evaluations on class- and domain-incremental benchmarks demonstrate that our method significantly reduces the loss barrier between consecutive tasks.


## 精读解读（中文）
### 一、研究动机
连续学习模型在非平稳数据流上顺序训练时会发生灾难性遗忘，而现有权重正则方法多采用固定的标量欧氏惩罚，忽略了参数空间真实的黎曼几何结构；预条件梯度方法虽有潜力，但当前方案往往短视或依赖内存密集型回放。因此，论文希望把连续学习从离散约束梯度问题重构为弯曲损失景观上的规范导航与最优控制问题，以同时缓解遗忘和僵化。

### 二、技术方案（Method）
TMLN 将连续学习建模为部分可观测损失景观上的最优控制问题：在任务边界用小容量回放缓冲估计对角线经验 Fisher 信息矩阵 F，作为局部黎曼度量；训练每个 mini-batch 时混合当前任务样本与回放样本，计算损失和梯度 g，并用 F+λ1+γS_bar 对梯度做逐元素预条件更新 θ←θ-η g/(F+λ1+γS_bar)，其中 S_bar 是由历史参数轨迹调制得到的敏感性累积量。训练过程中同时累加路径积分 ω←ω-(g⊙Δθ)，任务结束时对 ω 做 ReLU 截断并按 1/2 F(Δθ)^2 归一化，得到参数敏感性分数后按每任务最大值归一化累加到 S_bar；随后更新回放缓冲、重算 Fisher、保存参数锚点并清零 ω。推理阶段沿用单头网络，评估时不需要任务标识。

### 三、结果（Result）
论文在 class-incremental 与 domain-incremental 基准上评估，包括 Split CIFAR-100 和 CORe50 的单头无任务标识设置，报告 TMLN 显著缩小连续任务之间的损失障碍，并在稳定性-塑性权衡上优于现有方法。方法保持内存 O(N+B)、每步计算 O(N)，避免显式二阶方法的 O(N^2) 内存与 O(N^3) 求逆开销。由于提供的全文预览截断，具体数值表格和逐基准提升幅度未在可见内容中给出。

### 四、结论（Conclusion）
论文主张将连续学习重铸为黎曼流形上的轨迹优化，通过轨迹调制的预条件梯度而非加性惩罚来主动屏蔽历史关键参数方向，从而在保护旧知识的同时保留新任务塑性。该框架桥接了自然梯度的几何严谨性与局部启发式方法的可扩展性，为高维连续学习提供了一种有原则的新范式。实际部署仍依赖回放缓冲和对角近似，且需要进一步验证完整实验细节与理论保证。

### 五、方法论与关键技术细节
关键实现包括：仅用回放缓冲 M 在任务边界估计对角经验 Fisher 以定义局部曲率；用历史轨迹路径积分累积参数对损失下降的贡献，ReLU 截断负贡献避免奖励振荡或有害更新；敏感性分数分母为 1/2 F(Δθ)^2+ε，并跨任务按最大值归一化累加为 S_bar。主要超参有学习率 η、基础 Tikhonov 阻尼 λ_base、轨迹强度 γ、回放容量 M 和训练轮数 E，算法复杂度与内存为 O(N+B)、每步 O(N)。局限在于对角 Fisher 忽略参数间 off-diagonal 相关性、仍需小型回放缓冲、性能依赖 γ/λ 等超参，且摘要和预览未给出完整数值结果与理论收敛保证。
