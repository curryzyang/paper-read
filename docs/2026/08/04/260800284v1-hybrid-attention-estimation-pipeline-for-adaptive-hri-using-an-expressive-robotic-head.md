# Hybrid Attention Estimation Pipeline for Adaptive HRI Using an Expressive Robotic Head

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Pablo Moraes, Monica Rodriguez, Christopher Peters, Hiago Sodre, Tobias Doernbach, Bruna Guterres, Ricardo Grando
- 机构：Technological University of Uruguay, Ostfalia University of Applied Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00284v1) · [PDF](https://arxiv.org/pdf/2608.00284v1)

## TLDR
The paper presents a hybrid visual attention estimation pipeline for an expressive robotic head that combines a fast geometric perception layer with a vision-language semantic observer to enable state-based adaptive human-robot interaction, demonstrating reliable attention-aware pause and resume behaviors across 40 trials.

## Abstract
This paper presents an applied case study on hybrid visual attention estimation for human-robot interaction using an expressive robotic head based on the InMoov ecosystem. The proposed pipeline combines a fast geometric perception layer with an independent semantic perception layer based on a vision-language model. The geometric layer provides high-frequency face and head-pose information for temporal regulation, while the semantic layer receives only raw egocentric camera frames and produces contextual attention labels related to attention toward the robot, phone use, or attention elsewhere. These signals are integrated through a finite state machine that regulates adaptive interaction behavior, including activation, waiting, interaction resumption, and return to rest. The system was evaluated with 10 participants across 40 trials covering baseline and adaptive interaction conditions. Results show reliable interaction start across all trials, consistent pause behavior in the adaptive distraction condition, and non-redundant semantic information between the geometric and semantic outputs.
