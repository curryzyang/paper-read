# Generalizable Robustness Testing of DNN-Based Robotic Navigation Systems via XAI-Guided Search

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Khizra Sohail, Miren Illarramendi, Aitor Arrieta
- 机构：Mondragon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06862v1) · [PDF](https://arxiv.org/pdf/2610.06862v1)

## TLDR
This paper proposes an explainability-guided multi-objective evolutionary search that generates generalizable robustness tests across clustered representative images for DNN-based robotic navigation, achieving a 70% median success rate and demonstrating that simulation can prioritize transferable failures to a physical robot while still requiring real-world validation.

## Abstract
**Context:** Deep Neural Networks (DNNs) increasingly control Cyber-Physical Systems (CPSs), yet small input perturbations can cause unsafe system-level behavior. Existing approaches often optimize perturbations for individual images and evaluate them only in simulation, limiting their generalizability and practical validity.
  **Objectives:** This work aims to generate robustness tests that remain effective across operational observations and to evaluate whether the resulting failures transfer from simulation to a physical robot.
  **Methods:** We propose an explainability-guided multi-objective evolutionary approach that generates sparse perturbations over representative images selected through visual and behavioral clustering. Aggregated Integrated Gradients guide mutations toward influential image regions. We evaluate the approach on a DNN-controlled LeoRover in Gazebo, conduct an ablation study, and validate a stratified subset of perturbations on the physical robot.
  **Results:** The approach achieved a median success rate of 70.0%, compared with 53.85% for unguided search, and increased median hypervolume from 0.65 to 0.73. Multi-image optimization improved the success rate from 50.0% to 57.5%, while XAI guidance further increased it to 70.0%. In the sim-to-real evaluation, simulation achieved 0.95 precision and 0.67 recall, and simulated and physical failure times showed a significant positive correlation of 0.617.
  **Conclusion:** Combining multi-image optimization with explainability-guided search improves robustness testing for DNN-controlled robotic systems. Simulation effectively identifies and prioritizes transferable failures, but physical validation remains necessary because some real-world failures are not reproduced in simulation.


## 精读解读（中文）
### 一、研究动机
现有DNN鲁棒性测试多针对单张图像优化扰动，容易过拟合特定场景而难以泛化到其他操作观测；同时多数研究仅在仿真中评估，未验证失败是否迁移到物理机器人。DNN控制的CPS中微小输入扰动可能传播为系统级不安全行为，因此需要生成跨操作观测仍有效的鲁棒性测试，并检验仿真到现实的迁移性。

### 二、技术方案（Method）
方法分为三阶段：首先用DINOv2(ViT-B/14)提取视觉嵌入并与机器人线速度、角速度等行为特征结合，降维后用HDBSCAN聚类，并从每个簇采样一张代表图像构成代表性场景集；其次对代表图像计算以零图为基线的Integrated Gradients，聚合绝对归因得到全局归因图并归一化为概率分布W；最后采用基于存档的多目标进化搜索，候选解编码稀疏圆形扰动区域，同一扰动在代表图像集上评估，以最大化转向输出偏差并最小化扰动像素数为目标，变异含Add、Remove、Move、Scale并按W偏向高归因区域，注入高斯噪声N(0,sigma^2)后更新Pareto存档，最终输出非支配扰动集合。

### 三、结果（Result）
该方法在Gazebo中的DNN控制LeoRover上取得中位成功率70.0%，高于无引导搜索的53.85%；中位超体积由0.65提升至0.73。消融显示，多图像优化将成功率从50.0%提高到57.5%，再加入XAI引导提高到70.0%。仿真到真实迁移中，仿真精度0.95、召回0.67，仿真与物理失败时间显著正相关，相关系数为0.617。

### 四、结论（Conclusion）
结果表明，将多图像优化与可解释性引导搜索结合，可提升DNN控制机器人导航系统鲁棒性测试的有效性与可迁移性。仿真能有效识别和优先排序可迁移失败，但其召回率有限，说明安全关键评估仍需物理验证。

### 五、方法论与关键技术细节
关键实现点包括：以视觉与行为联合特征聚类选择代表图像，HDBSCAN无需预设簇数并可标记噪声；用零基线Integrated Gradients的绝对归因聚合为全局先验W；候选扰动为稀疏圆形区域，通过Add、Remove、Move、Scale随机变异并注入高斯噪声；优化目标为转向偏差最大化与扰动像素数最小化的冲突目标，采用轻量存档式多目标搜索而非完整NSGA-II，以应对多图像评估开销和变长解结构；父代从Pareto存档均匀采样以避免过早偏向某一目标。评估在LeoRover的Gazebo仿真与分层物理子集上完成，主要局限是仿真精度0.95但召回0.67，部分真实失败无法在仿真中复现，因此物理验证仍必要。
