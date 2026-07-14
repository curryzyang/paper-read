# What Context Does a Coding Agent Actually Need to Act?

- 区域：速读区
- 排名：13
- 匹配度：1.7/10
- 来源：arxiv
- 作者：Brian Sam-Bodden
- 机构：Integrallis Software
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09691v1) · [PDF](https://arxiv.org/pdf/2607.09691v1)

## TLDR
TLDR: Coding agents need surprisingly little context to edit code—source code itself is essential, while natural-language summaries and surrounding structure add almost no value, and compressed context matches whole files at a third of the tokens.

## Abstract
A modern coding agent can hold an entire repository in its context window. Most of its reading is wasted -- and the interesting question is not how much context an agent can use, but what it actually \emph{needs}. We study that question at the moment it matters most: when the agent must \emph{edit} code. Separating \emph{finding} the work site from \emph{acting} on it, we hold localization fixed with an oracle, vary only how the code is represented, and score context against real issue resolution on SWE-bench Verified. The answer is starkly minimal. The signal lives in the code being edited itself: natural-language summaries of it answer almost none of the behavioral questions that the source answers ($4/45$ vs.\ $27/45$, held-out repositories, independent judge), and the gap belongs to the representation, not the summarizer -- a frontier model's summaries score exactly as poorly as a 3B model's. The surrounding context hardly matters either: across every multi-file instance in Verified, under a protocol frozen before any data, rendering a file's remainder as UML skeletons and signatures resolves no more issues than deleting that remainder outright ($N{=}70$, exact McNemar $p{=}0.75$). That was our registered hypothesis, and it failed. Compressed context, meanwhile, matches whole files at a third of the tokens: a resolved issue costs $19$K context tokens, not $94$K. The instrument also yielded a finding the field should keep: temperature-0 API inference flips ${\sim}9\%$ of per-instance outcomes between byte-identical runs. That is a noise floor under every small effect reported on this benchmark, including ours. We release the instrument -- gold-validated environments, per-instance proof that every reference edit is expressible from every arm's context, deterministic patch construction, and pre-registered hypotheses whose nulls we publish.
