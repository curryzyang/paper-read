# Developing Combined Manipulation and Locomotion Skills with Interaction Representation and Skill Composition

- 区域：速读区
- 排名：5
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Fanxing Meng, Jing Xiao
- 机构：Worcester Polytechnic Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.00208v1) · [PDF](https://arxiv.org/pdf/2608.00208v1)

## TLDR
A humanoid robot learns a generalizable whole-body grasping policy using cubic-harmonics-based spatial interaction representations and a developmental curriculum, then composes it with a standing/walking policy via interaction-based joint control—achieving 93% zero-shot grasping of unseen objects and 96–100% success standing while holding them, while showing that full-body training is essential for seamless policy composition.

## Abstract
This paper addresses how to enable a humanoid robot to learn motion policies based on developmental principles and combine policies to create more sophisticated and useful behaviors. Specifically, we present an approach to (1) learning a whole-body reaching and grasping policy and (2) combining it and a standing-up and walking policy to compose a more complex policy of manipulation and locomotion: grasping, standing up, and walking.
  In (1), our method draws inspiration from harmonic analysis and adopts cubic harmonics as weights to represent the hand-object spatial relationship via spatial convolution. Utilizing an intra-episode finger joint decoupling curriculum based on developmental principles, a robot can autonomously learn a generalizable grasping policy without relying on external datasets or pretrained models.
  In (2), our method combines the grasping policy with a separately learned getting-up policy by providing both policies with their respective observation vectors and using hand-object interaction scores to determine when each policy should control which robot joints. Our results show a 93% zero-shot success rate for grasping unseen objects and a 96-100% success rate for standing up while holding the object. Our work also demonstrates that combining different policies is only effective if each policy learning happens on the same whole humanoid body even if a policy (such as for locomotion) does not seem to need all the body parts (such as fingers).
