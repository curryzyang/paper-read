# Enhancing generalization in endwall film cooling prediction: Incorporating the superposition principle into transformer-based neural operators

- 区域：精读区
- 排名：2
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Qineng Wang, Liming Song, Tianyuan Liu, Zhendong Guo
- 机构：Hebei Key Laboratory of Compact Fusion, Xi'an Jiaotong University, ENN Science and Technology Development China Co., Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31633v1) · [PDF](https://arxiv.org/pdf/2609.31633v1)

## TLDR
This paper proposes a superposition-based deep neural operator (SDNO) that incorporates the film-cooling superposition principle into Transformer-based neural operators with signed distance function encoding to predict turbine endwall film cooling, achieving accurate generalization from training layouts with 1–5 holes to unseen layouts with 10–20 holes while improving accuracy over a fully supervised baseline.

## Abstract
In this study, a physics-enhanced neural operator framework is proposed to enhance the generalization prediction ability of the cooling layout of a turbine endwall with variable number of film holes. Specifically, inspired by the film cooling superposition principle, we propose a film cooling prediction model, namely superposition-based deep neural operator (SDNO), that divides the endwall temperature field prediction into two stages. In the first stage, the cooling layout of a turbine endwall is divided into several sub-parts with randomly assigned film holes, and a Transformer-based neural operator network, namely Calculate Net, is designed to predict the temperature field of each sub-part. Then, in the second stage, another neural operator network, i.e., Super Net, is trained to combine the temperature fields predicted by Calculate Net for each sub-part and obtain the superposed temperature field of the full cooling layout. Additionally, instead of directly taking the film cooling contours as pixel plots, a signed distance function (SDF) which is sensitive to the variable locations of cooling holes, is designed to encode the location information of cooling holes. Furthermore, the proposed endwall film cooling prediction model is trained with the samples that changing the number of film holes from 1-5 with variable locations. Then, the trained prediction shows excellent generalization prediction ability, which can accurately predict the film effectiveness of the cooling layout with 10-20 film cooling holes that are unseen in the training samples. The proposed SDNO also improves prediction accuracy relative to the fully supervised baseline. With the above, the effectiveness of our proposed prediction model has been well demonstrated.


## 精读解读（中文）
### 一、研究动机
燃气轮机涡轮端壁气膜冷却受马蹄涡、通道涡等复杂流动影响，传统CFD评估成本高，纯数据驱动代理模型虽在训练分布内精度高，却难以泛化到训练中未见的冷却孔数量与布局。实际设计需要模型在保持精度的同时具备外推能力，因此本文试图把气膜冷却叠加原理引入神经算子，提升端壁温度场预测对变孔数布局的泛化。

### 二、技术方案（Method）
基于Pak-B叶片端壁耦合传热CFD数据，先用SDF在128×128规则网格上编码冷却孔位置，替代易产生锯齿和空洞的二值像素图；再构建两阶段SDNO：第一阶段将完整冷却布局分解为若干子区域并随机分配冷却孔，由Transformer神经算子Calculate Net预测各子区域温度场，第二阶段由Super Net神经算子将子区域预测场叠加为完整布局温度场。训练采用分解-计算-叠加策略，包含联合训练与微调训练，训练集仅含1、2、3、5孔布局，验证/测试含10、15、20孔等未参与训练的孔数配置，并以CFD温度场/气膜冷却效果进行监督。

### 三、结果（Result）
全监督Transformer基线在训练分布内表现尚可，但对训练集外更高孔数布局外推误差显著，传统Sellers叠加公式也难以直接用于复杂耦合传热预测。SDNO能够较准确预测训练中未见的10-20孔冷却布局的气膜冷却效果，且相对全监督基线提升预测精度，验证了其外推泛化能力和训练效率。

### 四、结论（Conclusion）
将气膜冷却叠加原理与Transformer神经算子结合，可把物理先验嵌入数据驱动模型，显著增强端壁气膜冷却温度场预测的泛化性与精度。该方法为变孔数冷却布局的快速评估与优化提供了高效可靠途径，也说明物理增强神经算子在复杂工程场预测中具有应用潜力。

### 五、方法论与关键技术细节
数据来自Pak-B叶片端壁耦合传热数值模拟，网格约280万-360万节点，4核并行单样本约3小时；边界条件包括Re_out=1.98e5、Ma_in=0.029、Ma_out=0.047、主流总温323K、冷气总温286K、湍流强度6%、速度边界层33mm、动量边界层2.5mm。孔布局参数化中孔直径设为4mm、倾角30°，孔间相对距离大于0.15，相对坐标u∈[0.05,0.8]、v∈[0.05,0.95]；共生成2730组样本，训练集2000组仅含1、2、3、5孔，验证集700组覆盖各孔数，微调测试集30组针对更多孔数，训练与验证按孔数严格不混合。SDF编码解决小尺度孔边界锯齿和信息空洞；主要局限是叠加原理对强耦合传热和孔间干扰的适用性、以及网络损失函数与Transformer超参在摘要层面未完全展开。
