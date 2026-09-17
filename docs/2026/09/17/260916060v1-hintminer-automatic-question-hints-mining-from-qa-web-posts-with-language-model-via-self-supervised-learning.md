# HintMiner: Automatic Question Hints Mining From Q&A Web Posts with Language Model via Self-Supervised Learning

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Zhenyu Zhang, JiuDong Yang
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16060v1) · [PDF](https://arxiv.org/pdf/2609.16060v1)

## TLDR
HintMiner is a self-supervised language-model-based tool that mines relevant Q&A web posts and uses a transformer encoder-decoder with copying mechanisms to automatically generate helpful hints for user questions, achieving strong results on 60,000 Stack Overflow questions.

## Abstract
Users often need ask questions and seek answers online. The Question - Answering (QA) forums such as Stack Overflow cannot always respond to the questions timely and properly. In this paper, we propose HintMiner, a novel automatic question hints mining tool for users to help them find answers. HintMiner leverages the machine comprehension and sequence generation techniques to automatically generate hints for users' questions. It firstly retrieve many web Q\&A posts and then extract some hints from the posts using MiningNet that is built via a language model. Using the huge amount of online Q\&A posts, we design a self-supervised objective to train the MiningNet that is a neural encoder-decoder model based on the transformer and copying mechanisms. We have evaluated HintMiner on 60,000 Stack Overflow questions. The experiment results show that the proposed approach is effective. For example, HintMiner achieves an average BLEU score of 36.17\% and an average ROUGE-2 score of 36.29\%. Our tool and experimental data are publicly available.
