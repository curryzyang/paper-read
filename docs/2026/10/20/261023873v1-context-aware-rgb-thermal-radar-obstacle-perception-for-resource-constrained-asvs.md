# Context-Aware RGB-Thermal-Radar Obstacle Perception for Resource-Constrained ASVs

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Pranav Kedia, Edwin Redhead, Heiko Hamann
- 机构：University College London, University of Konstanz
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23873v1) · [PDF](https://arxiv.org/pdf/2610.23873v1)

## TLDR
This paper proposes a context-aware RGB–LWIR–mmWave radar fusion architecture with inertial context and a compact bearing-sector interface for small ASVs, showing through closed-loop lake trials that calibrated multimodal fusion preserves reliable obstacle perception when RGB fails, at the cost of slightly lower ranking accuracy than RGB alone when RGB is usable.

## Abstract
Reliable obstacle perception is challenging for small autonomous surface vessels (ASVs): reflections and glare confound visible-light cameras, vessel motion shifts the apparent waterline, and darkness removes the dominant sensing modality altogether. Rather than treating multimodal fusion as a static accuracy gain, we propose a context-aware architecture that combines RGB and long-wave infrared (LWIR) imagery, frequency-modulated continuous-wave (FMCW) mmWave radar, and inertial context. A bearing-sector interface provides the navigation controller with calibrated obstacle probabilities, radar ranges, and sensor status. It also distinguishes sensor dropout from a valid observation with no detected obstacle. Using new multimodal lake recordings, we deployed the pipeline in a 24-leg closed-loop pilot under uncontrolled lake conditions (16 day, 4 dusk, and 4 night; 351 m), including night legs in which RGB was unusable and the vessel drove on LWIR and radar evidence alone. On eight held-out low-light recordings, the calibrated fusion model achieved average precision (AP) 0.869 and expected calibration error 0.108, compared with AP 0.673 for rule-based fusion, 0.620 for gated fusion, and 0.903 for RGB alone. Our results expose a central tradeoff: RGB ranks best when usable, whereas fusion preserves a navigation input when RGB fails. This work is a step toward perception that remains usable and degrades predictably across multi-day ASV missions.
