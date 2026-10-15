# Do Vision CIL Methods Transfer to Protein? A Diagnostic Benchmark of Frozen Protein Encoders

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Ziyuan Gao
- 机构：University of Cambridge
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18879v1) · [PDF](https://arxiv.org/pdf/2610.18879v1)

## TLDR
This paper systematically benchmarks nine vision-derived class-incremental learning methods on frozen protein encoders across multiple datasets and representations, finding that none transfer reliably because performance is strongly representation-dependent, and concludes that protein CIL requires encoder-aware methods that adapt to embedding geometry.

## Abstract
Protein function annotation operates over an expanding label space, making class-incremental learning (CIL) a natural framework for incorporating newly discovered functions without full retraining. Yet existing CIL methods have been developed largely in vision and have not been systematically evaluated over frozen protein representations. We conduct a controlled benchmark of nine representative CIL methods across five sequence-, structure-, and sequence--structure-based protein encoders and two enzyme function datasets at different scales, while keeping the encoders frozen and evaluation settings consistent across representations. We find that no method transfers reliably across encoders, and that these failures persist across alternative phase constructions. Diagnostic analyses reveal that this instability arises from weak gradient-based stability signals, substantial heterogeneity in embedding geometry, and covariance assumptions whose appropriate capacity changes with both dataset scale and encoder. These findings suggest that the representation itself should be treated as a central component of continual-learning design rather than a passive feature extractor. More generally, reliable protein CIL will require encoder-aware methods that adapt their statistical assumptions and capacity to the geometry of the representation on which they operate. Code is available at https://github.com/zygao930/ProteinCIL.
