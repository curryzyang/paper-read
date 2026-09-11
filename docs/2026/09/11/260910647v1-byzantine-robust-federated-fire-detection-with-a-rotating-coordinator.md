# Byzantine-Robust Federated Fire Detection with a Rotating Coordinator

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Georgia Argyrou, Aymen Bahrouny, Hedi Fendriy, Alexander Jung
- 机构：Aalto University, Kudelski Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10647v1) · [PDF](https://arxiv.org/pdf/2609.10647v1)

## TLDR
This paper introduces a communication-efficient, Byzantine-robust federated learning framework for indoor fire detection, combining a curated dataset, compressed edge-deployable MobileNet-V2 updates, and history-aware aggregation with a rotating coordinator to eliminate the fixed-server single point of failure while matching fixed-server accuracy.

## Abstract
We study the application of federated learning (FL) to indoor fire detection. Such fire-detection systems use edge cameras that record sensitive footage which cannot easily be collected at a central server. Existing federated solutions leave three practical obstacles unaddressed: limited uplink bandwidth, Byzantine (malicious or faulty) clients, and unconditional trust in a single, permanently fixed aggregation server. Our main contributions address all three. In particular, we provide (i) a curated indoor fire-detection dataset assembled from eight public sources; (ii) an edge-deployable detector whose model updates are compressed up to 10 time with only a small loss in balanced accuracy; and (iii) a semi-decentralized Byzantine-robust FL method that combines history-aware aggregation with a rotating coordinator, evicting stealthy attacks that per-round filters miss while removing the fixed-server single point of failure. On the held-out test set the rotating-coordinator method matches its fixed-server counterpart in accuracy and detection speed, and a physically distributed six-node cloud deployment confirms feasibility.
