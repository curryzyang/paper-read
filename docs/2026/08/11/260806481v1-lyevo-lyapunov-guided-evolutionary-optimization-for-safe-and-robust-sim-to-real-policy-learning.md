# LyEvO: Lyapunov-Guided Evolutionary Optimization for Safe and Robust Sim-to-Real Policy Learning

- 区域：精读区
- 排名：3
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Riccardo Curcio, Hongpeng Cao, Marco Caccamo
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06481v1) · [PDF](https://arxiv.org/pdf/2608.06481v1)

## TLDR
LyEvO combines Lyapunov-based stability analysis with constrained evolutionary optimization and statistical model checking to jointly optimize, verify, and expand safety regions for policies, enabling safe and robust sim-to-real transfer as demonstrated on Cartpole and Quadrotor benchmarks.

## Abstract
Training controllers that are safe and robust in simulation, and systematically assessing their readiness for real-world deployment, remain key challenges in sim-to-real transfer. To address this, we propose LyEvO, a physics-grounded framework that combines constrained Evolutionary Optimization and Statistical Model Checking (SMC)-based verification with Lyapunov-based stability analysis. Leveraging prior knowledge of the system dynamics, LyEvO uses Lyapunov analysis to compute an initial candidate stability region. An iterative loop then uses operational scenarios drawn from this region to jointly optimize and statistically verify a policy, and subsequently expands the region's boundaries based on the verification outcome. This integrated procedure provides a practical criterion for assessing deployment readiness. We evaluate LyEvO on Cartpole and 3D Quadrotor benchmarks through extensive simulations and targeted real-world experiments, demonstrating safe and robust sim-to-real transfer.


## 精读解读（中文）
### 一、研究动机
训练在仿真中安全且鲁棒的控制器，并系统评估其真实世界部署就绪度，仍是sim-to-real迁移的关键挑战。

### 二、技术方案（Method）
提出LyEvO框架，结合约束进化优化与基于统计模型检验（SMC）的验证，并融入Lyapunov稳定性分析。利用系统动力学先验知识，通过Lyapunov分析计算初始候选稳定区域；随后在迭代循环中，从该区域抽取运行场景，联合优化并统计验证策略，再根据验证结果扩展区域边界。

### 三、结果（Result）
在Cartpole和3D Quadrotor基准上通过大量仿真和针对性真实实验进行评估，展示了安全且鲁棒的sim-to-real迁移。

### 四、结论（Conclusion）
LyEvO的集成流程为评估部署就绪度提供了实用准则，能够实现安全鲁棒的sim-to-real策略学习。

### 五、方法论与关键技术细节
方法依赖系统动力学先验知识；稳定区域通过Lyapunov分析初始化并在迭代中扩展；使用统计模型检验（SMC）进行验证；评估涵盖仿真与真实实验；框架强调安全性和鲁棒性，但摘要未给出具体指标、超参或复杂度细节。
