# Disentangling Attention in Deep Operator Learning: A Controlled Study of Data-Driven and Physics-Informed Architectures

- 区域：精读区
- 排名：2
- 匹配度：5.8/10
- 来源：arxiv
- 作者：Amar Alem Koric, Qibang Liu, Seid Koric
- 机构：University of Illinois at Urbana-Champaign, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.04407v1) · [PDF](https://arxiv.org/pdf/2609.04407v1)

## TLDR
This controlled study of five DeepONet variants with matched architectures isolates attention mechanisms under data-driven and physics-informed training, finding that per-sensor tokenization with query-dependent cross-attention is the most reliable and consistently accurate improvement (reducing mean relative L₂ error by factors of 2.4–32.3), while branch self-attention helps mainly for large, spatially complex functional inputs and global pre-mixing offers little benefit.

## Abstract
Deep neural operators learn mappings between input functions and complete PDE solution fields, enabling forward evaluations of new problem instances orders of magnitude faster than conventional numerical solvers. Attention mechanisms have recently been introduced into neural operators, but most studies change several architectural components at once, making it difficult to identify what actually improves accuracy. This work presents a controlled and systematic study of five deep operator network (DeepONet) variants with distinct attention mechanisms, trained under both data-driven and physics-informed regimes, to isolate the effects of cross-attention, self-attention, tokenization, and attention depth. We evaluate them on a source-driven transient one-dimensional nonlinear diffusion-reaction equation, a transient one-dimensional viscous Burgers equation with variable initial conditions, and a two-dimensional Poisson heat-conduction problem with heterogeneous source fields. Per-sensor tokenization with cross-attention reduces the mean relative L_2 error of the classical DeepONet in all benchmark-training combinations by factors of 2.4-28.0, while the best attention configurations reach 3.5-32.3. Branch self-attention paired only with dot-product fusion is inconsistent, degrading the one-dimensional problems while helping the more complex two-dimensional source field; added on top of cross-attention it improves all six cases, though by less than cross-attention fusion alone. Global pre-mixing provides no consistent benefit. Increasing cross-attention depth further improves accuracy, but with diminishing returns and a substantially higher cost under physics-informed training. Overall, query-dependent cross-attention is the most reliable mechanism, whereas branch self-attention is most useful for large, spatially complex functional inputs.


## 精读解读（中文）
### 一、研究动机
深度神经算子虽然能以远超传统数值求解器的速度进行正向评估，但现有引入注意力机制的神经算子研究往往同时改变多个架构组件，难以精确判断究竟是哪个机制真正提升了精度。本文旨在通过受控的组件级研究，将交叉注意力、自注意力、tokenization方式和注意力深度对算子学习的影响逐一分离，为注意力机制在深度算子网络中的实际价值提供可靠证据。

### 二、技术方案（Method）
以经典DeepONet为基线，构建五种仅在指定组件上不同的变体：V1为标准DeepONet点积融合；V2将分支输入按传感器token化并用交叉注意力替代点积融合；V3保留点积融合但在分支token间加入自注意力；V4在V2基础上加入全局信息注入；V5同时采用分支自注意力和交叉注意力。所有模型在数据驱动和物理信息（PDE残差约束）两种训练模式下，对一维非线性扩散-反应方程、一维粘性Burgers方程和二维Poisson热传导问题三个基准进行训练和评估，严格控制模型容量、优化器、采样预算、训练调度和评估流程，以隔离单一组件的影响。交叉注意力以trunk输出为查询、分支token为键值，使用多头注意力块（含残差和LayerNorm）；分支编码先经嵌入层和token FFN，并在指定位置加入位置编码。

### 三、结果（Result）
逐传感器token化结合交叉注意力在所有基准-训练组合中使经典DeepONet的平均相对L2误差降低2.4-28.0倍，最优注意力配置达到3.5-32.3倍；分支自注意力若仅搭配点积融合则表现不一致，会恶化一维问题但对更复杂的二维源场有帮助；在交叉注意力基础上叠加自注意力能改善全部六个案例，但增益小于单独使用交叉注意力融合。全局预混合无一致收益，增大交叉注意力深度可进一步降低误差，但收益递减且物理信息训练下成本显著增加。总体而言，查询相关的交叉注意力是最可靠机制，分支自注意力主要对大尺度、空间复杂的函数输入有意义。

### 四、结论（Conclusion）
在深度算子学习中，交叉注意力作为分支-骨架融合机制比经典点积更有效，且应避免将自注意力与点积融合混用；分支自注意力仅在输入函数空间变化复杂时值得使用。注意力深度增加虽能提升精度但需权衡训练开销，尤其物理信息学习下成本更高。该受控比较为注意力神经算子提供实践指导。

### 五、方法论与关键技术细节
研究采用逐传感器tokenization，将每个传感器值映射为p维token，位置编码按基准和训练范式设计；物理信息训练使用自动微分计算PDE残差、初边值条件损失，且二维Poisson模型中readout省略LayerNorm。所有模型使用JAX实现，注意力采用h头、head维度p/h，配置在深度研究中可堆叠N个交叉注意力块。模型容量、优化器、采样预算等保持一致以确保归因有效。局限：未与所有现代算子架构比较，且位置编码形式未独立变化。
