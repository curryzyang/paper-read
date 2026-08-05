# PatTree: a novel approach for automated creation of multimodal, graph-based patient representations for medical classification tasks

- 区域：速读区
- 排名：15
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Julia Gehrmann, Lars Quakulinski, Hamza Naseem, Oya Beyan
- 机构：University of Cologne, Fraunhofer Institute for Applied Information Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02692v1) · [PDF](https://arxiv.org/pdf/2608.02692v1)

## TLDR
PatTree automatically builds multimodal, graph-based patient representations from heterogeneous clinical data without pre-standardization, enabling direct classification with state-of-the-art accuracy (98.5% balanced accuracy) on Alzheimer's disease diagnosis tasks.

## Abstract
Access to holistic, multimodal data improves the performance of Artificial Intelligence (AI) in medical classification tasks compared to utilizing single modalities or data sources. However, the inherent heterogeneity and complexity of clinical real-world data pose significant challenges to structured data analysis and AI application. This heterogeneity includes missing values, multiple time points, diverse modalities, and inconsistent formats and semantics. Data harmonization prior to data integration tackles this challenge but remains resource-intensive and error-prone, limiting the scalability and reproducibility of holistic, AI-driven decision support on clinical real-world data. We therefore propose PatTree, a graph-based, holistic representation of patients that can be derived from real-world clinical data through the automated structuring of multimodal clinical data. PatTree enables early-stage data integration without relying on pre-standardized inputs. While representing heterogeneous clinical data within a unified knowledge graph, PatTree preserves the semantic relationships between data elements across modalities and data sources, facilitating interoperability and machine-interpretable data access. Using a subset of the ADNI-1 cohort (n = 763), we demonstrate that classification of patients is directly feasible on PatTree reaching state-of-the-art classification performance. In the three-class classification task distinguishing Alzheimer's disease, mild cognitive impairment, and cognitively normal individuals, we achieve a balanced accuracy of 98.5% and an F$_1$ score of 0.987 on the held-out test set. Our results show that assumption-free, automated structuring of multimodal medical data can serve as a scalable foundation for clinical AI pipelines bypassing tedious data preparation and standardization.
