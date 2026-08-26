# KAN-Robust-Bench: A Benchmark for Evaluating the Robustness of Kolmogorov-Arnold Networks

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Mohammad Meymani, Roozbeh Razavi-Far
- 机构：University of New Brunswick
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21488v1) · [PDF](https://arxiv.org/pdf/2608.21488v1)

## TLDR
This paper introduces KAN-Robust-Bench, a benchmark that systematically evaluates the certified and empirical robustness of various Kolmogorov-Arnold network architectures against strong evasion attacks (FGSM, PGD, and C&W) using defenses such as randomized smoothing, adversarial training, and interval bound propagation on CIFAR-10 and SVHN.

## Abstract
While machine learning models have demonstrated strong performance in many domains, these models have shown profound vulnerabilities when they are exposed to adversarial threats. While adversarial attacks fall into various categories, the most prominent category in research studies is evasion. In evasion attacks, the adversary generates perturbed versions of samples, which might not be observable by human eyes. These samples generally fool the machine learning models with high confidence. This phenomenon poses a significant security violation against machine learning models. In this paper, we investigate the certified and empirical robustness of various Kolmogorov-Arnold network architectures against strong evasion attacks. At first, we provide the mathematical foundations for randomized smoothing and interval bound propagation, and report the $\ell_2$-certified robustness of the models under randomized smoothing. After that, we systematically evaluate the robustness of various defended and undefended KAN models under FGSM, PGD, and C&W attacks in order to find out the optimal defense strategies and architectures.


## 精读解读（中文）
### 一、研究动机
现有针对KAN的对抗鲁棒性研究大多集中于KAN与MLP/CNN等传统架构的对比，缺少在KAN家族内部、相同对抗条件下对不同KAN架构的系统性基准评估。本文旨在系统评估多种KAN视觉架构在强白盒逃逸攻击下的经验鲁棒性与认证鲁棒性，并比较不同防御策略，以确定最优的KAN架构与防御组合。

### 二、技术方案（Method）
以CIFAR-10和SVHN为基准数据集，选取KAN-Mixers、KANICE、PoolKANNeXt等具有代表性的KAN计算机视觉架构。攻击端采用白盒逃逸攻击FGSM、PGD和C&W生成对抗样本；防御端涵盖对抗训练、随机平滑（RS）和区间边界传播（IBP）。随机平滑通过向输入添加高斯噪声并利用蒙特卡洛采样进行多数投票构造平滑分类器，进而根据最可能类别与次可能类别的概率计算ℓ2认证半径；IBP训练则将最终损失定义为干净损失与IBP损失的加权组合，通过λ控制鲁棒性与准确率的权衡。实验流程首先在随机平滑下报告各模型的ℓ2认证鲁棒性，再对无防御和多种防御模型系统进行FGSM、PGD、C&W攻击测试，比较不同KAN架构和防御策略的鲁棒性表现。

### 三、结果（Result）
实验系统地给出了多种KAN架构在CIFAR-10和SVHN上的干净准确率、对抗攻击下的准确率以及随机平滑下的认证半径。结果表明鲁棒性高度依赖于KAN架构与防御策略的组合；随机平滑能够提供可证明的ℓ2鲁棒性保证，对抗训练可提升经验鲁棒性，而IBP通过可验证边界训练带来认证鲁棒性但伴随精度权衡。整体上，不同KAN架构在同一对抗条件下的表现存在明显差异，最优防御策略并非唯一。

### 四、结论（Conclusion）
KAN架构在对抗攻击下表现出与传统模型不同的鲁棒性特性，且KAN家族内部不同架构的鲁棒性差异显著。系统比较对抗训练、随机平滑与区间边界传播后，发现采用合适的防御策略可以显著提升KAN模型在CIFAR-10和SVHN上的鲁棒性，随机平滑在认证鲁棒性方面尤为有效。研究为KAN架构的鲁棒性基准测试和防御策略选择提供了参考。

### 五、方法论与关键技术细节
关键数据集为CIFAR-10和SVHN；攻击配置包含FGSM、PGD和C&W，均为白盒逃逸攻击。随机平滑使用高斯噪声和蒙特卡洛投票，认证半径依赖最可能类与次可能类的概率差及噪声方差σ。IBP训练使用最终损失为(1−λ)×ℓ_clean+λ×ℓ_IBP，λ控制鲁棒性与准确率权衡。评估包括无防御模型、对抗训练模型、随机平滑模型和IBP防御模型。局限性方面，研究主要聚焦白盒逃逸攻击，未覆盖投毒或黑盒攻击；认证鲁棒性仅针对ℓ2范数和随机平滑，其他范数与认证方法未系统比较；不同KAN架构的训练时间与计算复杂度差异也可能影响防御策略的实际适用性。
