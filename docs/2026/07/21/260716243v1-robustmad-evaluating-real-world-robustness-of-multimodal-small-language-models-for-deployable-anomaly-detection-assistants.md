# RobustMAD: Evaluating Real-World Robustness of Multimodal Small Language Models for Deployable Anomaly Detection Assistants

- 区域：速读区
- 排名：2
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Anushiya Arunan, Xin Li, Yan Qin, U-Xuan Tan, Nhu Khue Vuong, Xiaoli Li, Chau Yuen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16243v1) · [PDF](https://arxiv.org/pdf/2607.16243v1)

## TLDR
RobustMAD introduces a deployment-motivated benchmark for evaluating multimodal small language models in industrial anomaly detection, revealing that while top models surprisingly outperform larger ones like GPT-5 Nano, they still exhibit critical robustness gaps—including fragile multimodal grounding, insufficient comprehensiveness, and hallucination—that must be addressed for safe deployment.

## Abstract
Multimodal industrial anomaly inspection assistants are a critical component of next-generation smart factories, enabling interactive vision-language-based querying. However, multimodal large language models remain impractical for on-site deployment due to prohibitive computational demands and privacy risks from cloud-based inference. Compact multimodal small language models (MSLMs) offer a deployable alternative, yet progress is constrained by the lack of comprehensive robustness analyses and meaningfully challenging benchmarks that reflect real-world industrial conditions. To address this gap, we develop RobustMAD, the first deployment-motivated benchmark, designed to comprehensively evaluate model robustness through diverse open-ended queries spanning object understanding, anomaly detection, unanswerable problems, and visual quality degradations. Contrary to conventional assumptions, top-performing MSLMs exhibit promising capabilities, surprisingly outperforming even the larger GPT-5 Nano. However, they still fall short of safety-critical requirements, and RobustMAD reveals critical robustness gaps that pose operational risks. In particular, three recurring failure modes emerge: (i) fragile multimodal grounding under fine-grained distinctions or degraded visual conditions, (ii) insufficiently comprehensive responses, and (iii) weak logical grounding on unanswerable or ill-posed queries, leading to hallucinated outputs. Grounded in these insights, we provide actionable guidance for the design of next-generation multimodal industrial inspection assistants that leverage their promising competence. Code is available at https://github.com/en-research/RobustMAD.
