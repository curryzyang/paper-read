# Continuous-Time Set-Transformers for Asynchronous WiFi-IMU Indoor Localization

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Mohamed Bachar, Ilyass Abouelaziz, Yuehua Ding
- 机构：CESI
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.13057v1) · [PDF](https://arxiv.org/pdf/2611.13057v1)

## TLDR
The paper proposes a continuous-time set-transformer for asynchronous WiFi-IMU indoor localization that encodes each timestamped observation as a token and uses a single permutation-invariant attention block to fuse modalities without resampling or separate branches, while remaining robust to missing or stale sensor inputs.

## Abstract
Indoor localization commonly combines WiFi received signal strength indicator (RSSI) fingerprints with inertial measurements. However, these sensor streams are sampled asynchronously at different rates; therefore, observations rarely align in time and may be missing or stale. Most existing methods resample the data onto a shared clock and process each modality using a separate branch. We instead present a continuous-time transformer that represents observations as an unordered set of timestamped tokens. Each token encodes its measurement, modality, and elapsed time since acquisition. A single attention block jointly fuses information across modalities and time, avoiding both resampling and modality-specific branches while remaining invariant to token order. During training, we randomly mask entire modalities and individual observations, enabling the model to operate under missing or outdated inputs. We validate the modality-specific encoders on their respective benchmarks and evaluate the fused model on both simulated and real datasets, including a crosssession dataset collected on unseen days. The proposed approach improves upon an open WiFi fingerprinting baseline under cross-session drift, remains competitive with learned fusion and dead-reckoning baselines, and degrades gracefully as observations become missing or stale. These results suggest that a single continuoustime transformer provides a practical framework for indoor localization from asynchronous sensors.
