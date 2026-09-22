# Shake to Learn: Dynamic Interrogation of Hidden Object Physics for Robotic Manipulation with Physical Reservoir Computing

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Wen Sin Lor, Jun Wang, Suyi Li
- 机构：University of Michigan, Virginia Tech
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20970v1) · [PDF](https://arxiv.org/pdf/2609.20970v1)

## TLDR
This paper introduces “shake-to-learn” robotic perception, in which a soft origami arm acting as a physical reservoir computer infers hidden object properties such as center-of-mass position from the ringdown dynamics caused by a fixed shaking impulse, enabling a lightweight linear readout to guide downstream manipulation like regrasping.

## Abstract
Many physical properties relevant to robotic manipulation are hidden from vision. A sealed object, for example, may reveal little about its center of mass (COM) or internal contents until it is lifted, shaken, or otherwise dynamically perturbed. This study shows that such interactions can enable a new modality of robotic perception and learning, in which interaction-induced dynamic responses are used to infer object physics that is inaccessible to conventional sensing. We implement this idea using an origami-inspired soft robotic arm that functions as a physical reservoir computer. After grasping an object, the arm is excited by a fixed shaking input at its base, and the resulting ringdown response is recorded through either camera tracking or embedded sensors. Because the input is held constant across trials, hidden object properties, such as the COM position, are encoded through their effect on the dynamics of the coupled robot-object system. A lightweight linear readout can then decode these dynamics to recover interpretable information about the hidden object physics. Using this framework, the soft robotic arm reservoir completed three tasks of increasing difficulty: inferring the orientation of the object's hidden COM, inferring the COM distance from the grasp point, and using the inferred COM information to guide a subsequent regrasp. We further develop a dynamic summary representation of the ringdown response that improves prediction accuracy. Together, these results establish shake-to-learn mechanical interrogation as a promising strategy for robotic systems to convert brief physical interactions into actionable cues about hidden object properties for downstream manipulation.
