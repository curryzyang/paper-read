# An Asynchronous Federated Learning Platform for Lung Adenocarcinoma Grading via Foundation Models and Structural Pruning

- 区域：速读区
- 排名：10
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Moon-Il Joo, Md Ariful Islam Mozumder, Hee-Cheol Kim
- 机构：Inje University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14590v1) · [PDF](https://arxiv.org/pdf/2611.14590v1)

## TLDR
This paper presents a web-based asynchronous federated learning platform that combines the UNI2 foundation model and CLAM-SB MIL for privacy-preserving lung adenocarcinoma PD/WMD grading, showing that FedNova with 40% L1-norm structural pruning offers the best practical trade-off between communication efficiency and classification performance.

## Abstract
Classification of lung adenocarcinoma into poorly differentiated (PD) and well-to-moderately differentiated (WMD) subtypes plays an important role in patient survival; however, consistent classification is difficult due to inter-observer variability among pathologists. Collecting data from multiple hospitals is also challenging due to patient privacy concerns. This study proposes a web-based federated learning system that shares only locally trained model weights without sharing patient data between institutions. The UNI2 foundation model and CLAM-SB were used to classify pathological whole slide images. A four-client federated learning system was constructed, and the NLST cohort was reserved exclusively for external validation. In centralized evaluation, joint training with CPTAC and TCGA outperformed single-institution training on external validation, confirming the necessity of multi-institutional data integration. FedAvg, FedProx, FedBN, and FedNova were compared as federated learning algorithms under identical experimental conditions. Test AUC ranked as FedBN, FedProx, FedNova, and FedAvg. FedNova showed the most balanced classification performance between PD and WMD. L1-norm structural pruning at 20%, 30%, and 40% sparsity was applied to reduce model transmission size. FedAvg, FedProx, and FedBN showed a tendency of decreasing Test AUC under pruning, while FedNova achieved improved Test AUC across all sparsity levels. A web-based application was developed supporting slide upload, local training, AI classification, and attention heatmap-based visualization. The combination of FedNova and 40% pruning was confirmed as a practical approach that improves communication efficiency and classification performance while protecting patient privacy.
