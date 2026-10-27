# Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill Adaptation

- 区域：速读区
- 排名：6
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Zhihao Yang, Haojin Wang, Juncheng Wu, Kuan Zhang, Yukun Chen, Run Luo, Yaojie Lu, Yuyin Zhou, Lu Wang, Xianpei Han
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33024v1) · [PDF](https://arxiv.org/pdf/2610.33024v1)

## TLDR
This paper shows that harness skills benefit models unevenly and introduces a meta-skill-guided skill adaptation method that reformulates guidance to match an executor’s capabilities, improving weak-model performance and final scores within harness self-evolution.

## Abstract
Harness self-evolution offers a practical route for LLM agents to improve from execution experience without updating model parameters. Its effectiveness depends on whether models can successfully act on the guidance provided by their harnesses. However, we find that harness benefits are not uniform across model capabilities: skills that improve stronger models can provide little benefit or even degrade performance for weaker ones. Across seven models and three benchmarks, we identify 103 task-skill pairs where skills improve GPT-5.6-luna by 31.1 points but degrade Gemma-4-E4B by 8.8 points. In 86% of failed weak-model runs, the violated requirement is already stated in the skill. This motivates skill adaptation: reformulating existing skills to match the executor's capabilities and make their guidance easier to execute. To achieve this, we diagnose failures in tool execution, context management, instruction following, and verification, and distill these diagnoses into a fixed meta-skill that guides adaptation during harness self-evolution. Guided by the meta-skill, a capable external rewriter, Kimi-K3, adapts skills without execution evidence, improving the three weak executors by 5.1-14.1 points over the original skills. We then incorporate this adaptation into a five-round self-evolution loop, where each model revises its own skill from execution trajectories and verifier feedback. Across seven executors, from Gemma-4-E4B to Kimi-K2.5, the meta-skill consistently improves final scores by 2.0-5.1 points over the same loop without the meta-skill. Our findings provide practical design guidance for developing more effective harness self-evolution methods.
