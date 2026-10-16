# Same Answer, New Box: How Much of RLVR's Out-of-Domain Gain Is Answer Format?

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Zongye Lyu
- 机构：Monash University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20639v1) · [PDF](https://arxiv.org/pdf/2610.20639v1)

## TLDR
Much of RLVR’s reported out-of-domain multiple-choice gain is an answer-format artifact—82% of it on four released 7B SimpleRL base–RL pairs disappears when the same outputs are re-scored with a format-agnostic extractor, because RL mainly moves already-correct answers into `\boxed{}` where public harness extractors look first.

## Abstract
Reinforcement learning with verifiable rewards (RLVR) is credited with gains beyond the domain its rewards check, such as higher MMLU accuracy after training on mathematics. Such accuracies are usually read out of the model's text by an answer extractor. A model that learns to write its answer where the extractor looks can therefore score higher without answering better. We measure how much of the gain reported by extractors copied from public code arises this way. We generate outputs from a base model and its RL model and score them twice: with those extractors, and with one extractor of our own that reads a stated answer whether it is in the answer box \boxed{} or in the text. On four released 7B SimpleRL base-RL pairs, 82% of the out-of-domain multiple-choice gain that these extractors report disappears under ours: it is a gain in answer format, not in answers. The base models already state most of their answers in text, and RL moves them into the box, where these extractors look first. Independent LLM readers, in place of our extractor, put the figure at 77%. With a prompt that itself asks for the box, our extractor puts it at 79%. On a 32B pair trained with another recipe, almost none of the reported gain is format gain: its base model boxes its answers when asked, and its RL model rarely does when not. A reported gain is partly a property of the extractor that read it, and re-scoring stored outputs with a second extractor shows how much, without re-running RL.
