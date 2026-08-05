# CT-HEG: A Bidirectional, Timestamp-Attributed Event Graph for ICU In-Hospital Mortality Prediction - An Architectural Ablation Study

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Mohammad Nasir Uddin, Rahnuma Tabassum Orpita, Asaduzzaman Anik, Eklachur Rahman Bhuiyan, Marjahan Risalat, SM Wali Ullah, Asif Ahamed
- 机构：Westcliff University, Washington University of Science and Technology, Northern University Bangladesh, Stanton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02663v1) · [PDF](https://arxiv.org/pdf/2608.02663v1)

## TLDR
TLDR: This paper introduces CT-HEG, a continuous-time heterogeneous event graph for ICU mortality prediction, and shows via ablations on MIMIC-IV that bidirectional edges are structurally essential and timestamp-attributed edge features improve AUROC, while collapsing heterogeneous edge types can actually match or beat the full model.

## Abstract
Accurate ICU mortality prediction requires modeling irregular clinical observations across heterogeneous entity types. Existing sequence models handle irregular sampling but ignore typed relational structure; existing graph models assume fixed-interval inputs. We introduce the Continuous-Time Heterogeneous EHR Graph (CT-HEG) schema and evaluate which architectural choices drive predictive performance. CT-HEG encodes each ICU stay as a typed, timestamped graph with three node types (visit, vital, lab_event) and 2D edge attributes (t_hours/48, value_norm) encoding timing and value without imputation. We instantiate CT-HEG as CHIRP-Net, a four-layer heterogeneous GATv2Conv network, evaluated on MIMIC-IV v3.1 (31,142 ICU stays, LOS>=48h, 13.4% mortality) with five seeds and bootstrapped confidence intervals, against logistic regression, mTAND, a Transformer, and GRU-D, plus an ablation study. CHIRP-Net achieved 5-seed mean AUROC 0.8449+/-0.0071 (AUPRC 0.4958+/-0.0209); the ensemble achieved AUROC 0.8618 (95% CI: 0.8485-0.8745). Removing reverse edges disconnected observation nodes from the visit readout, cutting AUROC by 0.1968+/-0.0073. Time-attentive edge features contributed 0.0247+/-0.0093 AUROC. Collapsing heterogeneous edge types into one relation (7x fewer parameters) outperformed the full model on all seeds. Post-calibration ECE was 0.0307. Temporal and demographic subgroup analyses were explored but not reported here, pending follow-up work. Bidirectional connectivity was necessary for the model to use its inputs at all, and CT-HEG was reasonably well calibrated after validation-fitted temperature scaling. These results support CT-HEG for irregular EHR data, while external validation, a pre-specified temporal evaluation, and a demographic fairness audit remain necessary before any claim of robustness. Code: https://github.com/nasiruddinstudents-ctrl/chirp-net-mimic-iv.
