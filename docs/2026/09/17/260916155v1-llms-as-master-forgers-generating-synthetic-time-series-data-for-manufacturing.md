# LLMs as Master Forgers: Generating Synthetic Time Series Data for Manufacturing

- 区域：速读区
- 排名：5
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Mantek Singh, Jeshwanth Challagundla, Prateek Karnal, Gagan Ganapathy, Vineet Shah, Ridam Arora
- 机构：Stony Brook University, Liverpool John Moores University, UMass Amherst, IIT Patna, IIT Indore, University of Texas at Arlington
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16155v1) · [PDF](https://arxiv.org/pdf/2609.16155v1)

## TLDR
This paper introduces an LLM-based framework that uses fine-tuning and retrieval-augmented generation to create high-quality synthetic manufacturing time-series data, outperforming ARIMA and LSTMs and improving downstream anomaly detection.

## Abstract
This paper presents a novel framework leveraging Large Language Models (LLMs) to generate synthetic time series data for manufacturing processes. Motivated by the scarcity of labeled time-series data in real-world manufacturing settings, which hinders the development of robust machine learning models, we explore the potential of LLMs to learn complex temporal dependencies and generate realistic synthetic data. Our approach involves fine-tuning pre-trained LLMs on manufacturing process instructions and employing a Retrieval Augmented Generation (RAG) technique to enhance data diversity and realism. We evaluate our method against traditional time series modeling techniques like ARIMA and LSTMs, using quantitative metrics, PCA analysis, and downstream task performance (anomaly detection). Results demonstrate that our LLM-driven framework outperforms these baselines, generating high-quality synthetic time series data that effectively captures temporal dependencies and statistical properties of real manufacturing data, leading to improvements in downstream task performance.
