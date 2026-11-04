# Probabilistic Steering of Generative Priors for Lab-in-the-Loop Antibody Optimization

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Anisha Parsan, Sebastian Ober, Calvin McCarter, Nick Bhattacharya, Hunter Elliott
- 机构：Massachusetts Institute of Technology, BigHat Biosciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03844v1) · [PDF](https://arxiv.org/pdf/2611.03844v1)

## TLDR
The paper introduces CHAD, which unifies de novo antibody discovery and iterative optimization by steering a frozen structure-based generative prior at inference time with a probabilistic surrogate acquisition reward, using posterior uncertainty to smoothly hand off from prior-driven exploration to lab-data-driven exploitation and thereby improving low-N optimization efficiency and molecular diversity.

## Abstract
Therapeutic antibody development is often framed as comprising two discrete stages: initial discovery of novel binders followed by iterative optimization to refine these hits into therapeutic-grade molecules. Models and methods often reflect these stages, with generative structure models applied to discovery and probabilistic black-box optimization methods applied to refinement. Here we propose to unify these stages by smoothly transitioning a generative discovery model into iterative optimization, allowing the handoff between the structure-based prior and supervision from wet lab data to be guided by the posterior uncertainty of a probabilistic surrogate. We show that this yields improvements in optimization efficiency in the low-N regime, as well as improved diversity amongst the optimized molecules.
