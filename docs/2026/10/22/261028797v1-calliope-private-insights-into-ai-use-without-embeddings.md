# CALLIOPE: Private Insights into AI Use, Without Embeddings

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Edith Cohen, Vadym Doroshenko, Badih Ghazi, Charlie Harrison, Pritish Kamath, Alexander Knop, Ravi Kumar, Ethan Leeman, Pasin Manurangsi, Mikhail Pravilov, Adam Sealfon, Yurii Sushko, Marika Swanberg, Chiyuan Zhang
- 机构：Google Deepmind, Google, Google Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28797v1) · [PDF](https://arxiv.org/pdf/2610.28797v1)

## TLDR
CALLIOPE is a differentially private, top-down framework that discovers topic hierarchies in unstructured data by using LLMs directly in the text domain—without vector embeddings—and achieves better utility than embedding-based methods, especially in high-privacy regimes.

## Abstract
We introduce CALLIOPE, a top-down framework for discovering topic hierarchies in large corpora of unstructured data (e.g., LLM conversations), while supporting differential privacy (DP). Unlike traditional and even recent LLM-augmented approaches that ultimately rely on clustering vector embeddings, our framework leverages LLM capabilities directly for the entire pipeline. Experiments demonstrate that this approach provides better utility over existing (embedding-based) methods in the DP setting, especially in the high privacy regime. We evaluate the quality of CALLIOPE outputs using a variety of traditionally studied clustering metrics, as well as some novel utility metrics that we introduce.
