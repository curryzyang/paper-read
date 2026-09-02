# Generative artificial intelligence for reliable mechanistic reasoning for corrosion

- 区域：速读区
- 排名：10
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Bharath M N, R K Singh Raman, Alankar Alankar
- 机构：Indian Institute of Technology Bombay, Monash University, IITB-Monash Research Academy
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00099v1) · [PDF](https://arxiv.org/pdf/2609.00099v1)

## TLDR
The paper introduces a retrieval-augmented generation framework with fine-tuned open-weight LLMs and a proposition-graph tool called Reason Map that, by comparing answer and evidence graphs, detects causal inversions and unsupported inferential leaps in corrosion knowledge synthesis—limitations that standard factuality metrics miss—demonstrating reliable, mechanistically defensible reasoning on magnesium alloy corrosion.

## Abstract
Corrosion accounts for approximately 4% of global GDP, and reliable prediction is essential for timely mitigation. Machine learning effectively predicts corrosion rates from composition, microstructure, and environmental variables, but cannot explain the underlying mechanisms. A reliable approach in safety-critical materials engineering requires not only accurate retrieval but also mechanistically defensible reasoning, a capability that existing factuality metrics cannot assess. This work presents a domain-adapted retrieval-augmented generation framework for corrosion knowledge synthesis, demonstrated on magnesium alloy corrosion. Three open-weight language models (Llama-3.1-8B, Qwen-2.5-7B, Mistral-7B) are fine-tuned on 3,309 expert-verified question-answer pairs from 840 peer-reviewed papers and integrated with a hybrid dense-lexical retrieval pipeline. Retrieval augmentation produces Token F1 gains of 143-194%, with system faithfulness of 0.964 and context recall of 0.988. Blind external validation on newly published literature and in-house electrochemical data confirms trend-level generalisation. Reason Map, a proposition-graph framework, is further introduced; it independently constructs directed evidence graphs from generated answers and retrieved literature, enabling systematic detection of causal direction inversions and unsupported inferential leaps that flat factuality metrics cannot expose. The modular architecture can be applied across domains, offering a generalizable blueprint for trustworthy AI-assisted knowledge synthesis to circumvent corrosion, which can also be applied to other engineering domains.
