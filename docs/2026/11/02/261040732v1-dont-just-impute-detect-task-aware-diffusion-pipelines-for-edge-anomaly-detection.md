# Don't Just Impute, Detect: Task-Aware Diffusion Pipelines for Edge Anomaly Detection

- 区域：速读区
- 排名：8
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jeongsu Park, Taehyeon Yun, Geonwoo Kim, Yuji Lim, Moohong Min
- 机构：Sungkyunkwan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40732v1) · [PDF](https://arxiv.org/pdf/2610.40732v1)

## TLDR
The paper proposes TADR, a task-aware conditional diffusion refiner that aligns block-missing data imputation with a frozen downstream anomaly detector’s objective rather than MSE, thereby preserving anomaly evidence, reducing false alarms, and improving edge anomaly detection while remaining CPU-deployable.

## Abstract
Industrial Internet of Things (IIoT) edge pipelines routinely lose contiguous blocks of multi-sensor data to network dropouts and hardware faults. The standard remedy is a disjointed "impute-then-detect" pipeline whose imputer is trained only for Mean Squared Error (MSE). Such an imputer fills a missing block with the most probable normal pattern: a partially observed anomaly is smoothed back toward normality, and boundary artifacts on normal data raise false alarms. We call this imputation bias and propose the Task-Aware Diffusion Refiner (TADR), a conditional diffusion refiner trained against the loss landscape of a frozen downstream detector. Because back-propagating through the sampling trajectory is intractable, the task-aware terms act on the one-step clean-window estimate that the noise prediction already yields, so training costs no more than plain diffusion training. Under strict Point-to-Point evaluation over five seeds with paired significance tests, TADR raises F1 by $0.338$ over the unrefined detector on SMD ($p = 0.0015$), and the anomaly enhancement objective alone contributes $0.463$ in ablation. We also characterise when the method helps: the gain tracks the continuous, mutually redundant channels available and the anomaly evidence the outage removes, and it is absent on telemetry datasets dominated by one-hot command channels and on PSM. At ten sampling steps TADR runs in $41.4$ ms per window on a single CPU core, sustaining about $24$ concurrent 1 Hz streams from a $4.03$ MB model. Code and per-seed results are available at https://github.com/int-park422/TADR.
