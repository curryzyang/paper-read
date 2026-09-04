# ObserverBench: Testing Mechanistic Estimates for Intervention and Control

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Vijay Erramilli
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03026v1) · [PDF](https://arxiv.org/pdf/2609.03026v1)

## TLDR
ObserverBench is a benchmark framework that evaluates mechanistic interpretability estimates by how well they support downstream intervention, control, and safety decisions, showing that prediction accuracy alone can misrank methods relative to the action losses they incur.

## Abstract
Mechanistic interpretability is increasingly used to guide interventions such as activation steering, circuit removal, and safety monitoring. Yet an internal estimate that is accurate on average can still choose a poor action.
  We present ObserverBench, a benchmark framework for testing whether an internal estimator---an observer---is adequate for the intervention, control, or safety task it directs. Each task fixes the model, information boundary, allowed actions, decision rule, held-out cases, and loss. The benchmark reports estimation accuracy separately from the loss caused by the chosen action.
  Theory and experiments show why both are needed. In closed-loop control, observer errors matter at the starting point and along directions the allowed intervention can reach. On circuit-intervention tasks in GPT-2-small and Qwen2.5-7B, pairwise observers predict unseen effects more accurately without always choosing better actions; observers trained on action loss choose lower-loss actions. In safety triage, a score that perfectly separates violations can allocate a fixed intervention budget poorly when violations have different costs. Across Qwen2.5-7B, Gemma-2-9B-it, and prospectively frozen Qwen3.5-9B APPS tasks, AUROC can rank monitors differently from deployment loss, and the best information source changes across models. Sparse SAE readouts also trail their layer-matched dense controls on the reported Qwen panels, under disclosed activation-density or checkpoint mismatches.
  ObserverBench provides fixed task contracts, runnable baselines, and table-based submissions for evaluating interpretability methods through the actions they enable.
