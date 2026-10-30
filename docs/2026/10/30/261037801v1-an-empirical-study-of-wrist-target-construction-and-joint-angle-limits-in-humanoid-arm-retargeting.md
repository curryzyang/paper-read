# An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting

- 区域：速读区
- 排名：14
- 匹配度：3.2/10
- 来源：arxiv
- 作者：MinJun Chang
- 机构：Georgia Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37801v1) · [PDF](https://arxiv.org/pdf/2610.37801v1)

## TLDR
In humanoid arm retargeting on a Unitree H1-2, constructing the wrist target from demonstrated arm directions and robot segment lengths often drives computed joint angles to their limits, whereas reach-normalizing the shoulder-to-wrist distance while preserving direction largely avoids these limit events—showing that target construction and posture matching should be treated as separate retargeting decisions.

## Abstract
Motion retargeting maps a demonstrated human movement onto a robot to compute its joint motion. This study examines how the construction of the desired wrist position affects whether computed arm joint angles reach their permitted limits on a Unitree H1-2. A reconstructed target is formed from demonstrated arm directions and robot segment lengths, so its shoulder-to-wrist distance depends on the demonstrated angle between the segments even when no posture-matching preference is applied. A reach-normalized target retains that direction while rescaling the distance, using the same processed demonstrations and the same joint-angle method. Across a forward-reach sweep the reconstructed target places a joint angle at a bound in 10 of 20 repetitions and the reach-normalized target in none. Across 25 recordings from one participant the corresponding counts are 8 and 6 on the reaching arm and 14 and 5 on the supporting arm, and a second participant repeats the bricklaying and lifting comparison. In hardware replay a joint is commanded to a bound in 12 of 16 direction-matching arm-records and in none of the 16 normalized records, and within the eligible records both tracking error and executed torque at those frames exceed their values elsewhere in the same run. Cross-body reach and arm-to-arm clearance identify limits of radial adjustment. The findings support treating target construction and posture matching as separate retargeting decisions, and evaluating both alongside the wrist positions and clearance that manipulation requires.
