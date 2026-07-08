# Learnable Weighting of Intra-Attribute Distances for Categorical Data Clustering with Nominal and Ordinal Attributes

- 区域：精读区
- 排名：10
- 匹配度：1.4/10
- 来源：arxiv
- 作者：Yiqun Zhang, Yiu-ming Cheung
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05464v1) · [PDF](https://arxiv.org/pdf/2607.05464v1)

## TLDR
This paper proposes a unified distance metric for nominal and ordinal attributes and a clustering algorithm that jointly learns intra-attribute distance weights and data partitions to improve categorical data clustering performance.

## Abstract
The success of categorical data clustering generally much relies on the distance metric that measures the dissimilarity degree between two objects. However, most of the existing clustering methods treat the two categorical subtypes, i.e. nominal and ordinal attributes, in the same way when calculating the dissimilarity without considering the relative order information of the ordinal values. Moreover, there would exist interdependence among the nominal and ordinal attributes, which is worth exploring for indicating the dissimilarity. This paper will therefore study the intrinsic difference and connection of nominal and ordinal attribute values from a perspective akin to the graph. Accordingly, we propose a novel distance metric to measure the intra-attribute distances of nominal and ordinal attributes in a unified way, meanwhile preserving the order relationship among ordinal values. Subsequently, we propose a new clustering algorithm to make the learning of intra-attribute distance weights and partitions of data objects into a single learning paradigm rather than two separate steps, whereby circumventing a suboptimal solution. Experiments show the efficacy of the proposed algorithm in comparison with the existing counterparts.


## 精读解读（中文）
### 一、研究动机
现有分类数据聚类方法通常将名义属性和有序属性等同对待，忽略了有序属性值的相对顺序信息，且未考虑两类属性间的相互依赖关系，导致信息丢失和聚类性能次优。因此需要一种能统一度量名义与有序属性内部距离、并自动学习距离权重的聚类方法。

### 二、技术方案（Method）
输入为包含名义和有序属性的分类数据集。首先将名义属性的每个可能值转化为布尔属性（即二元有序属性），从而将所有属性统一为有序类型。然后基于属性间的条件概率分布定义统一的内部属性距离：对于任意两个属性，利用一个属性值条件下另一个属性值的分布差异（如KL散度）作为距离度量。随后提出迭代聚类算法，同时学习距离权重和数据划分：初始化距离权重为等权重，计算对象与簇模式之间的加权距离，将对象分配到最近簇，更新簇内概率分布，根据簇内紧凑性调整距离权重（增大有助于减小簇内距离的权重，减小不重要的权重），重复直至收敛。算法无需人工设定超参数。

### 三、结果（Result）
在多个真实数据集（包括混合类型、纯有序和纯名义数据）上的实验表明，所提算法在聚类准确率、标准化互信息等指标上全面优于现有距离度量（如基于熵的度量）和聚类算法（如k-modes、属性加权聚类等），尤其在混合属性数据集上性能提升显著，验证了统一度量与可学习权重机制的有效性。

### 四、结论（Conclusion）
提出的基于图视角的统一距离度量与可学习加权聚类算法能够有效处理任意类型（混合、纯有序、纯名义）的分类数据聚类，通过将名义属性转化为有序属性并利用属性间依赖信息，避免了信息丢失；同时通过联合优化距离权重与数据划分，克服了分步优化带来的次优解问题，是一种无参数、高鲁棒性的聚类方法。

### 五、方法论与关键技术细节
关键点包括：(1) 名义属性值被转化为布尔属性，视为有序属性的特例，实现了两类属性的统一；(2) 内部属性距离基于属性间的条件概率分布，使用对数几率或KL散度计算，充分捕捉属性依赖；(3) 距离权重在聚类迭代中根据簇内距离的方差自动调整，使重要距离贡献更大；(4) 算法无超参数，避免了调参问题；(5) 计算复杂度约为O(t n d² v)，其中t为迭代次数，v为平均取值数，适用于中等规模数据集；(6) 局限性：当属性间独立时距离度量可能失效，且对高维数据可扩展性需进一步验证。
