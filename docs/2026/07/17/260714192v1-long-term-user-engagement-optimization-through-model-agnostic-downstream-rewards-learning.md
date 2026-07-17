# Long-term User Engagement Optimization through Model-agnostic Downstream Rewards Learning

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Dingsu Wang, Filip Ryzner, Kelly He, Armando Ordorica, David Woo, Aditya Mantha, Liyao Lu, Usha Amrutha Nookala, Haoran Guo, Jiacong He, Olafur Gudmundsson, Matt Chun, Krystal Benitez, Dhruvil Deven Badani, Yijie Dylan Wang
- 机构：Pinterest
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14192v1) · [PDF](https://arxiv.org/pdf/2607.14192v1)

## TLDR
This paper proposes a unified, model-agnostic downstream reward framework that derives session-level behavioral signals as proxy rewards to optimize long-term user engagement and retention in large-scale recommendation systems, demonstrating consistent improvements in online A/B experiments across multiple Pinterest surfaces.

## Abstract
As recommender systems mature in the past few years, their optimization objectives have evolved from a primary focusing on short-term behavioral signals to a broader emphasis on long-term user engagement and retention. However, directly optimizing retention is difficult because return signals are sparse, delayed, and only partially attributable to earlier recommendations. Prior work has addressed this challenge with sequential modeling and reinforcement learning, but these approaches typically require task specific reward engineering, substantial computational overhead, and surface specific implementations that are difficult to generalize. In this paper, we present a unified, model-agnostic downstream reward framework for optimizing long-term user value in large-scale recommendation systems. First, we formulate the downstream reward learning problem and develop an offline screening framework to identify session level behaviors that are both observable early and predictive of future retention. We then propose several model-agnostic downstream rewards signals derived from observed user action patterns across multiple sources. We further discuss the engineering effort to productionize the proposed rewards derivations and challenges we faced when adding them to our ranking models. Online A/B experiments demonstrate consistent improvements in engagement and retention-related metrics, and the framework has been deployed across multiple Pinterest surfaces, including Homefeed, Related Pins, Search, and Notifications.
