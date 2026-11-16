# Alignment with Reflect-Reasoning: Learning How To Follow Principles

- 区域：速读区
- 排名：4
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Henry Bell, Caroline Zhang, Dhaval Potdar, Mohammed Mobasserul Haque, Brandon Fain
- 机构：Duke University, Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17398v1) · [PDF](https://arxiv.org/pdf/2611.17398v1)

## TLDR
**TLDR:** Reflect-Reasoning is a training method that teaches LLMs how to reason about and revise responses according to arbitrary in-context alignment principles—rather than hardcoding specific principles—enabling better conformance to novel and out-of-distribution constitutions, fewer serious violations, and maintained safety without additional fine-tuning.

## Abstract
The appropriate governing norms and principles for the alignment of Large Language Models (LLMs) often depend on cultural context and deployment application. However, most alignment techniques focus on training models to conform to human preferences or constitutional principles specified at training time and subsequently fixed. In practice, many deployers rely on system prompting to implement contextual norms and guardrails at inference time. Prior work has shown that post-generation reflective reasoning with critique and revision can improve conformance compared to simple system prompting, but such methods are limited to the reasoning abilities inherent in the trained model. We introduce Reflect-Reasoning, a training method that teaches models how to reason about alignment to principles, rather than simply which principles to follow. Across five models, Reflect-Reasoning consistently outperforms both system prompting and explicit prompting strategies for in-context reflective reasoning. These improvements extend and generalize to entirely out-of-distribution domains of medical and financial principles. We additionally demonstrate that Reflect-Reasoning reduces the occurrence of rare but serious principle violations. Finally, we show that Reflect-Reasoning does not erode the safety engineering of a model and is robust against jailbreaking attempts using adversarial constitutions. Overall, our results demonstrate that Reflect-Reasoning is a scalable method for training constitutional alignment as a generalizable reasoning capability, enabling models to adapt to novel principles and produce transparent reasoning traces without additional fine-tuning.
