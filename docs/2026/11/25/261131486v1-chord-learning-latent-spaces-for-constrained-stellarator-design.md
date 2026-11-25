# CHORD: Learning Latent Spaces for Constrained Stellarator Design

- 区域：精读区
- 排名：6
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Santiago A. Cadena, Andrea Merlo
- 机构：Proxima Fusion
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31486v1) · [PDF](https://arxiv.org/pdf/2611.31486v1)

## TLDR
CHORD is a feasibility-regularized conditional VAE that penalizes predicted constraint violations along decoded latent interpolants and uses self-consistent conditioning to enable feasible interpolation and design exploration for stellarator optimization, achieving up to 81% simulator-validated mid-segment feasibility and denser Pareto-front coverage.

## Abstract
In high-dimensional, PDE-constrained design, interpolating between known feasible solutions can reveal trade-offs without repeating expensive optimization campaigns. In stellarator design for fusion energy, direct interpolation of plasma boundary parameters can violate physical constraints even when both endpoints are feasible. Learned latent representations can capture nonlinear relationships among design variables, but latent interpolation can still cross infeasible regions, and conditioning on target metrics can become inconsistent with the decoded design. We introduce CHORD, a conditional variational autoencoder that penalizes predicted constraint violations along decoded latent interpolants during training, paired with self-consistent inference that aligns conditioning with the decoded design's predicted metrics. Geometric benchmarks show the benefit of regularizing latent interpolants. In stellarator interpolation between distinct geometry families, CHORD reaches up to 81% simulator-validated mid-segment feasibility, compared with 50% for an unregularized conditional VAE and 28% for direct interpolation of boundary parameters. Ablations show that both ingredients are needed for this gain. Beyond interpolation, latent-space optimization finds simulator-feasible designs, while self-consistent sampling produces more diverse feasible alternatives. On the ConStellaration benchmark, chord-regularized models with linear conditioning reuse data from five optimization campaigns and simulator-labeled rescalings to populate the Pareto front more densely. After low-fidelity screening, 93% of 1.2k generated candidates pass the benchmark's high-fidelity feasibility test. We release code and over 600k designs for stellarator generation, surrogate training, and front-filling evaluation. These results support feasibility-aware latent learning for exploring constrained design trade-offs.


## 精读解读（中文）
### 一、研究动机
在PDE约束的高维设计中，直接对已知可行解之间进行插值可能穿越不可行区域，即使两个端点均可行；普通VAE或cVAE只保证端点重建与潜变量先验，不保证潜空间弦内部可行，且条件向量可能与解码设计的预测指标不一致。恒星器设计需要复用昂贵的优化活动、在不同几何家族间探索折衷并填充可行帕累托前沿，因此需要面向可行性的潜空间学习。

### 二、技术方案（Method）
以可行设计x及其条件向量y训练条件编码器-解码器；对可行端点对采样α，在潜空间做线性插值z(α)并解码，用冻结的可微物理代理预测指标，计算加权ReLU约束违反损失L_chord，与cVAE重建损失和β-KL损失相加，λ在重建与KL预热后逐步增大，梯度经解码器和代理回传但不经编码器；训练时条件轨迹y(α)取两端点线性混合，自洽映射只在推理使用。推理时固定潜点并迭代y_{k+1}=clamp(f̂_y(D_θ(z,y_k)))，把解码设计的预测指标反馈为下一条件，clamp可将受约束分量投影到带内部裕度的可行区间；同一迭代用于插值、从先验采样z并配合任务偏置y0的采样优化，固定迭代次数而不假设收敛，最终候选由真实模拟器校验。前端填充实验采用线性条件与ConStellaration基准约束。

### 三、结果（Result）
几何基准中，C-shape的CHORD中弦可行率达0.65±0.03，而cVAE为0.21±0.02；Shells中CHORD将采样的内部可行率提高58个百分点，并在held-out优化任务30个起点中成功28个，cVAE为20个。恒星器两个磁轴几何家族间插值时，CHORD达到最高81%的模拟器验证中段可行率，普通cVAE为50%，边界参数直接插值为28%，消融显示弦正则与自洽条件两个要素均需要。相同代理与评估预算下，潜空间CMA-ES能从CHORD潜空间返回可行候选而81维原空间没有，但该比较不单独隔离弦正则效应。ConStellaration上复用五次优化活动数据后，最大长宽比间隙从1.25降至0.51，超体积小幅提升；低保真筛选后1.2k生成候选的93%通过高保真可行性测试，并发布60万以上设计。

### 四、结论（Conclusion）
CHORD表明，在训练中惩罚解码潜弦上的预测约束违反，并在推理中对齐条件与解码设计的预测指标，可提升潜空间内部而非仅端点的可行性，从而用插值和采样填充受约束设计折衷。它可作为复用既有优化活动、密集化帕累托前沿的可行性感知生成工具，而非替代平衡求解器或通用优化器。结果支持面向可行性的潜空间学习用于恒星器及其他PDE约束设计探索。

### 五、方法论与关键技术细节
数据为等离子体边界Fourier系数及物理指标；固定长宽比实验约束为ι_edge∈[0.725,0.775]、Δ_edge≤0.4、真空井≥0，前端填充采用ConStellaration独立约束；弦损失对K个约束加权，固定长宽比实验w_k=1/K，即物理单位平均违反量，cVAE含β-KL，λ从0预热后增加。关键实现点包括可行设计过滤、冻结可微代理、条件编码器-解码器、自洽固定点与内部clamp裕度；局限包括代理误差需模拟器终验、固定迭代不保证收敛且固定点处clamp分量可能与预测指标不一致、研究约束非完整反应堆评估，以及与CMA-ES的比较未隔离潜空间学习本身效应。
