# Geometry Is Not Robustness: A Trajectory-Level Study of PGD Evaluation

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Dhairysheel Durgule
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14594v1) · [PDF](https://arxiv.org/pdf/2608.14594v1)

## TLDR
Trajectory-level PGD diagnostics (loss evolution, gradient alignment, steps-to-failure) describe optimization geometry but do not independently measure adversarial robustness, with steps-to-failure best separating robustness regimes—thus they should serve only as complementary, context-dependent tools alongside standard robustness metrics.

## Abstract
Projected Gradient Descent (PGD) is widely used to evaluate adversarial robustness, typically via final adversarial accuracy, which does not capture model behaviour throughout the attack. Recent work proposes trajectory-level diagnostics, such as loss evolution, gradient alignment, and steps-to-failure, for deeper insight into adversarial optimisation dynamics. However, whether these diagnostics reliably indicate robustness strength remains unclear. We conduct a trajectory-level investigation of PGD attacks on convolutional neural networks trained on Fashion-MNIST. We compare clean-trained and adversarially-trained models across multiple robustness regimes, using rigorous 20-step PGD evaluations with random initialisation and multiple restarts for robustness measurement, and single-initialisation trajectory recording for diagnostics. We record full PGD trajectories across 3000 clean-correct samples per model and analyse loss evolution, gradient alignment, and failure timing across attack iterations. Our results reveal a clear robustness hierarchy across models; however, trajectory metrics do not contribute equally to its identification. Mean loss trajectories and gradient alignment patterns appear quantitatively similar across adversarially-trained models with substantially different robust accuracies. In contrast, steps-to-failure distributions provide a clearer separation of robustness regimes, directly reflecting functional resistance to adversarial perturbation. These findings indicate that trajectory-level diagnostics describe optimisation geometry but do not independently measure adversarial robustness. Their interpretability depends on robustness regime, attack strength, and multi-metric evaluation. Trajectory-level analysis should be a complementary diagnostic tool, interpreted in context, rather than a replacement for standard robustness measurements.
