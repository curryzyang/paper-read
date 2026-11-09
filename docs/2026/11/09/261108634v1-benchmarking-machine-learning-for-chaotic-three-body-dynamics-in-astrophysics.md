# Benchmarking Machine Learning for Chaotic Three-Body Dynamics in Astrophysics

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Sheng Wan, Pavan Vynatheya, Duo Xu, Li Kevin Wenliang, Ye Zhu
- 机构：Google DeepMind, IP Paris, University of Toronto
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08634v1) · [PDF](https://arxiv.org/pdf/2611.08634v1)

## TLDR
This paper benchmarks general-purpose and physics-foundation ML models against astrophysical criteria on chaotic three-body systems near the stability boundary, finding that early dynamics enable strong stability prediction while precise long-horizon trajectory forecasting remains difficult.

## Abstract
Machine learning (ML) and generative AI have recently made impressive progress in understanding physics. We explore a hierarchy of prediction problems stemming from chaotic three-body systems and benchmark existing ML approaches, including general-purpose prediction algorithms and those that build on top of foundational physics models. We first simulate the trajectories of triple systems near the critical boundary of stable/unstable initial conditions. We then design a hierarchy of learning tasks, focusing mainly on two broad problems: stability prediction and trajectory prediction. The former classifies whether a given triple system has diverged or not up to a specific horizon, while the latter predicts the exact trajectory, both given suitable input features. We benchmark a range of ML approaches, from simple regression methods to state-of-the-art foundational physics models, across these tasks, and compare them against astrophysical methods such as the Mardling-Aarseth stability criterion. Our experiments reveal a clear order of task difficulties in chaotic three-body dynamics: early dynamics enable strong stability prediction, while precise long-horizon trajectory forecasting remains difficult. Code and dataset are publicly available at https://github.com/Simonwan03/ThreeBodyMLBench.


## 精读解读（中文）
### 一、研究动机
机器学习在物理建模和世界模型方向进展迅速，但混沌三体动力学这一经典且可控的强混沌问题仍缺乏系统评测。论文希望在稳定与不稳定临界区域附近构建基准，比较通用预测模型、物理基础模型与天体物理经验判据，明确现有方法在稳定性预测和精确轨迹预测上的能力边界。

### 二、技术方案（Method）
作者在稳定/不稳定临界边界附近模拟5000个基础层级三体系统，每个基础系统生成32个仅改变轨道相位或轻微半长轴的受控扰动变体，并用无量纲orbital15轨道特征表示状态。任务包括：A基于初始条件预测未来视界内稳定比例或二分类稳定性；B基于短轨迹前缀预测个体稳定性；C基于集合内短前缀通过离散条件风险模型输出多视界生存曲线；以及基于512步上下文预测后续128步单次轨迹和递归四块共512步开环轨迹。基线覆盖XGBoost、MLP、CNN、TCN、注意力模型、预训练时间序列基础模型及其微调版本，并与Mardling–Aarseth和Vynatheya等天体物理判据比较。

### 三、结果（Result）
初始条件稳定性任务中，XGBoost二分类准确率0.805、F1 0.535，高于Mardling–Aarseth的0.619和0.441，Vynatheya的MLP达到AUROC 0.909、AUPRC 0.718；XGBoost稳定比例回归MSE 0.088、R² 0.444。基于短轨迹前缀的动态摘要加XGBoost显著提升，二分类AUROC 0.9851、稳定比例MAE 0.0398；多视界生存预测中Chronos-2加直接池化取得MAE 0.0376、IBS 0.0416；轨迹预测中Chronos-2零样本MAE 0.228，短程有竞争力但长程精确预测仍困难。

### 四、结论（Conclusion）
实验揭示混沌三体动力学存在清晰的任务难度层级：早期动力学信息足以支持很强的稳定性判别和生存估计，基于初始条件的稳定性预测虽优于传统判据但仍有限，而精确的长视界轨迹预测仍是主要瓶颈。该基准说明现有ML方法可用于快速稳定性筛查和短期预测，但不能替代数值积分用于长期混沌轨道演化。

### 五、方法论与关键技术细节
关键实现包括以32变体扰动集合作为数据划分和评估的基本单元，避免近重复样本泄漏；稳定性标签由集合内保持束缚的变体比例或个体是否在视界前发散定义；生存任务用条件风险连乘保证生存曲线单调；评估覆盖分类AUROC/AUPRC/F1、回归MAE/MSE/R²、生存MAE/IBS及轨迹标准化误差、相关性和开环误差累积。局限在于真值来自有限视界的牛顿模拟，数据集中于层级三体临界边界，混沌敏感性和递归开环预测会放大误差，结论外推到其他质量比、初始条件区域或更长时标需谨慎。
