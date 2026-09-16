# Diagnosing Faults in Reinforcement Learning Simulators and World Models with Canonical Polynomial Invariants

- 区域：精读区
- 排名：8
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Tesfay Zemuy Gebrekidan, Hadush Hailu Gebrerufael
- 机构：MIU, Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13194v1) · [PDF](https://arxiv.org/pdf/2609.13194v1)

## TLDR
TLDR: Exact canonical polynomial invariants recovered as reduced Gröbner bases offer little predictive benefit for RL dynamics but enable a powerful diagnostic that screens for violated physical constraints and attributes faults to the responsible parameters, reliably localizing simulator and world-model errors.

## Abstract
A large literature builds physical structure into learned dynamics on the premise that models respecting the underlying physics predict better. We test that premise using exact polynomial invariants recovered from trajectories and canonicalised as reduced Gröbner bases over $\mathbb{Q}$. On Acrobot, exactness provides little benefit for prediction: a consistency regulariser reduces algebraic residual while leaving rollout fidelity essentially unchanged, and a shaping potential recovered from a system with a 100% mass error accelerates learning as effectively as the correct potential. Exact canonical invariants instead prove valuable for diagnosis. We develop two procedures: screening, which identifies the violated physical constraint, and attribution, which recovers the faulty invariant and identifies the responsible physical parameter. To enable this, we introduce normal-form deflation and quotient-space recovery. Across fifteen injected faults, screening localises every broken constraint with no false alarms, whereas observation-space baselines do not localise any; attribution recovers the responsible parameter on all seven parameter faults. Paired difference tests detect all faults, showing that the advantage is localisation rather than detection. Perturbing reference generators by $10^{-4}$ preserves 14--15/15 localisations, showing that screening does not require exactness, whereas ideal-equality decisions distinguish perturbations of only $10^{-12}$, showing that exactness is required for algebraic comparison. Applied to 350 release pairs across eleven RL environments, the diagnostic finds no evidence of changed simulator dynamics, instead revealing properties of the benchmark implementations themselves.


## 精读解读（中文）
### 一、研究动机
大量工作将物理结构（守恒律、哈密顿/拉格朗日架构、运动学约束）注入学习动力学，前提是尊重物理的模型预测更好，但这一前提很少用最强形式的结构——精确且规范的物理不变量——来检验，因为现有方法用的是学习到的或数值近似的不变量。同时，RL 依赖模拟器而模拟器是软件，会存在错写常数、漏项、积分器替换、观测向量顺序错误等问题，而现有检测工具（验证误差、rollout 偏差曲线、两样本检验）只返回标量，无法指出“哪里错了”。作者因此主张：精确规范的不变量对预测价值有限，但对故障诊断价值很大，因为只有规范形才能提供可判定的相等性。

### 二、技术方案（Method）
方法从轨迹中恢复精确多项式不变量并规范化为 Q 上约化 Gröbner 基。对消没约束使用消失理想 I(M)，对守恒量则因守恒量构成子代数（E 守恒则 E² 也守恒）改用差分字典 Δ_d={m(s')−m(s)}，其零空间向量对所有能量层同时守恒，并用 Jacobian 秩提取极大函数独立子集去冗余。为可扩展性引入两个组件：法形式亏缩（normal-form deflation）用已知生成元约化 Gröbner 基的 NF 一步精确删除全部代数冗余倍数（如 ⟨g⟩∩P_d 整块空间），以及商空间恢复：在精确有理算术下先算出 NF 映射像空间的正交基 Π，再对差分设计矩阵做 ΦΠ^T 并取最小奇异值方向，从而完全不做基于容差的零空间维数估计，仅保留无量纲谱间隙阈值 σ_min/σ_next=0.1。诊断分两级：筛选对每个生成元计算按数据尺度 RMS(‖x‖^deg p) 归一化的残差（消没约束用 RMS，守恒量用沿轨迹 std），把两系统轨迹切成 32 个连续块，对每个生成元做单侧 Mann–Whitney U 检验并做 Bonferroni 校正以定位被破坏的约束；归因则把恢复出的不变量方向按规范自由度（尺度 α 与可加常数 β）拟合参数模板 p(x;θ)，每次只放开一个物理参数、其余固定在规格值，给出参数故障、与规格一致、无法用参数故障解释三种判决。

### 三、结果（Result）
在 Acrobot 上，精确性对预测几乎没有收益：一致性正则项降低了代数残差但 rollout 保真度基本不变，而从一个质量误差达 100% 的系统恢复出的塑造势与正确势在加速学习上效果相当。相反，精确规范不变量在诊断上表现突出：15 个注入故障中筛选定位出每一个被破坏的约束且无误报，而观测空间基线一个都定位不出；归因在全部 7 个参数故障上都找回了责任参数；成对差分检验能检测所有故障，说明优势在于定位而非检测。将参考生成元扰动 1e-4 仍保留 14–15/15 的定位，表明筛选并不需要精确性；而理想相等性判定能区分仅 1e-12 的扰动，说明代数比较必须依赖精确性。将诊断应用于 11 个 RL 环境的 350 个 release 对，未发现模拟器动力学发生改变的证据，反而揭示了基准实现本身的性质（积分器敏感性、Reacher 的观测不一致性、混沌动力学对长时程 release 比较的限制）。

### 四、结论（Conclusion）
该工作表明，把物理结构以最强形式（精确、规范的 Gröbner 基不变量）引入，对预测能力的提升十分有限，其真正价值在于诊断：规范形带来的可判定相等性使两个不变量理想是否相同、某约束是否成立都能被精确判定。基于此构建的筛选加归因诊断能够定位被违反的物理约束并找出负责的物理参数，在注入故障上全面优于观测空间基线，并且筛选对生成元扰动鲁棒、精确性仅在代数相等性判定时必需。由于理论结果是带必要性/充分性缺口的可靠性保证，该诊断应仅作为必要条件来解读，其价值在于指出“哪里错了”而非取代系统辨识或完整验证。

### 五、方法论与关键技术细节
关键实现细节包括：必须区分消失理想（可规范化）与守恒量子代数（不可规范化，需差分字典与 Jacobian 秩去冗余，且极大独立子集不唯一，仅证明非冗余而非规范）；法形式亏缩是归因的前置条件而非效率优化，缺少该投影时最小变化方向会完全落在琐碎子空间内（实测占比 1.0000），14 维退化导致无法确定方向，加上投影后与真能量对齐度达 1.0000；谱间隙阈值固定为 0.1，对字典列缩放与样本量不变，列归一化会迫使 Π 重新正交化；故意不做 snap-rounding，因为有理先验等同于假设系统正确，会把故障系数抹平；筛选残差必须按生成元次数归一化，否则高阶生成元在大量级速度上会被误判，检验使用 32 个连续块（因守恒漂移定义在轨迹片段上），但同轨迹切块并非独立重复，水平膨胀在局限性一节量化，同时报告以整条轨迹加精确置换零假设的版本；归因的规范自由度不可省，因为 Acrobot 能量每个系数都含 m₂，没有无参数单项式可用于归一化；模板单项式多于参数，错误假设表现为大残差；理论保证（命题 1、2）只给出必要性方向的可靠性，且在群体层面残差仅通过生成元作用于状态，重播种无法改变。限制包括：规范形不保证最小性、不保证物理正确性，也不构成完整诊断流程。
