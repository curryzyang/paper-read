# Explaining the Saliency Map Sparsity of Adversarially-Trained Neural Networks

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Yannick Lunk, Atell Yehor Krasnopolsky, Damien Garreau, Leon Bungert
- 机构：University of Würzburg, Technical University of Munich
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10666v1) · [PDF](https://arxiv.org/pdf/2610.10666v1)

## TLDR
This paper theoretically explains the sparse saliency maps observed in adversarially-trained neural networks by showing that, for two-layer ReLU networks, adversarial training converges to a Bayes classifier with minimal anisotropic gradient norm (such as an ℓ₁ penalty under ℓ∞ attacks), which promotes sparse input gradients.

## Abstract
Understanding why deep neural networks make a given prediction is of great importance for their safe deployment. In computer vision, saliency maps, which highlight the image region most influential for a prediction, remain a widely-used form of explanation. An empirical observation is the apparent sparsity of gradient saliency maps of adversarially-trained neural networks. In this paper, we propose a theoretical explanation of this phenomenon for two-layer ReLU networks. We build on the established equivalence of adversarial training to the minimization of the empirical risk with weight-decay penalization and an added adversarial total variation term -- valid for certain loss functions. As the number of data points and neurons grows and the regularization parameters are sent to zero at appropriate rates, we prove that minimizers converge to a Bayes classifier with minimal gradient and Barron norm. Sparsity appears since for adversarial training with $\ell_\infty$-attacks the gradient norm is anisotropic and favors axis-aligned / sparse gradients. We illustrate our theoretical findings experimentally by evaluating the gradient $\ell_1$-norm and thresholded sparsity of naturally versus adversarially trained models.


## 精读解读（中文）
### 一、研究动机
对抗训练模型的经验观察是其梯度显著图常显得稀疏且更可解释，但对抗训练的目标只针对最坏扰动鲁棒性，并未显式优化梯度结构，因此这一现象缺乏理论解释。本文旨在为两层ReLU网络建立数学机制，说明为何ℓ∞对抗训练会诱导稀疏的输入梯度显著图。

### 二、技术方案（Method）
作者利用ℓ1损失下对抗训练与经验风险加权重衰减及对抗非局部总变差（TV）项的等价性，研究有限样本两层ReLU网络的经验最小化问题；在样本数n与神经元数m_n趋于无穷、对抗预算ε和权重衰减系数按适当耦合速率趋于零时，用Gamma收敛证明经验最小化子列收敛到极限问题。该极限问题在Bayes分类器中最小化Barron半范数与∫‖∇f(x)‖_* dμ(x)的加权和，其中‖·‖_*是攻击范数的对偶范数；将网络嵌入齐次Barron空间以推导泛化界和定量逼近。实验在二维玩具数据及ImageNet ResNet50上比较自然训练与不同ℓ∞预算对抗训练，计算输入梯度的平均ℓ1范数和阈值化稀疏度。

### 三、结果（Result）
理论结果表明，在耦合渐近极限下，对抗训练选择的Bayes分类器会显式平衡精度、Barron复杂度与输入梯度的对偶范数平均；对常用ℓ∞攻击，对偶范数为ℓ1，因此极限目标包含梯度ℓ1型惩罚，促使轴对齐或稀疏梯度，从而解释显著图稀疏。数值上，对抗训练系统性地降低输入梯度平均ℓ1范数并提高阈值化梯度稀疏度，二维实验中非局部TV正则与对抗训练得到低各向异性周长且近似轴平行的决策边界，而自然训练边界更振荡。

### 四、结论（Conclusion）
本文给出了对抗训练导致显著图稀疏的可证明机制：鲁棒训练通过非局部TV项隐式正则化输入梯度的对偶范数，ℓ∞攻击下等价于梯度ℓ1正则，因而产生稀疏解释。该结果把鲁棒性与可解释性联系起来，但理论限于两层ReLU、特定损失和耦合渐近制度，深层网络与有限超参情形仍主要由实验支撑。

### 五、方法论与关键技术细节
关键细节包括：数据为二分类i.i.d.样本，理论域Ω有Lipschitz边界；模型为式b0+∑a_iσ(w_i·x+b_i)的两层ReLU网络，权重衰减R_WD=1/2∑(a_i^2+‖w_i‖_2^2)且不控制偏置；对抗风险为sup_{x~∈B_ε(x)}ℓ(f(x~),y)，在ℓ1损失下与R(f)+εTV_ε(f;μ)等价，经验TV用每类样本的sup/inf差分定义；TV中的ε缩放使极限出现对偶范数积分，ℓ∞攻击对应ℓ1梯度惩罚；证明依赖Gamma收敛、齐次Barron空间、泛化界和逼近率，要求n、m_n→∞且ε、权重衰减以适当速率→0；实验指标为输入梯度ℓ1范数和阈值化稀疏度，局限是理论针对两层ReLU/特定损失/渐近设定，偏置不受权重衰减控制，实际深层模型结论为经验验证。
