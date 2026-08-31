# When Muon Meets Task Interference: A Spectral Perspective on Continual Learning and Model Merging

- 区域：速读区
- 排名：4
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Shangge Liu, Yuehan Yin, Yinghuan Shi, Lei Wang, Wenbin Li
- 机构：Nanjing University, University of Wollongong
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27518v1) · [PDF](https://arxiv.org/pdf/2608.27518v1)

## TLDR
This paper unifies continual learning and model merging as a shared "task interference" phenomenon bounded by the spectral norm of weight updates, and shows that the Muon optimizer—by construction—minimizes this factor to improve both paradigms.

## Abstract
Continual learning (CL) and model merging (MM) both aim to obtain a single model that performs well across multiple tasks, challenged respectively by catastrophic forgetting and weight-disentanglement error. In the literature, these difficulties are merely treated separately and mitigated through a variety of solutions, while the geometry induced by the base optimizer is treated as an implementation detail. In this work, we show that the two difficulties are in fact two instances of the same phenomenon: a parameter update useful for one task shifts the model's outputs on another. We formalize this shared phenomenon as \textit{task interference} and reduce it to a common layer-wise Frobenius inner product $\langle ΔW_\ell, J_\ell(x)\rangle_F$. This quantity, in turn, is utilized to expose the role of the optimizer. We theoretically derive an upper bound that isolates the spectral norm $\|ΔW_\ell\|_2$ as an optimizer-controllable factor of task interference, and a per-mode analysis shows that this bound tracks the dominant part of the empirical interference. Specifically, we then identify the recent Muon optimizer as a mechanism that regulates this factor by construction. Our work reveals that its elegant control on spectral norm tightens the interference bound for both CL and MM, positioning Muon as a principled optimizer-centric approach complementary to existing solutions. Our theoretcal analysis is well validated by experimental results. Replacing the AdamW optimizer with Muon improves accuracy by up to +5.02 points on the eight-task model-merging benchmark across three CLIP backbones. For continual learning, Muon also delivers uniformly positive gains across ten class-incremental protocols, three task-incremental protocols, and the 11-task MTIL benchmark.
