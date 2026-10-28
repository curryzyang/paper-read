# Exploratory creative pre-ranking: Hierarchical empirical-Bayes Thompson sampling for real-time creative optimization

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Jiale Han, Ajith Moparthi, Dan Xie, Xiaowu Dai
- 机构：UCLA, Roblox
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36020v1) · [PDF](https://arxiv.org/pdf/2610.36020v1)

## TLDR
The paper proposes an exploratory creative pre-ranker that uses hierarchical empirical-Bayes Thompson sampling with audience-segment-level marginal counters to cheaply shortlist each campaign’s creatives before ad ranking, enabling calibrated exploration of cold creatives and improving predicted play-through rate with negligible serving latency.

## Abstract
Dynamic creative optimization decides which creative of an ad to render for each request. Recent work places that choice before ad ranking, but relies on deterministic point predictors with no calibrated uncertainty. AI-generated content has made creatives nearly free, while feedback per creative remains sparse and selection faces a tight latency budget. We introduce a creative pre-ranker that scores every recalled creative and shortlists each campaign's pool before the per-user ranker runs. Creatives sit in a hierarchy of audience segment, advertised item, campaign and creative, so a cold creative falls back on what its parent levels have earned, and how much it borrows from its parents is set in closed form from historical logs, with one parameter per level and nothing tuned. To stay within the latency budget, the pre-ranker predicts for an audience segment rather than an individual user, from per-attribute counters. It selects by a single Thompson draw per creative, balancing exploration and exploitation so that a new creative still has a chance to be learned. Replaying Roblox Sponsored-ads traffic over campaigns with competing creatives, the shortlist lifts predicted play-through rate by 8.14% against 2.80% for an equally sized random shortlist, forwards more than 40% fewer creatives than the full pool, and adds only 0.2% to serving time. After an A/B test on live traffic, the method now serves in production at Roblox.
