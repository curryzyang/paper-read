# Terrain-Aware Thompson Sampling for Multi-Drone Search and Rescue

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Riana Gagnon Souleiman, Giovanni Beltrame
- 机构：Polytechnique Montreal
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14685v1) · [PDF](https://arxiv.org/pdf/2611.14685v1)

## TLDR
The paper proposes a decentralized terrain-aware Thompson Sampling algorithm for multi-drone search and rescue that combines terrain-informed lost-person priors with forest-occlusion uncertainty to balance exploration and exploitation, and demonstrates high success rates in YOSAR-based simulations across different search-area and drone-team configurations.

## Abstract
In this work, we propose a decentralized terrain-aware multi-drone Thompson Sampling algorithm tailored for search and rescue (SAR) applications. A probability distribution of locating a lost person is informed by terrain data, using established SAR models (displacement ring, elevation, watershed, dispersion angle, and track offset) derived from historical SAR case data on lost person behavior. Exploration is conducted by a team of drones using Thompson Sampling, where candidate actions are selected by drawing samples from this probability distribution, represented by a per-cell Gaussian posterior whose mean and variance are updated through Bayesian inference. This approach balances exploration of uncertain regions with exploitation of high-probability areas to locate a lost person. Observation uncertainty is incorporated through fractional forest coverage, which measures the percentage of an observation occluded by tree coverage and accounts for reduced detection performance in densely vegetated areas. Simulations using real SAR case data (YOSAR) evaluate the proposed method against a coverage planner and a probabilistic active search method in search regions of 1.5 and 3.8 square kilometers, with 5, 10, 15, and 20 agents flying at 50 km/hr. We demonstrate that our method achieves a success rate of approximately 87% within 60 to 247 seconds in the 1.5 square kilometer region, and success rates of approximately 75% to 91% within 161 to 466 seconds in the 3.8 square kilometer region, across different agent configurations.


## 精读解读（中文）
### 一、研究动机
野外搜救中失踪者生存率随时间快速下降，而大范围远程区域搜索耗时且资源密集；多无人机虽可并行搜索，但集中式协调受通信与单点故障限制。因此需要一种去中心化、能利用地形与失踪者行为先验、并兼顾不确定区域探索与高概率区域利用的多无人机主动搜索方法。

### 二、技术方案（Method）
方法将搜索区离散为30 m×30 m网格，用位移环、海拔、流域、散布角和轨迹偏移等SAR模型的历史数据构造每格高斯先验均值，并以5个模型等权α=0.2归一化混合；每架无人机维护局部后验，在10×10局部窗口内通过Thompson Sampling从每格高斯后验采样候选动作，用Dijkstra规划轨迹并加入300 m范围内斥力项减少重复搜索；观测通过贝叶斯推断更新均值与方差，并用分数森林覆盖度构造观测权重W_tt=1−λσ²以反映植被遮挡导致的不确定性，执行后与其他无人机共享观测并重复规划直至发现目标或达到1800 s电池约束。

### 三、结果（Result）
在基于YOSAR真实SAR案例的仿真中，所提方法在1.5 km²区域、5至20架无人机、50 km/h飞行条件下约60至247 s内达到约87%成功率；在3.8 km²区域约161至466 s内达到约75%至91%成功率。实验将该方法与覆盖规划器和概率主动搜索方法在相同搜索区域与不同无人机数量配置下进行比较。

### 四、结论（Conclusion）
结果表明，地形感知的去中心化Thompson Sampling能够利用SAR先验优先搜索高概率区域，同时通过后验采样探索不确定区域，并在多无人机配置下较快定位失踪者。该方法面向大范围远程搜救，具有去中心化、可扩展和减少冗余搜索的潜力。

### 五、方法论与关键技术细节
关键实现包括：使用YOSAR历史案例、NASA SRTM高程、线性特征与流域提取构建先验；每格先验方差初始化为1，后验更新采用期望最大化与对角观测权重，超参a=0.1、α=0.2、斥力η=1000、斥力半径d0=300 m；网格尺寸对应80 m高度、21°视场相机。局限性包括假设无人机间持续全局通信、模型权重为固定默认值而非学习得到、遮挡不确定性以森林覆盖度近似，且验证主要基于仿真环境。
