# Progress Reward Modeling for Robotic Learning: A Comprehensive Survey

- 区域：精读区
- 排名：5
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Jianshu Zhang, Keliang Wu, Haoran Lu, Anbang Liu, Ce Zhang, Weijie Yin, Chengxuan Qian, Xiyuan Yang, Zhenyu Pan, Guo Ye, Han Liu
- 机构：University of California, Santa Barbara, University of Illinois Urbana-Champaign, University of Wisconsin–Madison, Carnegie Mellon University, Northwestern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21655v1) · [PDF](https://arxiv.org/pdf/2607.21655v1)

## TLDR
This survey provides a unified framework for progress reward modeling in robotic learning by organizing the field into three interconnected perspectives—interface, methods, and data/benchmarks—and highlights limitations and future directions.

## Abstract
Robotic learning takes place in dynamic environments with large behavior spaces. A terminal success signal only tells the robot whether the task is completed. It does not explain whether the current behavior is making progress, remaining unchanged, or undoing earlier progress. For this reason, recent studies have increasingly explored progress rewards that provide feedback during task execution. However, the current literature lacks a shared framework. Existing methods use different observations, goal specifications, output signals, supervision sources, and evaluation protocols. This makes it difficult to compare them and understand what their results actually validate. In this survey, we provide a unified view of progress reward modeling for robotic learning. We organize the field in three connected steps. We first study the interface of a progress model. This defines the problem from the outside by asking what information the model receives and what form of progress signal it produces. We then move inside the model and study the methods used to construct this signal. This reveals the different assumptions and mechanisms behind progress estimation and reward generation. Finally, we examine the data and benchmarks that support these methods. This shows how progress supervision is obtained and what different evaluations actually measure. Together, these three perspectives connect what a progress model is, how it is built, and how its quality is validated. We further summarize the main limitations of current approaches and discuss future research directions.


## 精读解读（中文）
### 一、研究动机
终端成功信号仅反馈任务是否完成，无法提供中间执行中的进展信息，导致长时任务中信用分配困难。现有进展奖励方法使用不同的观测、目标、输出和监督方式，缺乏统一框架，难以比较和验证。

### 二、技术方案（Method）
提出统一视图，从三个相连步骤组织领域：首先研究进展模型的接口，定义模型接收什么信息（当前任务状态表示：单观测、时间上下文、比较、状态访问；任务目标指定：语言、视觉、结构/程序）和输出什么信号（状态式标量分数、进展delta、排名、程序化奖励函数）。其次打开黑箱，研究信号构建方法，识别四大范式：冻结基础模型评分、时序/相对监督学习、指令调优进展预测、程序化奖励构造。最后检查支持方法的数据和基准，说明进展监督如何获取以及不同评估测量什么。

### 三、结果（Result）
综述梳理了进展奖励建模的演化，总结四大范式各自的优缺点：冻结基础模型简单但缺乏适应性；时序/相对学习需要配对或偏好数据；指令调优依赖大型视觉语言模型且对历史敏感；程序化方法依赖显式状态变量。指出评估异质性问题：时序排序、标量预测误差、偏好准确性、成功检测和下游策略性能验证不同属性，导致直接比较困难。

### 四、结论（Conclusion）
进展奖励建模是机器人学习的重要方向，但当前文献碎片化。通过接口、方法和数据/基准的统一视图，可以连接进展模型是什么、如何构建以及如何验证其质量。未来需要更统一的评估协议、更好的泛化和鲁棒性，以及对长期依赖和部分可观测性的处理。

### 五、方法论与关键技术细节
关键方法论细节包括：输入表示选择影响在线可用性和信息含量（单观测低延迟但模糊，时间上下文更强但削弱在线性，比较更直观，状态访问依赖仿真API）。目标指定中语言易编码但欠指定物理细节，视觉减少模糊但需人工标注且对视角敏感。输出形式中标量分数最直接但需校准，进展delta自然对齐RL但需累积，排名易监督但间接，程序化灵活但依赖环境变量。监督来源分人工、半自动、全自动。局限包括：评估碎片化、泛化性不足、长期依赖建模困难、部分可观测性下进展推断问题。
