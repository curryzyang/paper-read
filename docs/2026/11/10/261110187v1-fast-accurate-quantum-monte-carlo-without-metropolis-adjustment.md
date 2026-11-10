# Fast Accurate Quantum Monte Carlo without Metropolis Adjustment

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Reuben Cohn-Gordon, Gabriel Pescia, Sumner N. Hearth, Jakob Robnik, Uroš Seljak, Peter Lunts
- 机构：Institute for Advanced Study, Episteme, UC Berkeley, Los Alamos National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.10187v1) · [PDF](https://arxiv.org/pdf/2611.10187v1)

## TLDR
Using unadjusted Hamiltonian Monte Carlo without the Metropolis–Hastings correction on a high-dimensional spin-fermion quantum Monte Carlo model yields order-of-magnitude higher sampling efficiency than adjusted HMC while maintaining accurate results with controlled asymptotic bias.

## Abstract
In quantum systems, physical quantities of interest can be expressed as expectation values of a probability distribution, which allows their estimation by Markov Chain Monte Carlo (MCMC) methods. This approach, an instance of Quantum Monte Carlo (QMC), plays a central role in obtaining predictions of system properties relevant to condensed matter and high energy physics. The use of Hamiltonian dynamics to design a Markov kernel, known as Hybrid or Hamiltonian Monte Carlo (HMC), is widespread in quantum applications. In this context, it is standard to use an HMC kernel that is ``adjusted'' with the Metropolis-Hastings (MH) criterion, so that estimates of expectations converge to their true value in the limit of infinite sample size. However, recent work in computational statistics suggests that an \emph{unadjusted} HMC kernel can be significantly more efficient, while safely maintaining an asymptotic bias which is small relative to the error arising from the variance of the finite sample size. We adapt this approach to the QMC setting, focusing on a challenging and high-dimensional \emph{spin-fermion} model of a quantum phase transition. We find that unadjusted methods outperform adjusted HMC in terms of effective sample size per gradient call, while retaining accurate results.
