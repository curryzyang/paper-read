# OmniHarness: Harnessing Generalizable Visual Generation via Symbolic Policy Learning

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Xu Xu, Jinxiu Liu, Zhangbo Qiao, Jiaxing Lu, Xiangyu Zhang, Yubin Gu, Fangwei Ning, Yan Shi
- 机构：Beihang University, National University of Singapore, The Chinese University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16057v1) · [PDF](https://arxiv.org/pdf/2609.16057v1)

## TLDR
OmniHarness is a symbolic policy learning framework that distills verified visual-generation executions into reusable, composable policies and uses self-directed inquiry plus intermediate verification to enable generalizable, continually improving visual generation, achieving 95.0% resolve on ComfyBench Creative and plug-and-play reuse across agent frameworks.

## Abstract
Unified multimodal large language models (MLLMs) and multi-agent systems have advanced visual generation. However, three limitations remain. (1) Existing methods often distill task-specific experience with limited generalizability. (2) Reflection is often deferred until task completion. (3) Knowledge is often acquired only in response to downstream task demands. To address these limitations, we introduce OmniHarness, a framework for generalizable visual generation via symbolic policy learning. OmniHarness abstracts verified executions into symbolic policies for visual generation task families, capturing shared procedures and applicability conditions while removing instance-specific inputs. The harness instantiates, adapts, and composes these policies for new tasks. Intermediate verification guides refinement and failure recovery during execution. Through self-directed inquiry, OmniHarness autonomously generates and executes practice tasks near its capability limits before downstream objectives are specified. Execution feedback continually refines the policies while model parameters remain fixed. Experiments across six benchmarks, three MLLM backbones, and three visual agent frameworks demonstrate strong performance and continual capability expansion. On ComfyBench's Creative tasks, OmniHarness achieves a 95.0% resolve rate, exceeding the strongest baseline by 27.5 percentage points. Frozen policy snapshots improve existing visual agent systems through plug-and-play reuse.


## 精读解读（中文）
### 一、研究动机
现有统一MLLM与多智能体视觉生成方法有三个局限：经验蒸馏偏任务特化、反思常滞后到任务完成、知识只在任务需求出现后被动获取。核心问题是构建能超越个例泛化、边执行边反思、并通过自主探索学习的视觉生成系统。OmniHarness以符号策略学习回应这一问题。

### 二、技术方案（Method）
方法将已验证执行抽象为面向视觉生成任务族的符号策略，保留共享流程与适用条件而去除实例特定输入，并维护工作流库与失败库。训练/推理前先自导向探究：proposer基于能力空间、场景上下文和策略库状态生成候选任务（描述、T2I/I2I模态、所需能力、源图），过滤重复并规避已知失败；按新颖度与能力前沿得分 N(tau)=平均 1/sqrt(n+1)、C(tau)=4 r(1-r)（r为最弱必需能力的可靠性，峰值在0.5）选择任务执行。执行时planner实例化、适配、组合策略生成计划，计划验证器检查顺序/依赖/任务一致性，writer生成类Python的Code-as-Policy程序，经可逆解释器编译为以ComfyUI节点为函数、数据流为连接的workflow。中间验证检查可执行性、每步预期效果及输出是否满足描述与约束；失败时diagnoser定位步骤并从失败库取纠正，在保留已验证步骤的前提下局部修复，必要时由子代理提供可复用子工作流，循环至成功或重试预算耗尽。整个过程中模型参数冻结，仅策略库由执行反馈持续更新。

### 三、结果（Result）
实验覆盖六个基准、三种MLLM骨干与三种视觉agent框架，显示强性能与持续能力扩展。ComfyBench Creative任务上OmniHarness达到95.0% resolve rate，比最强基线高27.5个百分点。冻结的策略快照可通过即插即用方式提升现有视觉agent系统。

### 四、结论（Conclusion）
OmniHarness通过符号策略学习、反馈引导执行与自导向探究，将一次性执行经验转化为可复用、可迁移的任务族策略，在模型参数不变的情况下实现持续能力扩展。它缓解了任务特化、滞后反思和被动学习三个问题，并为视觉生成多智能体系统提供可插拔的自进化harness范式。

### 五、方法论与关键技术细节
关键实现细节包括：符号策略抽象共享过程与适用条件但不含实例输入；工作流库存策略模板，失败库存失败证据与纠正策略。任务选择使用能力新颖度与Goldilocks可学习性启发式，可靠性取适用且未暂停工作流的95%置信下界（无可用工作流时用小先验epsilon），任务可靠性由最弱必需能力决定。执行侧采用planner、plan verifier、writer、可逆解释器、diagnoser与子代理，支持中间验证、局部修复和已验证步骤保持，受重试预算约束。局限在于效果依赖验证器质量、失败库覆盖、能力空间与ComfyUI节点/工作流定义，且方法不更新模型参数，泛化边界由符号策略库和自导向探究分布决定。
