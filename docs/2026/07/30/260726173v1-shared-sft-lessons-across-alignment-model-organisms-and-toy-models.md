# Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Anton de la Fuente, Arthur Conmy
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26173v1) · [PDF](https://arxiv.org/pdf/2607.26173v1)

## TLDR
This paper demonstrates that lessons about supervised fine-tuning (SFT) from one research area (alignment, model organisms, or toy models) can be successfully transferred to another, showing that training on the reason for a behavior improves generalization, mixing in benign on-model data preserves capabilities, and later benign SFT can erase trained behaviors.

## Abstract
Alignment training, model organisms, and toy models are usually treated as separate research areas. But projects in all three frequently use supervised fine-tuning (SFT) to pursue the same underlying goals. When projects share a goal, we should test whether lessons learned from one area transfer to the other areas. We study three such transfers, each taking a lesson developed in one SFT setting and testing it in another. First, we port a lesson about behavior generalization from alignment training into toy models. Training on the reason for a behavior, as in Teaching Claude Why, can make the behavior generalize better than training on examples of the behavior alone. Second, we port a lesson about capability preservation from model organisms into the Model-Spec Midtraining alignment setting. SFT on outputs written by a model other than the student (off-model outputs) can damage capabilities when trained on. Mixing in benign on-model (and on-policy) data into our training can prevent most of this damage while still embedding the target behavior. Third, we port a lesson about robustness from model organisms into the same alignment setting. We find that follow-up benign SFT can erase the alignment behavior while preserving capabilities, showing that capability preservation alone does not ensure robustness to subsequent training. Our work illustrates how porting SFT lessons between different research fields can uplift them all, suggesting more researchers should borrow techniques from outside their own areas.
