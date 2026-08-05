# Staying on Spec: Real-Time Monitoring under Uncertainty with a Maritime Case Study

- 区域：精读区
- 排名：4
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Elizabeth Dietrich, Hanna Krasowski, Emir Cem Gezer, Roger Skjetne, Asgeir Johan Sørensen, Murat Arcak
- 机构：Norwegian University of Science and Technology, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.02811v1) · [PDF](https://arxiv.org/pdf/2608.02811v1)

## TLDR
The paper proposes a real-time, data-efficient monitoring framework that uses data-driven reachable sets within probabilistic signal temporal logic (pacSTL) to evaluate complex specifications under uncertainty, demonstrating improved risk detection in maritime navigation under realistic disturbances.

## Abstract
Robotic systems must operate under uncertainty while satisfying complex task and safety specifications. Monitoring such specifications under uncertainty remains challenging, as existing formulations typically require extensive data or explicit uncertainty distributions. In this paper, we propose a real-time monitoring framework that reduces data requirements by leveraging data-driven reachable sets for specification evaluation. We instantiate the framework for maritime navigation, where complex specifications arise from traffic rules. We develop a data-efficient pipeline for constructing reachable sets and derive a monitoring formulation suitable for real-time deployment. Simulation and hardware experiments demonstrate robust monitoring under realistic disturbances, achieving improved risk detection compared to state-of-the-art metrics.


## 精读解读（中文）
### 一、研究动机
机器人在实际运行中需要同时满足复杂任务与安全规范，但不确定性使得规范监控十分困难。现有方法通常需要大量数据或显式的不确定分布，难以在真实海事场景中实时应用；同时，纯仿真数据生成的预测存在sim-to-real差距，直接使用真实数据又成本高昂。因此需要一种既能减少数据需求、又能适应真实扰动且可实时部署的规范监控框架。

### 二、技术方案（Method）
提出一个基于pacSTL（概率信号时序逻辑）与数据驱动可达集相结合的实时监控框架。离线阶段先用少量真实实验数据刻画扰动分布，将其注入高保真仿真模型以生成能够代表真实世界行为的大量轨迹，并利用数据驱动可达性分析构造具有PAC保证的可达集；在线阶段针对海事规则定义高效可计算的原子命题，并通过在可达集上求解鲁棒性的最小/最大优化得到每个时刻的鲁棒性区间，再以区间语义递归评估整个STL规范，从而在不依赖显式系统符号模型的情况下实时输出规范满足度区间。

### 三、结果（Result）
仿真与硬件实验表明，该框架在真实波浪扰动下能够实现鲁棒监控，相比传统STL监控和常用风险度量具有更强的表达能力和更优的风险检测性能。所提方法在有限真实数据条件下仍能有效捕获规范违反风险，与现有最先进基线相比改进了监控结果。

### 四、结论（Conclusion）
该工作证明通过数据驱动的可达集结合pacSTL可以在不确定环境下完成实时、数据高效的规范监控，并有效弥合仿真与真实部署之间的差距。框架尤其适合海事导航中由交通规则产生的复杂规范，为实际自主船舶的规范合规监控提供了可行方案。

### 五、方法论与关键技术细节
关键细节包括：基于pacSTL的PAC界限保证，鲁棒性上下界通过对可达集上的鲁棒函数做最小化和最大化获得；离线阶段使用少量真实实验数据估计扰动分布，再利用仿真数据构造可达集，从而降低对真实i.i.d.样本量的需求；利用系统不变性增强部署适用性；监控规范针对海事避碰规则设计原子命题以保证实时可计算性。局限性在于可达集的质量依赖高保真仿真模型和有限真实数据对扰动的刻画精度，且框架验证目前主要针对波浪扰动场景，其他复杂环境扰动仍需进一步研究。
