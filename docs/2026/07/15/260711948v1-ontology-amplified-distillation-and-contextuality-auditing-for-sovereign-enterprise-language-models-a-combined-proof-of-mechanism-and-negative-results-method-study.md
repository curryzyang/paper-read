# Ontology-Amplified Distillation and Contextuality Auditing for Sovereign Enterprise Language Models: A Combined Proof-of-Mechanism and Negative-Results Method Study

- 区域：精读区
- 排名：8
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Thanh Luong Tuan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11948v1) · [PDF](https://arxiv.org/pdf/2607.11948v1)

## TLDR
This paper combines a proof-of-mechanism study of ontology-amplified distillation—where a locally trained student model matches, but does not exceed, a frontier model's grounding on Vietnamese financial tasks (underpowered to establish equivalence)—with a negative-results contextuality audit showing zero residual contextuality, together providing a governance diagnostic for sovereign enterprise language models.

## Abstract
Regulated financial institutions operating under data-residency rules need tenant-owned language models that can run inside the institution's perimeter. This paper combines two related FAOS studies into one mechanism-and-control article. First, it reports a reduced-power proof-of-mechanism study of ontology-amplified distillation: a Qwen3.6-27B student is adapted to the Foundation AgenticOS ontology through supervised fine-tuning on frontier-teacher trajectories and ontology-grounded direct preference optimization (DPO), trained locally on a single Apple M5 Max from 47 synthetic, English-language, cross-domain preference pairs. On 40 held-out Vietnamese financial-domain tasks, the distilled student grounds 36 of 40 tasks (grounded rate 0.90; mean ontology term-coverage r_onto = 0.95 on a metric floored at 0.50), equal to the GPT-5 frontier baseline, which also grounds 36 of 40. The outcome is underpowered to establish equivalence: the paired-difference 95% confidence interval spans +/-4 tasks, and the run does not test or show the pre-registered amplification prediction that the student should exceed the frontier. Second, the paper consolidates a contextuality-audit method for enterprise-agent routing. In a separate negative-results pilot, the corrected canonical Contextuality-by-Default degree is zero for all Phase 1.3 groups in both the local-Qwen run and an explicitly labeled Gemma replication check; the useful signal is direct influence and construct coupling, not surviving residual contextuality. Together, the studies pair an ontology-grounded model-building mechanism with a governance diagnostic for deciding when apparent disagreement should trigger prompt standardization, multi-agent synthesis, or human review. The evidence supports neither deployability, safety, superiority, statistical equivalence, nor a contextuality-positive routing rule.


## 精读解读（中文）
### 一、研究动机
受数据驻留规则约束的金融机构需要能在内部运行的语言模型，但本地可部署的小模型通常参数覆盖不足。本研究旨在验证通过本体放大的蒸馏方法是否能使小模型达到前沿模型的接地质量，同时开发一种上下文审计诊断以支持企业代理路由的治理决策。

### 二、技术方案（Method）
采用两阶段蒸馏管线：首先对Qwen3.6-27B学生模型进行监督微调，使用注入本体切片的前沿教师（GPT-5）轨迹（451条）；然后进行本体接地直接偏好优化（DPO），使用47个合成的英文跨领域偏好对（医疗、保险、金融科技），将接地前沿答案标记为偏好，无本体基础答案标记为非偏好。训练在单个Apple M5 Max上本地完成，约32分钟，峰值内存58.1 GB。评估使用40个越南语金融领域保留任务（银行、保险、资本市场、房地产科技），每个任务由本体切片衍生术语，通过本体合规指标（接地率、平均术语覆盖r_onto，底线0.50）评分，不使用评判模型。并行的上下文审计方法基于Contextuality-by-Default框架，区分直接影响、构造耦合和残余上下文性，用于路由决策。

### 三、结果（Result）
在40个保留任务中，蒸馏学生接地36个（接地率0.90，平均r_onto=0.95），与GPT-5前沿基线相同（也接地36个）。但配对差异的95%置信区间跨越±4个任务，功效不足建立等价或证明预先注册的放大预测（学生超过前沿）。训练侧显示偏好准确率从0升至1.0，奖励边际从0升至0.307。上下文审计的否定结果中，所有Phase 1.3组的校正后规范Contextuality-by-Default度为零，有用信号为直接影响和构造耦合。

### 四、结论（Conclusion）
研究整合了本体接地模型构建机制与治理诊断，后者可决定何时表面分歧应触发提示标准化、多智能体合成或人工审查。当前证据不支持可部署性、安全性、优越性、统计等价性或上下文正环路规则；结果被视为降功率机制证明，而非部署声明。

### 五、方法论与关键技术细节
关键细节包括：数据合成自47个偏好对（英文，非目标领域），仅含约9%的计划专家标记；先验使用Foundation AgenticOS本体，切片固定800 token预算，优先保留法规部分；DPO损失为sigmoid DPO，超参为rank-8适配器、学习率1e-6、batch size 1、512 token上限、42次迭代（约一个epoch），更新0.014%参数；本体合规指标为降级代理（仅记录术语存在，非质量），底线0.50，未测试完整四分量复合指标；局限性包括：未测试预先注册的放大预测（学生应超过前沿），未处理成本、弃权安全、模型规模、跨语言对比等，且评估功效不足。
