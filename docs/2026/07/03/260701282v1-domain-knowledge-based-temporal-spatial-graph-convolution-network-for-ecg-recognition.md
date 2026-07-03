# Domain Knowledge Based Temporal-Spatial Graph Convolution Network for ECG Recognition

- 区域：精读区
- 排名：8
- 匹配度：1.6/10
- 来源：arxiv
- 作者：Wenting Ma, Zhipeng Zhang, Xiaohang Yuan, Ningwei Xie, Yuxin Xie, Xiaolin Wang, Meng Guo, Xingang Chai, Zhenjie Yao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.01282v1) · [PDF](https://arxiv.org/pdf/2607.01282v1)

## TLDR
This paper introduces a domain knowledge-based temporal-spatial graph convolution network for ECG recognition that models intra- and inter-cycle relationships using double-stream directed graphs with key PRQST landmarks, achieving state-of-the-art F1 scores, especially for rare categories.

## Abstract
In light of strides in Arti cial Intelligence (AI) and its wide spread application, challenges persist in the interpretability of AI models, particularly within specialized domains like healthcare, such as electro cardiograph (ECG) recognition. Rather than relying solely on end-to-end convolutional neural networks, this paper introduces a novel approach using a domain knowledge-based graph convolution network for ECG recognition. Key landmarks points of PRQST, vital to ECG interpreta tion, are incorporated as domain knowledge. The double-stream directed graph is employed to model both intra and inter ECG cycles. Speci cally, spatial directed graphs capture the positional relationships among key points, while temporal directed graphs delineate temporal dependencies between adjacent cycles in extended ECG sequences. Experimental re sults on the First Chinese ECG Intelligent Competition dataset, which speci cally classify ECG into nine categories, prove the e cacy of the proposed model. The overall average F1 score is 88.1%, the average F1 score of rare categories is 76.3%, both outperform the state-of-the-art models. The introduction of domain knowledge did enhance the detec tion performance, especially for rare categories.
