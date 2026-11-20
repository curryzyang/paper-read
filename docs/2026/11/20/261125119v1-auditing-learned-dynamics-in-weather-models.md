# Auditing Learned Dynamics in Weather Models

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Skylar Gu, Christina Last
- 机构：McGill University, Mila, Haziel
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25119v1) · [PDF](https://arxiv.org/pdf/2611.25119v1)

## TLDR
Using sparse autoencoder features in GraphCast, the paper shows that causally important internal features need not have physical semantics, while physically associated convection and vorticity features can be steered to improve tropical-cyclone intensity forecasts, reducing error by a median of 51%.

## Abstract
Learned weather models are experimentally accessible computational systems whose internal representations can be inspected and manipulated. Using sparse autoencoder features from GraphCast, DeepMind's autoregressive weather forecasting model, we test whether causal relevance requires physical semantics, a question that matters for auditing whether AI forecasters used in high-assurance settings rely on reliable mechanisms. We also look at whether physically associated latent directions can be steered to improve extreme-event forecasts, where interventions are applied to the model's internal activations during the rollout. We find that ablating a feature locked to GraphCast's computational mesh increases global geopotential height error despite lacking conventional physical semantics. Second, suppressing convection- and low-level-vorticity-associated features weakens predicted tropical-cyclone deepening (the fall in central pressure during intensification), while amplifying them reduces intensity error, with amplification of convection features through feature scaling achieving a median of 51\% error reduction over seven storms. Together, these results separate interpretable, physical association from causal utility and establish sparse features as experimental coordinates for auditing and intervening on learned weather dynamics.


## 精读解读（中文）
### 一、研究动机
学习型天气预报模型开始进入高保障决策，需审计其是否依赖可靠机制，而先前SAE特征虽能标出热带气旋等概念，却不清楚因果重要性是否必须伴随可识别物理语义。论文进一步检验与物理过程相关的潜方向能否在自回归滚动中被操控，以改善热带气旋快速增强等极端事件预报。

### 二、技术方案（Method）
基于0.25°、37层GraphCast，在2007–2018年每6小时ERA5分析态上教师强制运行，采集第8层后40,962个网格节点的512维状态，并使用预训练第8层SAE而不重新训练模型；对每个特征计算其在24个独立再分析窗口中对8个ERA5标准场的平均标准化异常，结合127次经度旋转零分布与BH FDR校准物理标签。将输入经度旋转下激活仍固定于计算网格的特征定义为grid-locked，比较其消融对+48小时全球z500 RMSE的影响。对7个快速增强热带气旋，从ERA5初始场做96小时自回归滚动，在每个6小时步对初始风暴中心1500km圆盘内第8层SAE特征按 f' = f+(α-1)max(f-f_normal,0) 修改后解码，并与未扰动预报、ERA5、firing-rate匹配特征、范数匹配随机方向及统计偏差订正比较。

### 三、结果（Result）
消融一个锁定在GraphCast计算网格上的特征，虽无常规物理语义，却使+48小时全球z500 RMSE增加1.50m；将对流特征和低层涡度特征恢复到无风暴常态分别去掉中位2.5hPa和3.0hPa的加深，而firing-rate匹配对照中位小于0.1hPa。按各风暴最优α放大对流特征在7个风暴上取得中位51%的MSLP误差降低，放大涡度特征也可降低误差，但最优α随风暴而异；加倍两类特征组可把TC特征激活提升到163和190，接近ERA5教师强制下的213。统计偏差订正的中位MSLP误差为2.3hPa，优于对流特征的7.4hPa和涡度特征的2.5hPa，但放大干预通过内部状态调整整个滚动轨迹，且leave-one-out选α时对流放大不再优于未修正预报（7.43 vs 6.40hPa）。

### 四、结论（Conclusion）
研究结论是因果相关性与物理可解释性可分离：架构或网格锁定的特征也能承载预报技能，而具有物理统计关联的特征可作为干预坐标对特定失败模式提供状态依赖的因果杠杆。SAE特征更适合作为模型状态坐标而非固定物理变量，需结合周围配置理解其因果效应；它们可用于审计、预报修正和极端事件内部结构探索，但物理标签与观测一致性及跨模型、跨风暴可迁移性仍需验证。

### 五、方法论与关键技术细节
实现上使用0.25°、37层GraphCast及预训练第8层SAE（512维、40,962个网格节点），在2007–2018年ERA5上每6小时教师强制采集状态，不重新训练模型；特征标签由24个独立再分析窗口、8个ERA5标准场的平均标准化异常、127次经度旋转零分布和BH FDR q=0.05校准。干预超参为 f' = f+(α-1)max(f-f_normal,0)，α=0去除超过无风暴类比日参考水平的激活、α>1放大，1500km圆盘掩膜在96小时滚动中每6小时重复且不重定中心；对照包括firing-rate匹配特征、5个与对流解码方向正交的范数匹配随机方向及leave-one-out偏差订正。主要约束与局限是标签只表征统计关联而非机制、7个快速增强风暴（对流另加5个南半球样本）剂量响应差异大且无统一最优α，leave-one-out选α后对流放大中位MSLP误差7.43hPa不优于未修正6.40hPa，ERA5最小气压比最佳观测浅40hPa以上。因此结果证明的是GraphCast内部因果杠杆和审计坐标，而非扰动表示更接近真实观测或可实时业务迁移的技能。
