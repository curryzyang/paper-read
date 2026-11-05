# The Confidence Score: a New Measure on Kernels

- 区域：速读区
- 排名：15
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Elizabeth Hofer, Martin v. Mohrenschildt
- 机构：McMaster University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05528v1) · [PDF](https://arxiv.org/pdf/2611.05528v1)

## TLDR
The paper proposes the **Confidence Score**, a new kernel measure that assesses how well a kernel preserves ground-truth structure—including intra-class structure—and shows it correlates more strongly with classification accuracy than existing kernel measures across real and synthetic datasets.

## Abstract
Across a wide range of applications, kernel measures are used to tune hyperparameters, select among candidate kernels, and assess the suitability of kernels for specific learning tasks. For classification, kernel measures are used to predict which kernels may produce accurate kernel classifiers. Many existing kernel measures, such as alignment to the ideal kernel, are designed to reward kernels which captures all samples from the same class as similar. While effective in many settings, this requirement is unnecessarily restrictive for classification, where classes may exhibit substantial internal structure. In this work, the "Confidence Score", a new kernel measure, is proposed. Unlike alignment-to-the-ideal kernel measures, the Confidence Score measures the alignment between an encoding of the ground truth and that ground truth projected by the kernel, allowing kernels that preserve intra-class structure to achieve high scores. Through experiments, it is demonstrated that the Confidence Score exhibits a higher correlation with classification accuracy across a variety of kernels on both real-world and synthetic datasets, compared to select other kernel measures.
