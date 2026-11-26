# Fast and Scalable Abstract Interpretation for Deep Neural Networks

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Avaljot Singh, Dushyant Bharadwaj, Yasmin Chandini Sarita, Heng Zhong, Charith Mendis, Gagandeep Singh
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33259v1) · [PDF](https://arxiv.org/pdf/2611.33259v1)

## TLDR
Scepter specializes DNN abstract interpreters by separating architecture-determined structural computation from numerical evaluation and compiling it into reusable tensor programs, enabling much faster and more scalable certification of large networks while computing the same bounds.

## Abstract
Abstract interpretation can certify properties of Deep Neural Networks (DNNs), but precise analyses remain expensive. General implementations repeat work when analyzing the same architecture under different inputs and properties. Interleaving this work with numerical operations limits GPU utilization and restricts how much of the analysis a tensor compiler can process together.
  We present Scepter, a framework for specializing DNN abstract interpreters through structural semantics. The semantics determine the structure of intermediate abstract values while deferring their numerical evaluation. Structural computations from successive operations can therefore be performed together before certification, generating an executable tensor program. With the abstract interpreter and DNN architecture fixed, the program can be reused with different weights and input regions. We prove that it computes the same bounds as the general interpreter in exact arithmetic. The generated program also exposes operations and their dependencies for tensor compilation and memory planning. We implement Scepter for the tensor programs that Neuton generates from ConstraintFlow specifications.
  We evaluate Scepter on eight abstract interpreters and 44 DNNs against six baseline systems on GPUs and CPUs. Scepter handles networks with up to 153x as many neurons as the largest completed by the corresponding baselines. It completes DeepPoly on ResNet50 and VGG-16, whereas none of the evaluated DeepPoly baselines completes either network. On configurations completed by both systems, GPU geometric-mean speedups over Neuton range from 11.9x to 44.4x across eight analyses, with a 2.60x geometric-mean reduction in peak memory. In an input-splitting case study, Scepter proves 68 properties for which the baselines time out.
  Code: https://github.com/uiuc-focal-lab/constraintflow.git


## 精读解读（中文）
### 一、研究动机
深度神经网络（DNN）的精确抽象解释认证仍然开销很大，而通用解释器在分析同一架构的不同权重、输入区域和性质时会重复进行大量非数值的结构性决策；这些工作与数值运算交错，既限制 GPU 利用率，也限制张量编译器对分析的整体优化。因此，需要把由网络架构决定、可复用的结构计算从每次认证的数值求值中分离出来，以将精确分析扩展到更大网络。

### 二、技术方案（Method）
Scepter 为 DNN 抽象解释器引入结构语义：对固定的解释器与网络架构，显式表示中间抽象值的结构，定义各操作如何从输入结构推导输出结构，同时推迟系数的数值求值并记录后续数值计算代码；将连续操作的结构计算合并，在认证前生成可执行的张量程序，并把仍依赖数值结果的控制决策保留在生成代码中。作者在 Neuton 从 ConstraintFlow 规范生成的张量程序上实现该方法，基于 g-BCSR 统一表示结构模式，使生成程序可暴露操作及依赖供张量编译和内存规划，并证明在精确算术下其计算结果与通用解释器得到相同边界。固定解释器、架构及输入/批形状后，生成程序可复用不同权重和输入区域。

### 三、结果（Result）
在 GPU 和 CPU 上对 8 种抽象解释器、44 个 DNN 与 6 个基线系统进行评估，Scepter 可处理的最大网络神经元数最高为对应基线已完成最大网络的 153 倍；它完成了 DeepPoly 对 ResNet50 和 VGG-16 的分析，而所评估的 DeepPoly 基线均未完成。两者均完成的配置上，GPU 相对 Neuton 的几何平均加速为 11.9 倍至 44.4 倍，峰值内存几何平均降低 2.60 倍；在输入分裂案例中，Scepter 证明了 68 个基线超时的性质。DeepPoly 下 Scepter 相对 auto_LiRPA、GPUPoly、IVAN 分别快 5.69、6.57、22.3 倍，CPU 上相对 ERAN 在 DeepPoly 和 DeepZ 下分别快 87.4 和 522 倍。

### 四、结论（Conclusion）
Scepter 通过结构语义将可复用的结构计算与数值认证分离，并生成架构专用的可执行张量程序，从而显著提升精确 DNN 抽象解释的规模、速度和内存效率，尤其适合输入分裂等需对同一网络反复认证的场景。该方法在保持精确算术下边界一致性的同时，为不同抽象域和认证算法提供统一专门化路径，推动精确认证在大模型上的实用化。

### 五、方法论与关键技术细节
关键实现点包括：专门化条件为固定抽象解释器、DNN 架构以及输入和批形状，权重与输入区域可变化；结构语义需覆盖可组合操作并跨抽象域/变换器工作，显式区分结构描述与数值载荷，改写依赖系数的控制流以允许结构执行先行；采用 Neuton 的 g-BCSR 表示网络结构模式；生成程序暴露操作依赖以支持算子融合、内存规划和独立神经元组提前释放大中间张量；正确性证明依赖精确算术，实际浮点执行及仍需数值决定的分支由生成代码中单独专门化的计算处理，且复用受固定架构与形状约束。
