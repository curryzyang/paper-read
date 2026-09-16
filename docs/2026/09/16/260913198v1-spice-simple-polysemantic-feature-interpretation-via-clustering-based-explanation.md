# SPICE: Simple Polysemantic Feature Interpretation via Clustering-based Explanation

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Sehyun Lee, Dahee Kwon, Damin Lee, Jaesik Choi
- 机构：Korea Advanced Institute of Science and Technology (KAIST), INEEJI
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13198v1) · [PDF](https://arxiv.org/pdf/2609.13198v1)

## TLDR
SPICE is a generalizable clustering-based framework that automatically disentangles polysemantic neurons by inferring the number of concept clusters per neuron, enabling systematic comparison of polysemanticity across CNNs and Transformers.

## Abstract
One of the pivotal recent challenges in neural network interpretability is polysemanticity, where a single neuron is activated by multiple, often unrelated concepts, hindering clear functional understanding. Although prior work has explored this phenomenon, existing approaches remain architecture-specific and depend on manual heuristics such as a fixed number of concept clusters ($K$), limiting their generality and scalability--especially for modern Transformer-based models. To address these limitations, we introduce SPICE (\textbf{S}imple \textbf{P}olysemantic Feature \textbf{I}nterpretation via \textbf{C}lustering-based \textbf{E}xplanation), a generalizable framework for analyzing polysemanticity in deep vision architectures. SPICE avoids architecture-dependent propagation rules, enabling the first systematic comparison of polysemanticity across both CNNs and Transformers, and automatically determines the number of concept clusters per neuron, eliminating reliance on a preset $K$ and supporting scalable analysis for large models. Using SPICE, we conduct a comprehensive investigation into how polysemanticity emerges, varies across depth and architecture, and forms through distinct computational pathways.
