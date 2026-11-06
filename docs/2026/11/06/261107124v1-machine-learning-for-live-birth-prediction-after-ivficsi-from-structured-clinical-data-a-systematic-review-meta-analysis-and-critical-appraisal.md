# Machine Learning for Live-Birth Prediction After IVF/ICSI From Structured Clinical Data: A Systematic Review, Meta-Analysis, and Critical Appraisal

- 区域：速读区
- 排名：13
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Abdul Raheem Shahzad, Muhammad Zaheer Khan, Umar Ajaib, Asad Ur Rehman, Juan Deng, Ming Zhang
- 机构：Zhongnan Hospital of Wuhan University, Clinical Medicine Research Center of Prenatal Diagnosis and Birth Health in Hubei Province, Wuhan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07124v1) · [PDF](https://arxiv.org/pdf/2611.07124v1)

## TLDR
**TLDR:** In a systematic review and meta-analysis of 48 studies, machine-learning models predicting live birth after IVF/ICSI from structured clinical data achieved pooled AUCs of 0.814 for internal validation and 0.756 for external/temporal validation—with extreme heterogeneity, mostly high/unclear risk of bias, low-to-very-low certainty, and no demonstrated clinical impact—and only modest gains over logistic regression (0.056 AUC) that came from aligning predictions with decision points and local calibration rather than deeper architectures.

## Abstract
Machine-learning models predicting live birth after in vitro fertilisation (IVF) or intracytoplasmic sperm injection (ICSI) from routine clinical data report performance from near chance to near perfect. We systematically reviewed these models under PRISMA 2020, searching OpenAlex, Scopus and Web of Science to 22 October 2026, appraised them with PROBAST+AI and TRIPOD+AI, and pooled their discrimination with random-effects meta-analysis on the logit scale. We define what fixes the meaning of a model's output (decision point, endpoint, unit of analysis, data source) and map the 48 included studies by model family, decision point and validation design. Models evaluated only internally pooled to an area under the receiver operating characteristic curve (AUC) of 0.814, against 0.756 (95% prediction interval 0.546-0.889) for models evaluated on a later period or another centre, and 0.764 for studies not at high risk of bias; neither difference was significant, and heterogeneity was extreme. Models whose decision point was not stated pooled to 0.910, the only significant moderator in meta-regression. Against logistic regression fitted to the same data, the best machine-learning model gained a pooled 0.056 AUC (95% CI 0.017-0.090). Of 48 studies, 47 were at high or unclear risk of bias, only four assessed the calibration slope, and no model has evidence of clinical impact. The certainty of the pooled evidence is low to very low; the gains that survive validation came from staging predictions to decision points and local calibration, not deeper architectures. We provide a TRIPOD+AI-mapped checklist, a benchmark specification and a research agenda.
