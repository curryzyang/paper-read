# Multi-robot Learning-based Informative Path Planning Using Spatio-Temporal Gaussian Process Kalman Filter

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Muqing Cao, Yunwoo Lee, Junbin Yuan, Lorenzo Schenk, Sebastian Scherer
- 机构：Daegu Gyeongbuk Institute of Science and Technology, Carnegie Mellon University, Singapore University of Technology and Design
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05515v1) · [PDF](https://arxiv.org/pdf/2609.05515v1)

## TLDR
TLDR: This paper presents a decentralized, learning-based multi-robot informative path planning framework that models target presence as a single grid-based spatio-temporal Gaussian process–Kalman field, incorporating realistic camera footprints, range-dependent noise, temporal uncertainty inflation, and conservative belief fusion to achieve about 20% lower target uncertainty in simulation and successful real-world two-UAV persistent monitoring over a 7,000 m² field.

## Abstract
Multi-robot informative path planning (IPP) for persistent target monitoring requires robots to reason about spatial uncertainty, temporal evolution, and practical sensing and communication constraints. Recent learning-based multi-robot IPP methods use Gaussian Processes (GPs) for target uncertainty, but often rely on simplified sensing models and centralized belief updates. We propose a grid-based spatio-temporal GP-Kalman filtering framework for learning-based multi-robot IPP. Instead of maintaining one GP per target, we represent anonymous target presence as a single latent field over a discrete workspace grid. The proposed recursive update considers all visible cells inside a camera footprint and supports arbitrary fields of view and range-dependent noise. A GP-consistent temporal process update accounts for moving targets and stale information by inflating uncertainty over time. For decentralized deployment, each robot maintains its own mapper and exchanges compact belief summaries rather than raw measurements. Received beliefs are fused using diagonal covariance intersection to remain conservative under unknown inter-robot correlations. We integrate the mapper with a reinforcement-learning policy for graph-based neighbor selection. Simulation benchmarks show about 20% lower average target uncertainty and improved target visitation compared with learning-based and classical auction/coverage baselines. Real-world two-UAV experiments demonstrate transfer to outdoor multi-robot search over a large field of more than 7000 square meters.


## 精读解读（中文）
### 一、研究动机
现有基于学习的多机器人信息路径规划（IPP）虽采用高斯过程表达目标不确定性，但多假设固定半径圆形感知、每目标每步最多一次二值观测、目标数量已知且需集中式原始测量同步，难以支持真实相机视场、距离相关噪声、移动目标及带宽受限下的分散部署。为此提出面向持续监测的网格化时空GP-卡尔曼滤波框架，将匿名目标存在性建模为单一潜在场，并兼容实际传感与通信约束。

### 二、技术方案（Method）
先将工作空间离散为G×G网格，对每个网格单元上的目标存在潜在场f维护单一高斯信念（均值向量m与协方差P），空间先验采用积分核GP以避免栅格伪影；当前时刻可见栅格由相机视场与视线决定，将每个可见单元的二值检测松弛为线性高斯观测，并用随距离/视角增大的对角噪声协方差建模传感退化。测量更新依据GP-积分核融合等价为卡尔曼更新，一次吸收视场内全部可见单元，并通过增益将信息传播到整个空间。时间更新采用Reece-Roberts GP-卡尔曼过程模型：用可分离时空核构造同时间协方差K与跨时间协方差C，令转移矩阵G=C K^{-1}、过程噪声Q=K-C K^{-1}C^T，以在目标移动时按时间相关性膨胀不确定性并遗忘过期信息。分散部署中每台机器人运行自身mapper，只交换压缩信念摘要（均值与对角方差）；收到队友信念后用对角协方差交叉融合，避免未知互相关下的过度自信。上层将信念映射与基于注意力/图结构的强化学习策略集成，策略在采样图节点处查询信念并选择下一邻居节点，从而端到端学习多机器人协同规划。

### 三、结果（Result）
仿真基准表明，该方法相较于COMPASS以及经典拍卖/覆盖基线，平均目标不确定性降低约20%，目标访问与覆盖表现更优；两架无人机在超过7000平方米真实户外场地的实验验证了从仿真到真实多机器人搜索的迁移能力。

### 四、结论（Conclusion）
提出并验证了一个可在真实传感与通信约束下工作的分散式多机器人持续监测框架：以网格化时空GP-卡尔曼滤波替代多GP中心化更新，结合紧凑信念交换与强化学习规划，可显著提升不确定性削减和目标访问性能，并成功部署于真实无人机系统。该结果表明将现实测量模型融入学习型IPP是提升实用性的关键。

### 五、方法论与关键技术细节
关键细节包括：1) 采用积分核GP计算单元面积上核积分，使栅格GP先验一致并减少离散化伪影；2) 对二值检测作Bernoulli到高斯松弛，Bernoulli方差不超过0.25，噪声模型在近完全确定时过估噪声，从而趋于保守而非过度自信；3) 测量更新只需对可见栅格数大小的创新协方差求逆，计算开销低；4) 时间过程模型假设空间与时间核可分离且时间平稳，用核值比联系跨时间协方差，动态膨胀陈旧信息；5) 为支持带宽受限通信，交换的是对角近似信念摘要而非原始测量或全协方差，融合采用对角协方差交叉，对未知互相关保持保守；6) 局限包括网格分辨率影响精度与复杂度、匿名场不保留目标身份、对角近似损失部分相关性、真实实验仅两架无人机等。
