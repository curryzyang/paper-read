# GRAFT: Grafted Reference Audio for Fine-grained Pronunciation in Zero-shot Text-to-Speech

- 区域：精读区
- 排名：9
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Antonis Asonitis, Francesco Verdini, Aref Farhadipour, Vijeta Avijeet, Pierre-Edouard Honnet, Marzieh Razavi, Juan Pablo Zuluaga Gomez
- 机构：University of Zurich, Sapienza University of Rome, AGIGO, ETH Zurich
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02633v1) · [PDF](https://arxiv.org/pdf/2607.02633v1)

## TLDR
GRAFT introduces a per-word pronunciation conditioning method for zero-shot text-to-speech that replaces text tokens with codec tokens from a short spoken sample of the target word, using voice conversion to disentangle speaker identity and achieving significant pronunciation improvements across multiple languages without sacrificing naturalness or speaker similarity.

## Abstract
We present GRAFT, a per-word pronunciation conditioning mechanism for text-to-speech neural codec language modeling. Existing systems reach high intelligibility and naturalness but inherit the ambiguity of text and mispronounce rare proper nouns, loanwords and technical terms. Even phoneme-conditioned models offer no direct acoustic handle for per-word pronunciation. GRAFT controls the pronunciation of a chosen word from a short spoken sample of it, encoded with the model's own speech tokenizer and bound to the word's position in the prompt. Voice conversion during training-data construction disentangles the hint speaker from the target speaker, so the hint may come from any voice while the output stays in the target voice. In a blind English listening study, human raters rank GRAFT first by a clear margin, judging its rendering of the difficult word closest to a reference recording of that word. On a five-language objective benchmark, GRAFT reduces target-word phoneme error rate by 22-39% over the identical text-only backbone and outperforms competitive open-source zero-shot systems, both phoneme- and text-conditioned, on target-word pronunciation, while preserving speaker similarity and naturalness.
