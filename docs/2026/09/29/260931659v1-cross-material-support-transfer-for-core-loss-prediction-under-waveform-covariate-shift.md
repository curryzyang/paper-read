# Cross-Material Support Transfer for Core-Loss Prediction Under Waveform Covariate Shift

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Cong Yao, Chunye Gong
- 机构：National Supercomputer Center in Tianjin, National University of Defense Technology, Changsha University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31659v1) · [PDF](https://arxiv.org/pdf/2609.31659v1)

## TLDR
The paper proposes MIST, a cross-material support-transfer method that conditions a single small jointly trained core-loss predictor on material identity via FiLM and reweights the scarce material’s true-label loss, showing that waveform covariate shift is a missing-information problem whose support can be borrowed from sibling materials, cutting material D’s p95 error from 20.39% to 12.38% without fine-tuning.

## Abstract
Power magnetic materials are characterized on the sinusoidal and triangular waveforms that excitation hardware conveniently produces, whereas deployed converters expose cores to trapezoidal, PWM-shaped flux trajectories, so loss models must predict exactly where their training data are thinnest. The final test of the MagNet Challenge embeds a deliberately extreme instance of this characterization-deployment mismatch: for material D, trapezoids form 16.4% of the test set but only 1.4% of the training set. The 95th-percentile relative error, hereafter p95, of the best submission, built on sequential transfer learning, stalled at 15.9%, the worst among the five materials. This paper shows that the obstacle is missing information under covariate shift rather than class imbalance, and that the missing support can be borrowed from sibling materials instead of being extrapolated. Controlled experiments first refute the imbalance reading: four standard remedies fail, and raising the trapezoidal share to the test-set level degrades accuracy further. The proposed material-identity support transfer, MIST, then trains one 2784-parameter predictor jointly on all five challenge materials. Material identity enters through feature-wise linear modulation, or FiLM, the scarce material's true-label loss is reweighted, and material D receives no fine-tuning, so that the bias of its trapezoid-free training set is never re-installed. MIST lowers the five-seed material-D p95 from 20.39+/-2.03% to 12.38+/-0.92% and the trapezoidal-class p95 from 37.4+/-8.8% to 15.16+/-1.69%, surpassing the best submission with one-sixth of its parameters and no fine-tuning stage; removing material identity at matched capacity inflates the error by an order of magnitude. These results argue that scarce materials should be characterized jointly with their siblings.
