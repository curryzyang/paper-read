# Counterfactual Predictions in Scientific Emulators Without Controlled Experiments

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Dingling Yao, Kahaan Gandhi, Valentin Duruisseaux, Boris Bonev, Francesco Locatello, Anima Anandkumar
- 机构：Institute of Science and Technology Austria, NVIDIA, California Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02252v1) · [PDF](https://arxiv.org/pdf/2610.02252v1)

## TLDR
ReRoute enables targeted counterfactual what-if predictions from scientific emulators without controlled experiments by fixing the queried input to a reference value, reintroducing its variation through a known mechanistic pathway, and fine-tuning on factual data, improving climate emulation under distribution shift.

## Abstract
Many scientific questions require reasoning about what was never observed: What if the conditions, interventions, or history had been different? Models can predict accurately on observed data yet fail on such what-if queries when correlated inputs are varied independently. A common remedy is to add controlled simulation data in which these factors are explicitly disentangled, but this requires access to a simulator, can be computationally expensive, and inherits the simulator's modeling assumptions. We introduce ReRoute, a framework for targeted scientific what-if prediction that combines factual data with partial mechanistic knowledge, without requiring controlled intervention data for adaptation. ReRoute fixes the queried input of a pretrained backbone to a reference value, reintroduces its variation through a known mechanistic pathway, and fine-tunes on the original factual data, while leaving downstream effects to the learned dynamics. We provide a causal identification result for this construction under explicit structural assumptions, with the core argument machine-checked in Lean. After showing that ReRoute achieves highly accurate counterfactual predictions in a controlled advection-diffusion system where exact responses are available, we turn to state-of-the-art climate emulation. On held-out coupled-climate interventions, ReRoute reduces aggregate climate error by 18.2-31.8% under severe CO$_2$ distribution shifts while preserving skill under standard conditions, at a small fraction of the cost of retraining on additional controlled simulations, without even accounting for the substantial expense of generating such data. Finally, on an emulator trained from historical ERA5 reanalysis, where no counterfactual reference exists, ReRoute preserves substantially more of the surface warming implied by the observed boundary conditions under a fixed-CO$_2$ counterfactual.
