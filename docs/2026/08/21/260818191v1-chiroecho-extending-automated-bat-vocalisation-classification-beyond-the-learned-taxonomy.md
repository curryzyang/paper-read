# ChiroEcho: extending automated bat vocalisation classification beyond the learned taxonomy

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Burooj Ghani, Welmoed Eversteijn, Milan van Hirtum, Juan Sebastián Cañas, Vincent J. Kalkman, Dan Stowell, A. Leonie Baier
- 机构：Leiden University, Tilburg University, University College London, Naturalis Biodiversity Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18191v1) · [PDF](https://arxiv.org/pdf/2608.18191v1)

## TLDR
ChiroEcho extends automated bat vocalisation classification beyond the learned taxonomy by combining joint species–genus predictions with geographic species distributions, enabling identification of species absent from training and increasing operational coverage of European bats from 73% to 85%.

## Abstract
Bats are key indicators of ecosystem health and are protected throughout Europe, making reliable population monitoring a conservation priority. Their cryptic nocturnal lifestyle makes passive acoustic monitoring essential, yet automated identification remains difficult as echolocation calls vary with behaviour and environment and overlap among species. We present a deep learning framework that jointly predicts species and genus and combines genus predictions with geographic species distributions at inference. When only one species of a predicted genus occurs in a region, the framework can resolve species absent from the learned taxonomy. This reframes geographic information as a means of extending, rather than constraining, a classifier's effective taxonomy. Using recordings spanning 35 European bat species, we evaluate closed-set classification, examine the instability of performance estimates for sparsely represented species, and conduct a controlled held-out proof-of-principle experiment. The rare-species analysis shows how limited evaluation data can obscure species-level performance, while the held-out experiment shows that genus predictions and location can recover labels unavailable to the species head. Geographic resolution extends operational coverage from 35 to 41 of the 48 native European bat species, increasing coverage from 73% to 85%. To our knowledge, this is the broadest operational coverage reported for automated European bat classification. More broadly, the bat framework provides proof of principle for resolving unseen fine-grained classes by combining coarse predictions with transparent external constraints.
