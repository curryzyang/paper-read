# Reeling It In: Flexible Needle Pick Up via Thread Manipulation for Autonomous Suturing

- 区域：速读区
- 排名：7
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Emma Huang, Zih-Yun Chiu, Neelay Joglekar, Shanglei Liu, Michael C. Yip
- 机构：University of California San Diego, Carnegie Mellon University, Johns Hopkins University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26337v1) · [PDF](https://arxiv.org/pdf/2607.26337v1)

## TLDR
This paper proposes an autonomous suturing framework that uses the suture thread as an assistive tool to indirectly pick up the needle, enabling safe and reliable grasping even when the needle is occluded or inaccessible, while avoiding unnecessary tissue contact.

## Abstract
Suture-needle pickup is necessary for autonomous suturing, as a needle can be unexpectedly dropped or strategically released to adjust the grasping configuration. Current methods for autonomous needle pickup typically guide a robot to move straight toward the needle and grasp it, limited to conditions where the needle is observable and directly approachable. In addition, grasping the needle lying on tissue can lead to the robot pinching nearby tissue or the needle jumping around due to its slippery surface, posing potential safety issues. This work proposes an autonomous framework that uses a suture thread as an assistive tool for indirect needle pickup, avoiding unnecessary tool-tissue contact and enabling pickup even when the needle is occluded or inaccessible. The framework spans the entire workflow, including thread and tissue reconstruction, safe grasp-point selection, stable thread lifting, and bimanual thread-following until securing needle grasping. The robot policies account for visual uncertainty to maximize robustness in real-world environments. We evaluate the proposed framework on a da Vinci Research Kit under various real-world conditions. The results demonstrate robust performance even with a challenging thread configuration or a non-approachable needle, closing the gap in applying autonomous robot policies to unstructured suturing environments.
