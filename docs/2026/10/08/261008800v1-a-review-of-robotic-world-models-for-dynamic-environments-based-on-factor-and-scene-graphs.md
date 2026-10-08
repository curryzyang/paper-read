# A Review Of Robotic World Models For Dynamic Environments Based On Factor And Scene Graphs

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Marco Giberna, Miguel Fernandez-Cortizas, Jose Luis Sanchez Lopez, Holger Voos
- 机构：University of Luxembourg
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08800v1) · [PDF](https://arxiv.org/pdf/2610.08800v1)

## TLDR
This review surveys factor- and scene-graph-based robotic world models for dynamic environments, organizing existing and hybrid approaches by representation, construction/update pipelines, and downstream exploitation while highlighting key open challenges.

## Abstract
Models based on graphs have emerged in robotics as a powerful foundation for internal world representations, where factor and scene graphs are among the most prominent model types found in the related literature and in successful robotic solutions. Initially, many of these models were assuming static environments as a simplification. Herein, factor graphs mainly provide uncertainty-aware geometric estimations while scene graphs enable a structured semantic abstraction. However, real-world robotic environments are often dynamic, posing severe challenges for purely static world representations. Therefore, this review presents a comprehensive view on how dynamic aspects of real-world environments can be addressed in such graph-based world models. We organize our assessments around three main aspects: (I) suitable representations, (II) pipelines to construct and update the representations, and (III) their exploitation for downstream tasks. We review approaches that are either based on factor or scene graphs, but put special emphasis on novel approaches that combine both types to form hybrid models. We mainly analyze how different types of dynamics can be modeled herein, and categorize common architectural patterns. Finally, emerging trends and open challenges are identified, including uncertainty propagation from learned perception through the representation layers, the observability of dynamic-entity motion and scale under minimal sensing, scalable lifelong maintenance, and the lack of datasets and evaluation protocols that ground world-model quality in downstream task performance under dynamics.


## 精读解读（中文）
### 一、研究动机
真实机器人环境本质动态，而传统因子图与场景图世界模型多假设静态，导致定位精度下降、数据关联错误、虚假地标以及下游任务失败。因子图擅长不确定性几何估计，场景图擅长结构化语义抽象，但二者都需扩展以处理连续运动、短期变化和长期结构演化，因此有必要系统综述动态环境下的图式机器人世界模型。

### 二、技术方案（Method）
该综述以因子图和场景图及其混合模型为对象，围绕三个问题组织：适合动态的表示、表示构建与更新管线、以及面向下游任务的利用与评估。技术上，因子图用二部图变量节点与因子节点表达联合概率分解，变量可包括机器人位姿、静态地图点、动态对象位姿和运动变换，因子可包括里程计、重投影、ICP、结构先验与语义运动先验，并用零均值高斯噪声和信息矩阵加权，通过 MAP 非线性最小二乘推断；场景图用对象节点、属性及 subject-predicate-object 关系边编码语义，生成流程通常包含特征提取、上下文关联、图构建与推理，结构上分扁平、分层和三维场景图；混合模型并行结合概率几何层与语义分层抽象。

### 三、结果（Result）
综述梳理出动态图式世界模型的三类主要路线：因子图、场景图与混合模型，其中混合模型如 Hydra 和 S-Graphs 将几何不确定性估计与语义分层抽象结合，是当前重要趋势。动态建模覆盖从连续运动到长期结构变化，并归纳了常见架构模式；同时指出开放挑战集中在学习感知到表示层的不确定性传播、最小感知下动态实体运动与尺度可观测性、可扩展终身维护，以及缺少将世界模型质量与动态下游任务性能绑定的数据集和评测协议。作为综述，它不提供新实验数值，而是给出分类框架与趋势判断。

### 四、结论（Conclusion）
该综述认为图式世界模型是动态机器人环境下内部表示的有力基础，但现有工作仍多在静态假设下发展。未来研究需在表示选择、构建更新和下游利用三个层面统一动态、不确定性、语义与长期维护，并建立以动态下游任务性能为导向的数据集和评测协议。

### 五、方法论与关键技术细节
关键实现细节包括：因子图形式化为 G={X,F,E}，联合分布因式分解，MAP 推断通常为非线性最小二乘；变量含机器人位姿、静态地图点、动态对象或智能体位姿及运动变换，因子含里程计、视觉重投影、点到面 ICP、位姿-平面、墙-房间和语义运动先验。场景图定义为 G=(O;E)，对象 o_i=(c_i,A_i)，边为 subject-predicate-object 三元组，关系类型涵盖空间、可见性与邻近、功能关系和可供性；生成方法分自顶向下两阶段和自底向上联合两类，结构分扁平、分层与三维场景图。局限与约束在于多数原始模型假设静态，动态会造成错误累积；最小感知下运动与尺度可观测性、终身可扩展维护、不确定性传播以及缺乏统一数据集和评价协议仍是待解决问题。
