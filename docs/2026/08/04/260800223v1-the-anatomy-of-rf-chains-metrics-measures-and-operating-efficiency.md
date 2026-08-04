# The Anatomy of RF Chains: Metrics, Measures, and Operating Efficiency

- 区域：速读区
- 排名：15
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Leonid Belostotski, Arjuna Madanayake, John Nielsen, Mostafa Abdelhadi, Xingchen Liu, Xinquan Wang, Guanyue Qian, Sabit Ekin, Theodore S. Rappaport
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00223v1) · [PDF](https://arxiv.org/pdf/2608.00223v1)

## TLDR
This paper extends Haus and Adler's noise measure into a system-aware framework of cascadable RF metrics—linearity, dynamic range, power efficiency, and waste measures—and introduces "operating efficiency," a unified metric that links power efficiency, dynamic range, and data rate through signal statistics for realistic communication scenarios.

## Abstract
In 1958, Haus and Adler [1] introduced the concept of noise measure. Noise measure is a single quantitative metric that provides a comprehensive basis for comparing devices (individual circuits or outcomes of optimization iterations) in terms of their contribution to overall system noise by incorporating both noise factor and available power gain. Unlike noise factor alone, which reflects how much a device degrades the signal-to-noise ratio, noise measure captures the trade-off between noise and gain, making it a system-aware metric. This distinction is especially important when comparing devices in multistage systems, where both parameters jointly influence the overall system noise. Building on Haus and Adler's work, this article aims to advance RF system design by extending traditional device metrics, such as noise factor and noise measure, with new system-aware metrics: linearity, dynamic range, power efficiency, and waste measures. These new measures are interpretable, computable, and cascadable, making them well-suited for comparing the impact of individual devices or tracking the convergence of circuit design iterations on overall system-level performance. Additionally, a new metric--operating efficiency--is introduced, which unifies power efficiency, dynamic range, and data rate by incorporating signal statistics and variability in communication circuits and systems. Operating efficiency enables robust evaluation of devices under realistic and transient operating conditions, including interference, modulated signals, and adaptive modulation schemes.
