# The Gradient Does Not See Rank: Rank-Indifference in Matrix-CODI on ProsQA

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Samuel Larson
- 机构：Pebble ML
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03090v1) · [PDF](https://arxiv.org/pdf/2609.03090v1)

## TLDR
Matrix-CODI's matrix-valued latent thoughts are rank-indifferent during training—rank-k truncation ablations stay flat across tasks, seeds, and readouts, and the gradient's constant Jacobian means rank is not a functional structural readout of reasoning, with the ablation conflating rank-blindness with position-irrelevance.

## Abstract
Continuous chain-of-thought models compress reasoning into latent tokens. Matrix-valued variants, which route each latent token through a d x d matrix bottleneck, introduce rank as a single-sample structural observable on the latent matrix Z. If matrix latents carry parallel reasoning paths via superposition, rank should track them, and truncating Z to low rank should hurt accuracy on tasks whose solutions plausibly require multiple components. Across four training regimes of a matrix-CODI model (three on ProsQA, one on GSM8K-Aug below the learning threshold), the rank-k projection ablation curve is flat to within 0.6 percentage points. A three-seed replication yields 81.0 +/- 2.0 percentage points accuracy while the final effective rank of Z spans {4, 12, 13}; the loss does not reward any particular rank. To test whether rank-blindness arises from the flatten-then-project readout alone, we trained four readouts: a bilinear reparametrization, a bilinear-plus-GELU readout nonlinear in Z, an SVD-augmented readout feeding singular values through an MLP, and a quadratic readout in Z Z^T. All four rank-k curves remain flat (Spearman p-values 0.63, 0.14, 0.82, 0.46). The flat curves persist for readouts nonlinear in Z. A linear probe on Z underperforms a raw pretrained hidden state at target prediction (AUC 0.673 vs. 0.846). A negative control on vanilla GPT-2 SFT (no matrix bottleneck, no Z, three seeds, n=500) reproduces a flat rank-k curve under the same intervention paradigm with pooled-mean range 0.20pp, and a random-h sensitivity floor lands at the same accuracy: the rank-k ablation alone conflates rank-blindness with position-irrelevance.
