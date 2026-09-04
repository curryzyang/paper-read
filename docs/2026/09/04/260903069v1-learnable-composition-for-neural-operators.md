# Learnable composition for neural operators

- 区域：精读区
- 排名：3
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Zituo Chen, Baiming Zhang, Sili Deng
- 机构：University of Toronto, MIT
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03069v1) · [PDF](https://arxiv.org/pdf/2609.03069v1)

## TLDR
TLDR: The paper proposes LatentDDM, a neural operator framework that pretrains a local subdomain predictor and then, for new domains or operating conditions, freezes it and trains only a lightweight learnable composition module to combine local predictions, achieving 36–56% lower error on larger Darcy flows and improved airfoil rollouts under few-shot adaptation.

## Abstract
Neural operators are fast, differentiable surrogates for physical simulation, but their accuracy often degrades when domain geometry, size, or operating conditions differ from training. Supervised adaptation can recover accuracy, but even a small target set requires costly high-fidelity simulations. We therefore ask how pretraining and transfer can be designed together to reduce this deployment cost. LatentDDM first pretrains a neural operator to predict fields on small subdomains. For a new setting, it freezes this operator and trains only a lightweight module that composes the local predictions. We evaluate our method on two complementary problems: steady Darcy flow, where long-range pressure coupling must extend across increasingly large porous domains, and unsteady incompressible flow around a pitching airfoil, where rollout errors compound as target pitching frequencies exceed the training range. Compared with the capacity-matched models that process the full domain at once, LatentDDM's error is 36-56% lower on larger Darcy domains after adaptation with 16 target simulations. It also improves 20-step field rollouts in fast-pitching airfoil flow, both zero-shot and after few-shot calibration. These results identify the co-designed local pretraining and composition-level transfer as a promising design principle for physical foundation models.


## 精读解读（中文）
### 一、研究动机
神经算子作为物理模拟的快速可微替代模型，在域几何、尺寸或运行条件与训练数据不同时精度常会下降。有监督适应虽可恢复精度，但即使少量目标样本也需昂贵的高保真模拟，部署成本高。因此需要联合设计预训练与迁移策略，以降低部署成本。

### 二、技术方案（Method）
提出LatentDDM框架，先将神经算子在小子域上预训练以预测局部场，冻结该局部算子；随后针对新场景仅训练一个轻量级可学习组合模块，该模块以各子域初预测结果及子域间相对位移为输入，通过轻量Transformer在子域token间交换信息并输出每个子域的输入修正量，再用同一冻结局部算子做第二次评估，最后组装全域场。对比方法包括全域Transformer（Point/Slice/Patch token化）和迭代式神经DDM（SNI）。目标任务适应时仅更新组合模块参数，局部算子保持冻结。

### 三、结果（Result）
在稳态Darcy流和俯仰翼型非定常不可压缩流动两个问题上评估。与同容量全域处理模型相比，在使用16个目标模拟进行适应后，LatentDDM在更大Darcy域上误差降低36%-56%；在快速俯仰翼型流动中，20步场滚动预测在零样本和少样本校准后均有改善。

### 四、结论（Conclusion）
局部预训练与组合层迁移的协同设计是物理基础模型的一种有前景的设计原则。误差分析表明局部预训练决定可达覆盖误差，组合模块决定选择误差，两者共同决定全场景预测精度；相比全域模型，当组合方式的覆盖与选择代价小于有限样本泛化差距的缩减时，组合迁移更有利。

### 五、方法论与关键技术细节
关键点：局部算子预训练目标为最小化子域预测与真实场的均方误差；组合模块为轻量Transformer，输入为子域初始预测、局部输入和相对位移，输出逐子域输入修正；推理流程为一次局部预测、组合修正、第二次局部预测并组装。适应时冻结局部算子仅微调组合模块，可显著减少所需目标高保真模拟数量（如16个）。理论误差界将总误差分解为局部覆盖误差、组合选择误差和有限样本估计误差。局限包括局部算子无法表达的目标响应会限制最终精度，且SNI类迭代方法在固定点失配时增加迭代无法消除该失配。
