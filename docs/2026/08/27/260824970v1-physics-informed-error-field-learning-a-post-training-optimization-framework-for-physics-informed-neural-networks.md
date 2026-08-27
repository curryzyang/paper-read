# Physics-Informed Error Field Learning: A Post-Training Optimization Framework for Physics-Informed Neural Networks

- 区域：精读区
- 排名：1
- 匹配度：6.9/10
- 来源：arxiv
- 作者：Jiuyun Sun, Yong Zhang
- 机构：Shandong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24970v1) · [PDF](https://arxiv.org/pdf/2608.24970v1)

## TLDR
PIEFL is a post-training optimization framework for PINNs that shifts the learning objective from the solution field to a physics-constrained error field learned by an auxiliary network, combining its correction with the primary prediction to achieve higher accuracy under the same computational budget without modifying the original network architecture.

## Abstract
Physics-Informed Neural Networks (PINNs) have emerged as an important class of numerical methods for solving partial differential equations (PDEs). However, during the late-stage optimization process, further parameter updates often yield diminishing accuracy improvements while increasing computational costs. To address this issue, this paper proposes a Physics-Informed Error Field Learning (PIEFL) framework for PINNs. Unlike conventional approaches that continuously approximate the solution field using a single network, PIEFL introduces an auxiliary error network after the primary network achieves satisfactory accuracy and shifts the learning objective from the solution field to the error field. By deriving error control equations under physical constraints, the error network learns the discrepancy between the current approximation and the exact solution, and the learned error correction is combined with the primary prediction to improve solution accuracy. The proposed framework avoids continuous optimization of the entire solution space and focuses computational resources on correcting existing prediction errors. Moreover, PIEFL requires no modification to the primary network architecture, making it compatible with existing PINN models and applicable as a general post-training optimization strategy. Numerical experiments on representative PDEs demonstrate that PIEFL achieves higher solution accuracy under the same computational budget, validating its effectiveness in improving the performance of PINNs.


## 精读解读（中文）
### 一、研究动机
物理信息神经网络（PINN）在训练后期存在明显的收益递减现象：继续更新网络参数只能带来微小的精度提升，却显著增加计算成本。为此，本文提出一种后训练优化框架，将学习目标从解场转向误差场，以更高效地利用计算资源提升解精度。

### 二、技术方案（Method）
PIEFL采用级联两阶段架构。第一阶段训练标准PINN作为主网络，得到近似解u_p和物理残差f_p；第二阶段固定主网络参数，引入辅助误差网络学习误差场u_e，其物理控制方程通过将u=u_p+u_e代入原PDE推导为∂u_e/∂t+N_e[u_e]+f_p=0，其中N_e[u_e]=N[u_p+u_e]-N[u_p]。误差网络的损失由误差场初边值数据损失MSE_ue和物理残差损失MSE_fe组成，误差初边值由原始IC/BC减去主网络预测得到。训练完成后最终解为u_final=u_p+α·hat_u_e，其中α为输出缩放系数。该方法无需修改主网络架构，可作为通用后训练优化策略。

### 三、结果（Result）
在KdV方程实验中，主网络预测相对误差为3.846063e-3，误差网络单独预测误差为1.659345e-2，PIEFL最终预测误差降至1.469116e-4；而训练15000步的标准PINN相对误差为9.480554e-4。误差演化曲线表明，PIEFL在约7000步时就已达到标准PINN训练15000步的精度，且后期误差下降更快、波动更小。

### 四、结论（Conclusion）
PIEFL通过将学习目标从解场切换为误差场，避免了持续优化整个解空间，能够将计算资源集中用于修正已有预测误差。在相同计算预算下，PIEFL可获得比标准PINN更高的解精度，且与现有网络结构改进、自适应采样、损失加权等增强技术兼容，是一种高效通用的PINN后训练优化策略。

### 五、方法论与关键技术细节
数值实验中网络结构为[2,20,20,20,20,1]；KdV方程求解域为[-10,10]×[-1,1]，训练点200个，配点8000个；主网络和误差网络的Adam迭代次数分别设为5000和10000；误差网络输出缩放系数α设为0.001。误差场幅值通常较小，引入α可降低学习难度。实际使用中需要主网络先达到满意精度，误差网络才能有效学习残差；对于强非线性或高维问题，误差场的物理残差计算复杂度可能较高。
