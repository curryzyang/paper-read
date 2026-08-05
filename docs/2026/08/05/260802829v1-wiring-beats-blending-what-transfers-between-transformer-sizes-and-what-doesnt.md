# Wiring Beats Blending: What Transfers Between Transformer Sizes -- and What Doesn't

- 区域：速读区
- 排名：3
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Ravi Satya Durga Prasad Yenugula
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02829v1) · [PDF](https://arxiv.org/pdf/2608.02829v1)

## TLDR
Converting a large pretrained transformer into a smaller sibling works best through structured initialization (least-squares compensation plus variance-preserving rescale) rather than dense weight blending, since representations align strongly across sizes but parameters do not, giving token-efficient gains at low budgets that converge to parity with subcloning at larger scales.

## Abstract
Model families train every size from scratch. Can a pretrained large model be converted into a smaller sibling? We characterize the 1.4B->410M conversion in the Pythia family end-to-end: (i) representations align strongly across sizes (ridge R^2=0.84) while parameters align weakly; (ii) dense weight projection is functionally destructive -- provably not an assembly artifact -- because basis mixing breaks rotary, per-head, GELU, and LayerNorm structure; (iii) after the best-fit linear operator, weight residuals are statistically indistinguishable from noise under shuffle controls; (iv) conversion value therefore lives in initialization. In matched-budget continued pre-training we decompose conversion into two independent levers -- least-squares compensation (function: best zero-shot) and variance-preserving rescale (dynamics: best endpoints). Compensation is a token-efficient, low-budget win rather than a universal one: at 30M tokens it beats the strongest subcloning variant on both a width-reduced pair (84.0 +/- 1.8 vs. 89.7 +/- 3.7, 3/3 seeds) and a held-out depth-reduced pair (109.3 vs. 117.9, 3/3 seeds), reaching a given quality with fewer tokens; at a 33x larger budget the two converge to parity (40.0 vs. 40.0), both far ahead of from-scratch, which transfer initialization always beats -- by up to 18x at low budget, the margin narrowing at convergence and at the largest scale. We further map the method's boundary: at ~5x the donor scale (6.9B->1.4B) stacking both levers over-corrects, which we trace to ill-conditioning of the compensation solve at large width, pointing to dimension-aware regularization as the fix. Code, checkpoints, and the frozen evaluation corpus are released.
