# Adaptive Question Generation for Ambiguous Robot Instructions Based on Information Gain and Human Cognitive Characteristics

- 区域：速读区
- 排名：14
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Ryo Terashima, Yuga Yano, Hakaru Tamukoh
- 机构：Kyushu Institute of Technology, Research Center for Neuromorphic AI Hardware
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23874v1) · [PDF](https://arxiv.org/pdf/2610.23874v1)

## TLDR
The paper proposes an adaptive robot question-generation mechanism that combines information gain with human cognitive characteristics to ask concise, intuitive questions about ambiguous instructions, achieving an 88.5% target identification success rate and high subjective ease-of-response ratings.

## Abstract
In this study, we propose an adaptive question generation mechanism that addresses uncertainty arising from ambiguous instructions. Natural-language instructions for service robots often contain ambiguities. In scenes with multiple similar objects, the robot must identify the target object by asking questions. However, existing question generation methods focus on probabilistic discrimination efficiency and do not sufficiently account for user ease of response. Asking questions without considering the user's ease of response may cause incorrect or uncertain answers. Such incorrect or uncertain answers lead to additional clarification turns and degraded dialogue efficiency. The proposed mechanism integrates probabilistic discrimination efficiency and human cognitive characteristics to generate questions that users can intuitively and easily answer. First, the proposed mechanism extracts visual attributes of candidate objects using a vision-language model (VLM). Next, the proposed mechanism computes the information gain (IG) of each attribute and selects the visual attribute (e.g., color, shape) that most reduces uncertainty in the candidate set. When multiple attributes have the same IG, the proposed mechanism applies a visual attribute filter based on cognitive characteristics to select the visual attribute that users can most intuitively perceive. The proposed mechanism then prompts the VLM with the selected attribute and the corresponding attribute values of each candidate object to generate a concise natural-language question. This process is repeated until the target object is uniquely identified. The proposed mechanism achieved a target identification success rate of 88.5% in the evaluation using a dataset of 120 scenes. Furthermore, the proposed mechanism received high ratings in subjective evaluations of response ease.
