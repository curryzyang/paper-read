# GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ruiyang Wang, Hao-Lun Hsu, Swarajh Mehta, Jiwoo Kim, Zhihao Dou, Miroslav Pajic
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.19315v1) · [PDF](https://arxiv.org/pdf/2609.19315v1)

## TLDR
GAVEL introduces an explicit graph world model that verifies, simulates, and repairs long-horizon LLM-generated robot plans—falling back to LLM replanning only for semantic failures and using probabilistic object-location beliefs to reorder multi-task subtasks under partial observability—boosting BEHAVIOR-1K success from 41.2% to 91.8% on single tasks and 19.9% to 92.6% on multi-task instructions with Qwen3-8B.

## Abstract
Large language models (LLMs) provide a flexible interface for long-horizon robot planning, but generated plans often fail to respect embodiment constraints, recover from planning errors, or reason effectively under partial observability. We present GAVEL, a framework for verifying and repairing long-horizon LLM planning built around an explicit graph world model. The graph represents relevant object-relations, action pre-conditions and effects, and probabilistic beliefs over unobserved object locations. This model can predict the consequences of LLM-generated actions before execution, detect violations, and repair those whose corrections follow directly from the world model. This method also reserves LLM replanning solely for errors requiring semantic reasoning. For multi-task instructions, GAVEL reasons over distributions of possible object locations to reorder remaining subtasks and minimize expected search cost. We evaluate GAVEL on BEHAVIOR-1K across 100 single long-horizon tasks and 500 multi-task instructions. With Qwen3-8B, GAVEL improves single-task success from 41.2% to 91.8% and multi-task success from 19.9% to 92.6%. Distributional belief reasoning also reduces travel distance by approximately 5.4% compared with a static variant. These improvements show that an explicit graph world model harness can substantially improve the reliability and efficiency of long-horizon embodied planning across compact and frontier hosted LLM capabilities.
