# Position: Stop Reactively Patching Your Model Every Time and Start Proactive Test-Driven AI Development

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Nadine Chang, Maying Shen, Jialiang Wang, Rafid Mahmood, Jose M. Alvarez
- 机构：University of Ottawa, NVIDIA
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20532v1) · [PDF](https://arxiv.org/pdf/2607.20532v1)

## TLDR
This paper argues for a proactive test-driven AI development approach, which maps feedback to a structured test space of task conditions, to achieve better generalization and efficiency than the standard reactive flywheel of patching individual errors.

## Abstract
Many modern AI systems are designed to operate under diverse, open-ended, use-cases. To help generalize deployed systems, many deployed-system maintenance pipelines use a reactive AI flywheel that observes emerging feedback from user behavior (errors) and patches the model accordingly. However, when used as the primary maintenance mechanism, these flywheels often ignore the broader context of these errors within the system's objectives, failing to preempt potential future edge cases, which leads to more unnecessary flywheel iterations. Also, it is statistically increasingly difficult to collect remaining errors due to the long-tail nature of open-world use-cases. This position paper argues that a proactive test-driven flywheel is required to address reactive flywheel's limitations and to approach a generalizable system. We advocate for creating a "test space" to technically map feedback data to task objectives, evolving the flywheel from reactive to proactive. We augment our position by mathematically proving a proactive one achieves better long-term scaling with fewer iterations than the reactive flywheel.
