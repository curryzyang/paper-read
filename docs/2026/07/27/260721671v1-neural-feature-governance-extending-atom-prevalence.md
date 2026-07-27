# Neural Feature Governance: Extending Atom Prevalence

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Idris Karel Seunda Ekwe, Patrick Tenga Shako, Ernest Parfait Fokoué
- 机构：Rochester Institute of Technology (RIT), US, African Institute for Mathematical Sciences (AIMS), Cameroon
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21671v1) · [PDF](https://arxiv.org/pdf/2607.21671v1)

## TLDR
Neural Atom Prevalence (NAP) extends the atom prevalence principle to neural networks via a hybrid Bayesian pipeline combining iterative magnitude pruning, spike-and-slab variational inference, and Poisson-Binomial layer-size selection to achieve state-of-the-art structural sparsity (e.g., 8% active nodes on MNIST) with well-calibrated uncertainty quantification and near-nominal predictive coverage.

## Abstract
Neural network compression and interpretability remain open challenges in modern deep learn- ing, where billion-parameter architectures deliver impressive accuracy at the cost of trans- parency, computational efficiency, and reliable uncertainty quantification. This paper introduces Neural Atom Prevalence (NAP), a principled Bayesian framework for structured node-level model selection in feedforward neural networks. NAP introduces the neural atom (activation unit) and functions as a hybrid method operating through a four-phase pipeline: Bayesian Lottery Ticket (BLT) identification via Iterative Magnitude Pruning (IMP), soft variational training of the Spike and Slab Independent Gaussian (SS-IG) model, Poisson-Binomial (PB) optimal layer-size selection, and Bayesian fine-tuning to produce a sparse, stable, interpretable, and accurate model. Extensive empirical validation across simulated nonlinear regression, two UCI benchmark datasets (Concrete, YearPredictionMSD), and the MNIST image classification task demonstrates that NAP achieves state-of-the-art structural sparsity, reducing active nodes to as few as 8% of the original dense architecture on MNIST, while well-calibrated probabilisti- cally: the aleatoric-epistemic uncertainty decomposition reveals that model ignorance accounts for only 3 to 4% of total predictive variance across all experiments, and regression reliability diagrams confirm a near-nominal predictive interval coverage (93.4% observed against a 95% target). These results establish NAP as a reliable, theoretically grounded, and computation- ally tractable solution to the simultaneous pursuit of sparsity, accuracy, interpretability, and uncertainty quantification in Bayesian neural networks.


## 精读解读（中文）
### 一、研究动机
现代深度学习中，大规模神经网络在取得高精度的同时，牺牲了透明度、计算效率和可靠的不确定性量化。为同时实现稀疏性、准确性、可解释性和不确定性量化，需要一个统一的框架。本文旨在将Fokoué的原子优势原则（基于最可能模型规模和top排名原子选择）成功扩展到神经网络，实现高效的节点级模型压缩。

### 二、技术方案（Method）
提出神经原子优势（NAP）方法，一种贝叶斯框架，用于前馈神经网络的结构化节点级模型选择。该方法包含四个阶段：1）通过迭代幅度剪枝（IMP）识别贝叶斯彩票（BLT），从密集网络中提取一个压缩的初始子网络；2）对Spike and Slab独立高斯（SS-IG）模型进行软变分训练，近似后验分布并计算每个神经元的包含概率；3）利用泊松-二项（PB）分布选择最优层大小，基于后验模型尺寸分布；4）进行贝叶斯微调，得到稀疏、稳定、可解释且准确的最终模型。输入数据包括模拟非线性回归、UCI基准数据集（Concrete、YearPredictionMSD）和MNIST图像分类任务。

### 三、结果（Result）
在MNIST上，NAP将活跃节点降至原始密集架构的8%，实现最先进的结构稀疏性。不确定性分解显示，aleatoric-epistemic分解中模型无知仅占总预测方差的3-4%。回归可靠性图表明，预测区间覆盖率接近名义水平（观测值93.4%，目标95%）。在模拟和UCI数据集上同样验证了方法的有效性和校准性。

### 四、结论（Conclusion）
NAP将贝叶斯彩票的压缩效率、Spike-and-Slab先验的精确稀疏性以及原子优势的概率选择逻辑统一到一个框架中，为贝叶斯神经网络同时追求稀疏性、准确性、可解释性和不确定性量化提供了可靠、理论扎实且计算可行的解决方案。

### 五、方法论与关键技术细节
数据包括模拟非线性回归、UCI Concrete和YearPredictionMSD、MNIST；先验采用Spike and Slab Independent Gaussian（SS-IG），通过变分推断近似后验；损失为变分下界（ELBO）；超参包括剪枝比例、SS-IG的超参数等；复杂度方面，从权重空间转向神经元空间降低了维度（例如小网络从27维降至10维）；局限性包括目前仅适用于前馈神经网络，且可能需要进一步验证在更深架构上的可扩展性。
