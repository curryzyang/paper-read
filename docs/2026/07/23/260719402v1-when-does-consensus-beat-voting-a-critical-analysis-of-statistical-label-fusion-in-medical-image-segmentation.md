# When Does Consensus Beat Voting? A Critical Analysis of Statistical Label Fusion in Medical Image Segmentation

- 区域：速读区
- 排名：5
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Renjie He
- 机构：The University of Texas MD Anderson Cancer Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19402v1) · [PDF](https://arxiv.org/pdf/2607.19402v1)

## TLDR
This paper critically analyzes statistical label fusion in medical image segmentation, demonstrating that STAPLE commonly degrades to thresholded majority voting, suffers from EM instability and class imbalance collapse, and offers no consistent advantage over simple majority voting, which remains a surprisingly robust baseline.

## Abstract
This paper provides a rigorous, self-contained investigation of consensus segmentation. We derive the mathematical foundations from first principles -- the generative model, EM algorithm, Van Leemput's marginalization analysis, identifiability conditions, Spatial STAPLE, and deep variational formulations -- and validate each theoretical prediction through controlled experiments. The central finding is sobering: under common conditions, STAPLE reduces to thresholded majority voting, suffers 95% EM suboptimality, and collapses under class imbalance. These are not edge cases but typical scenarios in medical imaging. Majority voting -- simple, non-parametric, and robust -- is a surprisingly strong baseline that the field has perhaps too hastily dismissed in favor of more "sophisticated" methods. At the same time, the deep consensus model demonstrates that the consensus problem is not inherently difficult -- it becomes tractable when the image is used alongside the labels. And conformal prediction shows that formal uncertainty guarantees are achievable and practical. We hope this work encourages practitioners to critically evaluate their consensus methods rather than applying STAPLE by default, and provides the mathematical and empirical foundation for more principled approaches.
