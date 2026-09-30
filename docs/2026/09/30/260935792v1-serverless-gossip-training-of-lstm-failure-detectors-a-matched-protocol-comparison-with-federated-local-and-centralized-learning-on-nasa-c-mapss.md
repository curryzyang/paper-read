# Serverless gossip training of LSTM failure detectors: A matched-protocol comparison with federated, local and centralized learning on NASA C-MAPSS

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yusuf Öztürk, Enes Göktekin, Bengisu Atlı, Akın Öztürk, Zhixiang Wang, Ulas Bagci
- 机构：Antalya Bilim University, Northwestern University, Ankara University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35792v1) · [PDF](https://arxiv.org/pdf/2609.35792v1)

## TLDR
Serverless synchronous ring gossip can train LSTM failure detectors on NASA C-MAPSS nearly as well as federated averaging—while outperforming isolated local training and approaching centralized performance—but its advantage shrinks as data heterogeneity and ring size increase.

## Abstract
Industrial predictive maintenance increasingly depends on learning from equipment spread across sites whose sensor data cannot easily be pooled. Federated averaging (FedAvg) solves this with a central aggregation server; gossip learning removes the server, but its behaviour for recurrent failure-detection models has not been measured under controlled conditions. We compare synchronous ring gossip with FedAvg, isolated local training and a centralized reference for a stacked LSTM that detects imminent failure on the NASA C-MAPSS turbofan benchmark. All methods share one open implementation, architecture, initialization, optimizer, data split and training budget, and the primary endpoint uses one terminal window per test engine to avoid the statistical dependence of overlapping windows. On FD001 (five seeds), gossip reached a terminal-window F1 of 89.6 +/- 1.3%, compared with 89.9 +/- 1.1% for FedAvg, 83.6 +/- 6.7% for local training and 93.5 +/- 2.1% for centralized training, while transmitting the same payload as FedAvg without a coordinator. Node models agreed closely but not exactly (1.8% pairwise decision disagreement versus 5.6% without communication). Across FD002-FD004, peer communication improved terminal-window F1 over local training by 13-28 points; gossip matched FedAvg on FD003 and FD004 but was 4.3 points lower on the multi-condition FD002 subset. Simulated message loss, node failure and server outage changed neither method appreciably, whereas larger rings degraded gossip faster. Ring gossip is therefore a practical serverless alternative when data heterogeneity is moderate, and faster-mixing topologies become important as heterogeneity grows.
