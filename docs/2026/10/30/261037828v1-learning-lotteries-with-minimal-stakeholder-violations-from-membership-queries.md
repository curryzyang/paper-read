# Learning Lotteries with Minimal Stakeholder Violations from Membership Queries

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Nicholas Teh, Paul W. Goldberg
- 机构：University of Oxford
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37828v1) · [PDF](https://arxiv.org/pdf/2610.37828v1)

## TLDR
The paper studies how an AI developer can learn a lottery over model versions from binary stakeholder membership queries to minimize the number of stakeholders whose acceptance thresholds are violated, showing the problem is hard in general but tractable under structural assumptions or random stakeholder sampling, while deterministic querying of only some stakeholders gives no worst-case guarantee for the unqueried.

## Abstract
An AI developer often has several candidate versions of a system and can deploy a mixture of them, sending each request to a randomly chosen version, as in A/B testing. Each stakeholder (e.g., a safety team, a regulator, or a customer with private test data) accepts a mixture exactly when its expected performance (e.g., its rate of harmful replies) meets the stakeholder's own standard, which the developer can learn only by asking whether a proposed mixture is acceptable. We model this as choosing a lottery over $m$ alternatives for $n$ agents, each of whom accepts exactly the lotteries in an unknown halfspace and answers such binary membership queries. While Choo et al. (ICML 2026) sought a lottery that every agent accepts, none may exist when, say, safety and helpfulness requirements conflict, so we minimize the number of rejecting agents. We show that this problem is APX-hard even when all halfspaces are known and all utilities are $0$ or $1$. We then give exact algorithms that run in polynomial time when $m$ is constant, and in quasi-polynomial time when, for a constant $η$, some optimal lottery has no accepting agent within $η$ of its threshold. When only some agents can be queried, optimizing over a uniform sample of agents gives additive and relative guarantees for the whole population, with a sample size that does not depend on $n$, and a linear program gives a polynomial-time method for any $m$. On the other hand, for $m\ge 3$, a deterministic algorithm that queries only $K$ distinct agents cannot guarantee fewer than $n-K$ extra rejections, and this is achievable; in other words, it can guarantee nothing for the agents it does not ask. Small synthetic experiments indicate that our worst-case bounds are conservative on random instances.
