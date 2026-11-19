# TRACE-MAS: Diagnosing and Repairing Collaboration Failures in Multi-Agent Systems

- 区域：速读区
- 排名：6
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Zekai Chen, Yihan Sun, Xunkai Li, Xun Wu, Xinmo Jin, Yinlin Zhu, Haodong Lu, Xuaner Chen, Rong-Hua Li
- 机构：Shandong University, Minzu University of China, Sun Yat-sen University, Beijing Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23362v1) · [PDF](https://arxiv.org/pdf/2611.23362v1)

## TLDR
TRACE-MAS is a fine-grained framework that learns normal collaboration patterns in LLM-based multi-agent systems to detect execution-level deviations, trace failures to their true sources rather than propagated symptoms, and apply minimal repairs, improving root-cause localization by 60.2% and task recovery across five benchmarks.

## Abstract
LLM-based multi-agent systems (MAS) rely on not only individual agent behaviors but also the interactions that connect agents, including message exchanges and task dependencies. Existing MAS safeguards mainly perform agent-level anomaly detection, which becomes insufficient when failures originate from agent interactions and detected anomalies do not necessarily reveal their true sources. To address this limitation, we propose \textbf{TRACE-MAS}, a finer-grained framework for diagnosing and repairing MAS failures. TRACE-MAS learns normal collaborative execution patterns from benign trajectories and detects deviations in agent state changes, message transitions, and task dependency evolutions. It further identifies responsible execution elements through source-aware attribution and selects minimal interventions to restore collaboration while preserving task-critical capabilities. Experiments on five MAS benchmarks demonstrate that TRACE-MAS significantly improves root-cause localization accuracy by \textbf{60.2}\% and achieves consistent gains in task recovery over strong MAS safeguards.
