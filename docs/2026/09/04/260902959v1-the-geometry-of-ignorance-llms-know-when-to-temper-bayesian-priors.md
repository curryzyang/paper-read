# The Geometry of Ignorance: LLMs Know When to Temper Bayesian Priors

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Toni J. B. Liu, Jiajun Bao, Yizhou Liu, Gurbir Arora, Nicolas Boullé, Raphaël Sarfati, Christopher J. Earls
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.02959v1) · [PDF](https://arxiv.org/pdf/2609.02959v1)

## TLDR
LLM unembedding matrices encode the training corpus unigram distribution as a "direction of ignorance" whose projection yields a prior-loading factor \(\lambda\) that aligns with a tempered Bayesian update, decreases with context, and can causally steer predictions toward or away from this Bayesian prior.

## Abstract
What does a language model predict when it has few clues? The answer lurks in its unembedding geometry: a single direction of the unembedding matrix encodes the unigram distribution of the training corpus, which serves as the Bayesian prior the model falls back on when uncertain. This structure --- which we term the \emph{direction of ignorance} --- appears in all four model families examined (\texttt{Llama}, \texttt{Qwen}, \texttt{Gemma}, and \texttt{Pythia}), ranging from 0.4B to 405B parameters. Projecting the final prediction state onto this direction yields a per-token \emph{prior loading factor} $λ$, which, empirically, declines steadily as the context becomes more informative. Formally, the same projection decomposes the prediction state into two orthogonal vectors that correspond exactly to the two factors of a tempered Bayesian update: a unigram prior raised to the exponent $λ$ and a context-driven likelihood. This geometric-probabilistic interpretation calibrates $λ$, making it meaningfully comparable across model sizes and families, with larger models generally exhibiting lower prior reliance in the high-context limit. Finally, we show that the direction of ignorance is causally active: raising or lowering $λ$ at the final prediction state steers the prediction toward or away from the unigram prior in KL divergence.
