# Symmetry-quotient Flatness and Generalization

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Taiki Miyagawa
- 机构：NEC Corporation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31634v1) · [PDF](https://arxiv.org/pdf/2609.31634v1)

## TLDR
This paper develops a symmetry-aware theorem-level pipeline showing that, after quotienting out function-preserving parameter symmetries, quotient linear stability of SGD implies quotient flatness, which controls input smoothness and thereby yields population generalization bounds.

## Abstract
This paper develops a theorem-level pipeline in symmetry-quotient settings: quotient linear stability implies quotient flatness, quotient flatness implies input smoothness, and input smoothness yields generalization under local covering assumptions. Flatness is often associated with generalization, and Stochastic Gradient Descent (SGD) is frequently viewed as implicitly biased toward flat solutions. However, standard flatness measures are typically defined in the raw parameter space and are therefore not invariant under function-preserving symmetries such as positive rescaling. We develop a symmetry-aware theory of quotient flatness, quotient linear stability, input smoothness, and generalization on quotient spaces of neural-network parameters. For square loss and models equipped with function-preserving group actions, we define quotient flatness as the trace of the Hessian of the empirical loss on the regular quotient manifold. We show that quotient flatness controls input smoothness through a quotient-space analogue of the flatness-to-smoothness argument. We also prove that one-step mean-square quotient linear stability of the linearized SGD dynamics implies an explicit quotient-flatness bound in terms of the batch size and learning rate, and extend this analysis to higher-order tensor moments. Finally, under local covering and boundedness assumptions, we derive population generalization bounds in terms of quotient flatness and, consequently, in terms of quotient linear stability.


## 精读解读（中文）
### 一、研究动机
平坦性常被认为与泛化相关，且SGD被视作偏向平坦解；但标准平坦性定义在原始参数空间，对正缩放、隐藏单元置换等函数保持对称不具备不变性，导致度量可能失真。已有工作给出平坦性到输入光滑再到泛化的显式管道，但尚未在对称商几何中表述。本文因此追问：能否在商掉函数保持对称后，建立数学显式的平坦性到泛化理论。

### 二、技术方案（Method）
设参数流形 Θ 上有函数保持李群或有限群作用 G，在正则层取商流形 M=Θ_reg/G，模型下降为 f_bar，并在平方损失下定义商经验损失 L_bar；商平坦定义为商流形上 L_bar 的 Hessian 迹。作者证明在插值解 [θ_star] 处商平坦等于样本输出商梯度范数平方的平均，并引入局部规范固定截面 s([θ])=(W1,ϑ) 和首层乘法分解 f=tilde f(W1x,ϑ)，用商梯度控制首层 W1 梯度，从而推出输入 Sobolev 型光滑界。随后在 M 的切空间上线性化 SGD：对 mini-batch I 大小 B 和学习率 η，Jacobian 为 M_I=Id-(η/B)Σ_b H_i_b^Q，其中 H_i^Q=a_i^Q⊗a_i^Q，并定义一步均方商线性稳定 E||M_I ξ||^2≤||ξ||^2；同时给出高阶张量矩递归。最后在局部覆盖与有界性假设下，由商平坦及商线性稳定推出种群泛化界。

### 三、结果（Result）
论文建立并证明定理级管道：商线性稳定 ⇒ 商平坦 ⇒ 输入光滑 ⇒ 泛化。关键恒等式为 Flat^Q([θ_star])=1/n Σ_i ||a_i^Q||^2，即插值处商平坦等于平均商梯度平方范数。输入光滑定理给出 1/n Σ_i ||∇_x f_bar(x_i)||_2^2 ≤ (Λ_star^2 C_sec^2/ρ^2) Flat^Q，其中 Λ_star=||W1_star||_op 且 ρ=min_i||x_i||_2。稳定性到平坦性定理给出一步均方商线性稳定时 Flat^Q([θ_star])≤2B/η，且高阶矩扩展给出更高阶输入光滑估计，最终在局部覆盖和有界性下得到泛化界。

### 四、结论（Conclusion）
本文将平坦性-泛化叙事重构到对称约化几何上，说明有意义的平坦性需在商掉函数保持对称后的商流形上度量。结果表明，商线性稳定先控制商平坦，再控制输入光滑，最终在局部覆盖假设下控制泛化。贡献不仅是给出对称不变平坦定义，更是证明优化到泛化的机制可以在对称商几何中完整重建。

### 五、方法论与关键技术细节
关键设置包括标量输出模型、平方损失、插值解、正则自由 proper 群作用、局部规范固定截面、首层乘法表示及商梯度控制首层梯度的 C_sec 假设，并要求 ρ>0 以避免界退化。稳定性条件对应经典 ηλ_max≤2 的商版本，逐 batch 充分条件为 λ_max(A_I)≤2/η，显式依赖 batch size B 与学习率 η。方法还通过高阶张量矩递推推广到高阶输入光滑估计。局限在于依赖插值、平方损失、局部覆盖/有界性和局部截面等较强假设，且主要处理函数保持对称（如正缩放与置换），未覆盖非插值或交叉熵等更一般损失场景。
