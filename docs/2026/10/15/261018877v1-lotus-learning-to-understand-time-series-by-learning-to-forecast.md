# Lotus: Learning to Understand Time-series by Learning to Forecast

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Van Dai Do, Huu Hiep Nguyen, Minh Hoang Nguyen, Manh Nguyen, Hung Le
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.18877v1) · [PDF](https://arxiv.org/pdf/2610.18877v1)

## TLDR
LOTUS introduces forecast grounding, a pretraining principle that trains language-aligned time-series representations to predict future patches via temporal-spectral patch embeddings, enabling compact models to retain temporal structure and outperform much larger baselines on TSRBench.

## Abstract
Time-series language models typically align numerical signals with language using labels, captions, or question-answer pairs. Although such supervision encourages linguistic representations, it does not explicitly require them to preserve information about how the underlying time-series signal evolves. We introduce forecast grounding, a pretraining principle that requires language-aligned time-series representations to remain predictive of the future evolution before they are adapted to downstream tasks. We instantiate this principle in LOTUS, which divides each time-series channel into non-overlapping patches and maps them into the LLM embedding space. It then predicts the next patch from the LLM hidden states of the time-series tokens, encouraging the learned representation to retain temporal information. To capture both temporal changes and periodic patterns, we also propose a temporal-spectral patch representation that combines each raw time-series patch with its spectral representation before mapping it into the LLM embedding space. Across three language model backbones and six downstream evaluation datasets, LOTUS achieves the best average performance with minimal trainable parameters, reaching 59.91% accuracy and outperforming the strongest matched baseline by 3.36%. Our representation analyses further show that LOTUS uses the numerical input and preserves temporal structure in its learned patch representations. These results establish forecast grounding as a promising pretraining principle, enabling compact time-series language models to outperform models 25 to 50 times their size on TSRBench.
