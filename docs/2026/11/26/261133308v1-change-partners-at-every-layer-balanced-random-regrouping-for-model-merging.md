# Change Partners at Every Layer: Balanced Random Regrouping for Model Merging

- 区域：速读区
- 排名：12
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Kaiyang Li, Shaobo Han, Shihao Ji
- 机构：NEC Laboratories America, University of Connecticut
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33308v1) · [PDF](https://arxiv.org/pdf/2611.33308v1)

## TLDR
**TLDR:** The paper shows that, for model merging across many fine-tuned experts, independently and randomly regrouping experts into equal-sized groups at every layer or weight matrix—Balanced Random Regrouping (BRR)—outperforms reusing one grouping or grouping similar experts, because layer-wise partner changes make merge-induced feature shifts vary independently rather than accumulate.

## Abstract
Model merging combines fine-tuned experts into one model that serves many tasks without retraining, but merging many experts this way substantially reduces accuracy. Grouping offers a middle ground: at every layer or weight matrix, the $N$ experts are divided into $K<N$ groups, the experts in a group are merged into one shared module, and a task uses the module merged from its expert's group. Natural choices are to keep the same partners across layers or to group similar experts. Surprisingly, we find that randomly changing partners at every layer outperforms both. We call this Balanced Random Regrouping (BRR): it independently partitions the experts into $K$ equal-sized random groups at each layer (BRR-layer) or weight matrix (BRR-matrix) and merges each group with an existing method. With validation-selected merge scales, both BRR variants outperform reusing one grouping across layers in all 24 CLIP settings, by 1.0-6.8 points, and BRR-matrix also outperforms the similarity-based FlexMerge in every setting. A first-order analysis explains this gain. At each layer, merging a task's expert with its partners shifts the task's output features; when the partners are the same at every layer, these shifts tend to point in similar directions and add up, whereas with new partners at every layer they vary independently and add up less on average. A series of experiments supports this analysis, which further guides a grouping search that can outperform BRR.
