# Privacy Leakage in Federated Learning in Radiology Reports: A Comparative Evaluation of Tokenizer-Driven Privacy Risks

- 区域：速读区
- 排名：14
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Santhosh Parampottupadam, Andres Martinez, Dimitrios Bounias, Sinem Sav, Klaus Maier-Hein, Ralf Floca
- 机构：Heidelberg University, Bilkent University, German Cancer Research Center (DKFZ), Heidelberg University Hospital
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14205v1) · [PDF](https://arxiv.org/pdf/2607.14205v1)

## TLDR
This paper demonstrates that gradient inversion attacks on federated learning of radiology reports can reconstruct substantial portions of text, with tokenizer design (particularly domain-specific ones like RadBERT) significantly influencing the severity of leakage, and that no tokenizer fully prevents this risk, underscoring the need for additional privacy safeguards such as differential privacy.

## Abstract
Federated learning (FL) enables multi-institutional training on clinical text without sharing raw data, but gradient inversion can reconstruct sensitive information from shared model updates. The extent of this leakage for radiology reports, and the role of tokenizer design, remains unclear. We quantify gradient-based text reconstruction in FL and compare privacy risk across three tokenizers with the model architecture held fixed. Six FL clients trained a GPT-2-style transformer (sequence length 32) on public radiology corpora (368,751 diagnostic reports, 98,206 discharge summaries, 1,500 MIMIC-CXR free-text reports) using the GPT-2, RadBERT, and LLaMA-2 tokenizers at batch sizes of 64, 128, and 256. Assuming an active malicious server that modifies the shared architecture before distribution, we applied analytic gradient inversion and measured reconstruction fidelity over five runs. Exact sentence reconstruction ranged from 31% to 44% across tokenizers (30.6-43.5% across the 27 tokenizer x dataset x batch-size cells). At batch size 64 on the Discharge dataset, accuracy was 42.1% (GPT-2), 42.3% (RadBERT), and 39.4% (LLaMA-2), decreasing to 37.3%, 37.2%, and 34.3% at batch size 256. S-BLEU declined as batch size grew (GPT-2: 0.44 to 0.33; RadBERT: 0.48 to 0.35). RadBERT yielded the highest reconstruction fidelity and recovered the most clinical terms (18.1% of a 1,440-term reference vocabulary, vs 12.5% for GPT-2 and 9.4% for LLaMA-2), yet no tokenizer prevented leakage. Substantial portions of report text are therefore recoverable from FL gradients even at larger batch sizes and with domain-specific tokenizers. Tokenizer design influences leakage severity and is a privacy-relevant decision, not only a utility one; safeguards such as secure aggregation and differential privacy are likely necessary to meet HIPAA and GDPR requirements for FL in radiology NLP.
