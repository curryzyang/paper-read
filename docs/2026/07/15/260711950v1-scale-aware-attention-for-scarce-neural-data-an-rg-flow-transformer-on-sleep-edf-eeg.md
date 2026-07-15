# Scale-Aware Attention for Scarce Neural Data: An RG-Flow Transformer on Sleep-EDF EEG

- 区域：速读区
- 排名：2
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Dibakar Sigdel
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11950v1) · [PDF](https://arxiv.org/pdf/2607.11950v1)

## TLDR
The RG-Flow Transformer, despite incorporating a renormalization-group inductive bias, does not outperform a vanilla transformer in sleep-staging accuracy on scarce EEG data, but uniquely enables interpretable recovery of the brain's aperiodic spectral exponent.

## Abstract
Brain field potentials are scale-free: their power spectra follow a $1/f^β$ law whose aperiodic exponent $β$ tracks cortical state, and sleep depth in particular is a shift in $β$. We ask whether a transformer endowed with an explicit renormalization-group (RG) inductive bias -- the RG-Flow Transformer, which couples ordinary self-attention to a scale-aware stream with a learnable anomalous dimension $γ$, block-spin coarse-graining, and an entropy-gated synchronization bridge -- has an advantage over a parameter-matched vanilla transformer on \emph{real, scarce} EEG. Using the PhysioNet Sleep-EDF corpus with a strict leakage-free by-subject hold-out, we (i) benchmark RG-Flow against a param-matched vanilla transformer and a hierarchy-only ablation on 5-class AASM sleep staging, (ii) sweep the per-subject data budget to look for the inductive-bias crossover predicted when data are scarce, and (iii) test whether RG-Flow's learned $γ$ tracks the measured spectral exponent $β$ out-of-sample -- a quantity the vanilla model does not possess. Across $5$ subjects and $5$ seeds under leave-one-subject-out cross-validation, RG-Flow and the vanilla transformer are statistically indistinguishable on 5-class staging (77.3\% vs 77.0\% accuracy; paired $p=0.294$), and the predicted scarce-data crossover does not appear: vanilla is numerically ahead at every data-limited budget. What does separate the models is interpretability -- RG-Flow recovers the continuous spectral exponent out-of-sample ($β$-recovery $R^2 = 0.416$), a capability the vanilla architecture has no analogue for.
