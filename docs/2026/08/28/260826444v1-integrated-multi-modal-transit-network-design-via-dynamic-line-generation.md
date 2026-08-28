# Integrated Multi-Modal Transit Network Design via Dynamic Line Generation

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ning Duan, Oktay Günlük, Samitha Samaranayake
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26444v1) · [PDF](https://arxiv.org/pdf/2608.26444v1)

## TLDR
This paper introduces a flow-based mixed-integer programming framework with a column generation heuristic for jointly designing fixed-route transit lines, service frequencies, and on-demand first/last-mile connections, showing significant ridership improvements over single-mode and decoupled baselines in Boston and Chicago.

## Abstract
The integration of fixed-route public transit and on-demand mobility services presents both a modeling challenge and a computational opportunity for large-scale network design. We propose a flow-based mixed-integer programming formulation that jointly optimizes transit line planning and service frequencies while explicitly capturing first- and last-mile connectivity via on-demand services, under a fixed operating budget. To achieve tractability at urban scale, we develop a novel column generation heuristic scheme with tailored pricing subproblems. Applied to networks and demand in Boston and Chicago, the framework yields operationally feasible designs that substantially increase demand served. Relative to transit-only and on-demand-only baselines, ridership increases by up to 20.99% and 93.58% in Boston, and by up to 10.63% and 149.84% in Chicago. Compared to a multi-modal benchmark, our approach improves ridership by 5.42% and 5.80% in Boston and Chicago, respectively. These results demonstrate that (i) joint co-design of transit routes, frequencies, and on-demand legs within a unified optimization framework yields substantially greater ridership than single-mode or decoupled approaches under equivalent budget constraints; and (ii) the proposed formulation and column generation pricing scheme admit tractable, operationally feasible, high-performing solutions relative to tested baselines.


## 精读解读（中文）
### 一、研究动机
传统公共交通与按需出行服务的割裂设计导致系统效率低下，固定线路公交受限于高需求走廊而缺乏广泛可达性，按需服务则因高成本和空驶问题难以独立承担大规模出行。现有研究多假设公交网络给定或仅做解耦优化，缺乏在统一框架下联合设计公交线路、发车频率与按需接驳腿的端到端方案。本文旨在提出一种可扩展的大规模多模式公交网络设计方法，在固定运营预算下最大化服务乘客数。

### 二、技术方案（Method）
本文提出基于流的混合整数规划（MIP）模型，联合优化公交线路规划、服务频率及按需出行（出租车）的首末公里接驳。输入为道路网络、OD出行需求、公交容量、运营成本及预算。模型显式刻画乘客路径选择，限制换乘次数，并施加线路长度不超过端点最短路两倍、最大长度及最小发车频率（即最大等待时间）等服务质量约束。为求解城市规模问题，开发了列生成启发式方案：在主问题LP松弛对偶信息的引导下，通过定制的定价子问题近似候选线路的检验数，动态生成线路；在每次迭代中限制于对偶信息优先的子图，并采用预选启发式筛选有潜力的候选线路加入主问题。算法交替求解主问题与定价子问题直至收敛，最终得到运营可行的线路与服务频率方案。

### 三、结果（Result）
在波士顿和芝加哥的真实网络与需求数据上验证，所提框架相比纯公交基线，乘客量最高提升20.99%（波士顿）和10.63%（芝加哥）；相比纯按需出行基线，提升最高达93.58%（波士顿）和149.84%（芝加哥）；相比多模式基准方法，波士顿和芝加哥分别提升5.42%和5.80%。结果表明在同等预算下，联合协同设计公交线路、频率与按需腿能显著提升乘客量，且列生成定价方案具备可处理性与运营可行性。

### 四、结论（Conclusion）
联合优化公交线路、发车频率与按需接驳腿的多模式系统设计，相比单一模式或解耦方法能在同等预算下服务更多乘客，并生成运营可行的方案。所提出的流式MIP模型与定制的列生成定价方案能够在城市规模实例上高效求解，为多模式公交网络规划提供了一种新的可行框架。

### 五、方法论与关键技术细节
关键点包括：模型允许乘客通过公交、按需服务或两者组合（如按需到公交再按需）出行，但限制换乘次数以避免多商品流模型中无限换乘的不现实假设；为保证服务质量，每条线路要求最大等待时间对应的最小车辆数，且线路端到端距离不超过最短路两倍；定价子问题因缺乏线路特有约束的对偶变量，采用近似检验数的启发式方法；列生成中利用LP松弛的对偶信息优先搜索子图，并通过预选启发式降低主问题中连续、整数和半连续变量交互带来的计算负担。方法局限可能在于按需服务仅考虑单人出租车模式，且实验基于静态需求，未考虑动态波动。
