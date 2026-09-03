# Prompt-Space Meta-Learning Does Not Transfer Across Users: A Frozen-LLM Negative Result

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Liam Byrne, David Dylan, Orla Fitzgerald, Eoin Doyle, Ciara Nolan, Padraig Lynch, Sinead Gallagher
- 机构：University College Dublin, Trinity College Dublin, Dublin City University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.01615v1) · [PDF](https://arxiv.org/pdf/2609.01615v1)

## TLDR
Prompt-space meta-learning for frozen-LLM user personalization does not transfer across users, because the meta-validation objective is blind to genuine user-support correspondence ("meta-objective collapse"), yielding no improvement over seed prompts or structure-broken controls.

## Abstract
Personalizing a frozen large language model (LLM) to individual users is often framed as a meta-learning problem in prompt space: each user is a task, and one seeks a shared natural-language adaptation policy that, given a handful of the user's labeled interactions, configures the frozen model for that user. The framing is attractive because it is backbone-agnostic and reuses the machinery of prompt optimization, yet the field rarely tests whether the optimized meta-objective encodes transferable cross-user adaptation rather than generic instruction quality. We study this question with Muse (Meta-learned User-adaptation via Shared Evolution), which evolves a single shared adaptation prompt over a meta-train user population by reflective prompt evolution, freezes it, and applies it zero-shot to held-out users; matched controls isolate learning from confounds of phrasing and selection. On two standard personalization benchmarks (LaMP-2 categorization and LaMP-3 rating) over 200 held-out users each, Muse does not significantly improve on its own un-evolved seed prompt or on a structure-broken control that meta-trains on mismatched user-support pairs, and is dominated by plain few-shot retrieval on the rating task (Delta MAE +0.175, p < 0.001). We attribute these outcomes to a single mechanism, meta-objective collapse: the meta-validation objective is statistically invariant to whether the user-support correspondence is genuine (p=0.555 on LaMP-2, p=0.622 on LaMP-3), so it cannot be optimized into transferable adaptation and instead rewards instruction polish and validation overfitting. The seed-prompt, wrong-support, and invariance-oracle controls form a reusable protocol that separates learned adaptation from these confounds.
