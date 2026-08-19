# Efficient Neural-Network-Based High-Resolution Radiative Transfer for CO___ Retrieval, and Application to Interferometric Sensing

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Jordan Lontsi Tedongmo, Yann Ferrec, Laurence Croizé, Pablo Musé, Gabriele Facciolo, Andrés Almansa
- 机构：Université Paris-Saclay, Institut Universitaire de France, ONERA, Université Paris Cité, Universidad de la República (UdelaR)
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14645v1) · [PDF](https://arxiv.org/pdf/2608.14645v1)

## TLDR
The paper proposes a neural-network (multilayer perceptron) surrogate for fast, accurate high-resolution radiative transfer in the CO₂ weak band, which when coupled with the NanoCarb interferometer forward model enables efficient and precise CO₂ concentration retrieval.

## Abstract
Studying climate change requires reducing uncertainties in CO2 and CH4 emission estimates to better distinguish anthropogenic from natural sources, which motivates spaceborne measurements with improved revisit frequency and spatial coverage. In this context, the Horizon Europe SCARBOn project assesses a low-cost satellite constellation featuring the NanoCarb imaging interferometer as its core sensor for monitoring CO2 and CH4 emissions in the atmosphere. However, estimating CO2 and CH4 concentrations with high revisit and spatial coverage poses significant challenges: full-physics retrieval algorithms commonly used rely on repeated high-resolution radiative transfer (RT) simulations, which are computationally expensive when using line-by-line RT models. As an alternative, we propose in this study a feedforward multilayer perceptron (MLP) surrogate designed to accurately and efficiently predict top-of-atmosphere radiances in the CO2 weak band, using a combined mean absolute error (MAE) loss on radiances and RT Jacobians to preserve both spectral accuracy and sensitivity to geophysical parameters. Coupling the MLP-based RT surrogate with the NanoCarb instrumental response yields an efficient and precise forward model for NanoCarb measurements, which shows promising results for CO2 concentration retrieval.
