# TreeWalker: Partial Evaluation for Grouped Tree-Ensemble Inference

- 区域：速读区
- 排名：15
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Durmus Karatay, Richard Newman
- 机构：Shopify
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03939v1) · [PDF](https://arxiv.org/pdf/2610.03939v1)

## TLDR
TreeWalker speeds up grouped tree-ensemble inference by partial evaluation—walking each tree once per group and using row bitmasks to exploit shared constant features—achieving 2.5–7.8× speedups over row-independent traversal with equivalent numerical accuracy.

## Abstract
Many inference workloads evaluate a trained tree ensemble on row groups that share feature values: discrete-time survival models expand each patient into $G$ time steps, click-through-rate models score every item in a search session, and scenario analyses vary a few inputs while holding the rest fixed. Standard inference treats each row independently and repeats the shared work $G$ times.
  We present TreeWalker, which applies partial evaluation to grouped inference: constant features are static, varying features dynamic. It walks each tree once per group, partitions a row bitmask at varying splits, and skips empty subtrees. Training is unchanged: TreeWalker reads standard LightGBM and XGBoost models.
  We prove a structural work decomposition: per-tree work splits into the constant-projected subtree size $|T_c|$, $G$ leaf writes, and a predicate-mask provisioning cost $Q$. For the trace evaluator, per-row work approaches a $(d_v+1)/(d+1)$ fraction of a row-independent walk as $G \to \infty$.
  On Intel, TreeWalker is 2.5-3.2$\times$ faster than a row-independent traversal at the reference configuration ($T=500$, $L=8$) and 6.8-7.8$\times$ faster at $G=128$ on the survival datasets, with larger gains on Arm. On a scenario-analysis benchmark it is faster in all 16 configurations on both architectures. For f64 models, outputs match treelite's GTIL up to summation order; for f32 models, f64 accumulation is closer to a Kahan-compensated reference than native f32 on 99.98% of rows and never farther.
