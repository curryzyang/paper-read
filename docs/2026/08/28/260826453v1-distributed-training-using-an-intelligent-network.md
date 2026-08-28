# Distributed Training using an Intelligent Network

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Nihar Shah, Ben Blier
- 机构：DoubleZero Foundation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26453v1) · [PDF](https://arxiv.org/pdf/2608.26453v1)

## TLDR
This paper proposes making the wide-area network an active participant in distributed training by using multicast and in-line FPGAs for efficient parameter exchange, alongside an optimization framework that generates rotating-clique synchronization schedules to maximize information flow and narrow the gap to colocated training.

## Abstract
Distributed training across a wide area network (WAN) is challenging, as continuous parameter exchange by islands of compute is constrained by limited bandwidth, high latency, and uneven topology. We propose making the network an active participant in training. On the systems side, such networks should leverage (i) multicast technology to replicate outbound traffic and (ii) in-line FPGAs to aggregate inbound traffic, to ease egress and ingress bottlenecks. These technologies are used for training across workers within a data center, but this paper extends them to the WAN. On the algorithms side, we develop an optimization framework that produces rich synchronization schedules (namely, rotating cliques of islands) around the underlying network topology and these technologies, to maximize information exchange. Finally, we illustrate this on a nine-city topology modeled on the DoubleZero network, a live programmable WAN equipped with both technologies, and show how the optimal schedules shift with the network's capabilities. Together, these can narrow the gap to the gold standard of colocated training.
