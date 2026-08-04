# AutoCause: A Python framework that automates expert decisions in environmental time-series causal discovery

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Marco Ruiz, Miguel Arana-Catania, David R. Ardila, Rodrigo Ventura
- 机构：University of Oxford, Instituto Superior Técnico, Caltech
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00198v1) · [PDF](https://arxiv.org/pdf/2608.00198v1)

## TLDR
AutoCause is an open-source Python framework that automates and records expert decisions in environmental time-series causal discovery by wrapping multiple established methods, deriving defaults from extended causal-audit diagnostics, and grading consensus-support links, thereby making the analysis auditable and reproducible while leaving causal interpretation to the analyst.

## Abstract
Environmental time-series causal discovery requires expert decisions about method choice, conditional-independence tests, lag horizons, sample-size adequacy, multiple-testing control, and evidence interpretation. Applied inconsistently across datasets, these choices yield graphs that cannot be compared, reproduced, or audited. We present AutoCause, an open-source Python workflow that records each decision, derives defaults from an extended causal-audit module, and admits domain-informed overrides. The workflow wraps four established causal-discovery methods from three families, adds non-causal reference models, and grades links by method-count support. On 145 datasets from DGP-Atlas, TimeGraph, and a topology-derived CausalRivers reference, the methods recover complementary parts of the reference graphs. Majority-supported links are more precise than single-method links on the synthetic benchmarks but not against river topology. AutoCause converts inconsistent expert practice into an auditable, repeatable analysis; causal interpretation remains with the analyst. Available at https://github.com/marcoruizrueda/autocause.
