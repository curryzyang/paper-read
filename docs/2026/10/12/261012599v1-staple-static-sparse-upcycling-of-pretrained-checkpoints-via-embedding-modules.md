# STAPLE: Static Sparse Upcycling of Pretrained Checkpoints via Embedding Modules

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ranajoy Sadhukhan, Euijin Hong, Sheng Cao, Zechun Liu, Shuowei Jin, Sha Li, Changlong Yu, Xin Liu, Qin Lu, Zhenyu Shi, Priyanka Nigam, Beidi Chen
- 机构：Amazon Research, Meta AI, D. E. Shaw Research, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12599v1) · [PDF](https://arxiv.org/pdf/2610.12599v1)

## TLDR
STAPLE is a static sparse upcycling method that augments pretrained LLM checkpoints by retaining their FFN up-projections and adding token-indexed embedding tables as a zero-initialized residual pathway, enabling sample-efficient, scalable performance gains over continued dense training and MoE upcycling while preserving training and serving efficiency via CPU offloading.

## Abstract
Sparse computation can scale the parametric capacity of LLMs without proportionally increasing active computation, but pretraining sparse architectures remains expensive and data-hungry. Existing sparse upcycling methods mainly target Mixture-of-Experts models, where expert homogeneity, sample inefficiency, and system overheads can limit practical scalability. Static sparse memory offers predictable access and token-specific updates that can help address these challenges, but naively integrating it into pretrained computation yields poor returns. In this work, we introduce STAPLE, a recipe built upon STEM for integrating static sparse memory into pretrained models. Whereas STEM replaces FFN up-projections with token-indexed embeddings, STAPLE retains them and adds the embeddings as a residual pathway, preserving pretrained computation while learning complementary token-specific information in a scalable manner. On OLMo-2 1B, STAPLE improves over continued dense training by 4.27 points on HumanEval, 2.80 on MBPP, 2.27 on GSM8K, and 1.65 on DROP. Average performance increases with static capacity, and improvements persist on the larger OLMo-2 7B backbone. STAPLE also outperforms static sparse baselines such as STEM and an Engram-style model, and achieves a higher average score than an MoE upcycling baseline while decoding 2x faster with less than half its GPU model memory and measured GPU energy per token in our throughput-oriented decoding evaluation. Importantly, despite introducing billions of parameters late in training, our host-offloaded implementation keeps generation throughput within 1.5% and training throughput within 3% of the dense baseline, while caching only the ~5% most frequent embeddings on GPU. These results show that static sparse memory can provide a sample-efficient, scalable, and sustainable path for expanding pretrained models without sparse pretraining from scratch.
