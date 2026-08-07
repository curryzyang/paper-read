# Beyond Full-Model Rollback: AuroSFT for Adapter-State Multi-Task Fine-Tuning

- 区域：精读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yue Han, Ziniu Liu
- 机构：China Electronics Corporation, National University of Defense Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05250v1) · [PDF](https://arxiv.org/pdf/2608.05250v1)

## TLDR
AuroSFT improves multi-task supervised fine-tuning by replacing full-model rollback with compact, mergeable adapter states (using weight-transformed nonlinear low-rank adapters) while preserving task-wise peak detection and rollback, achieving higher accuracy across five backbones.

## Abstract
Multi-task supervised fine-tuning (SFT) often casts a heterogeneous data mixture as a single optimization problem, even though different tasks may reach their best generalization at different times. msft exposes this mismatch through task-wise roll-out, exclusion, and rollback, but its original formulation materializes the scheduler state as full-model checkpoints, making stage transitions costly to store, restore, and deploy. This paper introduces AuroSFT, a parameter-efficient framework that recasts the carried state of overfitting-aware multi-task SFT as a compact, mergeable adapter state. AuroSFT freezes the pretrained backbone, trains only injected adapters, rolls back adapter checkpoints at task-wise peaks, and continues on the remaining active mixture. At the layer level, each adapter applies an AuroRA-inspired adaptive nonlinear layer to a low-rank weight factor rather than to the sample representation. The resulting update remains linear in the input, rank-bounded, and exactly mergeable into the frozen projection. Under the retained-backbone comparison protocol, AuroSFT achieves 61.36% average accuracy, compared with 59.85% for the corresponding msft reference row, and obtains higher accuracy on all five backbones. Our code is available at the anonymous repository: https://anonymous.4open.science/r/AuroSFT-80D1.


## 精读解读（中文）
### 一、研究动机
多任务监督微调（SFT）通常将异构数据混合视为单一优化问题，但不同任务达到最优泛化的时间不同，统一预算会导致部分任务过拟合或欠训练。mSFT通过任务级滚动、排除和回滚机制缓解了这一时间错配，但其原始实现将调度器状态物化为全模型检查点，使得阶段切换的存储、恢复和部署代价高昂。

### 二、技术方案（Method）
AuroSFT将过拟合感知多任务SFT的携带状态重构为紧凑、可合并的适配器状态。具体方案是：冻结预训练主干，仅训练注入q/k/v/o/gate/up/down投影的适配器参数{A,B,ANL}；在每一层，对低秩权重因子A施加类AuroRA的适应性非线性层得到\bar A=σ(A^T)^T，再与B构成更新ΔW=(α/r)B\bar A，使层输出保持对输入线性、秩有界且可精确合并到冻结投影。调度流程沿用mSFT的迭代过程：在活动混合上滚动训练，记录各任务验证准确率，找到最早达到峰值的任务，将其排除并回滚到该峰值的适配器检查点，然后在剩余活动混合上继续训练。

### 三、结果（Result）
在保留主干比较协议下，AuroSFT平均准确率达到61.36%，高于对应mSFT参考行的59.85%，并在全部五个轻量骨干（OLMo2-1B、Qwen2.5-0.5B/1.5B/3B/7B）上一致取得更高准确率。在细分类别上，AuroSFT在科学与知识、常识与语言、数学与定量等基准上也普遍优于mSFT。

### 四、结论（Conclusion）
AuroSFT通过将过拟合感知调度器的状态载体从全模型检查点转变为可合并的非线性低秩适配器，不仅显著降低了多阶段微调的存储与部署开销，还提升了异构多任务SFT的平均性能，表明适配器状态是比全模型回滚更优的状态空间设计方案。

### 五、方法论与关键技术细节
关键实现细节包括：ANL层σ(Z)=tanh(tanh(Z)H^T)+S(Z)W_s^T，其中H为可训练自投影，S为B样条基，W_s为样条权重，同时包含tanh路径与可学习样条路径；更新秩被r限制，并经α/r缩放；训练中仅优化{A,B,ANL}，回滚时只恢复适配器检查点，部署时可将ΔW精确合并到W_0。实验覆盖十个基准和五个轻量骨干，消融实验表明移除Weight ANL会显著降低准确率，验证了权重变换的作用；当前工作主要聚焦轻量模型，大规模模型上的扩展性和更复杂任务混合的适用性仍需进一步验证。
