# Interpreting Language Model Parameters

- 区域：精读区
- 排名：2
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Lucius Bushnaq, Dan Braun, Oliver Clive-Griffin, Bart Bussmann, Nathan Hu, Michael Ivanitskiy, Linda Linsefors, Lee Sharkey
- 机构：Independent, Goodfire, MATS
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20748v1) · [PDF](https://arxiv.org/pdf/2610.20748v1)

## TLDR
The paper introduces adVersarial Parameter Decomposition (VPD), a method that decomposes a language model’s parameters into simple, mechanistically faithful subcomponents that preserve behavior even under adversarial ablations, enabling circuit-level analysis and predictable model editing.

## Abstract
Mechanistic interpretability aims to uncover how neural networks use their parameters to implement their impressive neural algorithms. Although previous work has uncovered substantial structure in the intermediate representations that networks use, little progress has been made to understand how the parameters and nonlinearities of networks perform computations on those representations. In this work, we present a method that brings us closer to this understanding by decomposing a language model's parameters into subcomponents that each implement only a small part of the model's learned algorithm, while simultaneously requiring only a small fraction of those subcomponents to account for the network's behavior on any input. The method, adVersarial Parameter Decomposition (VPD), optimizes for decompositions of neural network parameters into simple subcomponents that preserve the network's input-output behavior even when many subcomponents are ablated, including under ablations that are adversarially selected to destroy behavior. This encourages learning subcomponents that provide short, mechanistically faithful descriptions of the network's behavior that should aggregate appropriately into more global descriptions of the network's learned algorithm. We study how sequences of interactions between these parameter subcomponents produce the network's output on particular inputs, enabling a new kind of 'circuit' analysis. While more work remains to be done to deepen our understanding of how neural networks use their parameters to compute their behavior, our work suggests an approach to identify a small set of simple, mechanistically faithful subcomponents on which further mechanistic analysis can be based.


## 精读解读（中文）
### 一、研究动机
机制可解释性希望逆向工程语言模型学到的神经算法，但以往工作主要揭示中间表示的结构，很少说明网络参数与非线性如何在这些表示上执行计算。基于激活的分解方法使用与原始网络不同的函数形式，难以把解释关联到真正做计算的参数和非线性上，也妨碍精确编辑参数和预测分布外行为。已有参数分解方法虽有前景，但尚未扩展到完整语言模型，且缺少对对抗选择消融下机制忠实性的充分验证。

### 二、技术方案（Method）
VPD将网络参数矩阵分解为若干秩一子成分，即用 W_l≈Σ_c U_c^l (V_c^l)^T 表示，并允许子成分数超过矩阵秩以容纳叠加表示；同时引入Δ分量刻画残差并施加Δ-L2损失以保持参数忠实。训练一个因果重要性函数预测每个批次和序列位置上子成分的可消融性 g∈[0,1]，在保留重要子成分的前提下对大量子成分做对抗选择的部分消融，使任意包含重要成分的子集都尽量保持网络输入输出行为。再用子成分聚类得到完整参数组件，并基于子成分交互构建归因图分析电路；实验对象是一个在Pile上训练的67M参数四层语言模型。

### 三、结果（Result）
在67M四层Pile语言模型上，VPD找到了高度可解释的参数子成分，既能按数据集样例解释其激活，也能通过子成分交互序列形成可分析的电路，并首次较满意地将注意力层计算分解为跨多个头的功能特化子成分。与逐层和跨层transcoder潜变量相比，VPD在标准训练目标下取得更好的稀疏度-重构权衡，对训练与评估协议不匹配更鲁棒，可解释性相当且特征分裂更少。作者还展示归因图可追踪信息流，并用参数子成分手动编辑模型中的表情符号预测。

### 四、结论（Conclusion）
VPD把基于消融的参数分解扩展到完整小型语言模型，并通过对抗选择的部分消融提升机制忠实性，表明可以识别少量简单且机制忠实的子成分作为进一步机制分析的基座。该路线支持跨头注意力分解、子成分电路分析和可预测的模型编辑，但仍需更多工作来加深对网络如何用参数计算行为的理解。

### 五、方法论与关键技术细节
关键细节包括：参数矩阵被分解为超完备秩一子成分，以处理叠加表示；用Δ分量和Δ-L2辅助损失保证子成分和尽可能等于原始参数；因果重要性函数输出连续消融分数，并以对抗部分消融近似检查所有潜在消融组合，要求少数子成分必要、且任意包含必要成分的子集充分。方法还引入显式聚类把子成分合成为完整参数组件，实验在67M四层语言模型和Pile上进行，并与CLT/transcoder比较稀疏度-重构和鲁棒性。局限在于模型规模仍小、机制存在性带有哲学假设、聚类仅在部分分析中使用，且对更大模型和更广泛任务的扩展仍需验证。
