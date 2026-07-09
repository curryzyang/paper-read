# Learning to Control LLM Agent Harnesses with Offline Reinforcement Learning

- 区域：精读区
- 排名：2
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Haiwen Yi, Xinyuan Song
- 机构：University of Toronto, Emory University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05458v1) · [PDF](https://arxiv.org/pdf/2607.05458v1)

## TLDR
This paper introduces a method to learn the execution harness of a frozen LLM agent as a control policy via offline advantage-weighted regression from terminal task rewards, demonstrating consistent improvements in verification behavior and selective final task quality gains dependent on offline buffer support.

## Abstract
Large language model (LLM) agents are usually improved by changing prompts, models, or hand-written workflows, while the execution harness around the model is treated as fixed infrastructure. We argue that this harness is itself a learnable control layer. We formalize harness operation as a finite-horizon Harness MDP, where a lightweight controller selects structural execution actions while the LLM executor remains frozen. The controller is trained from offline rollouts using advantage-weighted regression with only terminal task-rubric rewards. We also separate final task quality from a post-hoc Harness Maturity Score, which measures whether the harness follows reliable execution patterns rather than only whether the final answer is correct. This separation gives a finite-buffer view of harness learning: final-quality gains require high-return support in the offline buffer, while process behavior can shift whenever it aligns with advantage-weighted actions. Across six controlled domains and two public-benchmark adapters, the learned controller consistently improves verification behavior and selectively improves final task quality, with the largest gains on adapted tau-bench retail, adapted AgentBench DB-Bench, and coding with a calibrated structural verifier. Ablations against behavior cloning and Forced CHECK show that the gains are not explained by imitation or by simply adding checks. These results identify harness control as a learnable layer for frozen LLM agents, while showing that offline support limits when better process control becomes better final answers.


## 精读解读（中文）
### 一、研究动机
现有大型语言模型Agent的改进通常聚焦于提示词、模型或手工工作流，而执行框架（harness）被视为固定基础设施。本文论证该框架本身是一个可学习的控制层：固定规则如“总是检查”或“直接提交”会导致资源浪费或失败，因此需要学习一个状态条件化的控制器来动态选择下一步结构化操作。

### 二、技术方案（Method）
定义有限时域Harness MDP，状态向量包含轨迹进度、草稿状态、证据覆盖、工具输出、验证器反馈、剩余预算等特征；控制器从七个结构化动作（观测、检索、调用工具、草稿、检查、修订、提交）中选择，域适配器屏蔽无效动作。使用离线轨迹缓冲区收集基础与探索策略的轨迹，每个轨迹以终端任务评分标尺返回作为奖励。采用优势加权回归（AW）训练控制器：通过指数权重重加权轨迹似然，增加高优势轨迹中状态-动作对的概率，同时保持LLM执行器冻结。控制器为单隐藏层MLP（64隐藏单元），softmax输出；训练使用Adam（学习率1e-3）、批次256、20轮、AW温度0.2，权重裁剪[0.1,10.0]，熵正则0.01。过程质量通过事后Harness Maturity Score（HMS）诊断，不参与训练。

### 三、结果（Result）
在六个受控域和两个公共基准适配器上，AW一致提升了提交前检查（CheckBeforeSubmit）行为，整体HMS在五个域和两个适配器中改善，但改善主要源于检查事件而非均匀提升。最终任务质量选择性提升：编码任务在标定结构验证器下改善，τ-bench零售与AgentBench DB-Bench适配器获得最大外部增益。消融实验表明AW优于行为克隆与强制检查基线，证明增益来自学习何时执行检查而非单纯模仿或机械插入检查。

### 四、结论（Conclusion）
本研究识别出固定LLM Agent的框架控制是一个可学习层，过程行为可通过优势加权从离线缓冲区中广泛改善，但最终任务质量的提升依赖于缓冲区中是否包含高回报轨迹。更好的过程控制（如检查）并不总能转化为更好的最终答案，其转化受限于离线轨迹支持。

### 五、方法论与关键技术细节
状态向量包含轨迹进度、草稿状态、工具输出、验证器反馈、错误计数、剩余预算、最近测试结果与先前动作；动作空间为七个结构化操作并由域适配器屏蔽无效。奖励仅为终端任务评分（势能函数为零），避免中间动作偏好。控制器为单隐藏层MLP（64单元），温度β=0.2，权重裁剪[0.1,10.0]，熵正则0.01。离线缓冲区需要高回报轨迹支持才能提升最终质量；过程改善要求行为与优势权重正相关。局限性包括无法发明缓冲区中不存在的高回报轨迹、多工具验证器仅验证最终工件与工具结构而非中间过程。超参数固定跨域，未针对各域调优。
