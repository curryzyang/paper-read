# TSSM: Triaxial State Space Model for Global Station Weather Forecasting with Temporal-Variable-Historical Modeling

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Songru Yang, Zili Liu, Tao Han, Ben Fei, Fenghua Ling, Lei Bai, Chang Liu, Xiangyang Ji, Zhenwei Shi, Zhengxia Zou
- 机构：The Chinese University of Hong Kong, Shanghai Artificial Intelligence Laboratory, Beihang University, Tsinghua University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13101v1) · [PDF](https://arxiv.org/pdf/2607.13101v1)

## TLDR
TSSM proposes a triaxial state space model that leverages period-aligned historical weather data across temporal, variable, and historical axes to achieve state-of-the-art performance in global station weather forecasting, with significant gains in accuracy, extreme event prediction, long-horizon forecasting, and robustness to missing observations.

## Abstract
Global Station Weather Forecasting (GSWF) is pivotal for localized and extreme weather prediction over key regions. Despite efforts to exploit look-back windows, existing methods show limited accuracy gains and struggle with extreme events and error accumulation. These limitations stem from overreliance on short-term patterns, which are insufficient to capture chaotic weather dynamics, especially under partial observations. To address this problem, we propose a novel Triaxial State Space Model (TSSM) with a history-enhanced Temporal-VariableHistorical paradigm, which incorporates period-aligned historical weather data to compensate for long-term, large-scale periodic, and full-window weather patterns beyond the temporal lookback window. Specifically, TSSM stacks historical samples into period-aligned batches, where forecasting is causally supported by historical and current observations. Temporal, variable, and historical scanning are designed to capture axial temporal dependencies, variable correlations, and historical evolution. This structure is hierarchically shared to model seasonal to extreme events while alleviating misalignment across historical patterns. TSSM achieves SOTA performance on Weather-5K, the largest station weather dataset to date, with 10% and 61% gains in accuracy and extreme event metrics, and obtains 95% best or second-best results on human-involved datasets. Its advantages are more pronounced in long-horizon and iterative forecasting, reaching a 37.5% gain at 240h and up to 103.5% under a 48h times 5 iterative setting. Moreover, TSSM retains > 90% performance under up to 80% missing observations, compared with < 43% for baselines, demonstrating robustness and practical potential for reliable GSWF in global in-situ observation networks.
