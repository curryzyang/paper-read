# MOSAIC-SR: Transformer-Guided Symbolic Regression for Scientific Equation Recovery

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Peiyi Zheng, Yanming Kang, Hans De Sterck, Giang Tran
- 机构：University of Waterloo
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20997v1) · [PDF](https://arxiv.org/pdf/2609.20997v1)

## TLDR
MOSAIC-SR combines Transformer-generated equation sketches with MCTS-initialized local search, scale-aware constant optimization, and symbolic repair to achieve state-of-the-art symbolic equation recovery and strong predictive accuracy across scientific benchmarks.

## Abstract
Symbolic regression aims to recover closed-form equations from observations, providing interpretable models for scientific discovery. Existing approaches struggle to combine flexible structural search with efficient inference. Search-based methods can refine expression structure but often rely on costly combinatorial optimization with random initialization. Pretrained neural models generate formulas almost instantly, but their predictions often contain symbolic errors. We introduce MOSAIC-SR, which uses a pretrained Transformer to propose multiple initial sketches. These sketches initialize searches in several promising regions, avoiding random starts in the vast expression space. Each search jointly recovers structure and constants through scale-aware constant optimization and local symbolic repair. We evaluate MOSAIC-SR on the SRSD-Feynman dataset with and without dummy variables and on six additional benchmarks. MOSAIC-SR obtains the highest symbolic solution rate on every dataset while ranking among the top two methods in predictive accuracy. This advantage persists in the presence of irrelevant dummy inputs. The results show that learned priors can focus search on promising equation structures, and that numerical optimization and symbolic repair are important for recovery.


## 精读解读（中文）
### 一、研究动机
符号回归旨在从观测数据恢复闭式方程，以支持可解释的科学发现；但现有方法难以兼顾灵活结构搜索与高效推理：搜索类方法可修正结构却依赖昂贵组合优化和随机初始化，预训练神经方法生成快但常含符号错误。且高预测R²不等于代数等价，因此需要同时提升预测精度与符号解率。

### 二、技术方案（Method）
MOSAIC-SR 分三阶段：首先用合成方程（1–10个变量，含二元与一元算子，前缀波兰表示）经 SymPy 规范化，构造完整序列和将变量/常数替换为占位符的 sketch 序列；Stage 1 以双向 InfoNCE 对比学习对齐数值编码器（signed log 变换、Set Transformer、注意力池化）和符号编码器（前缀 Transformer）；Stage 2 将自回归解码器接在数值编码器上，以 teacher forcing 训练生成 sketch，并联合根算子/根度等辅助结构预测头。推理时随机解码多个合法 sketch，用 MCTS 把变量 token 映射到观测输入并拟合常数，按训练 NMSE 选前24个初始化独立局部搜索；每条搜索路径交替进行尺度感知常数拟合与局部符号修复，最终按验证 NMSE 和复杂度选式。

### 三、结果（Result）
在 SRSD-Feynman（含与不含 dummy 变量）及六个额外基准上，MOSAIC-SR 在每个数据集上取得最高符号解率，同时预测精度排名前二；在存在无关 dummy 输入时该优势仍保持。论文还表明，神经先验能把搜索聚焦到有希望的方程结构，数值优化与符号修复对从数值拟合走向代数正确恢复很关键。

### 四、结论（Conclusion）
MOSAIC-SR 说明将预训练 Transformer 作为结构提议器、再把变量赋值与常数估计交给推理期显式搜索，可以结合神经生成的速度与搜索方法的可修正性，提升科学方程恢复的符号正确性。其结论是：要恢复闭合方程，需优化符号解率而非仅优化预测 R²，并保留常数拟合与局部符号修复作为核心环节。

### 五、方法论与关键技术细节
关键细节包括：预训练数据由合成方程在随机输入分布/域上采样200点生成，表达式用 SymPy 规范化且刻意省略仿射变换以减少额外项；数值端对输入输出拼接做 sign(a)log(1+|a|)，按集合编码并保留集合表示供解码器交叉注意力；对比损失为温度 τ 的双向 InfoNCE，草图损失为 token 交叉熵加辅助结构损失 λ_aux；推理用 MCTS 做变量分配与常数拟合，常数采用对数间隔初始化以覆盖跨数量级科学常数，保留前24条轨迹并行搜索并做树编辑修复；评估沿用 SRBench 符号验证协议，预测精度用测试 R²>1−ε。局限/约束是仍需多轨迹局部搜索与验证集选式，计算开销和预训练分布外推能力可能影响恢复。
