# When Information is Worth the Risk: Behavioral Valuation for Hazardous Robotic Exploration

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Alkesh K. Srivastava, Aamodh Suresh, Carlos Nieto-Granda, Philip Dames
- 机构：Temple University, Lobster Robotics, U.S. DEVCOM Army Research Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10726v1) · [PDF](https://arxiv.org/pdf/2609.10726v1)

## TLDR
This paper proposes a risk-augmented Behavioral Information valuation layer based on Prelec probability weighting to help hazardous exploration robots decide when reducing uncertainty is worth potential failure, showing that changing only the path-scoring objective reshapes the information-risk frontier and can reduce hazard exposure while remaining Pareto-competitive.

## Abstract
Hazardous robotic exploration requires robots to map spatial risks, such as unsafe terrain, radiation, fire, mines, or structural damage, while operating where collecting information can itself cause failure. A highly informative path may expose the robot to hazards, terminate execution, and prevent future observations. Hazardous exploration therefore requires deciding not only where uncertainty is largest, but when reducing it is worth the risk. This paper introduces a valuation-layer view of this problem. We keep the belief update, sensor model, physical risk model, and finite-horizon informative planner fixed, and change only the scalar objective used to rank feasible paths. Within this framework, we introduce a risk-augmented Behavioral Information objective based on Prelec probability weighting, yielding an interpretable family of conservative-to-aggressive information-risk valuations. Theoretically, we show that valuation parameters create switching boundaries between high-information/high-risk and lower-information/lower-risk paths, and induce a transformed Pareto-frontier structure over feasible exploration policies. Large-scale failure-truncated grid-world experiments show that valuation alone reshapes the information-risk frontier. Shannon information planning remains a strong raw-information baseline, while risk-aware objectives can reduce hazard exposure and robot losses by avoiding failures that truncate future sensing. Risk-augmented Behavioral valuation is Pareto-competitive with standard risk-aware baselines and provides interpretable conservative and intermediate regimes. These results support a framework in which robots reason not only about how much uncertainty an action reduces, but whether that reduction is worth the risk required to obtain it.


## 精读解读（中文）
### 一、研究动机
危险机器人探索中，收集信息本身可能触发失败并截断未来观测，因此核心问题不只是哪里不确定性最大，而是何时降低不确定性值得冒险。现有信息规划与风险感知方法多把风险作为约束或惩罚，本文则把危险探索视为叠加在贝叶斯更新和有限时域规划之上的估值层问题，研究仅改变路径排序目标会如何改变探索行为。

### 二、技术方案（Method）
在固定信念更新、传感器模型、物理风险模型和有限时域信息规划器的前提下，论文将每个栅格的危险状态建模为二值隐变量并赋予致死率，机器人维护逐格危险概率；候选路径由同一可行路径集生成，路径观测为带真阳率与假阳率的二值观测，经贝叶斯更新得到后验。信息价值用Shannon熵减定义，物理风险用访问唯一栅格的失败概率或期望暴露定义。核心目标是风险增强行为信息目标J_{α,η}=B_α(Path)-η w_α(R(Path))，其中B_α为基于Prelec概率加权二值概率计算的Behavioral Information Gain，w_α为Prelec权重，α<1高估小概率而保守，α>1低估小概率而激进，α=1恢复线性风险惩罚；概率加权只作用于目标层，不改变贝叶斯更新、传感器模型或物理风险概率，路径选择为最大化J。

### 三、结果（Result）
大规模失败截断栅格世界实验表明，仅改变估值目标就能重塑信息-风险前沿：Shannon信息规划仍是强原始信息基线，但风险感知目标可通过避免导致未来感知截断的失败来降低危险暴露与机器人损失。风险增强行为估值与标准风险感知基线在Pareto意义上具有竞争力，并能产生可解释的保守与中间信息-风险权衡；不同α、η会引发高低信息高风险路径与低信息低风险路径之间的切换。

### 四、结论（Conclusion）
论文结论是，危险机器人探索不应只推理动作能减少多少不确定性，还必须判断这种不确定性减少是否值得其所需风险。将估值层与贝叶斯推断、传感器模型、风险模型和规划器解耦，可以在不改变底层概率模型的情况下系统研究信息-风险偏好，并为危险环境中的信息采集提供可解释的保守到激进策略族。

### 五、方法论与关键技术细节
关键实现细节包括：实验在失败截断栅格世界中进行，使用逐格二值危险观测与致死率模型；风险项R_fail按路径访问的唯一栅格计算，降低重复计数影响；目标中β固定为1以保留α=1、β=1时w(p)=p的恒等参考，α控制Prelec曲率，η≥0控制显式风险惩罚，η=0退化为纯Behavioral Information Gain。理论上，估值参数会产生高信息高风险路径与低信息低风险路径之间的切换边界，并诱导可行探索策略上的变换Pareto前沿。局限在于概率加权仅用于规划估值而非信念更新，β变化未系统探索，Behavioral Information Gain是规划估值泛函而非Shannon互信息的替代定理，且验证主要基于大规模栅格仿真而非真实机器人。
