# Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions

- 区域：速读区
- 排名：10
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Pin Qian, Su Wang, Yihang Chen, Qiaolin Yu, Xiaoyuan Wang, Zhitong Guo, Zhicheng Wang, Junxian You
- 机构：Georgia Institute of Technology, Cornell University, University of Glasgow, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21635v1) · [PDF](https://arxiv.org/pdf/2607.21635v1)

## TLDR
This paper argues that personal LLM agent evaluation requires a user-conditioned protocol that replays temporal interventions across varying persistent user states to measure cross-dimensional failure propagation, and finds that no existing benchmark satisfies all four formal conditions for such evaluation.

## Abstract
Personal agents maintain memories, learned skills, tool configurations, and policy state that evolve with each user. Existing agent benchmarks often evaluate these capabilities in isolation: tool benchmarks test invocation under fixed APIs, memory benchmarks test recall or forgetting, and safety benchmarks test static policy compliance. We argue that personal-agent evaluation requires a different protocol: replaying the same temporal intervention across different persistent user-conditioned states and measuring how failures propagate across agent components. We formalize this requirement as four conditions: explicit temporal intervention, persistent state across the intervention, induced cross-dimensional effects, and variation in user-conditioned state. A focused audit of public benchmark protocols selected by explicit inclusion criteria identifies several close cases. Under our explicitly narrow operationalization, we did not find a protocol in that audited set satisfying all four conditions. This claim is scoped as a focused gap analysis with bounded literature coverage. This position paper proposes a minimal benchmark design and candidate reporting metrics for user-conditioned adaptation. The result is a concrete design requirement for future personal-agent evaluation, with metrics used as reporting tools for that requirement.
