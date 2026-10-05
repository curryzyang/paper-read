# PowerBench: Measuring Language Model Bias in Power-shifting Requests

- 区域：速读区
- 排名：14
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Nicolas Martorell, Wendy Brau, Gonzalo A. Heredia, Tomás Pablo Korenblit, Gaspar Labastié, Tomás Gimenez Molina
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02303v1) · [PDF](https://arxiv.org/pdf/2610.02303v1)

## TLDR
The paper introduces PowerBench, an open-source benchmark of power-shifting requests that evaluates 24 US and Chinese language models and reveals systematic biases in refusal behavior across power type, affected-party scale, nationality, AI-agent users, and request language.

## Abstract
Language models increasingly assist people with power-related requests, so systematic differences in whom they help could shift the distribution of power at scale, or be exploited by users who learn which identities are refused less. We introduce PowerBench, an evaluation of power-shifting requests that distinguishes self-empowerment, disempowerment, and power grabbing, plus a control of refusal-inducing requests that shift no power. We build, curate, and open-source a dataset of such requests varying the power domain, the context, the scale of the affected party, and the prior power standing of the user, and evaluate 24 models (12 from US and 12 from Chinese developers) under three experimental conditions: reciprocal nationalities of user and affected party, an AI agent as the user, and 8 request languages. Models refuse power grabbing more than disempowerment, and disempowerment more than self-empowerment. Refusal of power grabbing rises with the scale of the affected party, from an individual to a society. Models are biased toward helping others take power from the US and against helping US users take power from others, but favor the US when it gains power and nobody loses it. When the user is an AI agent, refusal of power-shifting requests increases, especially in power grabbing against an individual. Finally, language biases refusal, but in model-specific ways that largely cancel on average. We release PowerBench to make these asymmetries measurable in current and future models.
