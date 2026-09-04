# Distilling deep optical flow stereo methods to retrieve dense three-dimensional wind fields

- 区域：速读区
- 排名：13
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Thomas J. Vandal, Dong L. Wu, James L. Carr, Derek J. Posselt, Elise Penn, Tristan Ballard, August Posch, Kate Duffy
- 机构：Zeus AI, Carr Astronautics, California Institute of Technology, NASA Goddard Space Flight Center
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03100v1) · [PDF](https://arxiv.org/pdf/2609.03100v1)

## TLDR
This paper replaces window-based tracking in cross-satellite stereo wind retrieval with a deep optical flow model (WindFlow) fine-tuned on radiosondes, and distills the stereo teacher into a single-satellite student model to produce dense, NWP-independent three-dimensional global wind fields with improved accuracy over operational AMVs in water vapor bands.

## Abstract
Geostationary atmospheric motion vectors (AMVs) provide the dense horizontal wind vectors (u,v) and heights ingested into data assimilation systems. Traditional AMVs track features using window-based cross-correlation and estimate heights via infrared brightness temperatures paired with numerical weather prediction (NWP) background states, creating a circular dependency that yields inaccurate heights, high computational cost, and sparse retrievals. Stereo winds from GEO-GEO and GEO-LEO geometrically resolve heights from parallax shifts across different poses, eliminating NWP dependence and improving accuracy, but they remain computationally heavy with limited coverage. In this work, we replace window-based tracking in stereo matching with deep optical flow for efficient, improved retrieval. Fine-tuning balances a self-supervised geometric residual loss with supervised radiosonde reconstruction. To eliminate multi-satellite overlap requirements, we distill the stereo teacher into a single-satellite student model. Chi-square and height uncertainties from the teacher are emulated by the student for quality assurance. The student generates winds across full-disk GEO imagery globally. Validation compares stereo and student models against radiosondes, operational AMVs, ERA5 reanalysis, and EarthCARE cloud profiles. Results through triple collocation show that stereo winds improve performance beyond operational AMVs for water vapor bands (6.2, 6.9, and 7.3 μm), wit degradation in the long-wave infrared (11.2 μm) band.
