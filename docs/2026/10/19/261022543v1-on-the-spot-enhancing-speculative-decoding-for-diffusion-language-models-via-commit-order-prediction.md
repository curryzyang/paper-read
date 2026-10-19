# On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models via Commit-Order Prediction

- 区域：速读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Eliezer Shlomi, Eliron Rahimi, Avi Mendelson, Chaim Baskin
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22543v1) · [PDF](https://arxiv.org/pdf/2610.22543v1)

## TLDR
SPOT accelerates diffusion language models losslessly by learning a tiny commit-order predictor that proposes a tree of candidate continuations from the target’s previous output distributions, which the target verifies in a single pass via coupled-noise matching—cutting target passes by up to 6.8× and reaching up to 3.2× standard decoding throughput while transferring across six DLMs.

## Abstract
Diffusion language models (DLMs) promise parallel text generation, but in practice face an unresolved speed-quality trade-off. Exact decoding fills in only one masked position per model pass, while faster multi-token decoding schemes are lossy. Speculative decoding is the standard lossless acceleration for autoregressive models. However, it does not transfer directly to DLMs, which must choose both what to generate and where. We show that this order is the missing piece: the model's own predictions from the previous pass already give the right token at 92-100% of positions, but not which position comes next. Based on this observation, we introduce Speculating Positions Order Trajectory (SPOT), which learns to predict this order. A 0.62M-parameter model reads only the target's output distributions and proposes a tree of candidate continuations, and the target verifies all of them in a single pass by checking whether each equals its own next state. On the verification side, our analysis shows that prior block-diffusion verification approaches either assume $T=0$ or a sequential proposal interface. To support tree-based speculation at any temperature, we propose using coupled-noise match verification for diffusion blocks, following shared-Gumbel-noise coupling approaches. Our comprehensive experiments show that SPOT cuts target passes by up to 6.8x and reaches up to 3.2x the throughput of standard decoding, beating the calibrated and training-free drafting baselines in every task and budget at $T=0$ and $T=1$. In addition, we show that the learned drafter transfers across models, demonstrating successful transfer across six different DLMs. Project page: https://eliezer318.github.io/SPOT-dLLM/
