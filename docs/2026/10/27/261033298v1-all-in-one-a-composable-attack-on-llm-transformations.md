# All-in-One: A Composable Attack on LLM Transformations

- 区域：速读区
- 排名：3
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Xiaohua Zhan, Kazuki Egashira, Robin Staab, Mark Vero, Martin Vechev
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33298v1) · [PDF](https://arxiv.org/pdf/2610.33298v1)

## TLDR
This paper introduces a composable attack framework that jointly trains an LLM to remain benign before deployment but become malicious when any of several common transformations (such as quantization, pruning, or merging) is applied, by approximating each transformation as a weight perturbation during training.

## Abstract
Quantization, pruning, and model merging are popular transformations applied to deployment-ready LLMs to improve efficiency and downstream performance. Recent work has shown that these transformations can introduce a security threat: an adversary can train a model that passes safety checks in its pre-transformed state, only turning malicious once it is transformed for deployment. However, prior attacks target one specific transformation (e.g., quantization) and generally rely on transformation-specific techniques, making them difficult to combine in practice. In this work, we introduce a simple, composable attack framework that targets multiple transformations simultaneously and triggers when any one of them is applied by a user. Our key insight is that the effect of each transformation can be approximated as a perturbation to the model weights, allowing us to jointly train the model with a benign loss on the original model and a malicious loss on each simulated transformed model. These perturbations are simple enough to simulate at every training iteration across diverse transformations, making them practically combinable within a single training objective, enabling a unified attack. Through extensive experiments across attack scenarios, model families, and a wide range of deployment-time model transformations, we show that our attack achieves high success rates. This demonstrates that model transformations may be utilized to trigger significantly different behavior from the original model and reinforces the associated security concerns by demonstrating that a single attack can jointly target diverse transformations.
