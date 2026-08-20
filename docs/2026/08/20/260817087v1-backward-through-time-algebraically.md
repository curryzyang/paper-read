# Backward through Time, Algebraically

- 区域：速读区
- 排名：2
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Konstantinos Kogkalidis
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17087v1) · [PDF](https://arxiv.org/pdf/2608.17087v1)

## TLDR
This paper presents an algebra-generic, differentiable evaluation engine for linear temporal logic over soft (e.g., neural) traces, showing that different semantic algebras correspond to different choices of how and in which direction to “disappoint,” and implements it as the PyTorch library `telos`.

## Abstract
Linear temporal logic is a modal extension of propositional logic that allows one to state how a system should behave over time. Its canonical domain is the booleans, but discretely-valued judgements are of little use in steering softly-valued systems (neural policies, adaptive controllers, sequence models, etc). In such cases, the goal formula's (dis)satisfaction becomes a training signal, and differentiability becomes a prime concern. Candidate differentiable semantics abound, but navigating them is tricky. Implementations, where available, are shallow embeddings, demanding an upfront commitment to a single semantic algebra and its (usually implicit) conduct. The paper casts the reader as a functional programmer asked to come to terms with this predicament, and refusing. Out of that refusal comes an evaluation engine that is algebra-generic and amenable to differentiation, together with an executable specification of the algebras it can accept. Various algebras are implemented and audited for their behavior, both forward and backward. Each algebra turns out to be a choice of which direction to disappoint, and how. Everything described (and more) is part of the PyTorch library telos, to be found at https://github.com/konstantinosKokos/telos.
