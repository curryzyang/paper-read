# AutoHebb: Self-Modifying Neural Networks that Zero-Shot Infer and Continually Learn

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Daniel Levine, David van Dijk, Kenneth Kay
- 机构：UCSF, Yale University, University of Rochester, Howard Hughes Medical Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40757v1) · [PDF](https://arxiv.org/pdf/2610.40757v1)

## TLDR
AutoHebb is a class of self-modifying feedforward neural networks that use meta-learned fixed weights and a neuromodulated three-factor Hebbian plasticity rule to achieve strong zero-shot inference and continual learning, outperforming modern models and revealing emergent learning abilities.

## Abstract
Humans and animals have a unique capacity to generalize and learn in novel circumstances, including "0-shot" inference (ZI) and continual learning (CL) -- two powerful cognitive abilities. Despite this importance, efforts to model ZI and CL are seriously limited in several ways. First, existing models typically lack components critical to ZI and CL in the brain, namely, strong inductive biases (for ZI) and autonomous control of learning (for CL). Second, models can be less tractable to analysis if model components are overly complex (lacking simplicity), or too task-restricted if model components are overly bespoke (lacking expressivity). Here we introduce autonomous Hebbian networks ("AutoHebb"), a class of online learning feedforward neural networks that realize strong inductive biases and autonomously controlled learning, and are both simple and expressive. Unlike standard models that learn via externally controlled optimization (e.g. gradient descent), AutoHebb networks combine external feedback with internally generated activity to produce a global learning signal ('neuromodulator') fed back to the network. The neuromodulator in turn gates a biologically grounded local learning rule (3-factor Hebbian rule) that updates networks' plastic weights. Using meta-learning to search for fixed (non-plastic) weights, we find that AutoHebb networks (1) succeed on ZI tasks, (2) show emergent (untrained) ZI/CL abilities, (3) admit reverse-engineering into explicit algorithms, and (4) outperform modern learning models on ZI/CL tasks. Lastly, performance comparisons to related models implied an essential role for three model components: meta-learning, Hebbian plasticity, and autonomous control of learning. These findings indicate that AutoHebb may be useful in hypothesis generation, analysis, and discovery of biologically grounded forms of learning and generalization.


## 精读解读（中文）
### 一、研究动机
现有模型在零样本推理（ZI）和持续学习（CL）上常缺少大脑式关键要素：ZI所需的强归纳偏置，以及CL所需的自主学习控制；同时模型若过于复杂就难分析，若过于专用又缺乏表达力。作者据此提出AutoHebb，试图用自生成学习信号门控局部可塑性，在简单前馈网络中同时实现强先验和在线持续学习。

### 二、技术方案（Method）
AutoHebb由主网络和控制网络组成，权重分为固定与可塑两类；主网络按 h_i=g((W_i+A_i⊙P_i(t))h_{i-1}+b_i) 前向计算并用固定线性读出加sigmoid产生二值响应，控制网络接收最后隐藏层h_L与外部反馈φ（正确为1、错误为0）并输出标量神经调质m。每个trial依次执行输入、输出、控制和更新：m门控三因子Hebbian局部规则 P_i(t+1)=λP_i(t)+ηm h_i h_{i-1}^T，仅用突触前后活动与全局m更新可塑权重。固定权重、塑性参数A、学习率η和衰减λ通过元学习外环优化，内环在episode内进行Hebbian在线更新且每个episode开始时P置0，外环用梯度下降和交叉熵基于episode表现更新固定参数。

### 三、结果（Result）
在四个具有简单零样本推理结构的ZI/CL任务上，AutoHebb成功完成ZI，并表现出未训练的涌现ZI/CL能力，包括快速知识组装和长度泛化；网络还可被反工程为显式学习-推理算法。对比结果显示其优于现代学习模型，包括需要学习多个零样本任务的情形；与缺少特定组件的相关模型比较表明，元学习、Hebbian可塑性和自主神经调质控制三者对性能均必不可少。

### 四、结论（Conclusion）
AutoHebb把强归纳偏置与自主学习控制结合在简单且可表达的前馈架构中，既能处理ZI/CL任务，又便于反工程和理论分析。它可作为研究生物基础学习与泛化的假设生成、分析和发现框架，并可能用于神经科学、心理学及应用场景。

### 五、方法论与关键技术细节
关键实现包括：任务为{0,1}二值响应，反馈φ仅指示对错；固定参数经元学习承载先验结构，可塑权重每episode初始化为0，三因子Hebbian更新含固定学习率η与衰减λ≤1；控制网络使用固定权重但可扩展为可塑。架构刻意限制为前馈、将神经调质生成隔离到控制子网并局部化可塑权重，以提升可分析性和任务适用范围；外环采用梯度下降交叉熵但也可换其他优化器。局限在于当前主要验证四个简单零样本结构任务，生物学习信号的具体身份与作用仍开放，且控制网络固定等设计约束了更广泛结论。
