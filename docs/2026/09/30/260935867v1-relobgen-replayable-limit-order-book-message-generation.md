# ReLOBGen: Replayable Limit Order Book Message Generation

- 区域：速读区
- 排名：15
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Junoh Kang, Kiseop Lee, Bohyung Han
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35867v1) · [PDF](https://arxiv.org/pdf/2609.35867v1)

## TLDR
ReLOBGen generates limit order book messages that are replayable by construction—selecting a referenced resting order via a learned distribution and masking invalid fields—thereby achieving 100% replayability, improved market realism, and a 2.7–3.6× speedup over LOBS5 without post-hoc correction or resampling.

## Abstract
We propose ReLOBGen, a method for generating limit order book (LOB) messages that are replayable by construction. Replayability is required for closed-loop market simulation, yet existing LOB message generators may produce non-replayable raw messages, i.e., messages inconsistent with the current market state. These generators therefore rely on post-hoc correction or rejection followed by resampling, which may alter the replayed message distribution or increase inference cost. ReLOBGen instead ensures replayability during generation: it selects the referenced order from the resting orders in the current LOB and then generates the remaining message fields to be consistent with that order and the market state. For realistic reference selection, ReLOBGen samples from a learned distribution over eligible resting orders, efficiently computed from cached order representations and a context-dependent query. It then enforces the consistency of the remaining fields by masking out invalid tokens. Together, these components enable efficient generation of realistic messages without post-hoc correction or resampling. In 500-message rollouts, ReLOBGen achieves 100% replayability, improves market realism, particularly for top-of-book statistics and the relative prices of LOB messages, and provides a $2.7\text{-}3.6\times$ speedup per replayed message over the LOBS5 baseline.
