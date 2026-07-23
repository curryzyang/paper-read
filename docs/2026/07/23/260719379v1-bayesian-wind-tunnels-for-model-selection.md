# Bayesian Wind Tunnels for Model Selection

- 区域：速读区
- 排名：2
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Siddhartha R Dalal, Vishal Misra, Abhay Parekh
- 机构：Columbia University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19379v1) · [PDF](https://arxiv.org/pdf/2607.19379v1)

## TLDR
Transformers can perform near-optimal Bayesian model selection for relational structures (e.g., involutions) but fail for arithmetic ones (e.g., rotations) under opaque tokens, revealing a sharp and persistent perceptual access condition barrier.

## Abstract
Prior work has shown that transformers can perform exact Bayesian filtering within a fixed
  hypothesis class. Can they also perform Bayesian model selection -- identifying the correct
  hypothesis class from data? We introduce model-selection Bayesian wind tunnels: controlled
  environments where ground-truth posteriors over hypothesis classes are available in closed
  form. Using fixed-point-free involutions -- whose defining property f(f(x))=x is purely
  relational -- a 2.8M-parameter transformer achieves 0.01-bit entropy agreement with the
  Bayesian optimum (3 seeds), with both integer tokens and opaque symbols whose meanings
  change every episode. This extends to non-nested comparisons: involutions vs. 3-cycles
  (where neither class is a subset of the other) achieve class-posterior MAE under 0.001,
  demonstrating genuine model selection beyond simplicity/subset bias. We then identify a
  sharp perceptual access condition: when the discriminative statistic requires arithmetic --
  modular addition (rotations) or multiplication (f(x)=cx mod p) -- model selection succeeds
  with integer tokens but fails completely with opaque symbols, and this boundary persists
  under 112x scaling (2.8M to 316M parameters). A stationarity control confirms the operative
  factor: opaque tokens with a fixed relabeling succeed (0.009-bit MAE), showing that stable
  semantics, not integer identity, enable circuit compilation. Header subtask diagnostics
  localize the failure to the composition of header inversion with arithmetic rather than
  header parsing itself. Probing frontier LLMs on the same tasks shows qualitative Bayesian
  behavior but a large calibration gap (~55x), measured through lossy probes and therefore
  directional rather than exact.
