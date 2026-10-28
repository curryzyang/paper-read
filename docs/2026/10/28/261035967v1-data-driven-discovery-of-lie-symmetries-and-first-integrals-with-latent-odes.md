# Data-driven Discovery of Lie Symmetries and First Integrals with Latent ODEs

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Matt L. Wiemman, Peter Melchior
- 机构：Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35967v1) · [PDF](https://arxiv.org/pdf/2610.35967v1)

## TLDR
LatentLieODE is a neural ODE framework that learns a decorrelated latent representation from time-series or video observations and jointly discovers linear Lie symmetry generators via a differentiable Lie-bracket residual and first integrals via a learned conservation network, accurately recovering known symmetries and conserved quantities across six benchmark systems.

## Abstract
We present LatentLieODE, a novel neural ODE method to discover linear Lie symmetries and first integrals of the learned dynamics from timeseries observations such as video inputs. It starts with an autoencoder, which learns a low dimensional representation of the observed system and then maps trajectories to decorrelated latent coordinates $z \in \mathbb{R}^d$. A bank of linear infinitesimal generators $\mathbf{A}_k \in \mathbb{R}^{d \times d}$ is fitted jointly against a differentiable Lie-bracket residual $\mathbf{J}_f(z)\mathbf{A}z - \mathbf{A} f(z)$, while an MLP optimises the latent ODE $f(z) = \mathrm{d}z/\mathrm{d}t$ to reconstruct the observation-space timeseries. After suitable generators and $f$ are found, we fit a third network $H_φ$ to generate the first integral of the system. Across six benchmark systems (harmonic oscillator, simple and twin pendulums, Lotka-Volterra, pixel pendulum, sphere geodesics) we find each system's relevant symmetries, and the discovered invariants match ground-truth conserved quantities at $|ρ| \geq 0.978$. On the sphere, the pipeline recovers a non-abelian $\mathfrak{so}(3)$, certified by the negative-definite Killing form of its recovered structure constants. This work presents significant advances in data-driven discovery of symmetries and provides a new pathway for neural surrogates of dynamical systems.


## 精读解读（中文）
### 一、研究动机
从含噪时间序列或视频观测中反推动力系统的连续对称性与守恒量，是物理与数据驱动建模的重要逆问题。现有方法多在观测空间搜索对称性，或以对抗方式学习群作用且预先固定群维数；而许多在观测空间中非线性的对称性，在合适坐标下会变为线性作用，因此需要一种能同时学习潜在坐标、线性Lie生成元与首次积分的端到端方法。

### 二、技术方案（Method）
LatentLieODE先用自编码器把状态或视频轨迹编码到低维潜空间，并通过基于批统计的中心化与保方差去相关构造潜坐标；再用MLP学习潜ODE f(z)=dz/dt，以重构观测时间序列并加入圆轨道与匀速惩罚促使周期运动呈作用量-角变量结构。随后联合训练一组过完备线性生成元A_k，最小化归一化Lie括号残差E[||J_f(z)A_k z-A_k f(z)||^2/(||f(z)||^2+ε)]，用前向模式Jacobian-向量积计算，并配合stop-gradient正交化、范数预算与谱间隙检测确定代数维数；最后用多个H_φ网络以cos^2(∇H,f)和Noether兼容项cos^2(sg[∇H],Az)学习首次积分。

### 三、结果（Result）
在谐振子、单摆与双摆、Lotka-Volterra、像素单摆和球面测地线六个基准系统上，方法均恢复出相关对称性，发现的守恒量与真值匹配达到|ρ|≥0.978；在球面上还恢复了非阿贝尔so(3)，并由其结构常数的负定Killing形式加以验证。生成元范数谱的乘性间隙使代数维数成为输出而非预设超参数，成对括号投影还用于检验闭合性。

### 四、结论（Conclusion）
该工作表明，仅凭时间序列或视频观测即可数据驱动地发现线性Lie对称性、代数结构及对应首次积分，为神经动力系统代理模型提供了新路径。其核心贡献在于可微Lie括号目标、谱间隙维数检测、尺度不变的首次积分学习及物理单位校准；但搜索空间限于学习潜坐标中可线性表示的对称性，且不假设Hamilton/Lagrangian结构，H_φ是首次积分而非生成动力学的Hamilton量。

### 五、方法论与关键技术细节
实现上，潜坐标去相关使用批方差与相关矩阵逆平方根，Newton-Schulz迭代并加ε=1e-8；生成元以过完备bank训练，stop-gradient正交化避免坍缩，范数预算含总范数约束与γ=0.05的逐生成元单位范数吸引；Lie括号残差在编码真实轨迹加小扰动的样本上以jax.jvp计算。训练时对称性项权重低于重构项并逐步升权，多首次积分用多头网络加梯度去相关；关键局限是仅搜索线性生成元、受潜空间宽度约束、对动作无表达性保证，且视频输入需以像素时间方差加权重构以抑制静态背景平凡解。
