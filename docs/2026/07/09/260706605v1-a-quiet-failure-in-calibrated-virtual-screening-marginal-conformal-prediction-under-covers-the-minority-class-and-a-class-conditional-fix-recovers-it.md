# A Quiet Failure in Calibrated Virtual Screening: Marginal Conformal Prediction Under-Covers the Minority Class, and a Class-Conditional Fix Recovers It

- 区域：精读区
- 排名：10
- 匹配度：1.7/10
- 来源：arxiv
- 作者：Muhammadjon Tursunbadalov, Mustafojon Tursunbadalov
- 机构：Champions College Prep
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06605v1) · [PDF](https://arxiv.org/pdf/2607.06605v1)

## TLDR
Marginal conformal prediction in virtual screening under-covers the minority class on imbalanced datasets, but class-conditional (Mondrian) conformal prediction restores per-class reliability.

## Abstract
Conformal prediction is being adopted in drug discovery to put an honest number on model reliability: pick an error rate alpha, and the method returns prediction sets containing the true label with probability at least 1 - alpha. We show this guarantee can be dangerous on imbalanced datasets. Across four datasets, standard (marginal) conformal prediction hits its global 90% coverage target while leaving the minority class badly exposed: realized minority coverage falls to 64.8% on blood-brain-barrier penetration and to 4.2% on clinical-trial toxicity, where the rare class is nearly abandoned. The failure is not tied to one model: a random forest, a graph network, and a frozen chemical language model all reproduce it (p < 0.001 in every case), with severity tracking baseline calibration on rare labels rather than architecture. A conservation identity explains the effect: the minority's shortfall equals the majority's surplus amplified by the imbalance ratio, predicting the measured gap to within one point and ordering severity across datasets. The failure survives realistic scaffold splits and a second conformal score, while aggregate accuracy and overall coverage stay reassuringly high, which is exactly why it is easy to miss. Class-conditional (Mondrian) conformal prediction closes the gap on every dataset, restoring minority coverage to target for a modest increase in prediction-set size. We localize the failures to generic molecular scaffolds - plain benzene and pyridine cores occurring in both classes - propose a one-number diagnostic, and show with a cost model that abstaining on affected compounds flips a screening campaign from net-negative to net-positive utility. Our contribution is demonstrating on real chemistry how severe and invisible this known conformal-theory gap becomes under imbalance, and laying out a practical protocol restoring per-class reliability.


## 精读解读（中文）
### 一、研究动机
标准（边际）共形预测在虚拟筛选中被用于提供模型可靠性的保证，但在类别不平衡数据集上，它虽然在整体上达到目标覆盖率，却严重低估了少数类（如毒性化合物）的覆盖率，导致这些关键化合物被遗漏。这种失败隐藏于良好的整体指标之下，对实际筛选项目构成危险。

### 二、技术方案（Method）
基于分割（inductive）共形预测框架，使用四个MoleculeNet数据集（BACE、BBBP、Tox21 SR-ARE、ClinTox CT-TOX），覆盖从接近平衡到极度不平衡的类别分布。三种代表性模型：随机森林（500棵树，2048位Morgan指纹半径2）、图卷积网络（两层GCNConv 32→64→64，平均池化，Atom特征为32维独热编码）以及冻结的ChemBERTa-77M-MTR（均值池化SMILES嵌入，Logistic回归头）。采用LAC非一致性分数(1 - 预测概率)，对所有模型使用相同的数据划分（50%训练，25%校准，25%测试）和90%目标覆盖率。边际阈值计算基于校准集经验分位数（有限样本校正），Mondrian（类别条件）阈值则按每个类别计算独立分位数。实验重复10次随机分割，报告整体和每类覆盖率及平均预测集大小。额外进行选择性预测（接受/弃权规则）和决策成本模型分析。

### 三、结果（Result）
边际共形预测在所有数据集上实现整体90.2%的覆盖率，但少数类覆盖率大幅下降：BBBP为64.8%，Tox21 SR-ARE为38.9%，ClinTox仅为4.2%。该失败在三种模型上均高度显著（p<0.001），且严重程度由基础模型对少数类的校准决定，而非架构。Mondrian共形预测修复了每类覆盖率，使少数类回到目标附近（如BBBP达90.3%），代价是平均预测集大小从1.05增至1.26。分解公式解释：少数类短缺口等于多数类盈余乘以不平衡比率，准确预测了跨数据集差距。该失败在真实骨架划分（scaffold split）下仍然存在，并通过集中错误分析定位到苯环和吡啶骨架。

### 四、结论（Conclusion）
边际共形预测在虚拟筛选的不平衡数据中具有隐蔽且严重的危险性，因为整体指标掩盖了少数类覆盖率的崩溃。必须采用类别条件（Mondrian）共形预测来保证每类可靠性。作者贡献了在真实化学数据上的系统性量化、解释（保守恒公式）、诊断（少数类覆盖缺口）和实用协议，展示了切换Mondrian配合选择性预测如何将筛选活动从净负效用转为净正效用。

### 五、方法论与关键技术细节
数据划分：50%训练、25%校准、25%测试，校准集大小影响阈值精度；Mondrian要求每类足够校准样本。模型超参：随机森林500棵树无特定调优；GCN训练60轮，学习率1e-3；ChemBERTa作为冻结特征提取器，仅训练逻辑回归头。损失与评分：仅用LAC分数，但验证了APS分数也能重现失败。复杂度：边际与Mondrian计算成本相当（分别计算1个或k个分位数），预测集大小增加是主要代价。约束：Mondrian不能保证标签之外的子组覆盖，且对极度稀疏类别可能不稳定。局限性：边际-条件差距在共形理论中已知，论文未提出新方法，而是实证剂量化，且仅针对二分类，未考虑多类分子属性。失败跟踪基础模型对少数类的校准而非架构，但校准本身（ECE 0.04-0.10）不足以预测该差距。
