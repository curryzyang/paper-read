# When Keywords Drop but Classifiers Hold: Soft Refusals under KV Cache Compression

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Kang Chen, Xiuze Zhou, Hong Chen, Yuanguo Lin
- 机构：Jimei University, Wenzhou-Kean University, The Hong Kong University of Science and Technology (Guangzhou)
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31678v1) · [PDF](https://arxiv.org/pdf/2609.31678v1)

## TLDR
Under KV cache compression, keyword-based refusal monitors can show large drops even when stronger classifiers and human judgments still treat the same outputs as refusals, so safety auditing under compressed inference should rely on multiple judges matched to the serving context rather than keyword rates alone.

## Abstract
KV cache compression is widely used for long context LLM inference under memory constraints, while deployed systems typically score refusals after generation with keyword filters or learned classifiers. Such monitors are intended to indicate whether a model declined a harmful request under the serving regime actually used. However, it remains unclear whether matched compression that preserves task accuracy also preserves agreement between lightweight lexical monitors and stronger refusal classifiers. We study this with a paired protocol on n=200 harmful prompts with a long filler context: each prompt is answered once under full retention and once under matched eviction after a shared prefill, and the same replies are scored by keyword heuristics, the HarmBench Llama-2-13B classifier, an auxiliary LLM judge, and humans on disagreements. On Qwen2.5-3B, keyword refusal falls from 98.0% to 80.5% (McNemar p~1e-8) while classifier refusal stays near ceiling (99.0%-99.5%) and MMLU accuracy is unchanged (50.0%); human labels predominantly follow the classifier, consistent with soft refusals. The gap is not universal and weakens under short fillers and paired SnapKV, so safety auditing under compression should rely on several judges matched to the serving context rather than on keyword rates alone.
