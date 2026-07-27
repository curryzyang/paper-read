# GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation

- 区域：精读区
- 排名：3
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Leesai Park, Jiho HOng, Sanghyun Kim
- 机构：Advanced Institute of Convergence Technology, Kyung Hee University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21661v1) · [PDF](https://arxiv.org/pdf/2607.21661v1)

## TLDR
GRACE introduces a gradient-free framework that guides pretrained diffusion policies for robot action generation by estimating the cost-conditioned posterior mean at each denoising step via a single MPPI update, enabling effective handling of nondifferentiable deployment-time constraints like collision checks and achieving superior success rates in simulation and real-world obstacle avoidance.

## Abstract
Diffusion policies generate multimodal robot action sequences from demonstrations, but steering them toward deployment-time constraints typically relies on differentiable guidance costs. This excludes many practical safety constraints, such as binary collision checks, joint limits, and black-box rollout costs that are nondifferentiable. We propose Gradient-free Robot Action generation via Combined diffusion-MPPI posterior mean Estimation (GRACE), which guides a pretrained diffusion policy with Model Predictive Path Integral (MPPI) control using only forward cost evaluations. Building on the common score-ascent structure of diffusion and MPPI, GRACE constructs a cost-conditioned guidance posterior at each reverse step and estimates its mean with a single MPPI update centered at the diffusion reverse mean. For differentiable costs, GRACE recovers conventional gradient guidance under a first-order, matched-covariance approximation. GRACE attains higher success rates than diffusion-based and sampling-based baselines in simulation. On a real 7-DoF manipulator, GRACE avoids a deployment-time obstacle that the unguided prior collides with in every trial. Code and experiment videos are available at https://anonymous.4open.science/w/grace-70BB/.


## 精读解读（中文）
### 一、研究动机
现有的扩散策略推理时引导方法依赖于可微分的引导成本，这使得它们无法处理许多实际部署中的安全约束，如二元碰撞检测、关节限位和黑盒 rollout 成本。因此，需要一种无需梯度、仅需前向成本评估的引导方法，以适应未知部署时的约束。

### 二、技术方案（Method）
GRACE 基于扩散反向步骤和 MPPI 更新均具有得分上升结构这一观察，在每个反向步骤中，以扩散预测的反向均值为中心，通过 MPPI 在协方差固定的高斯分布中采样 K 个候选动作序列，使用部署时的成本函数（可不可微）评估每个序列的代价，并通过重要性采样权重计算加权均值，从而估计成本条件化后验分布的均值。该后验均值用于参数化投影反向核的均值，并保留扩散过程的协方差，从中采样得到下一步去噪样本。整个过程无需重新训练扩散模型，仅需预训练的噪音预测器和前向成本评估。

### 三、结果（Result）
在仿真任务中，GRACE 相较于基于扩散梯度引导的基线和基于采样的基线取得了更高的成功率；在真实 7-DoF 机械臂上，GRACE 成功避开了一个部署时障碍，而未经引导的扩散策略在每次试验中均与障碍物发生碰撞。这表明 GRACE 能够有效适应未见过的、不可微的部署约束。

### 四、结论（Conclusion）
GRACE 通过将 MPPI 采样直接集成到扩散反向过程的每一步，实现了无需梯度的部署时引导，能够适应不可微、黑盒的成本函数，同时保持了扩散生成的多模态性，且无需对预训练模型进行重训练。该方法在仿真和真实硬件上均验证了其有效性和实用性。

### 五、方法论与关键技术细节
GRACE 使用预训练的 DDPM 扩散模型作为先验，其训练采用标准的去噪均方误差损失。推理时每个去噪步骤需执行 K 次 MPPI rollout（K 为采样数，通常数十到上百），成本函数可任意定义。MPPI 的温度参数 λ 控制分布锐度，协方差 Σ 与扩散过程的噪声协方差匹配时，可恢复一阶梯度引导近似。主要计算开销来自每次迭代的 K 次动力学 rollout，但无需动力学模型可微。局限性包括：依赖 MPPI 的采样效率，在极高维动作空间或极短计算时限内可能受限；且仅估计后验均值而非完整分布，可能损失部分随机性。
