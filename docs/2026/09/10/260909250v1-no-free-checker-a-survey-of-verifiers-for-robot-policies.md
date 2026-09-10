# No Free Checker: A Survey of Verifiers for Robot Policies

- 区域：速读区
- 排名：5
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yang Wan, Xihang Yue, Zhirui Liu, Ziyuan Chu, Shuxun Wang, Yuhan Chen, Xiaonan Jiang, Xukun Zhu, Yubo Dong, Linchao Zhu
- 机构：Zhejiang University, City University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09250v1) · [PDF](https://arxiv.org/pdf/2609.09250v1)

## TLDR
This survey of roughly 150 verifiers for robot policies categorizes them by judgment source—human, rule-based/formal, learned/pretrained, and model-intrinsic—and finds a fundamental trade-off in which credibility falls as availability rises, concluding that “there is no free checker” and proposing metrics to make verifier claims checkable.

## Abstract
A verifier for robot policies reads a candidate behavior and returns a score for how well it did, used both to evaluate vision-language-action policies and to train them. Verifiers range from success detectors and reward models to runtime monitors, safety filters, and temporal-logic specifications. We survey roughly 150 verifiers and compare them along two properties. Availability is how much a verdict costs, how early in a rollout the verdict arrives, and how often a verdict can be asked for. Availability rises as verdicts get cheaper, earlier, and denser. Credibility is how much a high score tells us about the task. Credibility falls as the judgment becomes gameable and self-serving. We group the verifiers by who supplies the judgment: human verifiers, rule-based and formal verifiers, learned and pretrained verifiers, and model-intrinsic verifiers. Across the four families, we find that credibility falls as availability rises. Regardless of who supplies the judgment, there is no free checker. We then examine what validates a verifier itself, and how much a high score tells us. Three measures appear in the literature: agreement with human labels, the performance of the policy it trains, and behavior under reward hacking. We close with nine metrics that make a verifier claim checkable, and coordinates for the verifiers still to be built.
