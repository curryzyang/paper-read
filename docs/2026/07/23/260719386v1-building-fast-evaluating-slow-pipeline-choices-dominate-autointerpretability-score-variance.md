# Building Fast, Evaluating Slow: Pipeline Choices Dominate Autointerpretability Score Variance

- 区域：速读区
- 排名：8
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Sinie van der Ben, Neele Roch, Anna Hedström, Mennatallah El-Assady
- 机构：ETH Zürich
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.19386v1) · [PDF](https://arxiv.org/pdf/2607.19386v1)

## TLDR
This paper reveals that methodological choices in the autointerpretability evaluation pipeline (e.g., corpus, sampling, explainer, phrasing) dominate score variance, often exceeding architectural differences between sparse autoencoders, thus undermining the reliability of cross-paper comparisons.

## Abstract
Cross-paper comparison of sparse autoencoder (SAE) interpretability often relies on autointerpretability scores. In this evaluation pipeline, a language model (LM) explains each feature, and another LM scores the explanation. For these comparisons to be meaningful, scores must reflect stable properties of the features rather than confounding aspects of the evaluation pipeline. Through systematic experiments across four metrics (simulation, detection, fuzzing, purity), two models (Pythia-160M, Apertus-8B), and four axes of methodological variation, we show that this assumption does not hold. Specifically, we find that R1) methodological variance collectively exceeds architectural variance across all metrics and tested models; R2) each metric exhibits a distinct instability profile, with detection being the most stable and fuzzing unreliable across all conditions; R3) top-k feature rankings do not stay consistent across corpus and draw conditions, masking per-feature instability behind stable mean scores; a failure that cannot be detected by monitoring explanation similarity alone. These findings suggest that cross-paper comparisons based on autointerpretability scores may reflect pipeline differences rather than architectural differences, with implications for the ongoing debate on SAE utility. More broadly, unreliable evaluation slows progress in interpretability research at a time when reliable tools for understanding AI systems are needed. To support evaluation, we contribute a variance decomposition approach, a Stability Check, and a Minimum Reporting Checklist.
