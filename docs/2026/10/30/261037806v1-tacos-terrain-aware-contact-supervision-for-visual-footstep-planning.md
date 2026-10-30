# TACOS: Terrain-Aware COntact Supervision for Visual Footstep Planning

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Jean-Michel Fortin, William Larrivée-Hardy, Gabriel Jeanson, Olivier Gamache, Daniele De Martini, François Pomerleau, Philippe Giguère
- 机构：Université Laval, University of Oxford
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37806v1) · [PDF](https://arxiv.org/pdf/2610.37806v1)

## TLDR
TACOS introduces a physically grounded, self-supervised per-footstep instability score derived from legged state-estimation factor-graph residuals and projects it into preceding images to train a dense visual foothold predictor that outperforms existing supervision methods and anticipates unstable, non-geometric terrain in real-world forest navigation.

## Abstract
Humans navigate their environment based on their vision system, anticipating how the ground will respond before committing to a step. Self-supervised learning could provide legged robots the same ability, but the supervisory signal is typically chosen on intuition, and its effect on what the model learns is rarely examined. We present Terrain-Aware COntact Supervision (TACOS), which proposes a meaningful and consistent footstep instability score, based on the residual of a factor graph in legged state estimation. It projects the continuous score into preceding images to supervise a dense visual predictor. We propose two variants, a hard score that exploits hindsight and a causal soft score available immediately. Both metrics are compared against state-of-the-art alternatives in two independent evaluations that share no data or labels. On 1716 manually annotated contacts, both variants outperform every evaluated alternative at detecting instability and ranking its severity, improving pooled severity ranking by 28 % over the strongest baseline. On three outdoor test runs, our metric also trains the most accurate visual predictor, improving rank correlation by 58 % over the strongest alternative, and by a further 25 % when supplemented with onboard context. In a real-world experiment over a 50 m forest trajectory, the trained predictor handles non-geometric terrain properties such as mud and vegetation, while stepping around geometric obstacles like fallen branches. Code is available for reproducibility at https://github.com/norlab-ulaval/TACOS.
