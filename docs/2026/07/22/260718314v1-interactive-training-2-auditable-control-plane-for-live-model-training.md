# Interactive Training 2: Auditable Control Plane for Live Model Training

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Wentao Zhang, Xuanhe Pan, Han Zhou, Yang Lu, Yuntian Deng
- 机构：University of Waterloo, University of Wisconsin-Madison
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18314v1) · [PDF](https://arxiv.org/pdf/2607.18314v1)

## TLDR
Interactive Training 2 introduces an open-source control plane with a shared protocol that enables humans and automated controllers to audibly steer live model training through typed settings and actions applied at safe control points, demonstrated across multiple NLP and reinforcement learning workflows.

## Abstract
Experiment trackers show how training is progressing, but changing a live run still usually requires trainer-specific code. We present Interactive Training 2, an open-source control plane for steering training through a shared protocol. Training applications declare which settings and actions they expose, humans and automated controllers submit requests through the same interface, and the training loop validates and applies them at safe control points. A customized Aim workspace combines live metrics and controls with a chronological record of requests and outcomes. We demonstrate the system across five NLP and reinforcement-learning workflows. The released code and traces provide a reusable foundation for auditable human- and agent-guided training.


## 精读解读（中文）
### 一、研究动机
现有实验追踪器虽能显示训练进展，但修改正在运行的训练仍需编写训练器特定的回调或逻辑，缺乏通用接口。研究者希望根据实时行为（如损失曲线、评估结果）灵活调整学习率、数据平衡或保存检查点，但现有工具碎片化，无法统一实现可审计的人工或自动化干预。

### 二、技术方案（Method）
提出Interactive Training 2，一个开源控制平面，通过共享协议实现训练实时干预。训练应用注册类型化设置（knob）和结构化动作（action），例如学习率、评估、保存检查点；人类、脚本或LLM代理通过同一HTTP API提交请求；训练循环在显式控制点（如session.step()调用）验证并应用请求，并记录成功或失败结果。系统基于Python的TrainingSession，可选LLM代理执行计划（接收任务和设置列表）、行动（根据实时指标调用注册动作）和反思（总结教训用于下一轮）。集成Aim作为监控和控制UI，提供实时指标、请求队列和事件日志。支持HuggingFace回调、优化器包装和直接PyTorch循环三种集成方式，在五个工作流（情感分类、数据混合、层级GPT、Muon-AdamW GPT、RLVR计数）中验证。

### 三、结果（Result）
核心发现：同一协议可表示多种类型更改（如学习率、27个层级学习率、混合权重、课程难度）；每个请求产生记录结果（如save_checkpoint请求返回action_result和checkpoint_saved事件）；后续回合能利用先前反思（如情感分类R8反思不对称类别权重后R9/R10采用该策略，Muon-AdamW R4反思动量未尝试后R5降低动量值）。五个工作流均记录多轮分数提升：情感分类验证损失从0.354降至0.220，情感混合Macro-F1从0.568增至0.656，层级GPT验证损失从5.346降至5.055，Muon-AdamW GPT验证损失从4.797降至4.429，RLVR计数最难准确率从0.032增至0.232。

### 四、结论（Conclusion）
Interactive Training 2将实时训练干预从实验特定逻辑转化为可复用接口，使训练应用定义可修改项和安全应用点，控制器通过共享协议提交请求，日志记录完整决策序列。这种分离简化了训练转向、复用和跨框架检查，为交互式训练工具以及人类与自动代理监督学习提供了基础。

### 五、方法论与关键技术细节
数据/输入：训练任务自带数据集，控制平面不涉及数据增强。建模：关键模块包括TrainingSession（管理设置、动作、请求队列和事件日志）、注册knob（类型、范围、步长）、action（命令和参数）、LLM代理（GPT-5.5高推理努力，三阶段流程）。训练流程：session.step()在控制点记录指标、运行控制器、处理请求、调用处理函数、返回StepControl（指示停止、评估、保存等）。损失函数：由训练任务定义，控制平面不修改损失。超参：控制点频率（如每100步调用eval/controller）、请求队列处理方式（非阻塞HTTP返回ID，后续查询结果）。复杂度：训练循环等待LLM响应，不支持迟到的响应；自定义动作需应用自行检查；高安全性场景需额外批准门、资源预算和回滚策略。局限性：LLM响应延迟影响训练；代理无法保证安全最优动作。
