# Perfect Reconstruction Cannot Show Whether Two Codebooks on a VAE's Latent Space Agree

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Yusuke Hayashi
- 机构：AI Alignment Network, Humanity Brain, Artificial Life Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14012v1) · [PDF](https://arxiv.org/pdf/2610.14012v1)

## TLDR
The paper proves that perfect reconstruction and standard VAE training reports cannot determine whether a VAE’s written and read discrete latent codes agree, but shows the ELBO’s variational gap and rate can bound or certify that agreement, yielding a Certify-or-Measure protocol.

## Abstract
Many systems read the latent space of a variational autoencoder (VAE) as discrete codes, and rely on each latent being read back as the code it was written as. Shannon (1948) took such a shared codebook as given; inside a VAE nothing enforces it. We prove that no item of a standard training report can reveal whether the written and read codes agree on encoded data. We construct two VAEs that reconstruct every input perfectly, infer exactly, and match on every per-example ELBO and every code histogram, yet agreement is one in the first and zero in the second. We then show that the ELBO's own terms bound how far a measured agreement can move: the variational gap bounds the shift to exact inference, and the rate bounds the shift to generation from the prior. For Gaussian posteriors, a mean-field encoder pays an exact price in the gap that depends on its choice of axes. On probabilistic PCA the gap certifies a trained encoder in all 75 settings we test, at agreement between 0.76 and 0.97. On 240 trained VAEs, a floor set by the rate and the dataset size rules out rate-side certification in advance for 66 models, and none of them certifies. The results yield a simple protocol, Certify-or-Measure, for any pipeline that reads a VAE as codes.
