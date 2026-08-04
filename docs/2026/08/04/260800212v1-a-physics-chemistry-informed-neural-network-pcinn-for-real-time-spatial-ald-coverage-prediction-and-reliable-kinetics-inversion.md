# A Physics-Chemistry-Informed Neural Network (PCINN) for Real-Time Spatial-ALD Coverage Prediction and Reliable Kinetics Inversion

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Ning Hu, Chang Liu, Yunlei Jiang, Yuan Dong
- 机构：Hangzhou Dianzi University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00212v1) · [PDF](https://arxiv.org/pdf/2608.00212v1)

## TLDR
A physics-chemistry-informed neural network (PCINN) hybrid surrogate combines a small neural network for transport closure with a hard-coded, trainable surface-kinetics layer to achieve real-time (~7 ms), CFD-level spatial-ALD coverage prediction and reliable kinetics inversion, including an analytic identifiability diagnostic for parameter degeneracy.

## Abstract
Spatial atomic layer deposition (SALD) is a leading atmospheric-pressure, high-throughput route to industrial ALD, but design and control are limited by the cost of predicting surface coverage: high-fidelity CFD is far too slow for operating-window scans, while analytic models miss transport modulation such as the gas curtain. We present a physics-chemistry-informed neural network (PCINN), a hybrid surrogate with CFD-level accuracy at real-time speed: a query returns coverage in about 7 ms, roughly 5x10^4 times faster than a CFD solve, reaching a test R^2_log = 0.998 (leave-one-out R^2_raw = 0.974) from only 30 training cases spanning four orders of magnitude in coverage.
  The architecture is not a black box: a small network learns only the operating-condition to near-wall concentration closure, while the known surface kinetics is a hard-coded, trainable chemistry layer integrated along the substrate trajectory. This single-scalar bottleneck keeps it accurate under sparse data, interpretable and invertible.
  We add a full identifiability analysis (Fisher information, profile likelihood). The adsorption energy E_ads and desorption rate k_des are robustly identifiable; k_ads is not separately identifiable at a single temperature (only k_ads*c_wall is). Across four temperatures the prefactor nu and E_ads bind along a weakly identifiable degeneracy valley of slope 0.065 eV/decade, derived analytically as k_B T_eff ln(10) and turned into a reliability diagnostic: a seven-chemistry mismatch matrix shows it is invariant under any single-Arrhenius mismatch and shifts only when a second thermally activated process appears, so a slope departure flags unmodelled site heterogeneity.
  Data come from simulation with known ground truth inverted by the same kinetic form, so the study verifies pipeline self-consistency and the identifiability boundary, not real parameters.
