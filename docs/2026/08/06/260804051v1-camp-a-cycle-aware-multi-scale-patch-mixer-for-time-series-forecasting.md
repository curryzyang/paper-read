# CAMP: A Cycle-Aware Multi-Scale Patch Mixer for Time Series Forecasting

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Jung Min Choi, Vijaya Krishna yalavarthi, Lars Schmidt-Thieme
- 机构：University of Hildesheim
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.04051v1) · [PDF](https://arxiv.org/pdf/2608.04051v1)

## TLDR
CAMP is a cycle-aware multi-scale patch mixer that adaptively learns per-window dominant frequencies and models de-cycled residuals with horizon-guided, multi-resolution patch mixing, achieving state-of-the-art forecasting performance across long-term and traffic benchmarks.

## Abstract
Real-world time series are often governed by recurring patterns, but their dominant periods may vary across datasets, forecasting settings, and individual input windows. Existing cycle-aware forecasters commonly rely on a single period selected at the dataset level, which can be restrictive when periodic behavior changes over time or when multiple cycles coexist. Moreover, patch-based models typically process all patch positions uni- formly, although patches farther from the forecast boundary may require broader contextual refinement, while recent patches contain information that should be preserved more directly. Af- ter cyclic behavior is removed, the remaining dynamics may also span multiple temporal resolutions and cannot be adequately de- scribed at a single scale. We introduce CAMP, a Cycle-Aware Multi-Scale Patch Mixer designed to address these challenges. The Adaptive Cycle Learning module identifies dominant fre- quencies separately for each input window and generates both historical and future cyclic components without requiring a pre- defined cycle length. The Horizon-Guided Patch Mixer intro- duces position-dependent refinement, allowing earlier patches to incorporate broader temporal context while preserving infor- mation close to the forecast boundary. CAMP further models the de-cycled residual through temporally aligned multi-resolution representations, enabling complementary dynamics at different scales to be captured within one forecasting framework. Across seven long-term forecasting benchmarks, CAMP achieves the best average MSE on six datasets and the best or tied-best MAE on six. It also obtains the highest MSE win count across sixteen settings on four PEMS traffic benchmarks.
