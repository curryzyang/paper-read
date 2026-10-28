# Generalization in Learning: Eyring Formula and Predator-prey Model

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：S. V. Kozyrev, I. A. Lopatin, Alexander Pechen
- 机构：Ivannikov Institute for System Programming of the Russian Academy of Sciences, Steklov Mathematical Institute of Russian Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35965v1) · [PDF](https://arxiv.org/pdf/2610.35965v1)

## TLDR
The paper uses a predator-prey model and thermodynamic Eyring-formula arguments to explain improved generalization in stochastic gradient learning and GANs, the delayed-generalization “grokking” phenomenon via entropy-driven motion on a zero-risk manifold, and better polynomial approximation than gradient descent in a noisy-data recovery example.

## Abstract
In this work, generalization in machine learning is investigated using a predator-prey model. We overview biological and chemical interpretation of the stochastic gradient Langevin dynamics and generative adversarial network. For a particular example of recovering an unknown function by a polynomial of fixed degree from a set of noisy data, the predator-prey model provides better approximation compared to the gradient descent method. Further, thermodynamical arguments, in particular Eyring formula, are used to explain grokking (delayed generalization) phenomenon in machine learning.


## 精读解读（中文）
### 一、研究动机
论文关注机器学习中的过拟合与泛化问题，尝试用统计物理和生物捕食者-猎物模型解释随机梯度Langevin动力学、GAN以及grokking（延迟泛化）现象。其核心动机是借助宽（平坦）极小值、算法稳定性和Eyring公式，说明噪声随机优化为何倾向选择泛化更好的解，并给出可操作的过拟合抑制思路。

### 二、技术方案（Method）
作者将随机梯度下降建模为以经验风险为势能的随机梯度Langevin动力学SDE，并用Fokker-Planck方程、Gibbs分布和Eyring反应速率公式分析宽极小值选择；将GAN的判别器与生成器分别视为猎物与捕食者，写成两个耦合SDE，用捕食者追逐猎物解释判别器被推离窄极大值。数值部分以带噪声数据恢复未知函数f(x)=sin(πx)为例，用固定次数多项式作为单层网络模型，以训练集MSE为损失，比较普通梯度下降与捕食者-猎物方法的训练/测试MSE，并考察不同多项式次数下的过拟合与泛化表现。

### 三、结果（Result）
理论分析表明，Eyring公式e^{-β(F1-F0)}使高熵宽势阱具有更低自由能和更高占据概率，从而解释随机梯度优化的更好泛化；grokking被分解为快速记忆阶段（带漂移扩散，距离约随时间t增长）和沿零风险流形的慢速泛化阶段（零势Brownian运动，距离约随√t增长），与实验中约10^3步记忆、约10^6步泛化的时间尺度相符。GAN中生成器作为捕食者推动判别器离开窄极大值，可降低过拟合。数值回归实验中，摘要报告捕食者-猎物模型在固定次数多项式恢复噪声数据时相较梯度下降取得更好的逼近/泛化表现。

### 四、结论（Conclusion）
论文结论是，随机梯度Langevin动力学、Eyring公式和捕食者-猎物动力学为理解泛化、过拟合控制及grokking提供了统一的物理/生物视角；宽极小值与零风险流形的高熵区域对应更稳定、泛化更好的解，捕食者-猎物式优化可作为一种抑制窄极小值的过拟合控制策略。

### 五、方法论与关键技术细节
关键实现包括：训练集N1=20、测试集N2=10，噪声为标准差0.2的高斯噪声，候选模型为d=1,3,5,7次多项式，损失为训练MSE并以测试MSE评价，梯度下降与捕食者-猎物方法采用相同步数和学习率。理论部分依赖温度θ、逆温度β、自由能F=E-θS、Eyring过渡速率以及零风险流形熵随样本量近似线性下降等假设；GAN分析使用判别器/生成器参数空间上的耦合SDE。局限在于数值验证仅针对小型一维正弦函数回归和低阶多项式，grokking解释含唯象假设，且摘要未给出完整定量表格与所有超参数。
