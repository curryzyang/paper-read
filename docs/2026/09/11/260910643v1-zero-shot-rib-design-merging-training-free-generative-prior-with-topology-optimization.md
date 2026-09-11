# Zero-shot rib design: merging training-free generative prior with topology optimization

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Yongmin Kwon, Namwoo Kang
- 机构：Korea Advanced Institute of Science and Technology, Narnia Labs
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.10643v1) · [PDF](https://arxiv.org/pdf/2609.10643v1)

## TLDR
This paper presents a zero-shot, training-free rib-design framework that couples a frozen text-to-image diffusion model’s prompt-derived generative prior with density-based topology optimization via score distillation sampling, letting natural-language design intent guide FEA-filtered optimization that improves compliance, suppresses dead-end branches, and generalizes across domains and physics regimes without retraining.

## Abstract
Natural load-bearing patterns such as leaf venation, trabecular bone, and spider webs achieve high stiffness per unit mass, yet classical topology optimizers rarely reach such geometries, and few let engineers express structural design intent through natural language. This work treats a frozen text-to-image diffusion model as a training-free source of design knowledge and distills it into the physics loop of density-based topology optimization via score distillation sampling, so that a text prompt becomes an explicit, machine-interpretable representation of engineer intent. The prompt-induced generative gradient and the finite element sensitivity are combined at every iteration, letting physics decide which prompt-induced features survive. In 245 primary SDS runs spanning four geometric domains and two physics regimes, 38 of 49 prompt--domain combinations achieved statistically significant compliance reductions (up to $-31.5\%$ mechanical and $-23.0\%$ thermoelastic), outperforming gradient-based baselines. Cross-domain morphological analysis identifies a recurring structural signature of improvement: in most domains the generative prior suppresses dead-end branches in the rib skeleton, with endpoint--compliance correlation $r = +0.56$ to $+0.99$. A Heaviside projection with $β$-continuation resolves a pronounced intermediate-density tendency in this diffusion--physics coupling ($42.6\%$ to $<3\%$), and an automated skeleton-based pipeline converts optimized density fields into \rev{candidate geometry ready for computer-aided design. By retargeting the generative prior across domains, loading conditions, and physics objectives through a change of text prompt, with each new problem's physics setup specified separately, the framework uses a pretrained generative model as a reusable, training-free prior for engineering design.


## 精读解读（中文）
### 一、研究动机
自然承力图案如叶脉、骨小梁和蛛网具有高刚度质量比，但经典拓扑优化器难以达到这类几何，且很少允许工程师用自然语言表达结构设计意图。现有数据驱动扩散模型通常依赖大量域内训练数据，跨载荷/边界条件泛化差，并在生成时缺少与物理求解器的主动耦合。本文因此把冻结的文本到图像扩散模型视为免训练设计知识源，通过评分蒸馏采样注入密度基拓扑优化的物理回路。

### 二、技术方案（Method）
框架以SIMP密度场和Mindlin–Reissner板有限元为物理模型，输入为用户文本提示、设计域、边界与载荷条件及体积分数，先验为冻结的Stable Diffusion 2.1。每次迭代中，当前密度场被编码到扩散潜空间并加噪，U-Net在无分类器引导下预测噪声，经SDS反传得到文本生成梯度，并与有限元柔度灵敏度加权求和后更新密度。优化采用四阶段调度：30步warmup仅用物理梯度、500步余弦冷却令SDS权重衰减到零、扩散时间步从0.98线性退火到0.50、SDS梯度指数移动平均平滑；随后用Adam、二分法体积约束和Heaviside投影β连续化求解，收敛密度场再经二值化、中轴细化、Bézier曲线拟合和拉伸转为CAD候选几何。整个过程无需任务训练、微调或标注拓扑优化数据，重定向到新域、载荷或物理目标主要靠更换文本提示，但每个新问题仍需单独指定物理设置和数值参数。

### 三、结果（Result）
在245次主SDS运行、四个几何域（从合成基准到工业汽车悬架连杆）和两种物理机制（机械与热弹性弯曲）中，49个提示–域组合有38个取得统计显著柔度降低，机械最高降低31.5%，热弹性最高降低23.0%，并优于梯度基线。跨域形态分析发现改进的结构签名主要是抑制肋骨架中的死端分支，端点数量与柔度呈正相关，Pearson r为+0.56至+0.99。Heaviside投影与β连续化将该SDS–SIMP耦合中的中间密度比例从42.6%降至<3%；热传导任务出现负结果，说明方法存在适用边界；机械子集统计显著性为p=0.031。

### 四、结论（Conclusion）
结果表明，预训练文本到图像扩散模型可作为可复用、免训练的工程设计先验，通过自然语言提示把设计意图转变为机器可解释表示，并在每次迭代中由有限元物理筛选生成特征。该框架在多个域和物理目标上实现零样本或零重训迁移，为文本引导的肋加强结构设计提供了从优化密度场到CAD候选几何的自动化管线。其有效性依赖物理机制匹配，热传导负结果说明不能无条件外推，且每个新工程问题仍需完整定义物理与数值设置。

### 五、方法论与关键技术细节
关键实现细节包括：数据侧为零任务训练样本、零标注拓扑数据，先验为权重冻结的Stable Diffusion 2.1，损失/更新为SDS噪声预测梯度与FEA柔度灵敏度在每次密度更新中加权耦合，超参含warmup=30、cooldown=500、扩散时间步0.98→0.50、SDS梯度EMA、Adam、二分法体积约束及Heaviside投影β连续化。计算与约束上，训练成本记为0 GPU-hrs，重定向成本远低于需重训的数据驱动模型，但每个新问题仍需设计域、边界载荷、物理模型、体积分数和包括λ_sds^0在内的数值参数。方法局限包括SDS–SIMP耦合会产生显著中间密度倾向，需同步β调度与SDS调度缓解；热传导任务为负结果，且验证集中在二维密度基肋/板弯曲问题，CAD输出依赖骨架化后处理。
