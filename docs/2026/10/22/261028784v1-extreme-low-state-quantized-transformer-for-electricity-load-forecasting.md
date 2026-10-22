# Extreme Low-State Quantized Transformer for Electricity-Load Forecasting

- 区域：速读区
- 排名：2
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Muhammad Sabbir Alam, Harindra Sandun Mavikumbure, Victor Cobilean, Milos Manic, Jayasimha Atulasimha
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28784v1) · [PDF](https://arxiv.org/pdf/2610.28784v1)

## TLDR
This paper shows that Transformer-based electricity-load forecasting remains effective under extreme 3–16-state weight quantization—especially with quantization-aware fine-tuning or training from scratch—and introduces accumulated-update thresholding that reduces committed weight updates and state transitions by orders of magnitude with negligible NRMSE cost, pointing toward compact, low-activity edge forecasting with multilevel synaptic devices.

## Abstract
Aggressive low-state weight quantization can substantially reduce neural-network representational flexibility, making predictive performance difficult to preserve when only a few discrete weight states are available. We investigate this regime for Transformer-based electricity-load forecasting using 3-, 5-, 7-, and 16-state weight quantization across feed-forward-only and attention-plus-feed-forward quantization. Two tasks predict either the next hour or the next 24 hours from the preceding 48 hours across two co-primary electricity-consumption datasets. Direct post-training quantization (PTQ) increased mean normalized root-mean-square error (NRMSE) relative to full precision by 6.25 and 7.04 percentage points in Datasets A and B, whereas quantization-aware fine-tuning (QAT-FT) recovered approximately 90.2% and 94.5% of these penalties. Quantization-aware training from random initialization (Scratch-QAT) also produced competitive low-state solutions, with particularly favorable behavior at three states. We further introduce accumulated-update thresholding, which accumulates optimizer-proposed weight changes before commitment. Relative to paired Scratch-QAT controls, this reduced committed shadow-weight updates by approximately 99.7% and discrete state transitions by approximately 77--80%, while mean NRMSE changed by only +0.042 and +0.197 percentage points. These results show that useful Transformer forecasting can be retained under highly discrete weight representations while strongly suppressing target-state activity, supporting a prospective route toward compact, low-activity edge forecasting using multilevel synaptic devices.
