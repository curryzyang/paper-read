# Neural Fidelity Calibration for Informative Sim-to-Real Adaptation

- 区域：精读区
- 排名：5
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Youwei Yu, Lantao Liu
- 机构：Indiana University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28274v1) · [PDF](https://arxiv.org/pdf/2611.28274v1)

## TLDR
Neural Fidelity Calibration (NFC) uses conditional flow matching to jointly infer simulator physical parameters and residual sim-to-real/perception uncertainties online, enabling informative real-to-sim policy fine-tuning only when anomalies occur and substantially improving robot adaptation on challenging real-world terrain.

## Abstract
Deep reinforcement learning (RL) can transfer agile robot skills from simulation to the real world, but closing the sim-to-real gap by domain randomization requires expert physics knowledge, and simulator calibration from real data typically targets a few hand-picked parameters. Even then, simulators miss real-world effects, and environments reconstructed from onboard perception inherit sensing errors that limit policy improvement. We propose Neural Fidelity Calibration (NFC), which uses conditional flow matching to calibrate simulator physical parameters and residual fidelity domains online during deployment. Residual fidelity captures sim-to-real dynamics discrepancies and perception-induced environment uncertainty. NFC operates in a latent space so that realistic environments can be sampled from the inferred posterior for real-to-sim policy fine-tuning. The framework is informative: the pretrained policy is fine-tuned only when an anomaly is detected, sequential NFC seeds its proposal from the simulation-pretrained estimator, and a hallucination policy modulates posterior uncertainty following optimism in the face of uncertainty. NFC attains the most accurate posteriors among established simulation-based inference methods on five robots with up to 39 physical parameters and a 128x128 residual terrain. On a wheeled robot with a broken wheel axle deployed on snow, mud, and wet grass, NFC raises success on rough terrain from 26% to 70% and reduces orientation jerk by 88%. Code and videos will be released upon publication.


## 精读解读（中文）
### 一、研究动机
深度强化学习可将敏捷机器人技能从仿真迁移到现实，但域随机化依赖专家物理知识，基于真实数据的仿真器校准通常只调少数人工挑选参数；即使校准后，仿真器仍遗漏真实效应，且机载感知重建环境会继承传感误差，限制策略改进。论文因此要解决两个障碍：仿真器并非良校准，以及现有核方法或优化式仿真推断难以扩展到部署中的高维参数与丰富条件。

### 二、技术方案（Method）
NFC将真实转移分解为标称仿真器项、残差保真项和噪声项，其中物理参数ψ描述质量、摩擦等，残差保真φ同时包含仿真与真实状态差Δs及感知与真实环境差Δe，并对ψ、φ和轨迹τ学习联合后验。核心用条件流匹配训练条件密度估计器qθ(ψ,φ|τ)，在仿真生成的参数—轨迹对上最大化对数密度，采样时从高斯经少量Euler步积分速度场得到后验样本；在线采用顺序NFC，以仿真预训练估计器作为提案先验，用新模拟轨迹热启动更新。为处理128×128残差地形等高维目标，潜NFC用TCN编码状态—动作历史、MLP编码融合感知图，并在仿真中利用噪声观测轨迹与特权干净轨迹的嵌入差定义潜残差φz，估计器推断q(ψ,φz|·)，MLP解码器Z映射回φ，速度场、编码器和解码器联合训练负对数密度与重构损失并交替更新。策略侧从NFC后验采样N个域重置并行仿真器，幻觉策略πh按历史嵌入采样每坐标门g∈(0,1]，以x̃=μ+g⊙(x-μ)调制样本扩散，控制策略与πh用PPO联合优化；部署时仅当Siamese异常检测器在最新H步窗口上超过阈值η时触发一轮自适应：推断后验、门控扩散、重置并行仿真器、微调策略并用门控样本更新顺序NFC，任务结束后离线复用真实数据精炼NFC、检测器和策略。

### 三、结果（Result）
在五个机器人、最多39个物理参数及128×128残差地形的仿真评测中，NFC相较已有基于仿真的推断方法取得最准确的后验。真实实验使用轮轴断裂的Jackal轮式机器人，在雪、泥和湿草等野外地形上部署，NFC将粗糙地形成功率从26%提升到70%，并将方向抖动降低88%。

### 四、结论（Conclusion）
论文表明，将仿真器校准与残差保真显式分离，并在潜空间用条件流匹配在线联合推断，可把仿真器无法建模的动力学差异和感知诱导环境不确定性纳入real-to-sim微调。配合异常触发的信息性策略自适应和乐观不确定性调制的幻觉策略，NFC能在高维参数与复杂野外条件下显著提升真实机器人任务成功率与运动平稳性。

### 五、方法论与关键技术细节
关键实现包括：残差保真同时建模残差动力学与残差环境，轮式机器人示例中ψ为13维、残差动力学15维、残差高程图为128×128；训练目标为负对数密度加权重构损失α||Z(φz)-φ||²，异常检测用仅仿真数据训练的二元交叉熵Siamese分类器，阈值取保留名义样本对的第99百分位；在线每轮用最新H步窗口推断并以门控样本作为下一轮提案，N个并行仿真器由后验样本重置，流匹配少步Euler采样利于在线使用。约束与局限是假设ψ、φ和τ具有紧支撑与有界密度以保持物理合理性，依赖仿真预训练、感知图或高程输入以及可学习的残差结构，需要选择窗口长度、并行环境数、重构权重和异常阈值，且仿真预算与真实数据有限，目标是部署期信息性微调而非穷举预训练。
