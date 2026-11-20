# Rate-distortion Assessment for Hierarchical Content Summarization

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Yunye Gong, Indranil Sur, Jared Claypoole, Pritish Sahu, Ajay Divakaran
- 机构：SRI International
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25151v1) · [PDF](https://arxiv.org/pdf/2611.25151v1)

## TLDR
The paper proposes a QA-based semantic-hierarchy framework inspired by rate-distortion theory to quantitatively assess generative content summarization, benchmark LLMs’ compression–comprehension trade-offs, and guide more efficient retrieval-augmented generation.

## Abstract
Powerful generative models including large language and vision models have demonstrated success across a wide range of content generation, editing and manipulation tasks via end-to-end prompt-based generation. However, current assessment of the quality of generative content manipulation remains subjective, limiting scientific understanding of model capabilities. Inspired by rate-distortion theory from Shannon information compression theory, in this work we formalize hierarchical content summarization as an information encoding problem. We design a principled framework to extract the semantic hierarchy of the source content to support quantitative characterization of the rate-distortion trade-off between compression efficiency (rate) against information loss (distortion) during generative content manipulation, which allows us to benchmark various models with respect to performance conditional on rate budget of interest. We demonstrate the use of the framework with empirical experiments on content summarization for long-context question-answering with state-of-the-art large language models, offering new insights into their efficiency and comprehension capabilities. We further demonstrate the use of the semantic hierarchy as guidance for performing effective retrieval augmented generation, showing improved rate-distortion characteristics against current baselines.
