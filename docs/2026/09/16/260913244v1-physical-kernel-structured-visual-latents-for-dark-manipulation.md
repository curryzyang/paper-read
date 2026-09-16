# Physical Kernel: Structured Visual Latents for Dark Manipulation

- 区域：速读区
- 排名：13
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Jinting Hang, Hong Li, Zhenhui Cai, Zhihao Zhao, Jian He
- 机构：Harvest Praxis
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13244v1) · [PDF](https://arxiv.org/pdf/2609.13244v1)

## TLDR
This paper introduces a Physical Kernel that encodes a single lit RGB observation into structured visual latents, enabling “dark manipulation” where a latent policy and open-loop dynamics complete contact-rich skills without further pixels, achieving 68.1% stacking on ManiSkill StackCube versus 35.6% for per-step re-encoding and 0% for frozen/black baselines.

## Abstract
We study dark manipulation: after a brief lit Write encodes z0 = Enc(rgb), a policy pi(z) and open-loop dynamics f(z,a) complete contact-rich skills without further pixels (dark_f). On ManiSkill StackCube (n=160; seed packs 0/1000), dark_f attains 68.1% stacked on the five-rung chain (near_A -> grasped -> lifted -> on_B -> stacked), compared with 35.6% for per-step lit_reenc and 0% for freeze/encode_black. On a shared Write->HOLD protocol (n=40), occlusion and camera-aligned GT contact-neighbor masks drive lit lift from 43% to 0%, while dark_f holds 82.5%; shuffling actions inflates dynamics MSE by ~9.4x; write-time appearance shifts break encoding (night: 0% stacked), yet the same shifts during HOLD leave dark_f lift unchanged; Write length Tw is flat once the stop phase is reached, while earlier stops and write-time blur/JPEG sharply cut stacked. A dedicated pi_write reaches 35% vision-budget stacked (n=80); matched Dreamer-style/pixel nulls without privileged geom stay at 0%. Privileged state-RSSM MPC reaches ~35% stacked with 9D dark observations -- a stronger-observation null, not a matched visual baseline.
