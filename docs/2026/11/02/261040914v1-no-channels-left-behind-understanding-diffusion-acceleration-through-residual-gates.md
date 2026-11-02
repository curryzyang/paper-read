# No Channels Left Behind: Understanding Diffusion Acceleration through Residual Gates

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Junha Park, Jaemyung Yu, Jaehui Hwang, Jong-Seok Lee, Dongyoon Han
- 机构：Yonsei University, NAVER AI Lab
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40914v1) · [PDF](https://arxiv.org/pdf/2610.40914v1)

## TLDR
This paper shows that diffusion-transformer training acceleration is driven in part by reorganization of AdaLN-Zero residual gates, introduces normalized participation ratio to measure gate channel usage, and proposes a teacher-free radial objective that broadens gate participation and improves FID.

## Abstract
Training acceleration methods for diffusion transformers, such as REPA and dispersive regularization, are commonly explained by additional supervision, spatial-structure priors, or improved feature geometry. We revisit this view and uncover a striking internal change: the AdaLN-Zero residual gate $α$, which directly controls how conditioned updates enter the residual stream, is substantially reorganized by these methods. This observation motivates our hypothesis that acceleration arises, at least in part, from reshaping the residual gating pathway rather than solely from the feature structures explicitly imposed by auxiliary objectives. Supporting this view, accelerated models are markedly more sensitive to perturbations of $α$, and their gate geometry reflects semantic relationships among classes. We further introduce the normalized participation ratio (nPR) to characterize the channel-wise organization of the gates and find that, across REPA teachers, projector architectures, and radial-objective targets, broader gate participation accompanies better generation quality. Guided by this insight, we propose a simple teacher-free radial objective that promotes broader gate participation through feature-norm regularization, without pairwise feature comparisons. On ImageNet $256\times256$ with SiT-B/2, our method improves FID over dispersive loss while increasing mean gate participation over timesteps and classes, further supporting the link between gate organization and training acceleration. Our results identify residual-gate reorganization as a measurable axis of diffusion training acceleration and suggest a simple direction for further acceleration.
