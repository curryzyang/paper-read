# ExFold: Unified Expert Folding for Training-Free MoE Prefill-Decode Acceleration

- 区域：速读区
- 排名：8
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Juntong Wu, Yifei Liu, Junyi Chen, Siqi Fan, Chaoran Feng, Minghao Li, Liujie Zhang, Weihang Chen, Li Yuan
- 机构：University of Electronic Science and Technology of China, Peking University, Xiaohongshu Inc., Shanghai Jiao Tong University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24938v1) · [PDF](https://arxiv.org/pdf/2608.24938v1)

## TLDR
ExFold is a training-free expert-folding framework that accelerates both MoE prefill and decode by projecting budget-excluded expert contributions onto retained experts via calibrated scalar projectors, achieving up to 1.41× TTFT and 2.45× TPOT speedups while preserving about 99% of model quality.

## Abstract
Mixture-of-Experts (MoE) models scale capacity for strong quality while keeping per-token compute bounded through sparse expert activation. Yet low-latency MoE serving is increasingly challenging, because it spans two inference phases with fundamentally different bottlenecks: prefill is dominated by token-wise expert computation, whereas decode is constrained by memory traffic from the batch-wise activated expert set. However, existing training-free acceleration methods optimize only a single resource proxy, either the experts each token executes or the experts a batch activates, and either discard the excluded experts' contribution or leave it only implicitly approximated. In this paper, we propose ExFold, a unified training-free expert-folding framework for jointly accelerating MoE prefill and decode. ExFold casts both prefill and decode as one budgeted output-approximation problem: execute only a phase-specific constrained expert set while projecting the contribution of budget-excluded experts onto retained experts using calibrated scalar projectors. Motivated by the observation that many expert outputs are directionally aligned but differ in magnitude, ExFold calibrates a pairwise scalar-projector matrix on unlabeled data and uses it at inference time to fold excluded expert contributions into retained experts. Under this view, prefill acceleration becomes token-level Top-K folding, and decode acceleration becomes batch-level expert-pool folding. The two phases differ only in how retained experts are selected, while excluded contributions are recovered by one shared folding mechanism. We implement ExFold as a plug-and-play plugin in vLLM, with a lightweight expert-folding CUDA kernel, delivering up to 1.41x TTFT and 2.45x TPOT speedups while retaining about 99% of the original average quality.
