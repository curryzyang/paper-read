# Vision-Language Grounded Task-Context-Aware Imitation Learning for Robotic Disassembly

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jeon Ho Kang, Igal Tamarkin, Ethan Niu, Ian Novales, Satyandra K. Gupta
- 机构：University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17714v1) · [PDF](https://arxiv.org/pdf/2609.17714v1)

## TLDR
This paper proposes a vision-language grounded, task-context-aware imitation learning framework that uses a VLM for hierarchical task selection and counterfactual language-object grounding to enable long-horizon robotic disassembly across diverse unseen configurations, improving end-to-end task success by 35 percentage points over a diffusion-policy baseline and 75 percentage points over a prior task-context-aware baseline.

## Abstract
Real-world robotic disassembly requires long-horizon execution, where robots must perform ordered sequences of manipulation tasks across multiple parts within a single scene. Multiple valid task goals and diverse assembly configurations make it difficult for imitation policies to infer the intended skill from raw observations alone, particularly when training data cannot cover the combinatorial diversity of real-world configurations and part geometries. We show that incorporating task context through language alleviates these challenges by providing explicit structure for skill selection and associating language-specified tasks with their corresponding manipulation targets in the visual scene. The proposed framework combines hierarchical task selection with task-context-aware imitation learning to ground language instructions in spatial visual representations for robotic disassembly. The resulting framework generalizes across diverse connector geometries and assembly configurations without requiring explicit object annotations. Our method improves end-to-end task success by 35 percentage points over the baseline diffusion policy and by 75 percentage points over the previous task-context-aware baseline.
