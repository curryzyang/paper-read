# Lower expected Fisher rank implies better PAC generalization

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Marco Miani, Albert Kjøller Jacobsen, Albert Lopez i Serrano, Søren Hauberg, Georgios Arvanitidis
- 机构：AWS AI Labs, Technical University of Denmark
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33208v1) · [PDF](https://arxiv.org/pdf/2610.33208v1)

## TLDR
The paper introduces a Fisher-aligned PAC-Bayes parameter distribution that covers low-loss functional invariances with large volume, yielding a generalization bound that scales with the expected Fisher rank—so a lower expected Fisher rank implies tighter PAC generalization.

## Abstract
Deep learning architectures tend to generalize well to unseen data, but explaining this capability is still an open area of research. Under the assumption of i.i.d. data, PAC-Bayes provides a bound on generalization error, and its tightness relies on a parameter distribution that covers a large volume of low-loss solutions. The Fisher information metric endows the parameter space with a geometry for which distances reflect functional changes, and whose zero-component captures functional invariances. We define and study a Fisher-aligned parameter distribution for which we can simultaneously guarantee (1) a low-loss, thanks to the exploration constrained on the functional invariances and (2) a large log-volume of parameters, proportional to the number of zero eigenvalues. This distribution results in a high-probability generalization error bound, which scales with the expected rank of the Fisher information matrix, shedding light on the relevance of this quantity.


## 精读解读（中文）
### 一、研究动机
深度网络泛化好但缺乏可靠解释，局部平坦性等概念会被保持函数不变的参数重参数化破坏。PAC-Bayes 可给出泛化误差上界，但其紧致性取决于参数分布 q 是否同时覆盖大体积和低损失解。本文希望利用 Fisher 信息矩阵的零空间刻画函数不变方向，从而构造更优的参数分布并揭示 Fisher 秩与泛化界的关系。

### 二、技术方案（Method）
从已训练模型出发，在未标注数据集上计算 Fisher 信息矩阵及其 SVD，将参数空间分解为零特征值对应的核流形方向和非零特征值对应的正交方向。构造的 q 是无限个高斯分布的混合：沿核流形使用先验尺度的大扰动，并通过指数映射沿非恒定几何移动；沿非零特征方向只施加小扰动，使损失二阶泰勒展开足够准确并可解析计算期望。随后将该 q 代入参数无关的 PAC-Bayes 界，分别计算期望训练损失和 KL 项。

### 三、结果（Result）
分析表明该分布的期望训练损失与单个基模型相当；KL 在零特征值方向上为零，因为 q 与先验方差匹配，而非零方向贡献一个期望对数体积项。最终高概率泛化误差界随 Fisher 信息矩阵的期望秩增长，忽略对数项时界主要依赖非零特征值个数，因此期望 Fisher 秩越低，PAC 泛化界越紧。

### 四、结论（Conclusion）
论文提出 Fisher 对齐的参数分布，同时保证低损失和大参数体积，从而获得更紧的 PAC-Bayes 泛化界。其核心结论是较低的期望 Fisher 秩意味着更好的 PAC 泛化，说明 Fisher 秩可作为理解深度网络泛化能力的重要几何量。

### 五、方法论与关键技术细节
采用 i.i.d. 数据和损失有界于 [0,1] 的 PAC-Bayes 界；Fisher 由有限未标注数据集定义，只关注该数据上的函数不变性；关键假设是投影 Fisher 的秩在参数空间局部恒定，从而核流形维度等于零空间维度；方法依赖 Fisher 的 SVD、指数映射和二阶泰勒近似；KL 分解为核方向零项与非零方向对数体积项；局限性包括秩恒定假设、二阶近似有效性、指数映射计算成本以及界仍可能偏松。
