# Slow-Fast Multi-Teacher On-Policy Distillation for Capability Preservation

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Xiaofei Yin, Tong Chu, Jiyuan Fu, Jun Lan, Shuheng Zhou, Huijia Zhu
- 机构：Fudan University, Ant Group
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02324v1) · [PDF](https://arxiv.org/pdf/2610.02324v1)

## TLDR
SF-MOPD couples a fast student model with a slow EMA reference and projects each teacher-induced update to remove only components that increase slow-fast displacement, thereby preserving general multimodal capabilities while effectively acquiring domain-specific expertise in multi-teacher on-policy distillation.

## Abstract
Foundation multimodal large language models are designed to support a broad spectrum of capabilities across diverse domains. Multi-teacher on-policy distillation (MOPD) provides an effective framework for consolidating domain-specific expertise into a single student model. However, MOPD training gradually drives the student away from its initialization model, and general capabilities decline as the displacement grows, resulting in capability interference. A direct remedy is constraining the student toward its initialization, but this suppresses the acquisition of domain expertise as well. We propose Slow-Fast Multi-Teacher On-Policy Distillation (SF-MOPD), which couples a fast model, the current student updated directly by each teacher, with a slow model, an exponential moving average of the student. The slow model absorbs the learning signal gradually, serving as a moving capability reference that fuses the general foundation with confirmed domain expertise. For each teacher, SF-MOPD computes the teacher-induced update in log-probability space and removes only the component that pushes the fast model further away from the slow model, while retaining aligned and orthogonal components. Experiments across multiple model scales demonstrate that SF-MOPD effectively mitigates capability interference, enhances specialized multimodal capabilities, and reduces the average degradation on general-capability benchmarks, consistently outperforming vanilla MOPD.


## 精读解读（中文）
### 一、研究动机
多教师在线蒸馏（MOPD）可将多个领域专家的互补能力整合到单一学生模型中，但训练会逐渐使学生偏离其初始化模型，且随位移增大通用能力下降，形成能力干扰；直接用KL约束将学生锚定到初始模型虽可缓解漂移，却会同时抑制领域专长的获取，因此需要一种能区分专家能力吸收与通用能力侵蚀的参考机制。

### 二、技术方案（Method）
SF-MOPD维护快模型与慢模型：快模型是当前学生，直接由各教师在其on-policy样本上更新；慢模型是学生参数的指数移动平均，从同一初始化开始并逐步吸收学习信号，作为移动的能力参考。对每个on-policy样本，学生采样响应并与指令拼接后送入学生与教师；在log概率空间计算教师诱导更新方向与慢-快约束方向（慢模型与快模型log概率差，经CenterNorm归一化），用余弦相似度判断教师更新是否扩大慢快位移，并通过投影只移除与慢-快方向相反的分量，保留对齐与正交分量；随后用修改后的目标分布做JSD蒸馏，并保留原始MOPD损失作为正则项，整体目标为L_sf加β倍L_MOPD，数值稳定时可对更新方向做最大范数与逐元素裁剪并重新中心化。该过程仅需参数平滑，无需教师特定梯度存储或额外可训练参数。

### 三、结果（Result）
在2B、4B、8B三个Qwen3-VL学生规模、11个基准上的实验表明，SF-MOPD持续优于vanilla MOPD和instruct基线，在2B、4B、8B规模均取得最佳领域特定平均，并改善通用领域与领域特定的权衡；2B规模领域特定平均从38.4开始提升，8B规模完整模型总体平均为67.7，而移除Slow-Fast Projection后退化为经典Mean-Teacher式EMA约束并导致总体平均下降。通用能力保留方面，SF-MOPD降低了MMMU-Pro、MMBench-CN、MMBench-EN、MMStar、HallusionBench等基准上的平均退化；消融还显示慢模型作为EMA参考与每教师投影均有效，β在0.1至1.0范围内的敏感性实验给出了不同总体平均。

### 四、结论（Conclusion）
SF-MOPD通过慢-快能力参考与每教师投影机制缓解了多教师在线蒸馏中的能力干扰，在吸收领域专家能力的同时更好保留通用多模态能力，跨多个模型规模一致超越原MOPD，为多教师蒸馏中能力获取与保持的平衡提供了有效方案。

### 五、方法论与关键技术细节
数据使用DeepVision-103K按能力划分出的DataChart、RealWorld Item、Schematic Diagram，并加入Vision-OPD-6K细粒度视觉感知集；教师为Qwen3-VL-8B专家模型（前三个领域用GSPO训练），学生规模为8B、4B、2B。优化使用AdamW，学习率1×10^-5，batch size 64，训练1个epoch，教师权重相等；EMA平滑系数α=0.999，2B与4B模型β=1.0、8B模型β=0.1，投影中ridge项λ=10^-3，并可对投影后更新做最大范数和逐元素裁剪以保证数值稳定。评估用规则匹配抽取答案，失败时用Qwen3-VL-8B-Instruct做LLM-as-judge；领域基准包括MathVerse、VSTAR、ZoomBench，通用基准包括MMMU-Pro、MMBench-CN、MMBench-EN、MMStar、HallusionBench。局限性包括：固定初始化锚无法区分专长获取与通用能力侵蚀，方法依赖维护慢模型EMA且投影仅在慢-快位移方向起作用；此外，增加细粒度教师训练数据采样长度以降低任务异质性时，细粒度性能严重退化，ZoomBench降至40.7。
