# Improved upper bounds for five IHTC-2024 benchmark instances via exact reoptimization of the nurse-to-room layer

- 区域：速读区
- 排名：14
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Alfonso Gippini Requeijo
- 机构：Team Banzai S.L.
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00044v1) · [PDF](https://arxiv.org/pdf/2610.00044v1)

## TLDR
By exactly reoptimizing only the nurse-to-room-and-shift layer while holding all patient-side decisions fixed, the paper improves five IHTC-2024 benchmark upper bounds by 0.075–0.125% and shows that several published state-of-the-art solutions are still suboptimal in this layer.

## Abstract
The Integrated Healthcare Timetabling Competition 2024 (IHTC-2024) defined a benchmark that integrates surgical case planning, patient admission scheduling and nurse-to-room assignment. Its instance set remains live: the organizers keep a public table of best-known upper bounds that is open to new submissions. We report five improved upper bounds on that table, for instances i02 (1263, previously 1264), i05 (12744, previously 12760), m01 (3380, previously 3384), m03 (6692, previously 6697) and m04 (3315, previously 3318). All five solutions were checked with the official IHTP validator and carry no hard-constraint violations. The solutions are not built from scratch: each is derived from the corresponding solution published on the benchmark page, holding its admission days, room assignments and operating-theater assignments fixed, and reoptimizing only the nurse-to-room-and-shift layer to proven optimality. The improvements are small in magnitude, between 0.075% and 0.125%, but they carry a structural observation: on the instances where the nurse layer can be closed exactly, it closes within seconds on all but one of them, and several of the published state-of-the-art solutions fall short of optimality in that layer.
