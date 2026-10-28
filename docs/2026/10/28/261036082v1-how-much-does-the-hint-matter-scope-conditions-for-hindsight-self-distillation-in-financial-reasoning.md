# How Much Does the Hint Matter? Scope Conditions for Hindsight Self-Distillation in Financial Reasoning

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Johnny Yu, Cyril Gorlla
- 机构：CTGT, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36082v1) · [PDF](https://arxiv.org/pdf/2610.36082v1)

## TLDR
Fin-SD is a hindsight self-distillation method that localizes a student model’s first reasoning error and distills a hint-conditioned frozen copy of itself over a short truncated rollout, showing that most gains come from where supervision is applied rather than hint content, that no stronger hint-writing model is needed, and that it matches full-reference on-policy self-distillation with fewer tokens and no material compliance or general-reasoning regression.

## Abstract
Financial institutions operating under data-residency constraints are restricted to open-weight models small enough to locally host, which trail frontier systems on multi-step quantitative reasoning. On-policy distillation narrows such gaps by supervising a student on its own rollouts, but traditional OPD requires a strong external teacher, and on-policy self-distillation (OPSD) conditions on a full reference solution. We ask how much of that signal is necessary. We present Fin-SD, a localized hindsight self-distillation recipe for multi-step reasoning. Given a problem the student fails, the student itself identifies the first incorrect reasoning step and writes a short critique of that step. We truncate the student's trajectory immediately before the error (aiming to obtain a correct prefix), condition a frozen copy of the student on the same prefix plus the hint, and distill that hint-conditioned teacher into the student over a short rollout under reverse KL. No external model contributes a gradient. We apply Fin-SD to GPT-OSS-20B on a custom multi-step financial reasoning benchmark that requires deriving formula inputs from realistic scenarios via accounting conventions. We find: (i) replacing the critique with a generic-feedback control matches Fin-SD's entire 3.03 pp accuracy gain over the base model on the FinanceReasoning Hard subset, suggesting the gain comes from where supervision is applied, not hint content; (ii) the model writing the hint does not need to be stronger than the model receiving it: hints from same-family GPT-OSS-120B, at roughly 6x the parameters, yield no materially greater benefits than self-written hints; and (iii) Fin-SD matches on-policy self-distillation from full reference solutions on accuracy while generating 9.5% fewer tokens. With Fin-SD, general reasoning on MMLU-Pro and a fourteen-metric compliance audit on FinTrust show no material regression.


## 精读解读（中文）
### 一、研究动机
金融机构受数据驻留约束，只能本地部署小型开放权重模型，而这些模型在多步定量金融推理上落后于前沿系统；传统on-policy蒸馏依赖强外部教师，on-policy自蒸馏又依赖完整参考解。本文因此追问：在失败轨迹上做事后自蒸馏时，究竟需要多少提示信号，以及该方案能否在提升能力的同时保持合规与成本可接受。

### 二、技术方案（Method）
Fin-SD先让GPT-OSS-20B在自建多步金融推理题上采样，判错后用同一学生权重的冻结提示模型读取问题、失败轨迹和标准答案，定位首个错误片段并生成简短批评及错误类型；算术或舍入失误不产生梯度。随后在错误前截断得到学生自身前缀，让冻结的教师副本在同一前缀上额外接收提示，学生在100 token的短rollout上按逐token反向KL对齐教师分布，仅rollout位置计入损失；每个epoch重新挖掘失败集并重冻教师，用梯度累积和AdamW更新，全程无外部模型提供梯度。

### 三、结果（Result）
在FinanceReasoning Hard子集上，Fin-SD相对基座提升3.03个百分点；把批评替换为通用反馈的对照取得3.36个百分点，与Fin-SD的增益相当，说明增益主要来自监督施加的位置而非提示内容。由参数量约6倍的GPT-OSS-120B写提示并未显著优于学生自写提示；Fin-SD在准确率上匹配基于完整参考解的OPSD，同时评测生成token少9.5%，并在预算内完成率上方向性高2.44个百分点。MMLU-Pro通用推理和FinTrust十四项合规审计未见实质回退。

### 四、结论（Conclusion）
结果表明，在受数据驻留约束的金融推理场景中，局部化的事后自蒸馏可在不引入更强外部教师的情况下缩小能力差距；关键不是完整参考解或具体提示内容，而是准确找到首个推理错误并在学生自身前缀上施加密集监督。Fin-SD提供了一个兼顾准确率、token效率与合规风险的可落地后训练方案，但其结论仍受单一模型、自建基准和有限合规审计的约束。

### 五、方法论与关键技术细节
关键实现包括：以FinanceReasoning函数库的3,133个函数构造需按会计惯例推导公式输入的语料，并在238题Hard子集评估；错误定位通过让模型复述错误片段而非精确token位置来截断；L=100、反向KL、前缀掩码、教师按上一epoch学生权重重冻、失败集每epoch重挖；算术失误只不计梯度但仍计为错误，错误类型分类器非正式审计约96%准确；还做了通用反馈、120B提示模型及KL方向的消融，并用MMLU-Pro和FinTrust检查副作用。
