# Efficient Omni-modal Large Language Model Inference via Per-Query Modality Selection

- 区域：速读区
- 排名：10
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Shuqi Liu, Yuzhou Cao, Luke Ong
- 机构：Nanyang Technological University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31768v1) · [PDF](https://arxiv.org/pdf/2610.31768v1)

## TLDR
This paper proposes a cost-sensitive per-query modality selection framework that adaptively chooses which modalities to provide to a fixed Omni-LLM, improving the accuracy–cost trade-off and matching full-modality accuracy with substantially lower input tokens, latency, and monetary cost.

## Abstract
Omni-modal large language models (Omni-LLMs) can jointly process a broad range of modalities, such as text, audio, and video, enabling stronger multimodal understanding and reasoning capabilities, but often at substantial inference cost. We observe that the benefit of additional modalities varies across queries, indicating that a fixed modality configuration can be inefficient. Motivated by this, we study query-wise modality selection, which keeps the underlying Omni-LLM fixed while adaptively selecting which modalities to provide for each query. We formulate the problem as an accuracy-cost optimization problem and develop a cost-sensitive learning approach for modality selection. We evaluate our approach on WorldSense using Qwen2.5-Omni and Qwen3-Omni under three inference-cost measures: input tokens, latency, and monetary cost. Across both models, query-wise modality selection consistently improves the accuracy-cost trade-off and can even outperform the standard setting in which all available modalities are provided to the Omni-LLM. For Qwen2.5-Omni, our cost-sensitive approach matches or exceeds this full-modality accuracy while requiring only approximately 41% of the input tokens, 39% of the latency, and 61% of the monetary cost.
