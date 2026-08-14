# Unifying Generative Models with Path Integrals

- 区域：精读区
- 排名：6
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Ramon Winterhalder
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12438v1) · [PDF](https://arxiv.org/pdf/2608.12438v1)

## TLDR
Generative modeling is reformulated as a single path-integral master action that unifies flow, diffusion, variational, and adversarial models, and whose MSRJD perturbative expansion yields a one-loop deterministic correction reducing sampling error from 53% to 1.6%.

## Abstract
We formulate generative modeling as a path integral in which flow-based, diffusion-based, variational, and adversarial models arise as different evaluation principles for a single master action. Its Martin-Siggia-Rose-Janssen-de~Dominicis (MSRJD) form separates free from interacting probability flows and opens them to diagrammatic perturbation theory. The expansion yields a one-loop correction to deterministic samplers at no stochastic-sampling cost, which we validate on solvable and nonlinear drifts, where it reduces a 53 % tree-level error to 1.6 %. Imperfect learned scores enter as insertions and yield a response-weighted score-matching objective, and symmetry-equivariant drift design becomes an operator expansion with EFT power counting.


## 精读解读（中文）
### 一、研究动机
现有生成模型（流、扩散、变分、对抗）各自依赖独立数学框架，缺乏统一视角来揭示内在联系并系统化改进。本文旨在通过路径积分构建统一框架，使这些模型成为同一主作用的不同评估原则，从而将量子场论中的微扰工具引入生成建模。

### 二、技术方案（Method）
本文提出用路径积分表述生成建模。构建一个主作用（master action），将基于流、扩散、变分和对抗的生成模型统一为对该作用的不同评估原则；采用Martin-Siggia-Rose-Janssen-de Dominicis（MSRJD）形式分离自由概率流与相互作用概率流，进而应用图表微扰理论。由此导出一环修正项，改进确定性采样器且不引入随机采样成本。对于不完美学习的分数函数，将其作为微扰插入，得到响应加权的分数匹配目标；对称等变漂移设计则通过算子展开和有效场论功率计数实现。

### 三、结果（Result）
在可解漂移和非线性漂移上验证了所提一环修正，将树级相对误差从53%降低到1.6%，显著提升了确定性采样器的精度。

### 四、结论（Conclusion）
该工作为生成模型提供了统一的理论框架，通过MSRJD路径积分将不同模型家族联系起来，开辟了利用量子场论方法系统性改进生成模型的新途径。实验显示其修正有效，未来有望推广到更复杂和高维的生成任务。

### 五、方法论与关键技术细节
关键细节包括：MSRJD形式将自由与相互作用概率流分离，使得费曼图微扰展开成为可能；一环修正无需额外随机采样，计算开销低；不完美学习分数作为插入项，导出了响应加权分数匹配目标而非传统分数匹配；对称等变漂移设计被重构为算符展开，具有EFT功率计数。局限性在于当前验证限于可解和非线性漂移，真实高维数据上的表现及超参选择仍需进一步研究。
