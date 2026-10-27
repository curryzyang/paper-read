# Neural-DISCO: Source-Conditioned Counterfactual Editing of Neural Population Activity

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Nico Policzer, James Ho, Joseph Soo, Xin Tang
- 机构：University of British Columbia
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33145v1) · [PDF](https://arxiv.org/pdf/2610.33145v1)

## TLDR
Neural-DISCO is a disentangled representation-learning framework that separates neural activity into label-specific and residual latents, enabling source-conditioned counterfactual editing of behavioral or stimulus labels while preserving other observed and source-specific variability, and improving identification of label-relevant neurons.

## Abstract
Understanding how neural activity encodes behavioral and sensory variables is a key challenge in systems neuroscience. This requires models that go beyond predicting activity from labels and instead support source-conditioned counterfactual editing: given a recorded source response, we should be able to edit one measured behavioral or stimulus label and predict how neural activity would change while preserving other observed labels and source-specific variability not explained by the labels. Here, we introduce \textbf{Neural-DISCO}, a disentangled representation learning framework for counterfactual modeling of neural activity. Neural-DISCO partitions the latent space into label-specific components, each associated with an observed behavioral or stimulus label, together with a residual latent that captures variability not supplied through observed labels. Across simulated and real neural recording datasets, we show that this structure enables selective editing of measured labels to generate counterfactual neural responses while preserving the remaining content of the original activity. Further, to gain insight into how behavioral and stimulus labels are encoded at single-neuron resolution, we pair this disentangled framework with feature attribution methods that identify which neurons are most important for each label. We find that disentanglement enhances the recovery of known functional cell roles in both synthetic and real data. Together, these results support Neural-DISCO as a framework for counterfactual modeling of neural activity and provide a practical interface for probing how neural populations encode behavior and sensory information. Code is available at https://github.com/TangLab-UBC/Neural-DISCO-neurips.


## 精读解读（中文）
### 一、研究动机
系统神经科学需要超越从行为或刺激标签预测神经活动的模型，支持源条件反事实编辑：给定真实记录的源神经响应，编辑一个已测量的行为或刺激标签，并预测神经活动如何变化，同时保留其他已观测标签和无法由标签解释的源特异性变异。

### 二、技术方案（Method）
Neural-DISCO将潜空间划分为与各观测行为或刺激标签对应的标签特异分量，并加入一个残差潜变量以捕获未由观测标签提供的变异；模型将神经群体活动编码到残差潜变量，将标签嵌入到标签特异分量，再由生成器产生放电率并重构源活动。训练使用重构损失和残差正则化，其中带噪声的残差瓶颈与残差激活惩罚用于限制标签信息泄漏到残差。反事实推理时，固定源样本的残差潜变量和其他标签分量，仅替换目标标签的嵌入，经生成器得到反事实神经响应；并用积分梯度将各标签和残差的贡献归因到单个神经元。

### 三、结果（Result）
在RatInABox模拟数据、MC Maze猕猴 reaching 数据和Allen Visual Coding数据上，Neural-DISCO能够选择性编辑位置、头方向、手部运动或运行速度等标签，使目标因子的生成响应向编辑目标移动，同时保留非目标标签和 withheld 信息。模拟数据中用编辑目标的真实放电率计算R²，真实数据中通过下游解码评估编辑后活动对目标手位置、手速度、眼位置或速度的预测，并用平衡准确率检验未编辑刺激信息的保留；归因分析在合成数据中更好恢复位置细胞、头方向细胞和速度细胞角色，在Allen数据中与方向选择性指数相关并能区分运行调制单元。去掉残差瓶颈的消融模型出现源信息泄漏，反事实编辑失败或编辑后活动仍更像源 trial。

### 四、结论（Conclusion）
Neural-DISCO提供了一个源条件反事实编辑与神经元级归因相结合的框架，可作为探测神经群体如何编码行为与感觉信息的实用接口；其反事实结果在满足因果分解假设时具有干预解释，否则应视为学习分解下的模型预测。

### 五、方法论与关键技术细节
实验使用50 ms分箱的脉冲计数，10折交叉验证，种子为314159加折索引；RatInABox含300个合成神经元并 withheld 速度，MC Maze使用137个单元及手位置、手速度和眼位置标签，Allen Visual Coding用于运行速度和方向选择性分析。残差噪声在RatInABox和Allen中设为0.02、在MC Maze中设为0.04，并对残差正则系数λ做敏感性扫描；积分梯度使用零基线和50步Gauss-Legendre积分，每个折固定32个源样本。计算量约6个H200 GPU小时、训练峰值显存低于1 GB；局限性包括反事实的因果语义依赖真实条件分解与残差编码假设，远离训练支撑或违反标签自然依赖的编辑属于外推，且学习到的残差不等同于真实生成因子H。
