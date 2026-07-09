# AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation

- 区域：速读区
- 排名：9
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman Pozharskiy, Maksim Parshin, Sergey Nikolenko
- 机构：St. Petersburg State University, St. Petersburg Department of the Steklov Institute of Mathematics, Explyt
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06624v1) · [PDF](https://arxiv.org/pdf/2607.06624v1)

## TLDR
AgentLens is an open-source benchmark that evaluates interactive coding agents by combining formal verification with LLM-written trajectory reviews to assess the full agent trajectory, enabling model diagnosis, version comparison, and regression detection in production pipelines.

## Abstract
We present AgentLens, a production-assessed benchmark for interactive code agents. Most code-agent benchmarks reduce a run to a single bit -- did the task pass? -- but the people who actually use these agents experience the entire trajectory: how the agent follows instructions, uses its tools, verifies its own work, recovers from mistakes, and talks to them along the way. AgentLens evaluates that whole trajectory. It pairs formal verification, where an objective check exists, with LLM-written trajectory reviews and side-by-side comparisons, so that each run yields a readable explanation of why the score is what it is. This makes AgentLens useful for more than ranking models: we use it to diagnose model behavior, compare successive versions of our own agent, and catch product regressions in a nightly evaluation pipeline. We release the benchmark as open source at https://github.com/agent-lens/agent-lens-bench.
