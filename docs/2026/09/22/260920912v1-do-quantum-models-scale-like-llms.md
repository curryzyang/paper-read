# Do Quantum Models Scale Like LLMs?

- 区域：速读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：David S. Berman, Ying-Jer Kao, Roger G. Melko, Alexander G. Stapleton
- 机构：Perimeter Institute for Theoretical Physics, Queen Mary University of London, National Taiwan University, University of Waterloo
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20912v1) · [PDF](https://arxiv.org/pdf/2609.20912v1)

## TLDR
Training an autoregressive transformer on Rydberg-atom measurement data reveals that neural scaling laws hold near a quantum critical point—where the data’s mutual-information structure most resembles natural language—but weaken away from criticality, suggesting scaling behavior is a property of the model–data pair rather than language or architecture alone.

## Abstract
In this work, we study the neural scaling laws of RydbergGPT, an autoregressive transformer model trained on qubit projective measurement data gathered from interacting Rydberg atom arrays. The quantum system is known to exhibit a finite-size remnant of a critical point as the laser detuning parameter is varied. We find that near the critical point the transformer loss as a function of training dataset size is well described by a power-law with a loss floor correction. However, away from criticality the quality of the power-law description is substantially reduced. We then compare the statistical structure of both Rydberg measurements and natural-language corpora using an entropy-normalised, finite sample corrected mutual information "two-point" function. We find that near-critical statistics of the two point functions are closest to those observed in natural-language, whilst other qubit configurations far from the critical point have two-point functions that decay more rapidly. This supports the hypothesis that multi-scale dependence contributes to stable neural scaling, and that scaling behaviour should be viewed as a property of the model-data pair.
