# When Routing Reveals Membership: Privacy Leakage from MoE Router Telemetry

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yixin Tan, Jiayang Liu, Lu Sun, Yuke Hu, Zheng Li, Rui Wen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10616v1) · [PDF](https://arxiv.org/pdf/2610.10616v1)

## TLDR
Router telemetry from Mixture-of-Experts language models leaks fine-tuning membership information, enabling a router-augmented membership inference attack that consistently improves detection across architectures, domains, and training setups.

## Abstract
Mixture-of-Experts (MoE) language models produce routing information during inference that may be logged or exposed for monitoring, debugging, load analysis, and safety auditing. Unlike ordinary model outputs, this telemetry reveals a view of the model's internal computation, raising a privacy question: can it reveal whether an example was used to fine-tune the deployed model? We introduce a router-augmented membership inference attack that combines conventional output-side signals with aggregated routing features and applies a membership classifier learned from independently fine-tuned shadow models to the target model. Across three MoE architectures and three data domains, router telemetry consistently improves membership inference over a strong output-signal ensemble, increasing TPR at 1\% FPR by 2.7--9.4 percentage points across all nine settings. The leakage persists across full fine-tuning, frozen-router training, LoRA, and instruction tuning, and remains observable with only discrete expert selections, restricted telemetry, or a single shadow model. Mechanistic analysis further shows that the leakage does not require router-specific memorization: fine-tuning introduces membership information into hidden representations, while the router exposes a projection of this signal even when its parameters are frozen. Perturbing the telemetry reduces this additional leakage only as its fidelity degrades. Our results show that router telemetry can turn an operational signal into an additional privacy surface for fine-tuned MoE models.
