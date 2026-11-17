# Robustness as a Transferable Skill: Cross-Task Adversarial Defense for Vision-Language-Action Policies

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Jinquan Zhang, Run Yang, Dongfu Yin, Qiang Lai, Yufeng Yan, Pengshuai Yin, F. Richard Yu
- 机构：Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ), Shenzhen University, Carleton University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18702v1) · [PDF](https://arxiv.org/pdf/2611.18702v1)

## TLDR
The paper shows that adversarial-defense updates learned on source vision-language-action manipulation tasks can be reused as a transferable robustness skill for independently specialized target policies, with a new SN-TRV composition method improving robustness without target-side adversarial training—raising physical patch-attack success from 20.3% to 45.8%.

## Abstract
Vision-Language-Action (VLA) policies are vulnerable to adversarial visual perturbations, while defenses often require task-specific adversarial fine-tuning. We investigate whether robustness learned on source manipulation tasks can protect independently specialized target policies without target-side adversarial training. We first show that even a single source defense update improves robustness on held-out tasks, establishing cross-task defense reuse independently of multi-source aggregation. To combine source updates, we introduce Source-Norm Transferable Robustness Vector (SN-TRV), which retains the direction of their mean while calibrating its magnitude using source-update norms. The resulting update is applied to the target visual encoder without target adversarial data, target-side gradient optimization, or additional inference modules. Evaluations across three VLA backbones, fixed and adaptive attacks, and different source defense recipes show improved robustness over naive averaging and identify limits in attack coverage. Physical PiPER trials increase average success under printed adversarial patches from 20.3% to 45.8%.


## 精读解读（中文）
### 一、研究动机
VLA策略依赖视觉观测，易受可物理实现的对抗视觉扰动影响，而现有防御多需针对被保护任务进行对抗微调。本文探究在源操作任务上学到的对抗鲁棒性能否作为一种可迁移技能，在不对目标策略做目标侧对抗训练的情况下保护独立专门化的目标策略，并进一步解决多源防御更新如何组合的问题。

### 二、技术方案（Method）
将策略参数分为视觉编码器θ与其余组件ψ；对每个源任务先做EDPA对抗微调50k步，得到防御更新Δ_i=θ_i^R−θ_i，目标策略不参与更新构造。多源时先取均值方向u_def=Δ̄/||Δ̄||_2，再用源更新平均范数r_src=mean||Δ_i||_2校准幅度，构造SN-TRV更新Δ_SN=r_src u_def=(r_src/||Δ̄||_2)Δ̄，并将其仅加到独立专门化目标策略的视觉编码器θ_T上。该过程不需要目标对抗数据、目标侧梯度优化或额外推理模块，且目标动作头、本体感知模块等非视觉组件保持不变。

### 三、结果（Result）
在LIBERO的Goal和Long留出目标上，原始OpenVLA-OFT在EDPA Dual攻击下成功率仅22.2%和10.0%，单源Spatial防御更新可提升至87.2%和68.6%，单源Object更新达80.0%和60.6%，表明单源防御即可跨任务复用。多源朴素平均Mean-Δ仅76.6%和62.0%，SN-TRV提升至95.4%和79.4%，分别比Mean-Δ高18.8和17.4个百分点，比Spatial单源高8.2和10.8个百分点，同时保持清洁成功率97.2%和92.4%。在三种VLA骨干、固定与自适应攻击以及不同源防御配方上，SN-TRV优于朴素平均，物理PiPER试验在印刷对抗贴片下平均成功率由20.3%提高到45.8%，但也暴露攻击覆盖范围有限。

### 四、结论（Conclusion）
研究表明对抗鲁棒性可作为跨任务迁移的防御增量，源任务上学到的视觉编码器防御更新能保护独立专门化的目标VLA策略，而无需目标侧对抗微调。SN-TRV通过分离防御方向估计与幅度校准，缓解多源更新方向不一致导致的范数衰减，是一种无需额外推理模块的源侧防御复用方案。其效果依赖源-目标视觉编码器的架构、初始化和参数化对齐，并受攻击类型覆盖限制，物理场景成功率仍不高，不能替代目标侧对抗微调的全部收益。

### 五、方法论与关键技术细节
实验以LIBERO四个套件Spatial、Object、Goal、Long为数据，每个套件10个任务、每任务默认50次rollout即每条件500回合，Spatial和Object作为源、Goal和Long作为留出目标；主要骨干为OpenVLA-OFT，并测试OpenVLA与π0，攻击包括EDPA的Primary、Wrist、Dual及自适应攻击、SARF衍生更新和AGSD。关键实现是只迁移视觉编码器参数，源更新由EDPA-AF 50k步得到，比较Original、直接Spatial/Object迁移、Mean-Δ、Cos-Select、Cos-Select+SN、SN-TRV及WSC基线；Cos-Select按53个参数组的符号余弦相似度选择并保持源侧掩码。SN-TRV的参考幅度仅由源更新范数确定，等价于在固定源范数约束下最小化到各源更新的平方距离，是对几何一致性的刻画而非目标鲁棒性最优保证。局限包括源与目标需共享视觉编码器架构、初始化和参数化，目标侧无对抗优化使防御受攻击覆盖范围约束，物理试验成功率45.8%仍明显有限且计算主要涉及参数向量范数与方向组合、无需额外推理开销。
