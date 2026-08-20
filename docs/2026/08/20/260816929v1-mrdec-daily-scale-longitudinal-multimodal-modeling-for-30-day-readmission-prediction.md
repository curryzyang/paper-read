# Mr.Dec: Daily-Scale Longitudinal Multimodal Modeling for 30-Day Readmission Prediction

- 区域：速读区
- 排名：11
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Minjun Kim, Jong Hak Moon
- 机构：Yeji X
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16929v1) · [PDF](https://arxiv.org/pdf/2608.16929v1)

## TLDR
Mr.Dec proposes a daily-scale multimodal Transformer decoder that models hospital admissions as chronological sequences of daily EHR and intermittent chest X-ray events, achieving state-of-the-art 30-day readmission prediction with diagnosis-aware contrastive learning and clinically interpretable "Critical Days" identification.

## Abstract
Predicting 30-day hospital readmission is essential for assessing patient stability and optimizing healthcare resources. As clinical risk evolves with the accumulation of evidence during hospitalization, capturing these dynamic trajectories is essential. However, many existing approaches compress the complex longitudinal history into fixed representations, often losing the granular, day-level clinical signals that reflect a patient's evolving physiological state. To address this, we propose Mr.Dec (Multimodal Readmission-risk prediction Decoder), which models each admission as a natural chronological sequence of daily multimodal events. By leveraging a Transformer Decoder, Mr.Dec integrates daily Electronic Health Record(EHR) updates and intermittent Chest X-ray(CXR) findings in a time-aligned stream, reflecting the actual clinical workflow. To ensure robustness, we utilize Disease-Specific Supervised Contrastive Learning as an auxiliary regularization to induce a diagnosis-aware structure in the latent space. Evaluations on the MIMIC-IV and MIMIC-CXR datasets show that Mr.Dec achieves state-of-the-art performance by preserving the integrity of the clinical sequence. Furthermore, our model identifies "Critical Days" within an admission, providing actionable and clinically grounded interpretations for real-time risk stratification. Code is available at: https://github.com/yejix-ai/MR.DEC
