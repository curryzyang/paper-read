# Two Timescales of Forgetting in Fine-tuning of Language Models: Fast Behavioral Suppression and Slow Representational Drift

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Yilin Luo, Jin Hwa Lee, Andrew M. Saxe, Antonio Sclocchi
- 机构：University College London, Université Paris-Saclay, Principia
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33302v1) · [PDF](https://arxiv.org/pdf/2611.33302v1)

## TLDR
Fine-tuning language models on restricted data causes two-timescale forgetting: deleted-rule behavior is suppressed quickly while its underlying representations remain intact, and those representations are erased only later through slow parameter drift—a pattern also observed in natural-language fine-tuning.

## Abstract
Today, a core pipeline of artificial intelligence systems is pretraining on a broad range of text corpora and then fine-tuning on specific tasks or desired behaviors. Yet we still have limited understanding of how fine-tuning on a restricted data distribution modifies representations acquired during pretraining. In particular, it remains unclear whether surface behavioral suppression happens together with the erasure of latent representations that support it. In this work, we study supervised fine-tuning (SFT) by pretraining transformers on a controlled context-free grammar with hierarchical latent structure, the Random Hierarchy Model (RHM), and fine-tuning with a restricted subset of its generative rules. While during pretraining the model's ability to generate with the correct grammar rules coincides with building the internal representations of the corresponding latent, we find that SFT exhibits a very different dynamics: (i) the generation of deleted rules changes on a fast timescale inversely proportional to the magnitude of the token-latent correlation; meanwhile, their corresponding representations stay intact; (ii) the hidden representations of the deleted rules become forgotten on a much longer timescale, associated with a slow drift of the network parameters. Finally, we observe analogous results in a realistic setup with natural language, suggesting that this timescale separation in forgetting is a more general phenomenon of fine-tuning language models.
