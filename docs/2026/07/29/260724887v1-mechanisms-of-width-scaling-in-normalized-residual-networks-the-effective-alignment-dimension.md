# Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jinhao Zhang, Zeyu Liu, Zicheng Yan, Yunquan Zhang, Guangming Tan, Fangming Liu, Daning Cheng
- 机构：Huazhong University of Science and Technology, Institute of Computing Technology, Chinese Academy of Sciences, University of Science and Technology of China, Beijing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24887v1) · [PDF](https://arxiv.org/pdf/2607.24887v1)

## TLDR
This paper introduces the effective alignment dimension, a measurable signal-noise quantity of activation gradients, to derive a finite-sample certificate for test-risk improvement in normalized residual networks, and empirically shows that wider models exhibit larger effective alignment dimensions and lower misalignment.

## Abstract
Existing theories of neural-network width characterize asymptotic limits, but provide limited guidance on whether an expansion direction identified from finite training data remains beneficial on unseen data. We study this problem for function-preserving residual expansion and introduce the effective alignment dimension, a measurable quantity describing the signal-noise geometry of activation gradients. By deriving the exact mean and variance of the inner product between independently estimated training and test gradients, we obtain a finite-sample upper bound on misalignment probability. The bound depends only on the effective alignment dimension and an effective sample size, requiring finite second moments and a nonzero population gradient, without covariance spectral assumptions or prescribed width-growth rates. We integrate this certificate into the train-test residual-expansion framework, yielding a high-probability condition for test-risk improvement. Experiments across width-controlled LLaMA-style Transformers, Pythia, and ResNet-20 show that wider models exhibit larger effective alignment dimensions and lower empirical misalignment. Direct residual interventions confirm that the alignment statistic predicts the sign and magnitude of held-out loss changes.
