# Coverage, Not Difficulty, Sets How Much Synthetic Data an Activation Probe Needs

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Ankush Checkervarty
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10594v1) · [PDF](https://arxiv.org/pdf/2610.10594v1)

## TLDR
Coverage—not per-kind difficulty—determines how much synthetic data an activation probe needs: concepts whose data kinds transfer poorly (e.g., instruction following) require far more samples than those where one kind covers the others (e.g., high-stakes).

## Abstract
Activation probes that monitor deployed language models are trained on synthetic conversations, and how many a probe needs is open. We trace learning curves over 10-590 synthetic samples for three monitoring concepts, high-stakes situations, replies harmful to a person, and replies that do not follow the user's instruction, on fourteen held-out evaluation distributions and four probe models, varying the generator LLM and the prompt's detail. The need is set by what is monitored: probes for high-stakes and harmful are within a few hundredths of their plateau from 80 samples on Gemma-3-27B-IT, instruction probes need several times as many, and the ordering holds on three smaller probe models and on real samples (from dev set). Prior work advises spending a generation budget on breadth, more kinds of data, over depth, more of each kind. We read the depth a concept needs as the half-gain size of a fitted curve, the number of samples at which half the gain is in hand. Concept and distribution account for 42-45% of its variance, the generator, probe model, and prompt detail for under 10%. What sets the value of the half-gain size is coverage, not per-kind difficulty: the number of samples of its own kind a distribution needs to saturate. Every kind, one per evaluation distribution, has a median half-gain size of 7-11 own-kind synthetic samples under all three concepts alike. What differs is how far samples of one kind transfer to the concept's other kinds, almost fully under high-stakes, less under harmful, and least under instruction, which accounts for most of the gap between concepts on generated and real samples. Breadth therefore pays differently by concept: many kinds are necessary under instruction, where no kind covers another, and nearly redundant under high-stakes, where one kind covers the rest. We release the evaluation suites, dev sets, and generated sets.
