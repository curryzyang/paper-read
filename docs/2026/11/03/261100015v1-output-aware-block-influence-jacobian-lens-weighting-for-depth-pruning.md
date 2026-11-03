# Output-Aware Block Influence: Jacobian-Lens Weighting for Depth Pruning

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Kyle Lemoi, Jonathan Yong, Shubhankar Tripathy, Priestley Fernandes, Anirban Majumder, Zarreen Reza
- 机构：University of Massachusetts Amherst, Amazon Science, University of the Cumberlands, Independent, Algoverse Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.00015v1) · [PDF](https://arxiv.org/pdf/2611.00015v1)

## TLDR
Applying a Jacobian-Lens transport to Block Influence (J-BI) yields a more reliable depth-pruning criterion that improves post-pruning accuracy by up to 19 points and reduces perplexity damage versus standard Block Influence across several 8B–12B LLMs.

## Abstract
Depth pruning removes entire transformer blocks and therefore depends on a reliable criterion for identifying which blocks can be removed. Block Influence (BI) ranks blocks by how minimally they rotate the hidden state. However, local redundancy does not necessarily imply downstream irrelevance. We address this limitation using the Jacobian Lens (J-Lens) neural artifact, a map transporting perturbations at a layer to the final residual stream. At a common sparsity level, pruning scores applying J-Lens transportation to $BI$, what we call $J-BI$, were found to improve post-pruning accuracy by up to 19 points over $BI$ while reducing damage to perplexity for Qwen3-8B, Llama-3.1-8B-IT, and Gemma-3-12B-IT. We also perform a single-block ablation study and use J-Lens probing to explain why the proposed scores improved performance.
