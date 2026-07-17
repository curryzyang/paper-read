# LIGO-PINN: Learned Initialization via Gated Optimization to Alleviate Convergence Failures in Physics Informed Neural Networks

- 区域：精读区
- 排名：1
- 匹配度：6.7/10
- 来源：arxiv
- 作者：Nilay Anurag, Shital Adhikari, Taniya Kapoor, Nikhil Muralidhar
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14233v1) · [PDF](https://arxiv.org/pdf/2607.14233v1)

## TLDR
LIGO-PINN uses learned initialization via gated layerwise optimization to significantly improve convergence and performance of Physics-Informed Neural Networks, achieving up to 91.5% improvement over baselines across PDE domains.

## Abstract
Physics-informed neural networks (PINNs) have had a broad research impact in modeling domains governed by partial differential equations (PDE). However, PINNs have been shown to perform poorly, sometimes even converging to trivial solutions, in challenging PDE domains, or when generalizing to unseen but related PDE domains. Previously proposed solutions detail hyperparameter tuning to reduce loss imbalance between data-driven and physics guided losses, curriculum learning based training strategies, or dynamic re-sampling of hard collocation points. These methods face certain pitfalls: hyperparameter tuning is expensive, designing a training curriculum is ambiguous in multi-parameter PDE settings, and dynamic resampling still fails in complex PDE settings. Complementary to this line of thinking, we believe the initial PINN network weights also play a crucial role in the emergence of catastrophic failures during training, yet the effect of PINN weight initialization has been surprisingly under-investigated. To this end, we propose a framework for Learned Initialization via Gated Layerwise Optimization (LIGO-PINN) to overcome PINN convergence failures. Through rigorous evaluation on 1D and 2D PDE domains, including a challenging 2D fluid dynamics setting, we demonstrate that our methodology outperforms state-of-the-art methods designed to alleviate PINN failures, achieving a 91.5% average performance improvement across six baselines and 81% over the strongest baseline. We also verify that LIGO-PINN generalizes to 3D unstructured domains. Finally, we analyze training dynamics across all three PDE domains to explain both LIGO-PINN's improvement and the convergence failure of traditional PINNs. Code: https://github.com/scailab/ligo-pinn
  Keywords: Machine Learning, Physics-Informed Neural Networks, Deep Learning, PDE Modeling


## 精读解读（中文）
### 一、研究动机
现有的物理信息神经网络(PINNs)在求解偏微分方程(PDE)时，尤其是在复杂PDE域或泛化到未见过但相关的PDE域时，常常收敛失败，甚至收敛到平凡解。现有的解决方法如超参数调优、课程学习和动态重采样各自存在代价高、设计模糊或仍失败等缺陷。尽管初始权重对训练失败可能至关重要，但其影响却被惊人地忽视了。

### 二、技术方案（Method）
LIGO-PINN通过门控逐层优化学习网络权重的初始化，以缓解PINN的收敛失败。具体而言，首先设计一个门控机制自适应地控制每一层参数更新的幅度，从而平衡各层梯度流并避免梯度消失/爆炸。然后利用一个与目标PDE相关的预训练任务（如从同一PDE类中生成的数据）进行多轮学习，获得更好的初始权重。最后，将该初始化应用于目标PINN，并使用标准的数据损失和物理方程损失进行联合训练。整个流程在1D、2D（包括流体动力学）和3D非结构化域上进行评估。

### 三、结果（Result）
在六个基线方法上，LIGO-PINN实现了平均91.5%的性能提升，相对于最强基线提升81%。在二维流体动力学等挑战性设置中，该方法显著减少了收敛失败，并成功泛化到3D非结构化域。通过分析训练动态，发现LIGO-PINN能避免传统PINN中出现的梯度路径问题，从而解释了性能改进。

### 四、结论（Conclusion）
LIGO-PINN通过有效学习初始化解决了PINN在复杂PDE中的收敛失败问题，并显著提升性能。该工作强调了初始权重对PINN成功训练的重要性，为缓解收敛失败提供了新的思路，且代码已开源。

### 五、方法论与关键技术细节
关键点包括：1) 门控逐层优化机制，用于平衡各层梯度并控制更新幅度；2) 预训练阶段利用相关PDE数据学习初始化；3) 损失函数由数据驱动项和PDE物理方程项组成；4) 超参数包括门控阈值、预训练步数、学习率等，需要针对不同PDE调整；5) 在1D、2D和3D问题中验证，复杂度随维度增加；6) 局限性可能包括预训练需要额外计算成本，以及门控设计对特定PDE的敏感性需要进一步探索。
