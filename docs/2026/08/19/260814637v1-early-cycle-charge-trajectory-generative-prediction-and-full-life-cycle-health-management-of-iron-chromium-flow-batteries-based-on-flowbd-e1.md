# Early Cycle Charge Trajectory Generative Prediction and Full Life Cycle Health Management of Iron-Chromium Flow Batteries Based on FlowBD-E1

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Suyang Zhuang, Zekun Jiang, Tianhang Zhou
- 机构：China University of Petroleum (Beijing), Zhonghai Energy Storage Technology (Beijing) Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14637v1) · [PDF](https://arxiv.org/pdf/2608.14637v1)

## TLDR
FlowBD-E1, an early-cycle generative forecasting framework combining a multi-scale convolutional encoder, lifecycle Transformer, and age-aware FiLM decoder, predicts full future charge V/I trajectories and state-of-health for industrial Fe-Cr flow batteries from just the first few cycles, achieving sub-percent error and enabling long-horizon battery health management.

## Abstract
Long-duration stationary energy storage requires batteries whose degradation can be detected before substantial capacity loss has accumulated. Iron-chromium redox flow batteries are attractive for this role because they use abundant and low-cost active species, yet their operation is shaped by slow chromium kinetics, hydrogen evolution, membrane crossover and electrolyte imbalance. These coupled processes gradually reshape the full charge voltage/current (V/I) trajectory, but most battery prognostic studies either focus on lithium-ion cells or compress ageing into scalar capacity and state-of-health (SOH) labels. Here we study an industrial 33 kW Fe-Cr redox flow battery and introduce FlowBD-E1, an early-cycle generative forecasting framework that predicts complete future charge V/I trajectories from only the first few cycles. The model combines a multi-scale convolutional encoder, a lifecycle Transformer and an age-aware FiLM decoder, and we compare three deployment strategies: single-step latent extrapolation (SLE), recursive latent forecasting (RLF) and teacher-forced updating (TFU). Using the first 9 of 289 cycles, RLF achieved a joint V/I mean absolute percentage error (MAPE) of 0.731% over the remaining lifecycle and produced SOH estimates below 1% MAPE. Ablation and independent-sequence tests showed that the age-aware generative architecture outperformed LSTM and TCN baselines and retained sub-percent errors under industrial validation. These results suggest that early-cycle trajectory generation can turn a short commissioning record into a long-horizon diagnostic signal for flow-battery management.
