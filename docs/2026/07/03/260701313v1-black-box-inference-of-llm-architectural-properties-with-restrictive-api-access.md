# Black-Box Inference of LLM Architectural Properties with Restrictive API Access

- 区域：精读区
- 排名：6
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Christopher Ellis, Shreyas Chaudhari, Mei-Yu Wang, Leighton Barnes, Giulia Fanti, José M. F. Moura
- 机构：Pittsburgh Supercomputing Center, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.01313v1) · [PDF](https://arxiv.org/pdf/2607.01313v1)

## TLDR
Even with restrictive APIs that only expose a single logit per token and no logit bias, NightVision successfully infers an LLM's hidden dimension (within 23% average relative error), depth, and parameter count using common-set prompting and timing side channels.

## Abstract
In practice, most commercial LLM providers do not publicly release details of underlying LLM architectures. However, prior work has shown that given limited API access to an LLM (namely, top-$k$ logits and/or a logit bias function), one can recover certain architectural details of an LLM, such as the hidden dimension of the feed-forward network. Perhaps in response to these results, most commercial LLM providers have restricted their APIs to expose only the single logit for each decoded token, and they no longer give users the ability to bias logits. We show that even under current restrictive APIs, several architectural parameters are still recoverable. We present NightVision, an attack that uses restrictive black-box API access to estimate the hidden dimension, depth, and parameter count of an LLM. Algorithmically, NightVision relies on a novel common set prompting technique in which multiple prompts expose log probabilities for the same set of output tokens; a spectral analysis of these results is used to infer hidden dimension. NightVision additionally uses end-to-end time to first token (TTFT) measurements and the estimated hidden dimension to estimate depth and parameter count. We empirically evaluate NightVision on 32 open-source LLMs, recovering hidden dimension to within 23% average relative error across all models (9% on MoE models), and depth and parameter count to within 53% for models exceeding three billion parameters. We run extensive ablations to demonstrate how these accuracies scale with token budget and model properties. Overall, our results suggest that current LLM APIs are not sufficiently restricted to fully obfuscate the architectural details of their underlying models.
