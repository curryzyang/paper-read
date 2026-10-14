# When Log Parsing Removes What Matters: Detecting Failures in Distributed GPU Workloads

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Boyuan Cui, Yuyang Zeng, Yifang Tian, Hans-Arno Jacobsen
- 机构：University of Toronto
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14009v1) · [PDF](https://arxiv.org/pdf/2610.14009v1)

## TLDR
GF-Bench, a PyTorch-based benchmark of 220 labeled two-GPU runs with CUDA out-of-memory and straggler failures, reveals that generic log parsing discards critical distributed execution context—limiting detection to at best 0.667 F1 on parsed logs—while raw-log in-context LogPrompt reaches 0.983 F1 at 9.0× token usage and 8.7× cost, exposing a fundamental effectiveness-efficiency trade-off in distributed GPU failure detection.

## Abstract
Large AI models increasingly rely on distributed GPU execution, yet it remains unclear whether established failure analysis methods transfer effectively to this setting. We introduce GF-Bench, a PyTorch-based framework and dataset for generating diverse failures in distributed GPU workloads. The framework supports extensible workload and fault-injection logic; based on this design, the current release targets failures visible in multi-GPU communication logs and provides 220 labeled two-GPU executions covering normal runs, CUDA out-of-memory fail-stop failures, and persistent straggler fail-slow failures. Using GF-Bench, we evaluate three sequence-based methods (DeepLog, LogAnomaly, and LogBERT) and the LLM-based LogPrompt on parsed logs, and additionally evaluate LogPrompt on raw logs. On parsed inputs, no method reliably detects both failure classes, and the highest overall F1 score is 0.667. Raw inputs raise the overall F1 score of in-context LogPrompt to 0.983, at 9.0x its average input-token usage and 8.7x its per-run cost. These results expose a substantial trade-off between effectiveness and efficiency: generic log parsing lowers operational cost but discards the distributed execution context required for accurate failure detection. GF-Bench provides a reproducible basis for studying cost-efficient analysis methods and can be extended to additional GPU workloads and failure types.
