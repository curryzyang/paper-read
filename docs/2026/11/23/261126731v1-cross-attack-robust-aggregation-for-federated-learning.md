# Cross-Attack Robust Aggregation for Federated Learning

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Eyhab Al-Masri
- 机构：University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26731v1) · [PDF](https://arxiv.org/pdf/2611.26731v1)

## TLDR
FedTether is a federated-learning aggregation method that reweights client updates by their robust, MAD-normalized deviation from a coordinate-wise median with a dead-zone, suppressing only clear outliers and otherwise reducing exactly to FedAvg, thereby achieving cross-attack robustness under non-IID data without shared data or a validation set.

## Abstract
Federated learning (FL) lets resource-constrained IoT and edge devices train a shared model without exchanging raw data, but compromised or faulty devices can poison the global model. Existing robust aggregators each fail in some regime: naive averaging (FedAvg) collapses under high-magnitude attacks, whereas distance- and statistics-based defenses (Krum, median, trimmed mean) sacrifice accuracy on non-IID data and remain vulnerable to stealthy attacks. We present FedTether, which reweights client updates by their deviation from a coordinatewise median through a robust, dead-zoned score applied as a server-side optimizer step. Across three datasets, three attack types, and Byzantine fractions up to 40%, FedTether is the only method top-tier in every regime: it matches FedAvg under stealthy attacks with no robustness tax, exceeds robust baselines by up to 42 accuracy points, and stays accurate where high-magnitude attacks reduce FedAvg to near-random. These properties persist at 50 clients under partial participation, with no shared data or validation set.
