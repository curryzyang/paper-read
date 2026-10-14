# LabInstruct: Benchmarking Situated Instructional Video Generation for Lab Procedures

- 区域：速读区
- 排名：6
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yuming Fu, Weijia Wu, Jing Chen, Jiahao Tang, Feifei Chen, Hongyu Zhu, Xin Jin, Alex Jinpeng Wang
- 机构：Central South University, National University of Singapore, Monash University, Chinese Academy of Sciences, Beijing University of Posts and Telecommunications
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14020v1) · [PDF](https://arxiv.org/pdf/2610.14020v1)

## TLDR
LabInstruct introduces a 204-task, 5-discipline benchmark for generating situated laboratory instructional videos from workspace images and natural-language instructions, revealing through evaluations of 8 frontier image-to-video models that visually plausible outputs are often procedurally incorrect and thus insufficient for reliable experimental guidance.

## Abstract
Self-driving laboratories (SDLs) aim to automate the full experimental loop, from scientific decision-making to physical execution. Ideally, AI-generated plans could be carried out directly by robotic systems, but reliable automation remains difficult in complex, open-world laboratory environments, where experiments often involve fine-grained manipulation, long-horizon procedures, and substantial variation across tasks and setups. Humans therefore remain an important execution interface between AI-generated plans and physical experiments, creating a need for clear and effective human-facing experimental guidance. Because laboratory procedures are inherently visual, spatial, and dynamic, video is particularly well suited to communicating apparatus configurations, manipulation actions, temporal dependencies, and state changes. Recent advances in video generation now make it possible to synthesize experimental demonstrations directly from an initial workspace image and a natural-language instruction. However, whether such models can reliably communicate real laboratory procedures has not been systematically studied. We introduce LabInstruct, a benchmark for situated instructional video generation in real laboratories. LabInstruct contains 204 tasks across 5 scientific disciplines, with real reference executions and structured annotations of objects, actions, contacts, and state transitions. Evaluating 8 frontier image-to-video models, we find that visually plausible generations frequently remain procedurally incorrect, revealing a substantial gap between visual realism and the reliability required for experimental instruction.
