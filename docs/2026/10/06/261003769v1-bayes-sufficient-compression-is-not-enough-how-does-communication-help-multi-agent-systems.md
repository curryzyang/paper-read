# Bayes-Sufficient Compression Is Not Enough: How Does Communication Help Multi-Agent Systems?

- 区域：速读区
- 排名：13
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Yi Xie, Zhanke Zhou, Yi Fan, Yong Ge, Bo Han, Bo Liu
- 机构：University of Arizona, Hong Kong Baptist University, Amazon Web Services
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03769v1) · [PDF](https://arxiv.org/pdf/2610.03769v1)

## TLDR
This paper introduces receiver-relative bounded coordination to show that in multi-agent LLM systems a compressed message helps only when its receiver gain exceeds protocol tax and omitted-information/decoder-mismatch costs, so even Bayes-sufficient compression can fail due to bounded decoding and action-closure errors—motivating an inference-time selector that improves the accuracy-cost frontier.

## Abstract
Multi-agent LLM systems pair a sender with broad context and an executor with a limited local view. We study when a short message improves the executor's next decision, when raw context is preferable, and when a stronger sender helps. Our framework, \emph{receiver-relative bounded coordination}, expresses message utility as receiver gain minus protocol tax. Compression beats raw context when tax savings exceed losses from omitted information and decoder mismatch. Even \emph{Bayes-sufficient} compression can fail when a bounded executor cannot use its surface form. A three-stage decomposition separates externalization, absorption, and \emph{action closure}, explaining how errors remain after the correct content reaches the receiver. Under a single-crossing condition, sender upgrades help above a receiver-burden threshold. Across six benchmarks, the same Qwen protocol raises ContextBench joint accuracy from $0.633$ to $0.775$ but lowers ToolSandbox from $0.889$ to $0.653$. Fixed-message replay reveals closure failures despite correct artifact recovery. These results guide an inference-time selector that improves the accuracy-cost frontier on the evaluated communication regimes.
