# SJEPA: Learning Elegant Latent Dynamics with Hybrid Symbolic-Neural Predictors

- 区域：精读区
- 排名：2
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Yongchao Huang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04060v1) · [PDF](https://arxiv.org/pdf/2608.04060v1)

## TLDR
SJEPA is a reconstruction-free JEPA framework that learns predictive latent representations whose dynamics are compressed into compact symbolic laws with a regularized neural correction, favoring the simplest adequate dynamics while preventing representation collapse.

## Abstract
Joint-embedding predictive architectures learn abstract states by predicting target embeddings from context embeddings, but their transition models are typically opaque neural maps. We introduce SJEPA, a reconstruction-free JEPA framework that learns predictive representations whose induced dynamics admit compact symbolic descriptions. Its hybrid transition combines a symbolic law with a regularised neural correction for dynamics outside the selected grammar. The central principle is to learn the simplest adequate dynamics: representation constraints preserve informative, non-collapsed predictive coordinates, while operator compression favours low-complexity symbolic-neural transitions that remain predictively adequate. We formalise this principle through induced-dynamics complexity, analyse predictive-coordinate non-identifiability, and show that unconstrained operator compression creates a direct shortcut to representation collapse. The framework supports both alternating representation-equation learning and symbolic dynamics fitted to fixed representations. In controlled pendulum experiments, joint learning discovers substantially simpler symbolic dynamics with lower long-horizon rollout error and divergence than post-hoc fitting, while an unconstrained one-step diagnostic realises the predicted collapse shortcut. Under grammar misspecification, correction regularisation preserves the representable symbolic mechanism and directs the neural component towards residual dynamics. The results expose a controllable trade-off among predictive fidelity, representation quality, symbolic parsimony, and symbolic-neural allocation.


## 精读解读（中文）
### 一、研究动机
联合嵌入预测架构（JEPA）通过学习从上下文嵌入预测目标嵌入来获得抽象状态，但其转移模型通常是黑盒神经网络，难以揭示变量间的交互、动作如何影响未来以及所学坐标是否支持简洁的动力学描述。本文提出SJEPA，目标不是学习最短方程，而是学习对信息丰富且非坍缩的预测坐标而言最简单且充分的控制律，即同时实现表示压缩与算子压缩，避免为简化动力学而牺牲表示质量。

### 二、技术方案（Method）
SJEPA采用无重建的JEPA框架，将潜在转移分解为符号定律与正则化神经修正：预测目标由Z_T_hat = F_{E,alpha}(Z_C, eps) + c_phi(Z_C, eps)给出，其中F为符合语法树的符号表达式（结构复杂度由节点加权和定义），c_phi为神经修正项，eps为条件信息（如时间偏移或动作）。训练目标为约束算子压缩：最小化符号复杂度Omega(E)与修正正则项lambda_c R_corr(phi)，同时满足预测损失L_pred <= delta_pred且表示约束(theta, theta_bar) in Theta_repr（如VICReg式正则，避免表示坍缩）。支持交替学习表示与符号方程，或对冻结编码器拟合符号动力学；实验中使用稀疏库表示符号支撑，并以可微系数代理优化，最终报告阈值化支撑。

### 三、结果（Result）
在受控摆实验中，联合表示-方程学习比事后拟合发现更简单的符号动力学，并显著降低长时程展开误差和发散程度；无约束的一步诊断实现了理论预测的坍缩捷径（表示固定点坍缩）。在语法误设下，修正正则化保留了可表示的符号机制，并将神经分量引导至残差动力学。实验揭示预测保真度、表示质量、符号简洁性与符号-神经分配之间存在可调节的权衡。

### 四、结论（Conclusion）
SJEPA展示了在JEPA家族中学习优雅潜在动力学的可行方向：通过将潜在转移显式分解为紧凑符号定律与受控神经修正，能够在保持预测充分性的同时获得可解释的动力学描述。该框架支持贝叶斯扩展、行动条件化、敏感性分析与规划，适用于需要紧凑潜在动力学、显式结构约束或受控残差建模的场景。

### 五、方法论与关键技术细节
关键细节包括：使用EMA目标编码器提供缓慢移动的预测目标；在连续时间系统中，符号-神经分解可作用于向量场而非直接转移映射，实验采用前向欧拉积分H(z)=z+Delta t[F(z)+c_phi(z)]；表示约束使用VICReg风格正则器避免坍缩；符号复杂度可替换为MDL准则；理论分析表明预测坐标非可辨识，且无约束的算子压缩会直接导致表示坍缩，因此必须联合施加预测约束与表示约束；修正项通过正则系数lambda_c控制，防止神经分量不必要地吸收可表示的动力学。
