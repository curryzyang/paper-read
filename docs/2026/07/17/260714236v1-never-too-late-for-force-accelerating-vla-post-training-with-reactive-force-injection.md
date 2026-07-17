# Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Yi Wang, Wendi Chen, Zimo Wen, Han Xue, Xueqi Li, Wenye Yu, Zhijie Chen, Hao Yang, Jun Lv, Chuan Wen, Cewu Lu
- 机构：Shanghai Jiao Tong University, Southern University of Science and Technology, Shanghai Innovation Institute, Noematrix Ltd.
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14236v1) · [PDF](https://arxiv.org/pdf/2607.14236v1)

## TLDR
LIFT introduces reactive force injection via causal force memory and zero-initialized cross attention into pretrained VLA policies, enabling faster and more effective post-training for contact-rich manipulation while preserving general manipulation knowledge.

## Abstract
Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge. LIFT grafts a reactive action expert beside the original action expert, initializes it from pretrained action weights, and injects recent 6D end-effector force through causal force memory and zero-initialized cross attention, enabling actions to be refreshed during execution. To address the policy-dependent distribution shift of contact feedback, LIFT further couples reactive force injection with an online DAgger loop that trains on a mixture of offline task-alignment data and human-corrected online rollouts. Across towel folding, book insertion, and Hanoi ring placement, LIFT learns faster and reaches higher performance than vision-only post-training, while ablations show that reactive force memory and online corrective data are both important for robust contact-rich manipulation. Our code and data will be publicly available.


## 精读解读（中文）
### 一、研究动机
预训练的视觉-语言-动作（VLA）策略在下游任务中普遍依赖视觉信息，然而一旦操作进入接触阶段，场景遮挡、深度模糊或微小力误差会导致执行偏离离线演示分布。因此，亟需在VLA后训练阶段引入力反馈，以增强策略在接触状态下的实时反应能力。

### 二、技术方案（Method）
LIFT框架在预训练VLA的动作专家旁嫁接一个初始化自原权重的反应性动作专家，通过因果力记忆编码最近6D末端力，并使用零初始化的交叉注意力将其注入反应性专家，实现动作块内的因果解码与实时更新。训练采用两阶段：阶段一在离线视觉任务对齐数据上训练并屏蔽力路径；阶段二通过在线DAgger循环收集力纠正数据，与离线数据按1:1比例混合，使用加性流匹配目标联合训练，并对力路径施加选择性掩码以处理异质数据。

### 三、结果（Result）
在毛巾折叠、书本插入和汉诺塔环放置三个真实操作任务上，LIFT相比纯视觉在线DAgger后训练方法，学习更快且峰值性能更高：毛巾折叠达到0.825成功率（样本数2.8K），书本插入达到0.6（样本数4.6K）。消融实验表明去除反应力记忆或在线DAgger均导致性能下降，验证了关键设计的必要性。

### 四、结论（Conclusion）
力反馈能够显著加速VLA后训练并提升接触式操作任务的最终性能，而因果力记忆和零初始化交叉注意力机制可以保留预训练先验，在线DAgger则缓解了力分布的策略依赖漂移，使框架兼具快速反应和泛化保持能力。

### 五、方法论与关键技术细节
因果力记忆通过因果编码器将近期力序列对齐到动作时间戳，确保每个动作使用最新的力测量；零初始化交叉注意力的输出投影初始化为零，使模型在训练开始时输出与预训练VLA等价；Shifted causal attention配合拷贝的权重实现初始化等价；训练时通过力掩码使无力样本不更新力编码器，且离线/在线数据按1:1采样平衡先验保持与纠正学习；代码与数据将开源。
