# Don't Retrain, Remix: Adaptation of Web Agents using Mixture Hypernetworks

- 区域：速读区
- 排名：13
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Md Farhan Ishmam, Minh Pham Dinh, Kenneth Marino
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22539v1) · [PDF](https://arxiv.org/pdf/2610.22539v1)

## TLDR
WebMix adapts web agents to unseen or redesigned websites without retraining by using a scout agent to summarize the target interface and a lightweight router to compose previously trained low-rank adapters into a new adapter, matching or outperforming in-context learning and LoRA baselines.

## Abstract
The web is not static or uniform. Websites that serve the same purpose can look and navigate very differently. Even within a single site, successive redesigns can change how familiar features are presented and accessed. Humans adapt to this by recognizing familiar interaction patterns and reusing what they already know. We give web agents a similar ability with WebMix, a mixture hypernetwork that adapts them to unseen interfaces by composing previously trained low-rank adapters. WebMix begins with a bank of adapters trained on source interfaces. At deployment, a scout agent explores the target interface and summarizes its observations into a compact manual. A lightweight router uses this manual to predict mixing coefficients over the adapter bank, which combine the existing adapters into a new one for inference. Adapting to a new interface takes only a scouting run and a forward pass, without gradient updates on the target. With Qwen and Llama models, we evaluate domain transfer on TimeWarp and WebArena-Lite-v2, and version transfer on TimeWarp. In all three settings, WebMix matches or outperforms in-context learning and LoRA baselines, often matching the average success of specialists trained directly on those interfaces. On TimeWarp domain transfer, it gains about 8 percentage points on average over the best baseline with both models. These gains do not come at the cost of seen interfaces, where WebMix keeps its lead, and extend to version transfer. Adapting to a new interface can therefore rely on exploration and composition instead of retraining.
