# Depth-Linked Residual Tokens for Multimodal Retrieval and Generation

- 区域：速读区
- 排名：4
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Jiangfan Zhang, Wentao Bao, Xian Wu, Xiangjun Fan, Jianpeng Cheng, Jun Xiao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26752v1) · [PDF](https://arxiv.org/pdf/2611.26752v1)

## TLDR
**TLDR:** Depth-Linked Residual Tokens (DepThink) is a single-pass multimodal framework that appends K learnable residual tokens coupled by a lightweight learned recurrence to progressively capture complementary information, matching or outperforming looped architectures for retrieval and generation while significantly accelerating training and inference.

## Abstract
Iterative architectures such as looped language models improve parameter efficiency and reasoning capacity of transformers, yet their sequential backbone iterations introduce substantial computational latency. Conversely, parallelizable learnable special tokens (such as the register tokens in Vision Transformer) enable efficient single-pass inference, but often suffer from the absence of sequential refinement and exhibit redundant representations across tokens. To address these challenges, we introduce Depth-Linked Residual Tokens (DepThink), an efficient framework designed for multimodal retrieval and generation. Operating within a single pre-filling forward pass, DepThink appends a sequence of K learnable residual tokens whose hidden states are coupled through a lightweight, learnable residual recurrence. This mechanism enables each residual token to progressively capture complementary information missed by preceding tokens. Theoretically, we prove that DepThink provides strictly expanded geometric directional reachability over standard learnable tokens and guarantees a provable one-step descent advantage. We evaluate DepThink across multimodal retrieval and generation tasks. DepThink consistently outperforms learnable-token baselines and matches or exceeds looped architectures across dense (2B, 8B) and sparse mixture-of-experts (30B-A3B) backbones under both LoRA and full-parameter fine-tuning, while accelerating training by up to 11.9 and inference by 4.3 over looped architectures.
