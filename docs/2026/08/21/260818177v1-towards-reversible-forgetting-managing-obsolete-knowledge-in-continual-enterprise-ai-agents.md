# Towards Reversible Forgetting: Managing Obsolete Knowledge in Continual Enterprise AI Agents

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Nilutpaul Sarker Yash, Tirtho Roy, Ushashi Bhattacharjee
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18177v1) · [PDF](https://arxiv.org/pdf/2608.18177v1)

## TLDR
Enterprise AI agents should reversibly suppress obsolete knowledge—rather than indiscriminately retaining or erasing it—using a Hysteretic Reversible Memory Controller with auditable memory states, hysteresis, shadow-tested reactivation, and policy-gated retirement to manage knowledge lifecycles in non-stationary environments.

## Abstract
Continual learning has traditionally treated forgetting as a failure, emphasizing preservation of previously acquired knowledge as environments evolve. We argue that this objective is incomplete for enterprise AI agents operating in non-stationary environments, where customers, policies, tools, workflows, regulations, and market conditions change over time. Indiscriminate retention can allow obsolete knowledge to influence decisions, creating negative transfer and operational risk. We therefore propose reversible forgetting: a conceptual framework with three operational memory states: active, dormant, and retired, and a reactivation transition that can restore dormant knowledge when its relevance returns. We instantiate the framework as a Hysteretic Reversible Memory Controller that accumulates relevance evidence, uses asymmetric thresholds to prevent state oscillation, tests reactivation in shadow mode, and gates retirement through policy. The framework reduces the influence of obsolete information without conflating temporary suppression with permanent erasure. Finance illustrates the idea: knowledge useful under one market regime may become harmful under another yet regain relevance when similar conditions recur.
