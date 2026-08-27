# MacroAgent: Regularity-Aware Macro Legalization with LLM-Agent-Designed Contour Algorithms

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jiaxi Jiang, Xufeng Yao, Yuxuan Zhao, Yuntao Lu, Peiyu Liao, Zuodong Zhang, Yibo Lin, Bei Yu
- 机构：Peking University, The Chinese University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24946v1) · [PDF](https://arxiv.org/pdf/2608.24946v1)

## TLDR
MacroAgent is a four-stage, LLM-agent-driven macro legalization framework that uses automatically designed regularity-aware contour algorithms to significantly improve layout regularity, reduce routed wirelength, and enhance PPA over state-of-the-art methods.

## Abstract
Macros constitute a large part of the core area in modern very large-scale integration (VLSI) designs. Moreover, macro positions have a significant impact on the final quality of result (QoR), and macro legalization is typically the final step in determining the macro positions. However, existing approaches related to macro legalization either lack robustness or incur substantial computational costs or neglect the regularity between macros. To address these limitations, we introduce MacroAgent. The novel framework is a four-stage approach: clustering, contour generation, template matching, and inter-cluster refinement. We propose leveraging Large Language Models (LLMs) to discover multiple, effective heuristic regularity-aware contour algorithms. This framework successfully generates robust and effective algorithmic solutions for macro legalization. Compared with state-of-the-art macro legalization works, experimental results on TILOS and Chipyard benchmarks demonstrate a 2 to 8 fold improvement in layout regularity, a 3% to 5% reduction in routed wirelength with comparable congestion after global routing, and significantly better robustness with an acceptable runtime. Furthermore, end-to-end evaluation through Cadence Innovus place-and-route confirms that the regularity improvements translate into tangible PPA gains, including 2.9% lower routed wirelength and 68.3% TNS improvement over the DREAMPlace macro legalization baseline; it also achieves 1.8% lower routed wirelength when integrated into the Innovus macro placement flow.
