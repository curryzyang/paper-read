# From Weights to Words: Expressing and Editing Preference Model Inferences in Natural Language

- 区域：速读区
- 排名：7
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Zachary Wojtowicz, Ayush Nayak, Jacob Andreas
- 机构：MIT
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16232v1) · [PDF](https://arxiv.org/pdf/2607.16232v1)

## TLDR
This paper introduces a method that automatically discovers interpretable, natural-language-described preference dimensions from choice data, improving prediction accuracy and enabling human users to inspect and edit model inferences in real time.

## Abstract
The growing use of statistical learning algorithms to infer human preferences from high-dimensional choice data runs up against a fundamental challenge: choice alternatives typically differ in many ways simultaneously, so it is generally unclear which factors actually drove an observed decision and should be credited as preferences. Compounding this problem, the opacity of these methods leaves human operators unable to inspect, contest, or correct models when they err. We introduce \emph{weights to words}, a method that takes a dataset of choice problems as input and automatically discovers a collection of domain-relevant preference dimensions, each described in natural language and paired with a vector in the model's representational space. These dimensions address both under-determination and opacity: they can be applied to concentrate attribution on a small set of meaningful factors, and they can externalize the model's inferences in natural language so that users can inspect and edit them in real time. We first qualitatively illustrate the method's versatility on four diverse domains: moral dilemmas, movies, wines, and free-form LLM responses. We then report two pre-registered human-subjects experiments, on moral dilemmas ($N=450$) and movie selection ($N=449$), that demonstrate its benefits for learning preference models: (1) regularizing a preference model toward the learned basis increases prediction accuracy on held-out choices, and (2) incorporating participants' structured edits further improves accuracy. In head-to-head comparisons, participants prefer the method's inferred preference profiles and endorse its predictions as more accurate.
