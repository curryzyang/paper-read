# Understanding Fault Tolerance of Adversarially Robust Pruned Models

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Manali Dangarikar, Cory Merkel
- 机构：Rochester Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04173v1) · [PDF](https://arxiv.org/pdf/2608.04173v1)

## TLDR
Adversarially trained CNNs are more robust to input perturbations but more sensitive to stuck-at-zero weight faults, while pruning has minimal impact on fault tolerance or adversarial robustness.

## Abstract
Deep neural networks (DNNs) deployed on resource-constrained neuromorphic hardware face three concurrent challenges: the need for model compression through pruning, vulnerability to adversarial input perturbations, and susceptibility to hardware-induced weight faults such as stuck-at-zero errors. While each of these factors has been studied in isolation, their combined effects on model reliability have received little attention. This paper presents an empirical investigation of how pruning, adversarial training, and hardware fault injection interact to affect the robustness of convolutional neural networks. Using a compact three-layer CNN trained on MNIST, we conduct three experiments: (1) comparing the fault tolerance of naturally and adversarially trained models under simultaneous hardware faults and adversarial attacks, (2) evaluating how pruning affects adversarial robustness, and (3) characterizing the joint accuracy surface across fault rates, adversarial perturbation magnitudes, and pruning levels. Our results show that adversarial training improves robustness against input perturbations but increases sensitivity to stuck-at-zero weight faults. Contrary to intuition, pruning did not significantly increase fault sensitivity, and varying the pruning level had little effect across fault rates and attack strengths. These results highlight the need to jointly consider adversarial robustness and hardware reliability.


## 精读解读（中文）
### 一、研究动机
深度神经网络部署在资源受限的神经形态硬件上时，同时面临模型压缩（剪枝）、对抗输入扰动和硬件权重故障（如卡零错误）三重挑战。现有工作大多只孤立研究其中单个因素，对三者联合作用下的模型可靠性缺乏关注，因此本文首次实验探究剪枝、对抗训练和硬件故障注入如何共同影响卷积神经网络的鲁棒性。

### 二、技术方案（Method）
使用在MNIST上训练的三层卷积神经网络（三个卷积层分别有32、64、64个滤波器，后接10神经元全连接层），在PyTorch中开展实验。自然训练使用交叉熵损失和RMSProp优化器（学习率0.001，权重衰减5e-4，10轮）；对抗训练额外进行5轮，每轮同时使用自然图像和PGD生成的对抗图像，总损失为干净损失与对抗损失的均值。PGD采用L-inf约束，步长0.01，迭代40次，epsilon=0.3。剪枝采用基于幅度的非结构化剪枝，通过二值掩码与权重逐元素相乘来移除不重要连接。硬件故障通过软件故障注入模拟卡零错误，按比例将权重置零。评估时在epsilon从0到0.5（步长0.1）的FGSM和PGD攻击下，联合改变故障率（0到100%）和剪枝水平（0到80%），每个配置重复5次随机初始化并取平均。

### 三、结果（Result）
对抗训练显著提升了对FGSM和PGD攻击的输入鲁棒性，在epsilon=0.3且无故障时准确率保持在89%以上，但对抗训练模型对卡零权重故障更敏感，其干净准确率在故障率超过20%后明显低于自然训练模型。与直觉相反，剪枝并未显著增加故障敏感性，不同剪枝水平（0%到80%）在故障率和攻击强度变化下对准确率影响很小。联合表征显示，剪枝水平对鲁棒性-故障权衡几乎没有系统性影响，但中间故障率（20-40%）下模型行为方差较高，结果应视为方向性趋势而非精确效应。

### 四、结论（Conclusion）
本文通过受控实验揭示了剪枝、对抗训练和硬件权重故障之间的非平凡交互：对抗训练在增强输入鲁棒性的同时削弱了对卡零权重故障的容错能力，这种权衡可用决策边界几何解释——对抗训练将边界推离数据点，但权重故障破坏边界使其移回数据点附近，从而降低对抗鲁棒性。剪枝由于保留了大权重，并未额外加剧故障敏感度。该工作强调需要联合考虑对抗鲁棒性和硬件可靠性，为压缩、鲁棒模型在神经形态硬件上的可靠部署提供了初步依据。

### 五、方法论与关键技术细节
实验仅使用MNIST和简单三层CNN，未在更大数据集和真实神经形态硬件上验证。故障模型仅考虑卡零（stuck-at-zero），未包括卡一故障。剪枝采用非结构化幅度剪枝，训练时使用PGD对抗训练，攻击评估包括FGSM和PGD。中间故障率（20-40%）下运行间方差较大，结论需谨慎解读。论文提出决策边界几何解释作为假设，但未给出直接验证。未来方向包括不同数据集、架构、卡一故障以及真实硬件验证。
