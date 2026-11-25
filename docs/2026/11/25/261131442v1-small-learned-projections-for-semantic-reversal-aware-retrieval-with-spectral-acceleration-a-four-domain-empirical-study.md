# Small Learned Projections for Semantic-Reversal-Aware Retrieval with Spectral Acceleration: A Four-Domain Empirical Study

- 区域：速读区
- 排名：13
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Sayed Amir Karim
- 机构：Pelloran Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31442v1) · [PDF](https://arxiv.org/pdf/2611.31442v1)

## TLDR
A small learned projection suppresses semantic-reversal trap documents in dense retrieval—achieving zero trap hits in the top-10 across legal, medical, patent, and financial domains at pools up to 100,000 while retaining 93–99% correct paraphrases—and a boundary-conditioned spectral accelerator serves this projection efficiently at scale, making compact domain-specific indexes practical.

## Abstract
Dense-embedding retrievers can fail adversarially: when a query is answered by a document A and reversed by a near-copy B that differs from A by a small meaning-changing edit (a "trap"), raw cosine over E5-Large-v2 places B in the top-10 for 82-100% of queries at a pool of 5,000. We study two things. First, a small learned projection W: R^1024 -> R^d (d in {11, 32}), trained by a deterministic recipe on a declared set of cases, that suppresses the trap: for the declared cases, HN@10 = 0.0000 (no trap in the top-10) in all twelve (domain, pool-size) settings across four independent domains (legal, medical, patent, financial) and pools up to 100,000, while the correct paraphrase is retained for 93-99% of cases, under exact nearest-neighbour search. Second, a boundary-conditioned accelerator that serves the projection at that scale: an acceleration of spectral graph retrieval (SpectRAG) that replaces a dense eigendecomposition with a boundary-value solve, holding HN@10 = 0.0000 at n = 100,000 in every domain and retrieving the ~300-query suite in 0.6-1.1 s (~2-4 ms per query on average). Because the lens's output is the stored representation (a few floats per document), a hardened, specialised index per domain or tenant is ~90x smaller and dimension-proportionally faster than the full embedding, making many small declared indexes a practical alternative to one large vector store. The claim is scoped to the declared cases on the measured pools, with no probabilistic bound; the correct-answer rate drops for a reworded query against an unchanged corpus (about 0.79, trap suppression still holding). A projection transfers only partly to other domains, which we report in full. The recipe, lenses, trap sets and evaluation harness are released under AGPL-3.0; the accelerator's implementation is a reserved commercial component, and every HN number is reproducible under exact search.
