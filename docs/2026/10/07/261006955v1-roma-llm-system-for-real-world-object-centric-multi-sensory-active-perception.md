# ROMA: LLM System for Real-World Object-Centric Multi-Sensory Active Perception

- 区域：速读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Ruoxuan Feng, Yutong Chen, Ruihua Song, Huan Yang, Zhongyuan Wang, Guocai Yao, Di Hu
- 机构：Beijing Jiaotong University, Renmin University of China, Beijing Academy of Artificial Intelligence, Beijing Key Laboratory of Research on Large Models and Intelligent Governance, AresoX, Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06955v1) · [PDF](https://arxiv.org/pdf/2610.06955v1)

## TLDR
ROMA is an LLM-based system that integrates vision, audio, tactile, and force sensing into a reasoning–interaction–feedback loop to actively acquire missing multi-sensory evidence in the real world, supported by the ROMI-2K dataset and ROMA Bench, enabling complex long-horizon object-centric active perception.

## Abstract
Humans inherently understand the physical world through an active process. When sensory evidence is insufficient to infer physical properties, we naturally interact with the environment by deciding what information is missing, how to acquire it, and when sufficient evidence has been obtained. In stark contrast, existing multi-sensory robot systems mainly integrate sensory inputs rather than actively acquiring missing evidence through interactions. In this work, we introduce ROMA, an LLM-based system for Real-World Object-Centric Multi-Sensory Active Perception. ROMA integrates vision, audio, tactile, and force sensing into a reasoning-interaction-feedback loop. The model identifies missing evidence and determines the target objects, interactions, and modalities, while a physical interface executes the selected interactions and collects the multi-sensory feedback. To support this capability, we construct ROMI-2K, a large-scale real-world multi-sensory object interaction dataset covering nearly 2,000 objects and 6 atomic interactions with synchronized sensory feedback. Building on these data, we develop a two-stage training framework that aligns sensory modalities and equips the LLM to assess evidence sufficiency, select informative interactions, and reason over the multi-sensory feedback. We further characterize active perception as perception chains, where acquired evidence guides subsequent interactions and reasoning, and establish ROMA Bench to evaluate single-attribute, long-horizon multi-attribute, and intent-driven active perception. Experiments show that ROMA can actively acquire missing evidence and solve complex, long-chain multi-sensory perception tasks that existing methods struggle to handle, laying a strong perceptual foundation for active multi-sensory embodied agents.
