# Near-Zero Forgetting Is Not Enough: Out-of-Distribution Robustness in Continual Learning of Pretrained VLAs

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Adrià Ruiz, Bartłomiej Twardowski, Tinne Tuytelaars, Sergi Masip
- 机构：Universitat Autònoma de Barcelona, Computer Vision Center, KU Leuven, IDEAS Research Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31511v1) · [PDF](https://arxiv.org/pdf/2611.31511v1)

## TLDR
The paper shows that experience-replay continual learning of pretrained VLAs can achieve near-zero in-domain forgetting while still suffering severe out-of-distribution forgetting on previously learned tasks, driven by representational drift and misalignment concentrated in multimodal and action features.

## Abstract
Recent work shows that pretrained Vision-Language-Action (VLA) models exhibit near-zero forgetting in specific continual learning settings with experience replay. However, robustness to domain shift of learned tasks remains unexplored. In this work, we study the robustness of Pi0 fine-tuned with experience replay under out-of-distribution (OOD) data using the LIBERO and LIBERO-Plus benchmarks. While the in-domain (ID) setup achieves near-zero catastrophic forgetting, OOD performance on previous tasks quickly collapses. Specifically, we show that during the continual learning process, the OOD capabilities of the model degrade, following a shared representational pattern across domain shifts, which is also visible behaviorally in the two simpler suites. Representational analysis shows that drift concentrates in the multimodal and action features. Linear probes indicate that OOD features still retain task-relevant information, but appear unreadable, consistent with representation misalignment. These findings suggest that even when ID stability remains intact, severe OOD forgetting can still occur, accompanied by representational drift during continual learning.


## 精读解读（中文）
### 一、研究动机
已有工作报告预训练VLA在经验回放持续学习中域内近零遗忘，但其对已学任务域偏移（OOD）的鲁棒性尚不清楚。作者据此提出核心假设：经验回放下的近零遗忘可能只适用于ID评测，不能外推到分布偏移场景。该问题关系到终身机器人系统在真实环境变化下是否真正可靠。

### 二、技术方案（Method）
复现Pi0（PaliGemma视觉语言主干加flow matching动作专家）在LIBERO四个套件上的持续学习基线：按任务顺序训练，每个任务经验回放缓存1000帧，后续任务训练批次按1:1混合当前任务与回放样本，并保存每个任务后的checkpoint θ_k。评测同时使用ID LIBERO与OOD LIBERO-Plus的七类扰动（背景纹理、机器人初始状态、外部相机视角、物体布局、光照、语言指令改写、传感器噪声），计算ACA、NBT及OOD NBT。表征分析在视觉编码器后、VLM后和动作模块首个flow matching步（τ=0）三处提取特征，对非padding token均值池化为每帧向量，用线性CKA测漂移、MMD测ID-OOD分布差距、线性探针R²测任务信息可读性。

### 三、结果（Result）
ID评测复现了近零遗忘：Object、Goal、LIBERO-10的NBT分别为-0.005、-0.017、-0.036，Spatial为+0.026，整体稳定甚至轻微后向迁移。OOD则在习得时已下降，并随继续学习快速崩溃：平均OOD NBT在Spatial、Object、Goal、LIBERO-10分别为+0.40±0.13、+0.48±0.17、+0.42±0.15、+0.16±0.09，多数任务在一两个后续任务后成功率接近0；ID ACA稳定或略升，而OOD ACA持续下降。不同扰动下的失败位置高度一致（Spatial和Object的active cell模式平均相关r=0.73和0.82），表征的ID-OOD MMD²与CKA跨扰动相关在各套件均为正（MMD²为0.67/0.76/0.76/0.77，CKA为0.64/0.75/0.72/0.84），漂移主要集中在多模态与动作专家层，视觉编码器相对稳健；线性探针显示OOD特征仍含任务相关信息但线性可读性下降。

### 四、结论（Conclusion）
因此，域内近零遗忘不足以证明持续学习成功；即使ID稳定性保持，模型仍可能发生严重的OOD遗忘，并伴随多模态与动作表征漂移和ID-OOD表征错位。持续学习VLA的评测与方法设计应显式纳入OOD鲁棒性，而不能仅以ID NBT或成功率作为安全性依据。

### 五、方法论与关键技术细节
关键实现包括每任务1000帧回放、当前/回放1:1采样、按任务保存checkpoint并以NBT和ACA在ID及七类OOD扰动上评估；表征在视觉、VLM、动作模块三处提取，flow matching步固定τ=0并均值池化非padding token，CKA越低表示漂移越大、MMD越高表示ID-OOD差距越大、线性探针R²越低表示信息越不可读。局限在于结论基于Pi0、经验回放和LIBERO/LIBERO-Plus设定，未提出缓解方法；Goal与LIBERO-10行为层面多已塌缩为零，跨扰动行为一致性主要来自较简单套件，且部分分析依赖附录中的表征设置。
