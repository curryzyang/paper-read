# Benchmarking Classical and Transformer-Based Models for Document Sensitivity Classification

- 区域：速读区
- 排名：13
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Aleesha Zainab, Muhammad Ahmed Khalid, Faheem Ullah Khan, Asifullah Khan
- 机构：PIEAS
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16928v1) · [PDF](https://arxiv.org/pdf/2608.16928v1)

## TLDR
The paper introduces Strategic 16K, a leakage-controlled corpus of 16,000 WikiLeaks diplomatic cables for document sensitivity classification, and benchmarks six classical and transformer models, showing that eliminating label leakage prevents inflated performance and that BERT achieves the best accuracy (89.14%) while TF-IDF with logistic regression offers a strong, low-cost baseline.

## Abstract
Automatic sensitivity classification of organizational documents is a critical yet underserved problem, where the consequences of misclassification range from regulatory violations to security breaches. While AI-based approaches offer a scalable alternative to manual review, their reliability depends fundamentally on the integrity of training data. A pervasive but underreported problem in this domain is label leakage: residual classification markers embedded within document bodies that allow models to exploit surface shortcuts rather than learning genuine content-based sensitivity signals, producing performance estimates that are inflated and unreliable. This paper addresses this problem by introducing Strategic 16K, a carefully constructed, leakage-controlled corpus of 16,000 diplomatic cables sourced from the WikiLeaks Public Library of US Diplomacy (PlusD), and presents a systematic benchmark evaluating six model architectures spanning classical machine learning and transformer-based approaches. We document an extended leakage removal protocol that identifies and eliminates three categories of residual classification markers embedded within document bodies. On the clean benchmark, BERT achieves the strongest performance (Accuracy = 89.14%, F1 = 89.33%), followed by ELECTRA (Accuracy = 88.57%, F1 = 88.90%). Among classical models, TF-IDF with Logistic Regression achieves the strongest performance at significantly lower computational cost. These results constitute the first fully reproducible sensitivity classification benchmark constructed under explicit leakage-controlled conditions from WikiLeaks PlusD.
