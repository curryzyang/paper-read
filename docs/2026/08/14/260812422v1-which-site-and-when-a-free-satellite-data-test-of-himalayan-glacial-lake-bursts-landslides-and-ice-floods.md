# Which Site, and When: A Free-Satellite-Data Test of Himalayan Glacial Lake Bursts, Landslides, and Ice Floods

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Matthew Kahn, Milan Arjel, Nirmala Adhikari, Mingmar Sherpa, James Pope
- 机构：Cornell University, Tribhuvan University, University of Bristol, University of Alabama at Birmingham
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12422v1) · [PDF](https://arxiv.org/pdf/2608.12422v1)

## TLDR
The study shows that free satellite data—radar deformation and weather signals—can predict *which* Himalayan glacial lakes are susceptible and *when* triggers occur (with honest ROC scores of 0.76–0.83 for bursts and landslides), while highlighting that simple baselines beat deep learning and that terrain-based susceptibility is often overestimated unless matched against comparable unfailed sites.

## Abstract
Two free satellite signals carry real information about glacial-lake outburst risk in the Nepal Himalaya: radar interferometry sees a moraine dam slowly sagging, and satellite weather marks the weeks when a primed lake is under stress. A companion feasibility study found that deformation indicates which lake is destabilizing and weather indicates when it is at risk, but proposed no predictive model. To address this gap, we propose and evaluate models that predict which site is susceptible and when a trigger arrives. We test three related hazards on free data alone: large moraine- and ice-dammed bursts, rainfall-triggered landslides, and smaller floods from ponds on and around a glacier. Each hazard gets two questions, never blended. Using 589 dated outbursts from HMAGLOFDB and several thousand catalogued landslides, we match each event against similar but unfailed sites, and hold every model to a strong simple baseline under spatial cross-validation that withholds whole map tiles, so no model succeeds by recognising a trained-on neighbourhood. Antecedent weather times the trigger at ROC 0.73 for big bursts, 0.83 for landslides, and 0.82 for small floods. Terrain ranks susceptibility only in part: scored naively it appears near 0.9, largely because catalogued failures cluster in wetter ranges; matched against comparable nearby sites the honest figures are 0.76, 0.71, and 0.54 (no better than chance). The burst signal holds within single regions, reaching 0.89 in Nepal alone. Five deep-learning models do not decisively beat a simple gradient-boosted baseline. Three score marginally higher on landslides, a hint too small to confirm. For the lake hazards the baseline wins outright, reproduced by a three-rule decision tree on ruggedness and monsoon rainfall. We close with a ranked Nepal watchlist, a prioritisation aid, not a prediction, and note where free data reaches its limits.
