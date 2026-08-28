# Directional Optimality Conditions for Optimization Problems in Asplund Spaces

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Weihao Mao, Jane J. Ye
- 机构：University of Victoria
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26328v1) · [PDF](https://arxiv.org/pdf/2608.26328v1)

## TLDR
This paper extends directional necessary optimality conditions and directional metric subregularity criteria from finite dimensions to Asplund spaces, deriving limiting-subdifferential optimality conditions and new results that even improve finite-dimensional theory.

## Abstract
This paper develops directional necessary optimality conditions for constrained optimization problems in Asplund spaces. Under directional metric subregularity, we first derive a directional optimality condition in terms of limiting subdifferentials. We then introduce sufficient conditions for directional metric subregularity and establish their relationships with directional pseudo-normality and quasi-normality. For systems with joint constraints, we further propose a joint criterion for directional metric subregularity and use it to obtain necessary optimality conditions. The results not only extend several finite-dimensional directional constructions to an Asplund-space setting, but also yield conclusions that are new even in finite dimensions.


## 精读解读（中文）
### 一、研究动机
传统约束规范在处理非凸优化和几何约束问题时经常失效，且有限维方向变分分析难以推广到无限维Banach空间，因为弱*拓扑与范数拓扑的差异会导致乘子消失问题。本文旨在Asplund空间中建立方向性必要最优性条件，并给出更可计算、易验证的结果。

### 二、技术方案（Method）
考虑问题min f(x) s.t. P(x)∈Λ，其中X,Y为Asplund空间。通过方向度量次正则性和弱*严格Lipschitz性质，利用方向极限法锥、方向次微分和方向余导数，对约束系统进行标量化处理，推导出以极限次微分形式表达的必要最优性条件。同时引入方向伪正规性和方向拟正规性作为方向度量次正则性的充分条件，并在联合约束系统中提出联合顺序约束规范准则。

### 三、结果（Result）
在Asplund空间中建立了方向性必要最优性条件，扩展了有限维结果，且部分准则在有限维中也是新的。具体地，在方向度量次正则性下得到了基于极限次微分的方向最优性条件；方向伪正规性和方向拟正规性在方向PSNC条件下足以推出方向度量次正则性；对联合约束系统给出了联合方向度量次正则性准则并将其用于最优性条件。

### 四、结论（Conclusion）
本文结果不仅将有限维方向构造推广到Asplund空间，还提供了更具体、可操作的方向最优性条件，为无穷维约束优化问题提供了新的分析工具。

### 五、方法论与关键技术细节
关键点包括：使用方向法锥N(x̄;Ω;ū)和方向次微分等方向变分工具；需要Asplund空间和局部闭性假设；借助弱*严格Lipschitz性质处理无穷维弱*拓扑与范数拓扑差异；方向度量次正则性作为核心假设；联合约束系统采用顺序规范避免乘子消失。局限性在于方向度量次正则性等条件仍需验证，部分充分条件在应用中可能不易检验。
