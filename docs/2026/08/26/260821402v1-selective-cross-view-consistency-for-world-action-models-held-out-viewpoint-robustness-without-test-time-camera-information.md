# Selective Cross-View Consistency for World Action Models: Held-Out Viewpoint Robustness Without Test-Time Camera Information

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Bingqi Huang, Bingchuan Wei, Yingkai Cai, Zhaokui Wang
- 机构：Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21402v1) · [PDF](https://arxiv.org/pdf/2608.21402v1)

## TLDR
Selective cross-view consistency (SCVC) improves world action models' robustness to held-out camera viewpoints by enforcing a consistency loss only on view-invariant outputs (actions, proprioception, value) and not on view-covariant future frames, avoiding a provable shrinkage bias and requiring no camera labels or test-time camera information.

## Abstract
World action models (WAMs) jointly denoise future video frames and robot actions, and the video prior is expected to generalize their control. Camera viewpoint change remains one of their hardest perturbation axes. We study a question specific to this model class: when training with same-state cross-view image pairs, on which output coordinates should a consistency loss be imposed? The WAM denoising target mixes view-covariant coordinates, namely the predicted future scene, with view-invariant coordinates, namely the action chunk, future proprioception, and value. We show that consistency applied to the covariant block is provably harmful, shrinking legitimate view-specific content to a fraction $1/(1+4λ)$ of its true value, and we verify this shrinkage law in controlled experiments. Selective cross-view consistency (SCVC) therefore constrains only the invariant block, requires no camera labels, extrinsics, depth, or view synthesis at training or test time, and leaves the deployment interface unchanged. We introduce a carve-and-hold-out evaluation protocol on the LIBERO-Plus camera track that separates a distribution-matched ceiling from genuine interpolation and extrapolation to held-out viewpoints, with a matched pair-trained control isolating the effect of the consistency term from pair exposure. On held-out orbital viewpoints beyond the training envelope, SCVC improves closed-loop success over the matched control by 12.2 points (95% CI [7.4, 17.0]; +15.5, CI [11.7, 19.4], under an independent second seed) -- an effect two further camera axes replicate -- while interpolation within the envelope shows no gain in either seed (-1.2 and -4.3 points) and in-distribution competence is preserved (-0.6, -0.2). We also report a cross-backbone audit showing that published camera-robustness numbers are confounded by wrist-camera pose stability.
