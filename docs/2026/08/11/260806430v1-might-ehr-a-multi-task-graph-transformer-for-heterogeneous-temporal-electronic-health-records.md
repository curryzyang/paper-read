# MiGHT-EHR: A Multi-task Graph Transformer for Heterogeneous Temporal Electronic Health Records

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Anirudh Rayas, Yuan Wang, Pavan Turaga
- 机构：University of South Carolina, Arizona State University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06430v1) · [PDF](https://arxiv.org/pdf/2608.06430v1)

## TLDR
MiGHT-EHR introduces a unified multi-task graph transformer that jointly models heterogeneous clinical entities, temporal patient trajectories, and shared task dependencies in EHRs, outperforming state-of-the-art methods on drug recommendation, length-of-stay, mortality, and readmission prediction across MIMIC-III and MIMIC-IV.

## Abstract
Learning from Electronic Health Records (EHRs) has gained significant attention due to its potential to improve clinical prediction. However, effective learning remains challenging because EHRs encode heterogeneous, temporally ordered clinical interactions. In particular, EHRs contain: (i) heterogeneous clinical entities, including patients, visits, diagnoses, prescriptions, and procedures, together with their heterogeneous interactions, (ii) longitudinal patient trajectories across hospital visits and (iii) shared statistical dependencies across related clinical prediction tasks. Existing EHR learning methods capture only a subset of these properties. To bridge this gap, we propose Multi-task Graph transformer for Heterogeneous Temporal EHRs (MiGHT-EHR), which jointly models all three within a unified representation learning method. MiGHT-EHR constructs a heterogeneous graph from EHRs in which nodes represent clinical entities and edges connect statistically associated entities identified via normalized point-wise mutual information. Across MIMIC-III and MIMIC-IV datasets, MiGHT-EHR outperforms state-of-the-art methods on average across four tasks: drug recommendation, prediction of length-of-stay, mortality, and readmission, with particularly strong improvements in mortality and readmission prediction. Furthermore, a post-hoc analysis of the learned representations reveals that patient neighborhoods are organized by clinical outcomes, salient medical concepts are recoverable as linear directions in the representation space, and task probabilities are well calibrated. Collectively, these findings demonstrate that MiGHT-EHR representations support diverse prediction tasks while preserving clinically interpretable structure.
