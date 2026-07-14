# Safe responses matter: Output-aware safety guardrail mitigate over-refusal in MLLMs

- 区域：速读区
- 排名：1
- 匹配度：2.3/10
- 来源：arxiv
- 作者：Jiayi Li, Kun Zhan
- 机构：Lanzhou University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09697v1) · [PDF](https://arxiv.org/pdf/2607.09697v1)

## TLDR
The paper proposes OutGuard, a novel output-aware safety guardrail for multimodal large language models that predicts unsafe outputs from hidden states using a lightweight multi-instance contrastive learning classifier, significantly reducing over-refusal while maintaining strong safety performance.

## Abstract
Existing safety mechanisms for multimodal large language models (MLLMs) face a fundamental trade-off between safety and utility. Model fine-tuning achieves robust safety but compromises general utility. Input-side safety guardrails offer a lightweight alternative, yet they suffer from severe over-refusal, indiscriminately blocking benign queries or those the model could have safely answered through refusal or advisory responses. We identify that the root cause of over-refusal lies in the input-aware paradigm: safety guardrails make safety decisions without considering whether the model itself is capable of generating safe responses. Usually, MLLMs already possess intrinsic safety mechanisms that can transform harmful inputs into harmless outputs, but input-side safety guardrails override this capability, degrading user experience. Motivated by this insight, we propose a paradigm shift toward output-aware safety guardrails. Our method operates within the model's hidden state space to predict whether the forthcoming generation will be unsafe before it is fully produced. By training a lightweight classifier via multi-instance contrastive learning on hidden state representations, our approach distinguishes between inputs that will lead to unsafe outputs and those that will not, even when the inputs themselves contain risky elements. This enables precise intervention only when the model's actual response would be harmful. Extensive experiments demonstrate that our output-aware safety guardrail matches the safety performance of existing methods while drastically reducing over-refusal, preserving the model's utility and built-in safety capabilities. Code is available at: https://github.com/kunzhan/OutGuard
