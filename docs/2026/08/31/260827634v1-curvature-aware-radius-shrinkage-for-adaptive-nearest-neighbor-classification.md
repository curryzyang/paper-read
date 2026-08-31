# Curvature-Aware Radius Shrinkage for Adaptive Nearest Neighbor Classification

- 区域：速读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Alexandre L. M. Levada
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27634v1) · [PDF](https://arxiv.org/pdf/2608.27634v1)

## TLDR
CARSANN introduces a geometry-driven nearest-neighbor framework that adaptively shrinks the neighborhood radius based on local manifold curvature, significantly improving classification accuracy over standard k-NN across numerous real-world datasets.

## Abstract
Nearest neighbor classification relies fundamentally on how locality is defined, yet conventional $k$-NN imposes the same neighborhood cardinality throughout the feature space. This assumption can be inadequate for data whose local geometry varies substantially across the underlying manifold. We introduce Curvature-Aware Radius Shrinkage for Adaptive Nearest Neighbor Classification (CARSANN), a geometry-driven framework that adapts the spatial support of each neighborhood according to local geometric complexity. CARSANN first estimates intrinsic dimensionality using TwoNN and constructs an intrinsic representation through principal component analysis. Local mean curvature is then estimated using a shape-operator-based formulation and controls neighborhood scale: highly curved regions receive stronger radius shrinkage, whereas approximately flat regions retain broader spatial support. Unlike methods that modify only the number of neighbors or the local metric, CARSANN explicitly adapts the spatial extent of local evidence. Experiments on more than 70 real-world OpenML datasets show that CARSANN consistently improves upon standard $k$-NN and is competitive with adaptive nearest-neighbor methods. In a controlled comparison using the same base neighborhood size, CARSANN achieves higher balanced accuracy on 40 of 45 datasets, increasing mean balanced accuracy from 0.6506 to 0.7528. The advantage also persists against $k$-NN with fixed $k=5$. Friedman and Nemenyi tests confirm that the improvements are statistically significant. These results indicate that local manifold curvature can serve as an effective geometric control variable for adapting neighborhood support, providing a complementary paradigm to cardinality-based nearest-neighbor adaptation.
