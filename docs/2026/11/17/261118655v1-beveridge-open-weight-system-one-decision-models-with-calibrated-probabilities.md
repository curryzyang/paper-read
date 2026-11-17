# Beveridge: Open Weight System One Decision Models with Calibrated Probabilities

- 区域：速读区
- 排名：13
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Sathiskumar Jothi
- 机构：BDST: Big Data Science & Technology Ltd
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18655v1) · [PDF](https://arxiv.org/pdf/2611.18655v1)

## TLDR
Beveridge introduces open-weight System One decision models that answer up to 15 typed document questions in a single forward pass with calibrated per-option probabilities, outperforming larger general LLMs and a commercial API on operations-document decisions while enabling fast, high-confidence automation and releasing weights and code under Apache 2.0.

## Abstract
Many production systems need a model to make a narrow decision about a document (route a ticket, check a limit, refuse a request, pick the next step of a browser agent) rather than to write text about it. We present Beveridge, a family of open weight System One decision models that take a document and up to 15 typed questions (yes/no, choice among described options, or a level on an ordered scale) and return, in one forward pass without generating text, an answer with a calibrated probability for every option. Beveridge-Large-C (398M parameters) adds a 3.5M parameter decision network to ModernBERT-large: typed number and date features in the input, exact facts from a rule engine, question-to-document evidence attention, a three-step recursive core with learned halting and an exact yes/no path. Beveridge-Pro-C adapts Gemma 4 26B-A4B with LoRA to score option letters, and Beveridge-Pro-C-Web extends it to the next step of a browser agent. On held-out tests the 0.4B model reaches 93.0% on our operations-document benchmark against 91.1% for the best of five general LLMs (31B-675B) and 87.9% for a commercial System One API, and, because its confidences are calibrated (ECE 0.029 on that benchmark), it can hand over 76% of decisions automatically at 95% accuracy, where no general LLM we tested can hand over any. It answers in 4.9 ms per decision on one NVIDIA H200 GPU and 60 ms on the 14 core CPU of an Apple M4 Pro laptop. Beveridge-Pro-C-Web raises next-step accuracy on web pages from unseen site types from 49.4% to 98.2% and completes live browsing tasks without losing document accuracy. We describe the models, the training recipes and an evaluation on 19 held-out test sets against a commercial System One API and five general LLMs, including where the models are weak. Weights and inference code are released under Apache 2.0.
