# LLMs or Naive Bayes? Old Gems or New Ways

- 区域：速读区
- 排名：10
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Mohammad Firas Sada, Dmitry Mishin, John Graham, Seungmin Kim, Mahidhar Tatineni, Frank Würthwein
- 机构：Yonsei University, Lawrence Berkeley National Laboratory, University of California, San Diego
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13185v1) · [PDF](https://arxiv.org/pdf/2609.13185v1)

## TLDR
This paper benchmarks Complement Naive Bayes against zero-shot and few-shot LLMs across text classification tasks, finding that LLMs only dominate in zero-data (and contamination-prone) regimes, while with labeled data Naive Bayes matches or exceeds LLM accuracy at 40–486× higher throughput and far lower energy, and it provides a task-dependent decision line plus a Kubernetes Helm operator for automated model selection.

## Abstract
Large language models (LLMs) prompt a recurring question in research computing: should classical methods like Naive Bayes (NB) be retired? We benchmark Complement Naive Bayes against zero-shot and few-shot LLMs spanning four model families and a 37x range in scale (27B to a 1T-parameter mixture-of-experts) across text classification tasks. LLMs dominate only in zero-data regimes (98.0% vs 88.2% on Amazon Polarity sentiment), and even that win is contamination-prone: on a low-contamination sentiment task NB beats the zero-shot LLM (81.7% vs 73.0%). However, once labeled data is available (e.g., AG News), NB reaches 89.1% accuracy, statistically indistinguishable from the zero-shot 27B LLM (89.0%) and better than the 397B frontier model (84.8%), at thousands of samples/sec on a commodity CPU. Fine-tuned DistilBERT reaches 90.6% but at far lower throughput than NB at batch size 1 (Table 2). Our measured GPU throughput analysis shows small-LLM batched inference is 40-486x slower than NB CPU inference (the multiplier depends strongly on the host CPU), exposing a structural gap bounded by memory bandwidth, with roughly two orders of magnitude lower energy per sample. For resource-constrained HPC practitioners performing text classification with labeled data, NB remains the optimal choice. We show the decision line is task-dependent (NB reaches LLM parity around $N \sim 10^4$ labels for topic classification, while zero-data sentiment favors the LLM at all N tested) and provide a Kubernetes Helm operator that automates model selection using configurable thresholds and verifiable Prometheus metrics.
