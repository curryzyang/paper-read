# Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place

- 区域：速读区
- 排名：4
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Kobi Kelemen, Tomasz Niedziałkowski, Marcin Paszczak, Victoriano Montesinos
- 机构：Lute
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03779v1) · [PDF](https://arxiv.org/pdf/2611.03779v1)

## TLDR
This paper introduces a battery-powered handheld UMI with robot-matched soft, angled fingers that visibly deform as a force proxy, uses it to collect a 99.7-hour, 53-object pick-and-place dataset, and shows that adding a top camera boosts success by 13 points and multi-task mid-training improves fine-tuned success on unseen objects from 35% to 57%.

## Abstract
Training robot policies for multi-task pick and place requires demonstrations on many objects, which handheld Universal Manipulation Interfaces (UMIs) can collect quickly and cheaply. However, existing UMIs depend on external base stations, use rigid fingers that give no signal about contact forces, or use parallel-jaw fingers that limit grip strength. We present a battery-powered handheld interface, built on YUBI, whose soft, angled fingers wrap around objects, deform visibly under load as a visual proxy for force, and match the grippers of the robot. With it, we collect a 99.7-hour dataset over 53 objects, train $π_{0.5}$ policies on 49 of them, and hold out the other 4 as unseen objects. We find that a top camera raises success by 13 points even when only about half of the data includes it, and that mid-training on our multi-task data raises success after fine-tuning on unseen objects from 35% to 57%. Finger design, dataset, and data processing code: https://lute-corp.github.io/soft-yubi-site/
