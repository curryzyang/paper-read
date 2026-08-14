# MARCH: Scaling Recurrent Memory with Content-Routed State Anchors

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ming Zhang, Kaisen Yang, Shu Yu, Ermo Hua, Ning Ding, Xia Hu, Bowen Zhou, Chaochao Lu, Youbang Sun
- 机构：Shanghai AI Laboratory, Fudan University, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12435v1) · [PDF](https://arxiv.org/pdf/2608.12435v1)

## TLDR
MARCH improves recurrent sequence models by periodically caching content-addressable "state anchors" from the recurrent history, enabling a growing memory bank that allows selective retrieval of earlier states and substantially boosts long-context recall while retaining efficient recurrent computation.

## Abstract
Transformers owe much of their strong long-context retrieval capability to a token-level memory that grows with context length. This flexibility, however, incurs a quadratic computation complexity during training and a key--value cache that grows linearly during autoregressive inference. Recurrent alternatives offer efficient decoding by compressing the entire history into a fixed-size state, but often underperform on recall-intensive tasks since earlier associations usually get overwritten by subsequent updates, and only the most recent contextual information is retained. In this paper, we introduce Memory-Anchor Routing across Context History (MARCH), a network architecture that effectively scales state-space models beyond a fixed-size dimension, while maintaining computational efficiency over long-sequences. MARCH periodically caches cumulative recurrent-state checkpoints as state anchors and associates each anchor with a compact, content-conditioned anchor key. This lets MARCH maintain a memory bank, which can grow as context length increases, providing a controllable trade-off between historical resolution and memory cost. At each token, MARCH produces an anchor query to attend all causally available state anchors, and the output is calculated as an attention-style aggregation over all historical anchors along the current state. We show that after standard pretraining, MARCH consistently outperforms multiple linear attention variants across commonsense reasoning, LongBench, and in-context retrieval. These results demonstrate that content-routed state caching substantially strengthens recurrent long-range memory while preserving its native computation path.
