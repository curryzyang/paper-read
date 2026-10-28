# Condition-Enhanced Generative Adversarial Network for Aerodynamic Configuration Design of Commercial Aircraft

- 区域：速读区
- 排名：1
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Youzheng Yu, Jiaqing Kou, Weiwei Zhang
- 机构：National Key Laboratory of Aircraft Configuration Design, Northwestern Polytechnical University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35963v1) · [PDF](https://arxiv.org/pdf/2610.35963v1)

## TLDR
The paper proposes a Condition-Enhanced Generative Adversarial Network (CEGAN) that embeds geometric feasibility and surrogate-evaluated aerodynamic performance into the generative process and filters infeasible outputs, enabling more accurate and diverse commercial aircraft configuration designs that satisfy prescribed performance conditions, especially under extrapolation.

## Abstract
Generative machine learning provides an end-to-end framework for aerodynamic design optimization by generating diverse aerodynamic configurations conditioned on target performance. However, the generated designs may violate geometric constraints or deviate from the prescribed aerodynamic performance. Therefore, we propose a Condition-Enhanced Generative Adversarial Network (CEGAN) that embeds geometric and aerodynamic information into the generative process. A condition-informed loss function is developed by combining a geometry-guided feasibility penalty with an aerodynamic performance penalty evaluated by surrogate models trained on the same dataset. Additionally, an output filtering mechanism discards infeasible designs using these surrogate models, ensuring compliance with prescribed conditions. The method is demonstrated on aircraft configurations similar to the Cessna Citation X. Each configuration is represented by 28 shape parameters, whose aerodynamic performance is evaluated using OpenVSP. Interpolation and extrapolation tests are conducted for different network architectures and conditioning strategies. Compared with the baseline model, CEGAN reduces the average generation error by at least 36% for interpolated conditions and by at least 46% under extreme extrapolation conditions, while successfully producing diverse and physically feasible designs that extend beyond the training distribution. Therefore, the proposed CEGAN framework offers a robust and accurate tool for rapid aerodynamic configuration exploration during the conceptual design phase.
