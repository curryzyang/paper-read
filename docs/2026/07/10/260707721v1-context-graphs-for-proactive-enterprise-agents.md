# Context Graphs for Proactive Enterprise Agents

- 区域：速读区
- 排名：8
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Avinash Kumar
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07721v1) · [PDF](https://arxiv.org/pdf/2607.07721v1)

## TLDR
The paper introduces Context Graphs as a live relational data structure for enterprise entities, enabling proactive agents that detect state changes, rank insights by urgency and relevance, and deliver actionable notifications before human queries, as demonstrated by evaluations showing improved Precision@5 and a reduction in mean time to surface from 47 minutes to under 30 seconds.

## Abstract
Retrieval-Augmented Generation (RAG) and agentic frameworks have advanced enterprise AI considerably, yet agents remain fundamentally reactive: they wait for a human query before acting. This paper argues that genuine enterprise productivity gains require proactive agents: systems that surface relevant, actionable information to workers before they ask. We propose the Context Graph, a live relational data structure that models enterprise entities, their relationships, and state transitions over time. Built on this graph, we define a Delta Detection Engine that continuously monitors state changes, a Proactivity Scorer that ranks candidate insights by urgency, relevance, and persona-fit, and a Surfacing Layer powered by an LLM that delivers ranked notifications with grounded explanations. We formalize each component, derive a unified Proactivity Score function, and provide a complete end-to-end Python implementation using NetworkX and the Anthropic Claude API. Evaluation across three generic enterprise case studies (contract lifecycle management, engineering incident response, and sales pipeline hygiene) demonstrates that context-graph-driven proactivity achieves Precision@5 of 0.83, a false positive rate of 0.11, and reduces mean time to surface from 47 minutes (reactive baseline) to under 30 second.
