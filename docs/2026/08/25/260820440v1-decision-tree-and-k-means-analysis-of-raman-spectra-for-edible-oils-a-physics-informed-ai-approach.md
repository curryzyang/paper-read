# Decision Tree and K-Means Analysis of Raman Spectra for Edible Oils: A Physics-Informed AI Approach

- 区域：速读区
- 排名：11
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Amrita Shaw, Chandrasekar S. N., Sai Muthukumar V., Jhinuk Gupta, Deepak L. N. Kallepalli
- 机构：CogniEvolve AI Inc., Aix-Marseille University, Sri Sathya Sai Institute of Higher Learning
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20440v1) · [PDF](https://arxiv.org/pdf/2608.20440v1)

## TLDR
This paper introduces a physics-informed Raman spectroscopy and machine-learning framework that uses t-SNE, K-means, Decision Trees, and NNLS-based spectral decomposition to accurately authenticate edible oils in both pure and fried-food matrices using remarkably few interpretable spectral variables, supporting frugal and edge AI applications for food-quality monitoring.

## Abstract
Authentication of edible oils in processed foods is important for food quality, fraud prevention, and regulatory compliance. This study establishes an integrated Raman spectroscopy and machine-learning framework that links intrinsic spectral organization, interpretable classification, and Physics-Informed Artificial Intelligence (PI-AI). Five edible oils were investigated in pure form and within a fried-potato-chip matrix using t-SNE, K-means clustering, Decision Trees, and Non-Negative Least Squares (NNLS)-based spectral decomposition. Unsupervised analyses revealed substantially stronger class organization and separability in pure oils, whereas food-matrix effects introduced pronounced spectral overlap. Decision Trees achieved 100% classification accuracy for pure oils using only four Raman variables from the original 1866-feature spectral space. These four variables, consistently identified by both pre-pruned and post-pruned models, represented only approximately 0.21% of the available spectral information while retaining perfect test-set performance. For matrix-containing samples, NNLS-based PI-AI spectral decomposition substantially improved classification by separating oil-related signatures from paper and potato contributions. Optimized post-pruned models achieved accuracies of 86.4% and 85.4% for paper-subtracted and paper-plus-potato-subtracted datasets, respectively, while reducing the number of important Raman variables to only five and four. The compact four-feature representation further reduced the data footprint by 99.44% without loss of classification accuracy. Collectively, these findings demonstrate that accurate Raman-based oil identification can be achieved through physically meaningful, highly compact, and interpretable spectral representations, providing a promising foundation for Frugal AI, Edge AI, portable sensing, and embedded food-quality monitoring.
