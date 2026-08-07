# Quantum-Structured World Models (QSWMs) for Predictive Latent Dynamics

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Hailong Jiang, Emran Hossain, Feng Yu, Jianfeng Zhu, Guilin Zhang, Wulan Guo
- 机构：Kent State University, George Washington University, Youngstown State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.05371v1) · [PDF](https://arxiv.org/pdf/2608.05371v1)

## TLDR
TLDR: The paper introduces Quantum-Structured World Models (QSWMs), a quantum-inspired framework using complex-valued and density-matrix-like latent states for predictive world modeling, and shows that these structured representations offer useful local predictive inductive biases on elementary cellular automata while facing limitations in long-horizon rollouts and interpretability.

## Abstract
World models learn latent states that summarize interaction histories, evolve over time, and support prediction, simulation, or planning. Most existing world models represent these states using classical vectors, probability distributions, recurrent hidden states, or transformer activations. In this paper, we introduce Quantum-Structured World Models (QSWMs), a quantum-inspired framework for predictive world modeling with structured latent states, latent transition operators, and measurement-inspired decoding maps. We study whether mathematical structures inspired by quantum theory, such as complex-valued representations and density-matrix-like latents, provide useful inductive biases for world modeling. We establish three foundational properties: classical inclusion, predictive sufficiency, and structured compactness. We then instantiate complex-valued and density-matrix-like QSWM variants and evaluate them on elementary cellular automata against strong classical baselines. Results show promising local predictive potential for complex-valued QSWMs, while also revealing limitations in long-horizon rollout, density-matrix variants
