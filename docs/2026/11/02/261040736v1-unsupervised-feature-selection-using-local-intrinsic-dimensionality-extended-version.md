# Unsupervised Feature Selection Using Local Intrinsic Dimensionality -- Extended Version

- 区域：速读区
- 排名：15
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Oussama Chelly, Michael E. Houle, Ken-ichi Kawarabayashi, Muhammad Rajabinasab, Arthur Zimek
- 机构：Oratio Technologies, National Institute of Informatics, New Jersey Institute of Technology, University of Tokyo, University of Southern Denmark
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40736v1) · [PDF](https://arxiv.org/pdf/2610.40736v1)

## TLDR
The paper proposes **LIDFS**, an unsupervised feature-ranking method that treats each feature as a point and scores it by its maximum-likelihood Local Intrinsic Dimensionality to favor locally discriminative, nonredundant features without labels, producing a complete feature ranking in \(\mathcal{O}(d^2 n)\) time with strong performance on high-dimensional benchmarks.

## Abstract
High dimensionality degrades both the efficiency and the effectiveness of learning algorithms, and in many applications no class labels are available to guide dimensionality reduction. This paper proposes LIDFS, an unsupervised feature selection method based on Local Intrinsic Dimensionality (LID). The method builds on the formal equivalence between LID and the indiscriminability of distance measures. The data matrix is transposed so that each feature is treated as a point, and the LID of each feature is estimated by maximum likelihood from the distances to its $k$ nearest neighboring features. Features with lower LID exhibit greater local discriminability and receive higher importance scores. A refinement step then retains one representative per feature neighborhood and demotes locally redundant features. The result is a complete ranking from which any number of features can be selected without rerunning the procedure. LIDFS does not use any information about labels or the number of classes, and runs in $\mathcal{O}(d^2 n)$ time for $n$ instances and $d$ features. LIDFS is compared with classic and state-of-the-art methods and a random baseline on 23 high-dimensional datasets, the classic benchmark collection. The evaluation uses classification accuracy and AUC with five downstream classifiers, as well as clustering accuracy and normalized mutual information, over both full and aggressive selection ranges. LIDFS ranks first in the supervised evaluations and first or tied second in the clustering-based evaluations. It belongs to the top statistical group together with methods that require the number of classes, and it runs faster than its closest competitor. Several recent methods, by contrast, fail to outperform the random baseline. A sensitivity analysis shows that small neighborhood sizes yield the best results.
