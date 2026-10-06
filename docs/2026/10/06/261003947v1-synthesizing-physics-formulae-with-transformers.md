# Synthesizing Physics Formulae with Transformers

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Shuwei Wang, Vadim Bulitko, Michael Youngblood, Ramon Lawrence, William Yeoh, Shinichi Nakagawa, Matthew R. G. Brown, Yu Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03947v1) · [PDF](https://arxiv.org/pdf/2610.03947v1)

## TLDR
By curating training formulae and fine-tuning on noisy targets, the authors develop a transformer that synthesizes physics formulae in about ten seconds with better extrapolation and noise robustness than comparable methods.

## Abstract
Finding a compact formula that fits a set of input-output pairs and predicts outputs on unseen inputs is a fundamental problem in science. Symbolic regression automates the search for such formulae: search-based methods explore the space of possible formulae directly, while transformers pre-trained on synthetic data produce formulae of comparable quality substantially faster. Existing transformers, however, are prone to overfitting --- they find formulae that fit the training data well but do not extrapolate to input ranges unseen during training. We address this by shaping the set of formulae used to train a transformer, and show that the resulting formulae extrapolate substantially better. Fine-tuning the transformer on data with noise-corrupted target values further makes the synthesized formulae robust to noise in the observations. On SRBench and LLM-SRBench our transformer synthesizes a formula in about ten seconds and extrapolates better than all evaluated methods at a comparable budget. Search-based methods surpass our accuracy only when given one to three orders of magnitude more time.


## 精读解读（中文）
### 一、研究动机
从少量输入-输出观测中找出既紧凑又能外推到未见输入范围的物理公式，是科学建模的核心问题，符号回归正是将其自动化。基于搜索的方法直接探索公式空间、精度高但耗时，而在合成数据上预训练的 Transformer 生成公式快得多却容易过拟合：生成的公式能拟合训练数据，却无法外推到训练时未覆盖的输入区间。本文的目标是让 Transformer 合成的公式在保持速度优势的同时获得显著更好的外推能力，并对观测噪声鲁棒。

### 二、技术方案（Method）
方法沿用'合成数据预训练 + 序列到序列生成公式'的范式：输入是若干数值样本点（自变量与目标值），输出是公式的符号 token 序列，由 Transformer 自回归解码，推理时一个公式约十秒生成、无需逐候选搜索。核心改动有两点：一是塑造训练用的公式集合（formula prior），即改变合成训练数据的公式分布与采样方式，使模型见到的公式更具可外推的结构，而不是只会在训练区间内插值；二是在目标值被噪声污染的合成数据上做微调，使模型在观测含噪时仍能恢复正确的符号结构。训练与评测均以合成的公式-数据对为监督，推理为单次前向解码。

### 三、结果（Result）
在 SRBench 与 LLM-SRBench 两个基准上，该 Transformer 约十秒即可合成一个公式，在同等时间预算下其外推表现优于所有被评测的方法；只有基于搜索的方法在获得多出一到三个数量级的时间预算时，才能在精度上超过它。对噪声污染目标值进行微调进一步提升了合成公式在含噪观测下的鲁棒性，说明训练公式分布的改造是外推提升的直接来源。

### 四、结论（Conclusion）
结果表明，Transformer 符号回归的瓶颈主要在于训练公式先验与数据分布的设计，而非模型规模或搜索强度：通过塑造训练公式集并做噪声微调，可以在极低时间预算下同时兼顾拟合精度与外推能力。这使得预训练 Transformer 成为相对搜索式符号回归更实用的选择——以约十秒的代价换取与高出数个数量级时间预算的搜索方法相当甚至更优的外推表现。

### 五、方法论与关键技术细节
关键实现细节包括：训练数据由合成公式采样生成，训练公式集合的构造方式（分布塑形）是主要自变量，需控制公式族、复杂度与变量采样区间以覆盖外推所需的输入范围；噪声鲁棒性通过在目标值加噪的合成数据上微调获得，而非在损失中显式建模噪声；评测在 SRBench 与 LLM-SRBench 上以时间预算对齐比较，并以训练输入区间之外的外推性能为主要指标。局限在于：效果仍依赖训练分布对真实公式空间的覆盖，外推失败可能来自分布外结构而非拟合不足；噪声微调的有效范围受噪声水平与形式假设限制；在极高时间预算下搜索式方法仍能在精度上胜出，说明大公式空间与含常量/系数的精确回归仍是弱点。
