# Think Shallow, Solve Deep: Controlling Recurrent Dynamics for Reliable Test-Time Depth

- 区域：精读区
- 排名：8
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Ivan Viakhirev, Kirill Borodin, Amirah Almutairi, Serguei Barannikov, Maxim Abramov, Grach Mkrtchian
- 机构：lab260, CNRS, BitmanagerAI, KAU, ITMO, MTUCI, FRC RAS
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18222v1) · [PDF](https://arxiv.org/pdf/2608.18222v1)

## TLDR
A recurrent reasoner's test-time depth behavior is governed by its finite-time dynamical regime—settling, marginal, or drifting—where settling operators are depth-safe and can convert added iterations into accuracy on harder instances, and a single terminal fixed-point training objective causally controls this regime.

## Abstract
Recurrent-depth reasoners aim to solve harder problems by iterating their update longer at test time, but additional iterations can improve, preserve, or degrade an answer. We show that a measurable property of the trained operator, its finite-time dynamical regime (estimated as settling, marginal, or drifting), indicates which of these occurs. We give a sufficient condition for depth-safety: once an operator's per-step displacement is small relative to the decoder margin, the decoded answer cannot change under further iterations. Empirically, on algorithmic tasks trained from $800$ unaugmented examples per difficulty tier, settling operators do not degrade with added depth, and on some tasks convert it into higher accuracy on harder unseen instances (Sudoku, $0.19$ to $0.34$ past the training horizon). A single terminal fixed-point objective moves the regime and the depth behavior together: removing it induces drift and removes the gains, and adding it to a generic recurrence yields depth-safe extrapolation on carry propagation. We give four operational criteria for useful test-time depth, use them to catalogue failure modes, and, as a consistency check, apply the same measurements to Huginn-3.5B, which falls in the non-settling family.


## 精读解读（中文）
### 一、研究动机
循环深度推理器通过在测试时迭代更多步来求解更难的问题，但额外迭代可能提升、保持或降低答案质量。现有方法通常依赖大规模数据增强或增大参数量来补偿，而忽略了对训练后算子有限时间动力学特性的测量与控制。本文旨在建立可测量的动力学机制（settling/marginal/drifting）与测试时深度行为之间的联系，并提供可控的训练目标使推理器在更深的测试时迭代中安全且有效地泛化到未见难度实例。

### 二、技术方案（Method）
本文提出受控循环配方（CoRe），在固定无增强数据（每难度800个样本）下训练权重共享的迭代映射 z_{t+1}=f(z_t,x)，共16步循环并采用深度监督（4次监督展开）。输入在每一步前重新注入（input recall），状态更新沿任务相关的约束图（如数独的行/列/块）做结构化消息传递；关键训练项为终端不动点目标：惩罚最终更新位移 ||z_T-z_{T-1}||=a_T||f(z_{T-1},x)-z_{T-1}||，即固定点残差乘学习到的更新门。训练使用AdamW、梯度裁剪0.5、batch 64、4–8k步、d=256；推理时扫描测试深度h_c∈{3,16,32,64,128}。对每个训练好的算子测量五类信号：谱（Jacobian σ_max、ρ、Henrici非正规性）、动力学（有限时间Lyapunov谱、Kaplan-Yorke维、固定点残差、settle ratio）、信息流（logit-lens秩）、拓扑（持续同调Betti条）和训练时间指标；按λ_max标记regime：settle(λ_max<-0.05)、marginal(|λ_max|≤0.05)、drift(λ_max>0.05)。在固定输入尺寸难度阶梯（数独9×9孔率0.2→0.7、16节点可达性BFS深度2→12、2×32位加法最长进位2→28）上，用训练时未见难度tier评估，并对比七种重实现架构（TRM、UT/URM、FPRM、EqR、DEQ、Neural GPU、SE-RRM）及Huginn-3.5B（仅测量）。

### 三、结果（Result）
settling算子不会随深度增加而退化，且在部分任务上将测试时深度转化为更高准确率：数独未见难度tier上准确率从0.19提升至0.34（训练深度→最佳测试深度）；可达性任务保持未训练平台0.92。去除终端不动点目标后，架构与数据不变且σ_max≈5.6不变，但regime从settle翻转为drift（λ_max从-0.06变为+0.10，Kaplan-Yorke维从0变为8），数独未见困难实例准确率从0.34跌至0.03。将该目标加入通用循环（carry propagation）后，原本深度增加会退化的模型变为深度安全外推。Huginn-3.5B经测量属于非settling家族；基于同样分类的无标签目标修复其数字复制深度安全性（0.00→1.00），但不安装转化能力。四类操作化准则（R1外推、R2难度自适应稳定并转化、R3增量计算、R4收敛答案）可对失败模式分类，所有失败均可归入四类可测量模式。

### 四、结论（Conclusion）
训练后算子的有限时间动力学机制（settling/marginal/drifting）是测试时深度是否有用且安全的可靠预测指标。一个终端不动点目标可以同时改变动力学机制和深度行为：移除它导致drift并消除收益，添加它使通用循环获得深度安全外推。因此，要让循环深度推理器可靠地利用测试时深度，必须直接控制其不动点动力学，而仅控制谱半径或增大模型规模是不够的。

### 五、方法论与关键技术细节
关键数据：固定无增强训练数据，每难度tier 800个唯一样本，评估每tier 256个固定测试样本，三颗种子；数独验证使用有效性oracle而非参考匹配（未见困难tier上valid/reference差距5.5倍：0.34 vs 0.062），因为多解问题；数独唯一可解分数随tier下降：1.00/0.91/0.50/0.06/0.00。关键先验/设计：输入重注入是必要条件（移除后σ_max=1.0000且EM=0.00，退化为输入不敏感identity）；结构化消息传递决定循环计算内容，但无结构时模型能收缩却不正确（settle必要不充分）；固定点残差项不能通过关闭门平凡满足（附录验证）。超参：AdamW、梯度裁剪0.5、batch 64、d=256、4–8k步、16个训练循环步、深度监督4个展开；测试深度集合{3,16,32,64,128}。复杂度/约束：固定输入尺寸阶梯才可用于外推声明，尺寸/长度类泛化被排除；adaptive stabilization为事后诊断而非在线停时规则；Huginn-3.5B仅测量不可训练干预。局限性：settling不一定保证学到算法（可能只是覆盖），需R1-R4合取排除；低学习率并非必要（高LR消融反而0.42优于0.34），报告LR为匹配规模；不同架构在哪类任务上settle取决于任务（carry上TRM式注意力循环优于CoRe）。
