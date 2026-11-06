# Robust Stream Classification using Time Neutralising Decision Trees

- 区域：速读区
- 排名：10
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Brandon Gower-Winter, Georg Krempl
- 机构：Utrecht University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.06991v1) · [PDF](https://arxiv.org/pdf/2611.06991v1)

## TLDR
TNT is a decision-tree architecture for robust data-stream classification under concept drift that dynamically filters out outdated training instances and re-includes them when relevant, achieving best-in-class performance across 24 benchmark streams without relying on explicit drift detectors.

## Abstract
Data Streams are characterised as a potentially infinite source of data subject to non-stationarity. This non-stationarity, also called Concept Drift, often results in deployed predictive models having to be perpetually retrained as the underlying data generating process of the stream changes over time. Drift Detectors are a class of methods used to identify these changes, triggering these retraining procedures. Historically, Stream Learning has operated under the assumption that instances are only seen once, and cannot be stored for later use. Contemporary work relaxes this assumption, yet drift detection and simple resetting procedures are still ubiquitous.
  Building on related work which has shown that traditional Batch Learning algorithms often outperform Stream Learning algorithms when instances can be stored, we introduce Time Neutralising Trees (TNT), a Decision Tree architecture that enables robust stream classification in settings with Concept Drift. During training, TNT will filter out ("neutralise") old training samples that are no longer relevant given the current context of the stream. If those instances become relevant again, TNT will then re-include them. We evaluate TNT, and related algorithms on 24 real and semi-real classification data streams from the USP DS repository. Results show strong evidence that TNT achieves best-in-class performance on a wide-range of data streams with varying concept drift types.
