# CertBind from Multimodal Connectivity to Certifiable Retrieval Decisions

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Shuheng Cao, Zhenhao Zhang, Ruiqi Chen, Renjie Cao, Weijia Zhang, Siyu Zhang, Jiaxin Liu, Xiangyu Zeng, Haotian Geng, Fan Gu
- 机构：Yale University, Boston College, Tsinghua University, University of Michigan, Ann Arbor, ShanghaiTech University, University of California, San Diego, Nanjing University, Changsha University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06516v1) · [PDF](https://arxiv.org/pdf/2608.06516v1)

## TLDR
CertBind introduces a multiscale certification framework that, by analyzing node, edge, path, and query levels in frozen multimodal connector graphs, provides finite-sample guarantees for retrieval decisions—returning Direct, Certified, or Abstain—so that connected multimodal routes preserve native task performance while enabling safe cross-modal expansion.

## Abstract
Lightweight connectors make frozen multimodal encoders composable at the representation level. Deployment exposes a second problem at the level of task decisions. A connected route can expand cross-modal reach while changing an established native retrieval capability. We introduce CertBind, a multiscale theory of certifiable composition for frozen multimodal connector graphs. At the node scale, native anchors establish the exact task identification boundary under the stated chart model. At the edge scale, contract-aware conformal ranks provide graph-wide family-wise error control. At the path scale, an overlap-aware budget and clean calibration yield a finite-sample recovery radius under declared conditions. At the query scale, this radius yields a covered top-k candidate set that becomes a point certificate when its size equals k. CertBind therefore retains supported routes as Direct, sends only flagged routes to recovery, returns Certified for decisive recovery, and returns Abstain for unresolved queries. The evaluated C-MCR shared route reduced native CLIP R@1 from 0.524 to 0.290. The production fallback recovered 0.963 +- 0.002 of clean retrieval, while the passing branch recorded a no-harm value of 1.000. CertBind extends multimodal composability from connected representations to certifiable task decisions.
