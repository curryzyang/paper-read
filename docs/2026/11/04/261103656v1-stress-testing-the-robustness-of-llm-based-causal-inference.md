# Stress-Testing the Robustness of LLM-Based Causal Inference

- 区域：速读区
- 排名：3
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ankitkumar Patel, Jigarkumar Patel, Amit Kumar, Supreetha Sreeram, Venkatesh Kulkarni
- 机构：Texas A&M University--Corpus Christi, Pondicherry University, IntelliQuest Venture, University of Texas at Dallas, IIT - Guwahati
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03656v1) · [PDF](https://arxiv.org/pdf/2611.03656v1)

## TLDR
This paper systematically stress-tests LLM-based causal discovery across six dimensions and finds that LLMs overestimate causal links, that conventional metrics can be misleading unless evaluated with a proposed uncertainty-aware framework, and that scaling gains are fragile under declining metadata quality.

## Abstract
Why do some of the world's most powerful Artificial Intelligence (AI) systems still struggle to reason about cause and effect? Causal discovery, the ability to discern the underlying drivers of a system, is fundamental to scientific inquiry and has traditionally relied on structured data and statistical methods. Recently, Large Language Models (LLMs) have been explored as an alternative paradigm for causal inference, leveraging their broad knowledge and reasoning capabilities. Yet, despite their linguistic fluency, LLMs often rely on surface-level pattern recognition rather than genuine causal logic. While it is known that LLMs stumble in this domain, we lack a precise map of where, why, and how significantly these failures occur. In this paper, we propose a systematic stress-test framework across six critical dimensions: model scale, causal graph complexity, prompting strategy, metadata quality, data quality, and sensitivity to uncertainty. Our findings reveal a significant "optimism bias" in LLMs; models consistently overestimate causal links, leading to low precision across the board. Furthermore, we demonstrate that traditional evaluation metrics can be deceptive: while reasoning-heavy models lead in performance, the highest scores often occur when uncertainty in inference is overlooked. Once uncertainty is integrated into the evaluation, performance drops, providing a more honest reflection of causal reliability. We also find that, while scaling model size improves outcomes, these gains are fragile; performance degrades sharply as the quality of metadata decreases. This work serves as a practical guide to the blind spots of LLMs, offering a clear-eyed assessment of when these tools can be integrated into a causal discovery pipeline and when they are likely to lead researchers astray.
