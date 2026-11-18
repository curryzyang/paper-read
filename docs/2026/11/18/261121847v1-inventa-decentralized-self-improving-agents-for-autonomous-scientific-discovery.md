# Inventa: Decentralized Self-Improving Agents for Autonomous Scientific Discovery

- 区域：速读区
- 排名：9
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Prithwish Jana, Nikos Kanakaris, Purak Jain, Anoop Deoras, Sahika Genc
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21847v1) · [PDF](https://arxiv.org/pdf/2611.21847v1)

## TLDR
Inventa is a decentralized automated scientific-discovery framework in which autonomous research units evolve candidate ideas, locally adapt or restart stalled searches, and share only verified improvements and constraint violations, yielding more novel, feasible ideas and state-of-the-art results across five benchmarks with far fewer model calls.

## Abstract
Large language model (LLM) agents can generate research ideas and improve scientific discovery through iterative experimentation. However, increasing the number of agents or iterations does not automatically translate to producing more diverse or feasible ideas. Agents may converge on similar candidates, propagate unsupported claims through shared memory components and repeatedly apply search strategies that no longer yield any improvements.
  We introduce Inventa, a framework for automated scientific discovery that employs autonomous research units and verified shared knowledge. Each unit creates a lineage of candidate ideas using a mutator agent. A local orchestrator agent periodically adapts the mutator's harness. When progress stalls, the orchestrator agent replaces its model or restarts the idea evolution process. Verifiers evaluate each candidate idea and record verified improvements, useful components and constraint violations in a shared knowledge, the only channel between units. We evaluate Inventa on five benchmarks spanning the research cycle, covering retrieval (ScholarCatalyst), ideation (IdeaBench), proposal writing (IdeaScientist), and scientific law discovery (EurekaBench, SciLaws-Bench). It leads all five, achieving 73.6% on EurekaBench versus 56.2% for CORAL. On IdeaBench, it discovers 26.0 novel ideas per paper, compared with 18.6 for ResearchAgent, with 82% fewer model calls.
