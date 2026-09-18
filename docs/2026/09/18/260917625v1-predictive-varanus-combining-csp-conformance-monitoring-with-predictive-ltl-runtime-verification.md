# Predictive Varanus: Combining CSP Conformance Monitoring with Predictive LTL Runtime Verification

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Angelo Ferrando, Matt Luckcuck, Pedro Ribeiro
- 机构：University of Nottingham, University of Modena and Reggio Emilia, University of York
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17625v1) · [PDF](https://arxiv.org/pdf/2609.17625v1)

## TLDR
Predictive Varanus is a two-stage runtime verification pipeline that combines CSP-based conformance monitoring with predictive LTL monitoring by reusing the same CSP model as both a conformance gate and a Büchi automaton, enabling earlier verdicts on model-consistent traces, as demonstrated on a nuclear-inspection rover case study.

## Abstract
Runtime Verification is well suited to autonomous and robotic systems because it checks the behaviour that is actually observed during execution. Its main limitation, however, is that it is usually reactive: the monitor detects a violation only after the system has already performed a bad event. This can be too late in domains where failures are costly or unsafe. In this paper we present PREDICTIVE VARANUS, a two-stage verification pipeline that combines VARANUS, a runtime verifier that uses models written in the process algebra Communicating Sequential Processes (CSP), with predictive runtime verification for LTL. A CSP model is first used as a conformance gate over the observed event trace; the same model is then translated into a Buchi automaton that constrains the futures explored by a predictive LTL monitor. In this way, out-of-model behaviour is rejected immediately, while model-consistent prefixes can be classified as already guaranteeing satisfaction, already forcing violation, or still being inconclusive for the monitored temporal property. We formalise the combined monitor, explain its implementation, and illustrate the approach on a robotic rover for nuclear-store inspection. The case study shows how the combination of CSP validation and predictive LTL can provide earlier verdicts than standard runtime monitoring while reusing an existing design-time CSP model.


## 精读解读（中文）
### 一、研究动机
运行时验证适合自主与机器人系统，因为它检查的是执行中实际观测到的行为，但其核心局限在于通常是被动反应式的：只有系统已经执行了坏事件之后监视器才能报出违规，这在失败代价高或不安全的领域中往往为时已晚。预测性运行时验证（PRV）可以提前给出结论，但需要系统模型；而许多机器人规范早已在设计阶段以CSP形式编写并通过FDR或RoboChart分析过，因此复用这些既有模型进行预测性监控具有很高的实用价值。

### 二、技术方案（Method）
提出两阶段流水线 PREDICTIVE VARANUS：第一阶段用 VARANUS 把确定性有限状态的 CSP 进程 P 作为一致性闸门，借助 FDR 完成 CSP 解析与状态空间生成并显式物化可达 LTS（S,s0,ΣP,→），逐事件判定观测轨迹 σ 是否满足 σ∈Lang(P)，不合规则立即拒绝并终止后续推理。第二阶段把同一 CSP 模型翻译为面向命题的 Büchi 自动机 B_P=(S,s0,2^AP,δ,F_P)，其中 AP={proj(a) | a∈ΣP}∪{skip}，每条迁移 s→a s' 对应标签 λ(a)={proj(a)} 的一热编码，终止状态加 skip 自环以补全无限 stuttering 后缀且令 F_P=S，并以 HOA 格式导出。预测监视器对 LTL 性质 φ 构造同步乘积 A+=B_P×B_φ 与 A−=B_P×B_¬φ，读入投影轨迹后取可达状态集 S+σ 与 S−σ：若 Lang(A−,S−σ)=∅ 判为 ⊤（必然满足），若 Lang(A+,S+σ)=∅ 判为 ⊥（必然违反），否则判为 ?（不确定）。

### 三、结果（Result）
通过核仓库巡检机器人 rover 的案例研究表明，CSP 一致性校验与预测性 LTL 的组合能够比标准运行时监控更早给出判定，同时完全复用已有的设计期 CSP 模型；流水线可区分两类情形——不符合 CSP 模型的行为被立即拒绝，而符合模型的前缀可被分类为已保证满足、已必然违反或仍不确定。

### 四、结论（Conclusion）
论文将标准预测性运行时验证的自动机语言空性判定规则与基于 CSP 的行为模型集成，形式化了组合监视器的判定函数与模型翻译，使监视器既能在观测到不合规事件时立即拒绝，又能在合规前缀上对时序性质给出三值预测判定；该流水线是模块化的，预测层实现为 LTL 检查但可替换为其他预测推理方式。

### 五、方法论与关键技术细节
关键点包括：假设 CSP oracle 是确定性有限状态进程，其迹语义前缀封闭（σ∈Lang(P) 表示当前迹仍与规范兼容）；VARANUS 支持 strict 与 permissive（忽略字母表外事件）两种模式；预测判定采用三值逻辑，是合并了 possibly-true/possibly-false 的粗化语义；投影 proj 把参数化事件 move.i 映射为不同原子命题 m_i，保留事件区分度但丢失其结构化表示；终止状态以 skip 自环补全，使有限最大执行诱导无限字以适配标准 LTL 语义；判定复杂度来自两个乘积自动机的语言空性检查；主要局限性是判定以模型为条件，只预测模型一致的结果（如任务中止、覆盖失败、保证完成），无法预测模型之外的任意故障。
