# A Defense of the Quadratic Model

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Alexandru Meterez, Pranav Ajit Nair, Depen Morwani, Cengiz Pehlevan, Sham Kakade, Alex Damian
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21716v1) · [PDF](https://arxiv.org/pdf/2607.21716v1)

## TLDR
The paper defends the quadratic model as a surprisingly accurate and theoretically tractable proxy for predicting large language model optimization dynamics, including Hessian structure and stability, across training windows of up to 10%.

## Abstract
Due to the complexity of neural network loss landscapes, optimization theory is forced to rely on idealized models, and there is generally a tradeoff between how theoretically tractable the model is, and how accurately it describes the true optimization dynamics. In this work, we stress test the simplest possible model of optimization -- the quadratic model -- and show that it can be surprisingly predictive in an LLM setting with 150M parameters and 3B training tokens. Specifically, we show that Taylor expanding the model and the loss function at intermediate checkpoints through training can accurately predict the optimization dynamics over windows that can last up to 10\% of training. Having established this agreement, we then turn to analyzing the structure of these local quadratic optimization problems through two lenses: the Hessian spectrum and local stability. Using Lanczos quadrature with extremely deep probes, we are able to estimate the Hessian spectrum deep into the tail, and we find a surprising amount of structure in both the eigenvalues and eigenvectors, which depends on the batch size, preconditioner, and training time. We also empirically test local linear stability at intermediate checkpoints and compare it to theoretical predictions to demonstrate that optimization in LLMs typically occurs at a stochastic edge of stability, whose nature is also determined by batch size. Our results indicate the quadratic model may be a theoretically tractable proxy for pretraining optimization dynamics.


## 精读解读（中文）
### 一、研究动机
神经网络优化理论通常依赖于理想化模型，但这些模型在捕捉真实优化动态方面存在不足。本文旨在验证最简单的二次模型能否在大型语言模型（LLM）训练中提供准确预测，从而为理论分析提供可解代理。

### 二、技术方案（Method）
使用含有1.5亿参数和30亿训练tokens的LLM进行实验。在训练中间检查点对模型和损失函数进行泰勒展开，构建局部二次模型。通过该二次模型预测后续训练窗口（长达训练的10%）内的优化动态。同时，利用极深探测的Lanczos求积法估计Hessian谱的深尾部分，分析特征值和特征向量的结构；并实证测试局部线性稳定性，将其与理论预测比较，研究中受batch size、预条件和训练时间的影响。

### 三、结果（Result）
二次模型能够准确预测LLM训练中长达10%窗口内的优化动态。Hessian谱分析揭示了特征值和特征向量中丰富的结构，这些结构依赖于batch size、预条件和训练时间。优化动态通常处于随机稳定性边缘，其性质由batch size决定。

### 四、结论（Conclusion）
二次模型可以作为一个理论上可解且与实际预训练优化动态高度吻合的代理模型，为理解大型语言模型的优化行为提供了有力的工具。

### 五、方法论与关键技术细节
实验针对150M参数的LLM和3B tokens的训练数据；使用泰勒展开至二阶构建局部二次近似；关键分析工具包括Lanczos求积（深层探测）和线性稳定性分析；发现batch size和预条件显著影响Hessian谱结构和稳定性边缘；局限性在于二次模型仅在短窗口（约10%训练）内有效，更长时间的预测能力尚未验证。
