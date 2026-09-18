# RAF-VLA: Representation Alignment with the Future for End-to-End Autonomous Driving

- 区域：精读区
- 排名：6
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Dogun Kim, Yongjae Lee, Joonhee Lim, Yeina Lee, Junhyeok Park, Moogeun Park, Dongsuk Kum
- 机构：Korea Advanced Institute of Science & Technology (KAIST)
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17728v1) · [PDF](https://arxiv.org/pdf/2609.17728v1)

## TLDR
RAF-VLA aligns a driving policy’s hidden states with future-frame representations during supervised fine-tuning, avoiding explicit future generation and achieving competitive end-to-end planning performance on NAVSIM with far fewer training samples and minimal training/inference overhead.

## Abstract
Recent Vision-Language-Action (VLA) models for autonomous driving have incorporated world modeling by predicting future driving scenes alongside driving actions, demonstrating strong planning performance. Future driving scenes are utilized as dense supervision, encouraging the policy to learn rich internal representations useful for planning. However, these World-Modeling VLAs rely on explicit future generation to learn such representations, thereby introducing two key limitations: additional training burden and inference latency. To address these limitations, we propose RAF-VLA (Representation Alignment with the Future), a VLA-based autonomous driving framework that shapes planning-relevant internal representations through direct guidance from future-frame representations. RAF-VLA employs Future-Aligned Supervised Fine-Tuning, in which a straightforward regularization aligns the policy's hidden states with future-frame representations obtained from a pretrained world encoder while learning driving actions. This simple alignment allows RAF-VLA to avoid the training burden and inference latency associated with future generation. Extensive experiments on the NAVSIM benchmark show that RAF-VLA achieves competitive planning performance against state-of-the-art VLA planners with substantially fewer training samples seen. Moreover, RAF-VLA incurs only 3.8% training overhead and a negligible 1 ms inference overhead.


## 精读解读（中文）
### 一、研究动机
现有 World-Modeling VLA 通过显式预测未来驾驶场景来获得密集监督，从而学习规划相关内部表示，但这类方法需要优化额外生成目标，并带来额外训练负担与推理延迟。因此，作者希望在不生成未来场景的前提下，仍利用未来场景监督来塑造驾驶策略的内部表示。

### 二、技术方案（Method）
RAF-VLA 采用 Mixture-of-Transformers 架构，包含基于预训练 VLM 的 Vision-Language Expert 和轻量 Action Expert，两者通过层间联合注意力交互；输入为前视图像序列、导航指令和驾驶状态，输出未来 H 步 ego 轨迹航点。训练分两阶段：先进行 Future-Aligned SFT，在 Vision-Language Expert 中附加可学习 world queries，并用冻结的预训练 world encoder 从未来帧提取目标表示，再用可训练 MLP projector 将 world-query 隐状态投影到目标空间，以 MSE 对齐损失与动作预测损失联合优化；随后移除 world encoder 和 projector，保留 world queries，并进行 GRPO-based RFT，用 NAVSIM PDMS 规划奖励优化策略。

### 三、结果（Result）
在 NAVSIM 基准上，RAF-VLA 以显著更少的训练样本 seen 达到与最先进 VLA 规划器相当的规划性能；Future-Aligned SFT 仅带来 3.8% 训练开销，推理开销可忽略（约 1 ms）。消融和定性结果进一步支持该表示对齐方法的有效性。

### 四、结论（Conclusion）
RAF-VLA 表明，未来场景监督可仅在表示层面使用，无需显式未来生成即可塑造规划相关内部表示，从而避免世界模型 VLA 的训练负担和推理延迟，并为高效端到端自动驾驶提供可行路径。

### 五、方法论与关键技术细节
关键实现包括：world queries 作为未来对齐的表示槽，每个选定未来步分配 K 个，采用块因果注意力，同 horizon 内双向、后续 horizon 被 mask，且可关注图像和语言 token；Action Expert 对 VL Expert 为单向可见，AE 内部全双向；对齐损失为冻结 world encoder 特征与投影隐状态之间的均方误差，L_SFT=L_act+λ_align L_align。RFT 阶段使用 GRPO，从旧策略采样 G 条候选轨迹，按组内奖励归一化计算优势，使用 clip 和 KL 惩罚，奖励为 PDMS，评估采用 NAVSIM v1 闭环指标，部分对比设置使用 best-of-N（N=6）策略；局限性在于对齐目标依赖预训练 world encoder 的质量，具体超参和完整数值结果需参考原文。
