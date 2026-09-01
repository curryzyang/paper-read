# RankShift: In-Database Detection and Explanation of Categorical Shifts

- 区域：速读区
- 排名：15
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Omair Shafi Ahmed
- 机构：Microsoft
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28922v1) · [PDF](https://arxiv.org/pdf/2608.28922v1)

## TLDR
RankShift is an in-database, training-free method that detects and explains categorical distribution shifts—even when total event counts stay stable—by comparing category shares with a benign reference via a Pearson score, achieving accuracy comparable to or better than count-vector autoencoders on HDFS, BGL, and Thunderbird logs.

## Abstract
A login service can receive its usual number of failed sign-ins while one source grows from 2% to 30% of them. The same pattern appears in system logs when a rare event template becomes common while the message rate stays stable. These events change which categories are active without changing how many events occur. RankShift detects such changes inside the analytical database that stores the data. It compares each window's category shares with a benign reference using a Pearson score whose terms identify the categories responsible for the change. The same query returns the score, calibrated alert, and largest increasing contributions. We evaluate RankShift on HDFS, BGL, and Thunderbird. It matches the count-vector autoencoder within 0.001 AUROC on HDFS (0.999 versus 1.000) and leads on Thunderbird (0.983 versus 0.949). In a controlled fixed-volume experiment, RankShift detects rare-category shifts that are invisible to event-count monitoring, reaching 0.787 AUROC compared with 0.771 for the autoencoder. Across all three corpora, observed false-alarm rates track the requested operating levels. RankShift requires no model training or inference service, and the autoencoders deployed state is 137x larger.
