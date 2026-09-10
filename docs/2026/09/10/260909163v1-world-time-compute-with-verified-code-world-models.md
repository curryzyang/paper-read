# World-Time Compute with Verified Code World Models

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：James Schwoebel, Ingrida Semenec, Jenia Rousseva, Marcos Ortiz, Collin Overbay, Christopher Klaus, Anderson Edmond, Manish Bhatt, Rome Thorstenson, Jessica Tsai, Martin G. Frasch
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09163v1) · [PDF](https://arxiv.org/pdf/2609.09163v1)

## TLDR
Fine-tuning LLMs on trajectories from many independently verified code-based world models—dubbed world-time compute—drives generalization to held-out symbolic worlds mainly through exact labels rather than task variety, with large gains for small or weak models and saturation at scale.

## Abstract
LLMs generalize across a domain only after seeing many real, labeled examples, which most domains lack. We study a way to manufacture it cheaply. When a domain's dynamics can be written as code, one template instantiates into many world models: executable, verifiable programs over symbolic state, each an inexhaustible source of exactly-labeled trajectories. Fine-tuning an LLM on trajectories through many such worlds, which we call world-time compute, a training-time analogue of test-time compute, lifts generalization to held-out worlds it never trained on (synthesized world families). Gains are largest where capability is scarcest: +29 points at 0.5B; the largest model's lift is within noise, consistent with saturation. Labels can be trusted because the worlds are verified code: synthesized-then-checked dynamics are exact over 20-step rollouts and answer 10x out-of-distribution probes exactly (100%), whereas per-step LLM and MLP predictors compound error and collapse. Unlike domain randomization, each world is independently authored and verified; a corrupted-label control shows label exactness, not task variety, drives the gains. On real benchmarks (ARC-AGI grids, List Functions, CLRS) the same lever holds as per-world test-time training. On List Functions the harder cross-world form holds: one adapter trained on 128 disjoint worlds reaches 40% on held-out worlds versus 6% for a corrupted-label control (+34 points, CI [29, 39]). The gain is a saturating regularity, not a law: largest for few-step reasoning and small/weak models, fading for long chains, perception-induced tasks, and saturated tasks; cross-task transfer is weak without shared skill. Worlds are authored and served by OpenWorld, a zero-dependency framework (companion paper). Scope: symbolic state; pixel-native domains remain territory of learned models. All code, recipes, and this manuscript regenerate from one repository.
