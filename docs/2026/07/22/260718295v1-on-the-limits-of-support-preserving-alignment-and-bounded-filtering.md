# On the Limits of Support-Preserving Alignment and Bounded Filtering

- 区域：速读区
- 排名：4
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Aryan Dutt, Rui Mao, Anupam Chattopadhyay
- 机构：Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18295v1) · [PDF](https://arxiv.org/pdf/2607.18295v1)

## TLDR
This paper shows that even with sophisticated alignment methods and computationally bounded safety filters, harmful outputs from large language models cannot be fully eliminated, consistently plateauing above zero across various models and filter types.

## Abstract
We study whether alignment schemes that reshape a base model's output distribution, combined with bounded safety filters, can drive the probability of harmful behavior to zero in modern large language models. Recent research suggests that harmful behaviors can persist under preference-based alignment and that external filtering can be computationally hard in the worst case, but it remains unclear whether practical alignment pipelines that largely preserve internal representations can eliminate harmful behavior entirely rather than merely suppressing its most visible forms. We formalize this setting using support-preserving alignment operators together with bounded filtering algorithms under black-box, white-box, and statistical-query access, and analyze their ability to approximate an ideal eliminator that removes all harmful mass. Building on this framework, we provide computational and information-theoretic arguments indicating that, under these constraints, bounded filtering may fail to eliminate all harmful outputs supported by the base model's distribution. To evaluate these limits empirically, we analyze a range of state-of-the-art open-weight and hosted LLMs accessed via OpenRouter under bounded black-box, white-box, and statistical-query filters on adversarial prompts drawn from curated cybersecurity scenarios and PKU-SafeRLHF. Across models, filter classes, and query budgets, the estimated harmful-output rate decreases with additional filtering compute but consistently plateaus above zero, suggesting a persistent empirical harm floor.
