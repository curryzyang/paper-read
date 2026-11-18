# tmol: a GPU-accelerated implementation of the Rosetta energy function for machine learning

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Andrew Leaver-Fay, Kieran Didi, Jeff Flatten, Alex Ford, Guangfeng Zhou, Nathaniel Corley, Hahnbeom Park, Maxwell W. Kazman, Rafael I. Brent, Joseph Kleinhenz, Henry Solberg, Andrew M. Watkins, Brian Kuhlman, David Baker, Frank DiMaio
- 机构：Sungkyunkwan University, University of Oxford, University of North Carolina at Chapel Hill, NVIDIA Corp., Howard Hughes Medical Institute, Wistar Institute, Genentech, Korea Institute of Science and Technology, University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21857v1) · [PDF](https://arxiv.org/pdf/2611.21857v1)

## TLDR
tmol is a GPU-native PyTorch implementation of the RosettaGenFF forcefield that enables fast, batched, differentiable protein scoring and refinement—up to 362× faster than PyRosetta—and can be used as a machine-learning reward to improve generative protein design, e.g., by increasing interface hydrogen bonds and water bridges.

## Abstract
Physics-inspired forcefields complement generative machine learning models, showing better generalization beyond the training distribution. However, these forcefields are typically slow to evaluate, and their derivatives are difficult to integrate into ML frameworks. We introduce tmol, a GPU-native PyTorch library implementing the state-of-the-art RosettaGenFF forcefield. tmol supports efficient batched differentiable scoring and whole-structure refinement with up to 362-fold throughput increase (batched). Used as a reward in generative protein design, tmol increases hydrogen bonds and water bridges at designed interfaces.


## 精读解读（中文）
### 一、研究动机
物理启发的力场能弥补生成式机器学习模型在训练分布外泛化不足的问题，但传统力场评估慢、导数难以接入ML框架；Rosetta能量函数及其离散侧链优化、扭转空间最小化等采样算法此前缺乏可微的GPU原生实现。

### 二、技术方案（Method）
tmol用PyTorch将RosettaGenFF力场重构为GPU批量化张量运算：体系按氨基酸残基或配体分块，邻居块对分配到一个32线程CTA，坐标与参数载入共享内存，分块计算原子对能量并累加每原子梯度；实现全结构/残基对打分、离散侧链packing、笛卡尔与扭转空间最小化及FastRelax，并用分段扫描在GPU上完成内坐标与笛卡尔坐标转换，所有打分与优化通过autograd返回坐标或扭转导数。输入管线可自动参数化配体、修饰氨基酸、D-氨基酸、修饰核苷酸和多数金属配合物，并加入金属配位项及DNA/RNA扭转势。

### 三、结果（Result）
在1000个高分辨率蛋白结构上，tmol与PyRosetta各分项Pearson r均≥0.97、总分r=0.997；打分加梯度计算相对单线程PyRosetta实现233–362倍吞吐提升，扭转空间relax提升38–102倍。蛋白单体、蛋白-蛋白、蛋白-DNA诱饵判别、侧链rotamer恢复、配体对接和稳定性ΔΔG等基准总体相当，rotamer恢复因保留近天然rotamer而占优；配体参数化约1秒且无需人工检查。作为RFD4-Proteina束搜索奖励时，界面氢键和水桥增加，至少5对界面残基形成氢键的设计比例提高。

### 四、结论（Conclusion）
tmol使生成式ML、物理力场和物理引导模拟能够在同一可微框架内互操作，可作为生物物理先验提升数据受限场景下的模型泛化，并以开源BSD 3-Clause许可发布。

### 五、方法论与关键技术细节
实现中修正了count-pair权重不一致、羟基扭转双重计数和表格势表示，并调整FastRelax以改善rotamer恢复；新增金属配位项及按Yanover-Bradley方案从DNA/RNA结构导出的扭转势。速度对比基线为单线程PyRosetta，评测覆盖1000个高分辨率结构及多类已发表基准；摘要未给出训练超参，且部分ML奖励的精确数值在全文预览中截断。
