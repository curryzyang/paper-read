# Hilbert-Scale Stability of Posterior Diffusion Priors for Ill-Posed Signal Recovery

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Bahman Moraffah, Raha Moraffah
- 机构：Worcester Polytechnic Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27030v1) · [PDF](https://arxiv.org/pdf/2610.27030v1)

## TLDR
The paper develops a Hilbert-scale stability theory for posterior diffusion priors in smoothing linear inverse problems, deriving non-asymptotic recovery bounds and a recoverable regularity threshold that determines when weak-norm score errors remain controlled and shows that operator-adapted posterior corrections improve stability.

## Abstract
Indirect and noisy observations are difficult to invert when the forward operator smooths out the unknown signal. In this case, the unstable modes are precisely the modes that the data reveals least, thus the success of any reconstruction method depends on how prior information interacts with the geometry of the operator across regularity scales. Diffusion priors have become ubiquitous for such problems; however, the current theory still does not determine when a learned score remains informative under ill-posed forward operators. In this paper, we study posterior diffusion for linear inverse problems on Hilbert scales and derive a stability theory under an explicit score-amplification condition. Under a smoothing condition on the forward map, a source condition on the truth, and weak-norm control of score error, we derive non-asymptotic recovery bounds in \(\Hs^s\) that separate observation noise, score approximation, and reverse-time discretization. These bounds give a recoverable regularity threshold determined jointly by operator smoothing, truth regularity, score regularity, and the posterior correction. The threshold specifies the Hilbert-scale norms \(\Hs^s\) in which weak-norm score error remains controlled after propagation through the posterior reverse dynamics. For larger regularity indices \(s\), the inverse geometry magnifies the same error, and the Hilbert-scale recovery estimate no longer gives uniform stability. We also prove that a posterior correction adapted to the forward operator improves stability relative to isotropic guidance in the regularity ranges where the smoothing action of the forward map matters most. The recovery estimates give a regularity-sensitive theory of posterior diffusion and show how learned score error, operator smoothing, and reconstruction norm jointly determine the stable range predicted by the analysis.
