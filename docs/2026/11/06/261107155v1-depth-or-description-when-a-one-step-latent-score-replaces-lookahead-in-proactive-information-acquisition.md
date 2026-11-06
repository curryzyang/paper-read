# Depth or Description? When a One-Step Latent Score Replaces Lookahead in Proactive Information Acquisition

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Biswa Sengupta
- 机构：JPMorgan Chase & Co.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07155v1) · [PDF](https://arxiv.org/pdf/2611.07155v1)

## TLDR
A cheap one-step score on a suitably chosen, small latent cause can replace most expensive lookahead in proactive information acquisition when that latent encodes the decision, but it must be validated against exact lookahead because how the hidden cause is described determines whether the shortcut works.

## Abstract
A proactive agent must decide what to ask before it acts. Exact lookahead values combinations of questions but is expensive and leans on a fitted model; a one-step score is cheap but can miss them. Our main finding: the need for depth often lies in how the hidden cause is described. A one-step score on the label can be blind to an interaction among answers. A score on a suitable latent cause is not, and where that latent encodes the decision it replaces most of depth at a fraction of the search. Described differently, the same problem can defeat the score while exact values do not move, so keep the latent small and check it against exact values. Probabilities learned from one language model's answers do not carry to another unless planning allows for both; those read from tokens are worth only a few labels.
