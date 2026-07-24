# Do Active SAE Feature Planes Carry More Holonomy? A Preregistered Reversal in Gemma

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Larry Richards
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20522v1) · [PDF](https://arxiv.org/pdf/2607.20522v1)

## TLDR
Preregistered tests in Gemma 2 2B falsified the prediction that holonomy concentrates on active SAE feature planes, instead finding that such planes carry significantly less holonomy than matched mixed-feature controls, with the underlying cause still unresolved.

## Abstract
This paper tests whether holonomy concentrates on active sparse-autoencoder (SAE) feature planes in Gemma 2 2B, a concrete operationalization of the broader semantic-concentration prediction. Holonomy is measured at the final-token layer-12 to layer-13 residual-stream readout by carrying a local frame around small loops using the instrument's restricted-Jacobian transport rule, then normalizing the resulting rotation by enclosed area. The design, materiality threshold, analysis, and verdict rules were preregistered and frozen before the analysed measurements were inspected. The prediction was falsified in reverse: active-feature planes carried less holonomy than matched mixed-feature controls, with an adjusted log contrast of -0.29439 and 95% interval [-0.43989, -0.14889]. A magnitude-only explanation was not supported in this design, while the three-way ordering across random, mixed-feature, and active-feature planes was undefined at matched magnitude because common support failed. Post-freeze diagnostics at the same readout supported the area law on a small validation subset, bounded matched-center displacement under a simple paired regression, and identified transport distortion as a live mechanism or confound. The result is therefore a narrow, auditable operational reversal, not a causal claim that meaning suppresses holonomy. The cause remains open, with activation-strength geometry, degree of feature engagement, dictionary geometry, matched-center displacement, activation-manifold proximity, and transport shear as live alternatives.
