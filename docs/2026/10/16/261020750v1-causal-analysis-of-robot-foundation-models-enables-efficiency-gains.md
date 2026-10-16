# Causal Analysis of Robot Foundation Models Enables Efficiency Gains

- 区域：精读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Aiden Swann, Mathilde Papillon, Mozes Jacobs, Siddharth Boppana, Tal Haklay, Eric Bigelow, Andrew Lee, Conor Watts, Thomas Icard, Mac Schwager, Owen Lewis, Jack Merullo, Ekdeep Singh Lubana, Atticus Geiger, Thomas Fel, Matthew Kowal
- 机构：Goodfire, Harvard University, Stanford University, University of California, Santa Barbara
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20750v1) · [PDF](https://arxiv.org/pdf/2610.20750v1)

## TLDR
Causal analysis of three vision-language-action robot models reveals a narrow mid-to-late action-conditioning interface, enabling pruning of action-expert conditioning to only 3 of 36 layers and cutting inference FLOPs by up to 33% with comparable task success.

## Abstract
Vision-language-action (VLA) models are a promising approach to general purpose robot manipulation. While the internal computation of vision-language models, which compose the backbone of VLAs, has been studied extensively, less is known about how their perceptual and semantic representations are transformed into action in VLA models. We study this question mechanistically in three frontier VLA models ($π_{0.5}$, MolmoAct2, and MolmoBot) by analyzing the causal pathways through which the input image and the instruction shape actions. Across the three models, activation patching shows that causally relevant information influences the action expert (AE) through a narrow band of mid-to-late cross-attention layers, which we term the action-conditioning interface. The content of this information changes with token and layer within the model. Early-to-mid layer representations of the target noun token determine which object is selected, whereas mid-to-late layers carry the spatial information in text tokens that redirects the movement when patched. Where spatial information is stored in prompt tokens various based on the architecture. In MolmoAct2 the model forms task-conditioned representations at the text positions that follow the instruction, whereas $π_{0.5}$ additionally stores this information at image token positions. We show that these findings can be translated directly into improving model efficiency. We find that restricting MolmoBot's action expert conditioning to only 3 out of 36 layers reduces inference FLOPs by up to $33\%$ while maintaining comparable task success with the default model across 3,000 evaluation episodes ($46.7\%$ vs. $46.9\%$), and the same principle carries over to real-robot deployment of $π_{0.5}$.


## 精读解读（中文）
### 一、研究动机
VLA模型将预训练VLM主干与扩散或流匹配动作专家通过逐层稠密接口连接，但其如何把视觉、语义与本体感知表示转化为动作仍是黑箱。作者希望用因果分析回答这一映射问题，并把机制发现直接转化为推理效率提升。

### 二、技术方案（Method）
研究在π0.5、MolmoAct2、MolmoBot三个前沿开源VLA上进行：输入表示为图像I、指令u和本体状态s，通过激活修补与接口修补，把供动作专家第j个模块的条件C_j或主干残差流在指定层ℓ与token位置T替换为反事实donor值，同时保持其余计算不变。用共享生成噪声与前向运动学重建轨迹，并以归一化轨迹偏移E度量patch向参考轨迹移动的比例。构建156个反事实对象对，在交换请求物体或交换物体位置等设置下进行超过775,000次干预，扫描单连接与三层窗口，定位中后层窄带动作条件接口。随后把动作专家跨注意力条件限制到该接口层，并在MolmoBot仿真与π0.5真机上评估，包含原始预训练与50K微调适配。

### 三、结果（Result）
三个模型均显示因果相关信息只通过1–3个中后层跨注意力层影响动作专家，形成动作条件接口；修补单层如MolmoBot第24层即可恢复超过50%行为迁移。信息内容随token与层变化：早中层目标名词token决定选哪个物体，中后层文本token携带可重定向运动的空间信息；空间信息存储位置依架构而异，MolmoAct2在指令后的文本位置，π0.5还额外存于图像token位置。效率上，把MolmoBot动作专家条件限制到36层中的3层即23–25层，并在3000个评估回合中测试，推理FLOPs最多降低33%，平均成功率46.7%对默认46.9%，基本无损；单层24为45.6%，而无关层12微调后仅17.8%，同一原则也迁移到π0.5真机部署。

### 四、结论（Conclusion）
该工作给出VLA从感知到动作的因果机制解释：动作专家读取的是主干中后层窄带内已编码任务相关空间信息的表示，而非均匀依赖所有层。因此因果分析可直接指导稀疏化连接与层剪枝，在保持闭环性能的同时显著降低计算，并为已有启发式VLA效率方法提供机制依据。

### 五、方法论与关键技术细节
关键实现包括：反事实数据含156个家庭物体对，接口图基于26个场景的144,768次patch，总干预超过775,000次；行为度量E用前向运动学轨迹与参考轨迹的内积归一化，配对运行固定生成噪声且多在首时刻双物体可见时分析。模型侧差异需注意：MolmoBot以跨注意力供逐层隐藏状态，MolmoAct2供逐层key/value，π0.5条件于共享多模态前缀；注意力掩码也不同，MolmoAct2与MolmoBot图像位置不能注意后续指令token，π0.5前缀内双向。评估采用MolmoBot的Pick、Pick&Place、PnP Next-To等仿真基准，比较全部36层、23–25层、单层24及50K微调适配，共3000回合；局限是仅三个开源模型、FLOPs为估计、空间信息存储具架构依赖性、真机验证主要在π0.5，且未给出完整损失与超参细节。
