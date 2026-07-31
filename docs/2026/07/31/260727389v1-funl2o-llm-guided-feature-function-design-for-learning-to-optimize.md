# FunL2O: LLM-Guided Feature Function Design for Learning to Optimize

- 区域：精读区
- 排名：8
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Bingheng Li, Junyang Cai, Yupeng Zhang, Bistra Dilkina, Jayant Kalagnanam, Dzung T. Phan
- 机构：University of Southern California, University of Wisconsin–Madison, Michigan State University, IBM Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27389v1) · [PDF](https://arxiv.org/pdf/2607.27389v1)

## TLDR
FunL2O is the first unified framework that automates feature function design for learning-to-optimize via LLM-driven program evolution, consistently outperforming hand-crafted representations across continuous and discrete optimization tasks.

## Abstract
Learning-to-optimize (L2O) methods accelerate repeated optimization by training models to predict solutions, warm starts, branching decisions, or other forms of solver guidance. A critical yet largely overlooked component of these pipelines is the feature function that maps problem instances to inputs for machine learning models. Existing L2O methods typically rely on hand-crafted features, making representation design manual and largely fixed across domains. We introduce FunL2O, the first unified framework for automating feature design through LLM-driven program evolution for L2O. In a FunSearch-style loop, an LLM proposes executable feature functions, while a fixed evaluation process retrains the original L2O model and measures downstream optimization performance. We evaluate FunL2O on linear and quadratic programming tasks involving solution prediction and warm-starting, as well as on mixed-integer optimization tasks using GNN-guided backdoor branching and Predict-and-Search. Across continuous and discrete optimization tasks and four LLMs, the evolved features consistently outperform hand-crafted representations. These results establish LLM-driven feature evolution as a general and effective approach to automating representation design in L2O.


## 精读解读（中文）
### 一、研究动机
现有学习优化（L2O）方法通常依赖手工设计的特征函数来表示优化实例，这种表示设计是手动的且在不同领域中基本固定，忽略了特征表示对模型表达能力和下游优化性能的关键影响。因此需要一种自动化的特征设计框架，以替代耗时且领域相关的手工特征工程。

### 二、技术方案（Method）
FunL2O采用FunSearch风格的LLM驱动程序演化框架。具体而言，给定一个固定的L2O流水线（含原始模型、训练过程、数据、求解器），首先定义语义特征契约，包括可用实例字段、输出规范（类型、方向、最大特征宽度）、不变量和可执行验证器。搜索从手工特征函数φ0开始，每一代由LLM根据共享指令、当前精英函数源码、验证结果和评估反馈生成候选可执行特征函数，候选需通过静态检查和探针实例验证，验证失败则反馈错误条件并让LLM修复；通过验证的候选替换原特征函数，按原始训练流程重新训练模型，并利用下游优化指标（如可行性、目标间隙、迭代次数、枢轴数等）计算排序键进行lexicographic比较；排名的前K个精英函数进入下一代。搜索结束后返回最低排序键的特征函数，部署时仅为普通预处理代码，无需LLM。

### 三、结果（Result）
在LP和QP解预测、约束非线性预测、原始-对偶热启动、单纯形基初始化、枢轴选择以及MILP搜索（GNN引导的backdoor branching和Predict-and-Search）共8个L2O流水线上，使用四个不同LLM（包括GPT等）进行实验，进化得到的特征函数在可行性、目标质量和求解效率上始终优于原始手工特征表示；例如在可行率、解间隙、迭代节省等指标上均有一致改进，且改进幅度在不同任务和LLM间稳健。

### 四、结论（Conclusion）
FunL2O是第一个通过LLM驱动的程序演化来自动化L2O特征函数设计的统一框架。实验表明，仅改变输入表示而不改动模型架构、训练过程和求解器，就能持续提升多种连续和离散优化任务的性能，从而证明LLM驱动的特征进化是一种通用且有效的自动表示设计方法，也为未来L2O管道中的特征工程提供了新范式。

### 五、方法论与关键技术细节
关键细节包括：语义契约定义了不同流水线的特征接口（如异构图、稠密张量、求解器状态），并要求保留原始手工特征通道，通常采用追加式Concat(φ0, ψ)形式；排序键ρ=(b,v,q)以可行性是否违反为首位，次为不可行程度，再为目标或求解工作量，并统一为越低越好；候选评估必须重训练整个模型，因此单次评估代价高，但同代候选可并行训练；特征函数只能使用部署时可获取的信息，禁止访问参考解、标签、文件、网络或外部求解器；验证器先做静态源码检查，再在小型探针实例上运行检查输出维度、有限性和种子通道；最终选出的特征函数是普通预处理代码，部署时无需LLM参与，同时搜索过程不改变模型模板、隐藏结构、损失函数和超参数。
