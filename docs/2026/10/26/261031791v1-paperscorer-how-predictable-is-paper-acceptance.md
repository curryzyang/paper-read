# PaperScorer: How Predictable Is Paper Acceptance?

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Sachin Konan, Jonathan Liu, Zhuang Liu
- 机构：Princeton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31791v1) · [PDF](https://arxiv.org/pdf/2610.31791v1)

## TLDR
PaperScorer demonstrates that anonymized paper content—especially page images—contains a robust but limited, calibrated signal for predicting peer-review acceptance (68% on ICLR and 77% on arXiv), with accuracy concentrated on clearly low- or high-rated papers while mid-rated papers remain largely unpredictable.

## Abstract
Automated research is largely evaluated by benchmark performance, but the value of research rarely reduces to a single score. Humans judge a work's holistic contribution through peer review, which is hard to model because it is noisy and depends on many factors. However, what if, given only the paper, we could predict its peer-review decision directly? We introduce PaperScorer, a family of models that predict a paper's accept or reject decision from its extracted text or page screenshots, training only on the decision after removing author identity and formatting shortcuts. Vision models are the most predictive (68% accuracy on ICLR papers and 77% on ML papers from arXiv), beating text-only and frontier reasoning models. Unlike plain text, page images retain figures, layout, and presentation. This signal is robust, surviving smaller models and even compressing the whole paper into a single image. But accurate predictions are not evenly spread. PaperScorer is strongest on the lowest and highest rated papers, while papers rated in the middle stay unpredictable for our models and frontier systems alike. Additionally, its confidence is calibrated, so its most confident predictions are also its most accurate. Overall, PaperScorer shows how much of the decision a paper carries on its own, marking a first step toward AI-driven research evaluation.
