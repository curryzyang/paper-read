# AI Mindmeld: A Latent Interconnect Protocol

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Siavash Golkar, Jake Kovalic, Shirley Ho
- 机构：Flatiron Institute, Polymathic AI, Princeton University, Yale University, New York University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30215v1) · [PDF](https://arxiv.org/pdf/2610.30215v1)

## TLDR
The paper introduces the Latent Interconnect Protocol (LIP), which trains lightweight connectors to inject frozen specialist-model representations directly into the internal states of frozen LLMs at multiple layers, enabling extensible, compositional, zero-shot latent information exchange—demonstrated by linking protein and small-molecule specialists to Gemma 3 and Kimi K2.6 without joint training.

## Abstract
LLMs can act as scientific agents using tools to consult specialists and run experiments. Yet specialist information must enter their context, generally as text, images, audio or video: a bottleneck between models with rich, high-dimensional representations. We advocate direct representation exchange: a mindmeld conveying many properties, including information an LLM would not think to request. It should be extensible to new specialists, flexible across questions and tasks, and compositional across independently connected specialists without joint training.
  The Latent Interconnect Protocol (LIP) learns connectors mapping specialist representations into LLM internal states. Training only connectors keeps this practical as LLMs grow and evolve. We connect three protein and three small molecule specialists to Gemma 3 (4B and 12B parameters) and Kimi K2.6 (1T total, 32B active), freezing all pretrained models. Independently trained connectors provide useful information without changing the LLM or existing connectors, supporting familiar and new question types about unseen objects. We demonstrate zero-shot transfer to cross-domain tasks without joint training. Task performance and compositionality generally improve with LLM capability, with especially strong gains in zero-shot task transfer. Limitations remain: current LLMs were not trained for specialist representations as native inputs; access does not ensure reliable interpretation, integration or use in reasoning. We call on specialist developers to provide consistent representation interfaces and, especially, on LLM developers to train models to receive, combine and reason with these inputs. These efforts could expand scientific agents' information while preserving conventional tools' flexibility.
  Data, pretrained connectors, and code for training, evaluation and interactive inference: https://github.com/PolymathicAI/AI-Mindmeld
