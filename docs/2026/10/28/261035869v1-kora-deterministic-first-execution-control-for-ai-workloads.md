# KORA: Deterministic-First Execution Control for AI Workloads

- 区域：速读区
- 排名：3
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Albert Heekwan Kim
- 机构：Krako Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35869v1) · [PDF](https://arxiv.org/pdf/2610.35869v1)

## TLDR
KORA proposes a deterministic-first pre-inference control layer that routes requests through deterministic or structured handlers when possible, validates outcomes, records telemetry, and escalates to model inference only when necessary, reporting a bounded benchmark result of avoiding 80 of 100 simulated model calls with zero mismatches in the deterministic subset.

## Abstract
AI applications often invoke a model before they determine whether inference is necessary. That default is useful for ambiguous generative tasks, but it is poorly matched to work that is structured, deterministic, policy-bound, lookup-oriented, or directly verifiable. KORA introduces deterministic-first execution control: a pre-inference control layer that represents requests as task paths, attempts deterministic or structured routes first, validates route outcomes, records telemetry, and escalates to a model-candidate path only when deterministic handling is insufficient. This paper presents KORA as a deterministic-first execution-control architecture and reports bounded evidence from reproducible benchmark and validation workloads. In a reproducible 100-task deterministic-heavy benchmark, KORA-controlled execution avoided 80 of 100 simulated model invocations versus a naive direct baseline, with zero mismatches in the deterministic subset. The workload is intentionally deterministic-heavy: it includes categories such as FAQ lookup, policy/rule checking, schema or format validation, deterministic transformation, and a smaller set of model-needed ambiguous or generative tasks. A separate synthetic customer-support local/no-network validation workload demonstrates route measurement and avoided model-call accounting in an application-shaped setting. These results support bounded model-invocation reduction and validation visibility in documented workloads. They do not establish production behavior, real-provider outcomes, energy outcomes, API-cost reduction, or broad superiority.
