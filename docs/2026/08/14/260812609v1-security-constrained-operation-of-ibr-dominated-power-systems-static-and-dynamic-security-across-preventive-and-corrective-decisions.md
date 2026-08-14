# Security-Constrained Operation of IBR-Dominated Power Systems: Static and Dynamic Security Across Preventive and Corrective Decisions

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Buxin She
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12609v1) · [PDF](https://arxiv.org/pdf/2608.12609v1)

## TLDR
This paper presents a two-axis taxonomy and generic formulation for security-constrained operation in IBR-dominated power systems, spanning static versus dynamic security and preventive versus corrective decisions, and reviews how inverter-based resource capabilities can either expand feasibility and reduce costs or remain constrained by shared capability limits across coupled scheduling and control formulations.

## Abstract
Inverter-based resources (IBRs) couple power system operation to fast dynamics and controller-dependent responses. Their configurable capabilities are reshaping the formulation and coordination of security-constrained operation. This paper presents a two-axis view: static versus dynamic security and preventive versus corrective decision timing. Preventive scheduling is extending from static post-contingency feasibility toward dynamic security, while corrective operation spans equilibrium-based corrective actions and trajectory-based control. A generic formulation represents this change and makes the preventive--corrective tradeoff explicit. Existing formulations, methods, and capability representations are reviewed and synthesized within this framework. The surveyed work yields two findings. First, IBR capability can expand the feasible set or relieve security constraints, reducing operating cost or improving security performance. Second, shared capability and constraints across formulations determine whether that capability remains operationally deliverable. These findings motivate future research in IBR capability characterization and quantification, joint scheduling, and scalable solution frameworks.


## 精读解读（中文）
### 一、研究动机
大规模逆变器资源（IBR）的部署使电力系统运行与快速动态和控制器响应强耦合，传统安全约束运行主要关注静态事故后可行性，未统一比较安全表示与决策时序，也未解释IBR可配置能力如何影响预防与纠正决策的耦合。现有综述分别覆盖SCUC、SCOPF或稳定性分析，缺乏统一框架，因此需要建立静态/动态安全与预防/纠正决策的双轴分类，并给出通用数学表述。

### 二、技术方案（Method）
本文提出双轴分类框架：按安全表示分为静态安全（平衡态可行）与动态安全（轨迹/稳定裕度），按决策时序分为预防决策（事故前固定）与纠正决策（利用事故后信息）。在此框架下给出通用预防-纠正优化模型：目标为预防成本与事故后纠正成本的加权和，约束包括预防可行集、事故安全集和纠正可行集；静态安全模块采用代数方程和不等式描述事故后平衡，动态安全模块采用微分代数方程描述系统轨迹并施加动态约束。基于该模型，系统梳理并归类现有SCUC/SCED/SCOPF、动态安全约束调度、基于轨迹的纠正控制等文献，分析各方法的安全判据、决策变量和求解框架。

### 三、结果（Result）
综述识别两大趋势：预防调度从静态事故后可行性向动态安全约束扩展，纠正运行从平衡点纠正向轨迹控制扩展。基于文献综合得到两点核心发现：一是IBR能力（如P-Q运行点、控制模式、控制参数）可扩大可行集或缓解安全约束，从而降低运行成本或提升安全性能；二是同一IBR能力在不同公式中的共享能力和约束决定其是否仍能在运行中实际交付。分类比较显示DC模型可扩展但忽略动态，AC模型精度高但非凸且计算复杂。

### 四、结论（Conclusion）
双轴框架为IBR主导电力系统的安全约束运行提供了统一视角，明确预防与纠正决策的权衡以及IBR能力在其中的耦合作用。未来研究应聚焦于IBR能力的表征与量化、预防-纠正联合调度、以及可扩展的求解框架，以支撑实际系统中的应用。

### 五、方法论与关键技术细节
关键细节包括：分类中静态安全指平衡态约束，动态安全指经轨迹或稳定裕度验证的动态属性；预防决策包括事故前固定的调度、控制模式和RAS整定，纠正动作是事故后选择并受预防调度约束；通用公式中预防变量对所有事故公共，动态初始条件由Gamma_c确定，预配置自动响应作为自动控制律mu_c，纠正策略pi_c在Ac中；IBR能力包括有功/无功运行点、储备、GFL/GFM模式及控制参数，其功率和能量限制约束事故后可用响应；现有局限包括动态安全约束直接嵌入调度的计算代价高，以及共享能力跨公式的可交付性需要量化。
