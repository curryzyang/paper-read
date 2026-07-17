# How Much of a 10-K Matters? Aggregation-Dependent Value of Full-Text versus Risk-Factor Sentiment

- 区域：速读区
- 排名：15
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Sanggyu Sean Choi
- 机构：University of Edinburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14174v1) · [PDF](https://arxiv.org/pdf/2607.14174v1)

## TLDR
Supervised sentiment from full 10-K text outperforms that from the Item 1A risk-factor section at the sector and portfolio level, but the reverse holds at the individual-firm level, with a dictionary baseline showing persistent negative correlation with price.

## Abstract
Financial sentiment extraction has largely relied on news text and supervised extraction against return labels alone, leaving 10-K filings -- and volatility, the target risk disclosure is arguably best suited to informing -- comparatively unexplored. We extend a supervised lexicon-learning approach to 10-K filings and their Item 1A risk-factor sections, training sentiment scores against both return and volatility labels at three levels of aggregation: sector, portfolio, and individual firm. Across 1,383 filings from 94 Nasdaq-100 technology constituents (2006--2023), we evaluate the resulting twelve sentiment metrics on classification accuracy, correlation with realised market outcomes, and qualitative lexical content. Full-filing text produces more accurate sentiment at the sector and portfolio level for both targets, but this reverses at the individual-firm level, where the narrower Item 1A section performs better -- an effect we attribute to the interaction between document volume and the amount of independent training signal available at each level of aggregation. A Loughran-McDonald dictionary baseline is consistently, strongly negatively correlated with price at every level tested, underscoring the value of a supervised approach for regulatory disclosure text. These findings, and the design choices they motivate, establish the sentiment-generation methodology underlying a subsequent, larger-scale, multi-source system.
