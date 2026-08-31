# One year in a forest: Analyzing the challenges of autonomous navigation in subarctic environments

- 区域：速读区
- 排名：11
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Matěj Boxan, Nicolas Lauzon, Veronica Vannini, Mathis Turgeon-Roy, François Pomerleau
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27628v1) · [PDF](https://arxiv.org/pdf/2608.27628v1)

## TLDR
A year-long field study in a subarctic boreal forest evaluating nine odometry, localization, and mapping methods across seasons reveals that seasonal changes significantly degrade state-of-the-art navigation performance—especially for visual SLAM—while lidar-based approaches remain the most reliable for cross-season localization.

## Abstract
Subarctic regions have the potential to see increased deployment of autonomous robots in applications including forestry, mining, and environmental monitoring. In these conditions, an autonomous system's reliance on GNSS or cloud computing is precarious due to dense tree canopies and atmospheric attenuation, necessitating onboard sensing and data processing. However, established exteroceptive modalities, including cameras, lidars, and radars, are typically evaluated in structured urban settings or in environments that lack significant seasonal variations. To address this, we present a field report on a year-long deployment of a mobile robot in a subarctic boreal forest. We evaluate 64 km of data using nine odometry, localization, and mapping methods and assess their performance across seasonal changes. The performed experiments suggest that the environment changes significantly hinder the performance of state-of-the-art techniques, which show increased fragility when subject to conditions characterized by self-similar scenes or tall snowbanks. Additionally, complex Simultaneous Localization and Mapping (SLAM) algorithms offer limited accuracy gains over a proprioceptive baseline while significantly increasing system fragility. Furthermore, by correlating the position drift with features and confidence weight distribution, we show that visual-based SLAM methods are particularly affected by the seasonal changes. Additionally, we investigate the task of cross-season localization in a prior map. While lidar-based methods successfully completed localization runs between seasons, radar and visual methods are prone to failure due to a few matching features between runs, even within the same season. Finally, we detail the challenges and lessons learned from this year-long trial, including a multi-season Teach and Repeat (T&R) evaluation using both radar and lidar-based pipelines.
