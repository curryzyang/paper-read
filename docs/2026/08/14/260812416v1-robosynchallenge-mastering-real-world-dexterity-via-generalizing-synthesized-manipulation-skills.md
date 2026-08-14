# RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Runyi Zhao, Ruixin Wu, Chengkun Li, Hongrui Zhang, Ang Li, Ruixing Jin, Yueci Deng, Yingying Guo, Lihe Ding, Shaocong Dong, Tianfan Xue, Yanjun Gao, Yudong Luo, Pascal Poupart, Simo Wu, Kui Jia, Wei-shi Zheng, Guiliang Liu
- 机构：Shenzhen Loop Area Institute (SLAI), Fudan University, University of Waterloo, Sun Yat-sen University, The Chinese University of Hong Kong, The Hong Kong University of Science and Technology, University of Colorado Anschutz, The Chinese University of Hong Kong, Shenzhen, DexForce, Mila - Quebec AI Institute, Vector Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.12416v1) · [PDF](https://arxiv.org/pdf/2608.12416v1)

## TLDR
RoboSynChallenge introduces a unified benchmark that combines large-scale synthetic data generation with standardized real-world evaluation to assess and improve the generalizability of robotic manipulation policies across diverse tasks and environments.

## Abstract
Achieving generalizable robotic manipulation remains a central challenge in embodied intelligence. Despite rapid advances in model architectures and learning algorithms, progress is often limited by the scarcity and narrow diversity of real-world data. The RoboSynChallenge competition introduces a unified benchmark to evaluate and advance the generalizability of manipulation policies across a spectrum of tasks, environments, and difficulty levels. To alleviate the shortage of realistic data, the challenge integrates large-scale synthetic data generation with standardized real-world robotic evaluation. Participants are encouraged to leverage synthesized state-action trials to improve general-purpose policy learning, while final assessments are conducted exclusively on unseen real-world manipulation environments. Baseline implementations, including Transformer-, Diffusion-, Vision-Language-Action, and World-Action-Model-based policies, are provided to ensure reproducibility and comparability. By coupling scalable simulation-based training with rigorous real-world validation, RoboSynChallenge aims to foster the development of broadly capable, data-efficient, and adaptable manipulation systems, thereby paving the way toward truly general robotic intelligence.


## 精读解读（中文）
### 一、研究动机
真实世界操作数据稀缺且多样性有限，严重制约了机器人操作策略的泛化能力；现有基准要么局限于仿真环境，要么依赖昂贵且难以扩展的真实数据，且大多使用固定数据集，无法公平评估策略在未见真实环境中的泛化性能。为此，RoboSynChallenge提出一个统一基准，将大规模合成数据生成与标准化真实世界评估相结合，量化模拟数据在真实数据稀缺情况下对操作策略泛化能力的提升效果。

### 二、技术方案（Method）
RoboSynChallenge构建了完整的生成式数据与评估流水线：使用EmbodiChain生成式仿真框架，对光照、物体属性、桌面纹理、背景颜色、机器人配置以及相机内外参进行系统随机化，为每个任务生成1000条成功的仿真操作轨迹，并辅以少量遥操作采集的真实数据（每任务5种实验条件×4位置×3朝向共60条样本），支持仿真-真实协同训练。任务涵盖入门、中级、高级三档，涉及刚体、铰接物体、软体与工具操作，基于双AgileX Piper六自由度机械臂平台，仅依赖视觉观测与本体感觉。评估时在真实环境中系统变化背景（3种桌面纹理）、光照（3种位置/颜色）、物体（已见/未见实例）、干扰物（2/4/8个）和空间位置，逐因子扰动并报告成功率；同时提供Transformer、Diffusion、Vision-Language-Action和World-Action-Model等基线实现，确保可复现性与公平对比。

### 三、结果（Result）
RoboSynChallenge作为首个在统一框架下评估Sim2Real迁移能力的标准化基准，通过大规模合成数据训练与严格真实世界留出测试相结合，系统测量策略在背景、光照、物体、干扰物和位置变化下的成功率、推理时间与动作步数。该基准在刚体、铰接物体、装配和工具使用等任务类别上均覆盖，并支持双臂操作，区别于以往仅限单臂、仿真或离线数据集的竞赛；其生成式数据流（非固定人工数据集）与真实世界排名机制，能够直接反映模拟数据对真实泛化性能的贡献。

### 四、结论（Conclusion）
RoboSynChallenge通过耦合可扩展的仿真训练与严格的真实世界验证，旨在推动开发广泛适用、数据高效且适应性强的操作策略，为迈向真正通用的具身智能奠定基础。该基准强调模拟数据生成与真实评估的统一，有望填补Sim2Real标准评估的空白，促进机器人操作泛化研究的可复现与可比发展。

### 五、方法论与关键技术细节
数据集以EmbodiChain生成的成功轨迹为主，仅包含成功样本用于训练，真实测试数据不依赖地面真值标签，通过物理环境直接判定结果以避免泄露；合成数据协议采用多级随机化（光照、材质、几何、感知），每任务1000条轨迹，真实数据每任务60条样本，训练/评估环境均开放获取，数据采用CC BY-NC-SA 4.0许可；评估使用真实世界留出协议，训练观测与测试环境分布不同确保OOD；硬件为双臂Piper平台，配备三套相同备用工位以保证测试效率；基线模型在A800 GPU上统一部署，推理时间和动作步数作为效率指标；局限性在于真实评估依赖固定机器人平台和物理设置，扩展至其他硬件仍需额外适配。
