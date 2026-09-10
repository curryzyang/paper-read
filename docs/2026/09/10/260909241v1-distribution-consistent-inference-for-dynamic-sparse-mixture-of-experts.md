# Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts

- 区域：速读区
- 排名：8
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Dohyeon Kim, Bedionita Soro, Sung Ju Hwang
- 机构：DeepAuto.ai, KAIST
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09241v1) · [PDF](https://arxiv.org/pdf/2609.09241v1)

## TLDR
The paper shows that dynamic top-k routing in sparse Mixture-of-Experts LLMs causes a correctable distributional shift—increased RMS scale and variance in layer outputs—and proposes Layer-wise Distribution Alignment (LDA), a lightweight inference-time correction that aligns reduced-routing representations with the default top-k distribution to recover performance while preserving efficiency.

## Abstract
Mixture-of-Experts (MoE) architectures have emerged as a powerful paradigm for scaling model capacity while preserving efficient inference in large foundation models. However, most MoE models use a fixed top-$k$ expert selection policy, assigning the same expert budget to every token even when fewer experts may be sufficient. Inference-time dynamic top-$k$ routing can reduce computation without retraining, but existing methods often overlook the distributional shift caused by deviating from the training-time routing configuration. We show that reducing the number of activated experts consistently increases the RMS scale and variance of SMoE outputs, inducing a representation mismatch that contributes to downstream performance degradation in addition to the loss of expert capacity. To address this correctable component, we propose Layer-wise Distribution Alignment (LDA), a lightweight inference-time correction that uses layer-wise calibration statistics to align reduced-routing representations with the default configuration. Across multiple SMoE LLMs, benchmarks, and routing strategies, LDA recovers much of the performance lost induced by the distributional shift under reduced routing while preserving sparse-inference efficiency with negligible overhead.
