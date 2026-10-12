# Algebraic Integer Quantization for Machine Learning Applications

- 区域：速读区
- 排名：13
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Anthony Kostal-Vazquez, Vassil Dimitrov, Branden Butler
- 机构：Lemurian Labs Research Group, University of Calgary
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12494v1) · [PDF](https://arxiv.org/pdf/2610.12494v1)

## TLDR
The paper introduces algebraic integer quantization (AIQ), a configurable algebraic-integer-based format that enables error-free integer-only multiply-accumulate operations and achieves competitive LLM inference accuracy versus the MX format at equivalent bit-per-parameter budgets, while supporting matrix multiplication performance close to standard numerical hardware accelerators.

## Abstract
In this article, we propose algebraic integer number formats (AINF) as a framework for highly configurable and accurate compressed computation. A key property of AINF is its straightforward reduction to purely integer arithmetic, enabling error-free multiply-accumulate operations. We develop a matrix multiplication engine that exploits this property, obtaining performance within a predictable factor of the most efficient numerical counterparts on modern hardware accelerators. Another key advantage of AIQ is the freedom to select algebraic integers tailored to the numerical characteristics of a given use case, offering optimization opportunities that are fundamentally unavailable in floating-point or fixed-point formats. Motivated by these properties, we introduce algebraic integer quantization (AIQ), a lossy compression format for large language model (LLM) inference, and provide results demonstrating that AIQ achieves competitive accuracy compared to the industry-standard MX format across a diverse set of models and benchmarks at equivalent bit-per-parameter budgets. The experiments presented in this article employ algebraic integers of degree two (quadratic integers); generalizations to higher-order and, in particular, multidimensional algebraic integers promise even greater computational advantages and remain a promising direction for future work.
