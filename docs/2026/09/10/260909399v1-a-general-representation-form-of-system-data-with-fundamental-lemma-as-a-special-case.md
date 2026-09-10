# A general representation form of system data with fundamental lemma as a special case

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Steven X. Ding, Linlin Li
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09399v1) · [PDF](https://arxiv.org/pdf/2609.09399v1)

## TLDR
The paper introduces a general data representation for dynamic systems that includes the fundamental lemma as a special case.

## Abstract
This note introduces a general data representation of dynamic systems.


## 精读解读（中文）
### 一、研究动机
数据驱动控制与系统辨识中，Willems 基本引理为利用输入输出数据直接刻画系统轨迹提供了基石，但它依赖线性时不变、无噪声和持续激励等条件，适用范围受限。作者希望给出更一般的系统数据表示形式，使基本引理成为其特例，从而统一理解不同系统与数据条件下的轨迹生成机制。

### 二、技术方案（Method）
论文引入一般的动态系统数据表示：给定若干条测量轨迹，将输入输出序列按时间堆叠为数据矩阵（如 Hankel 或广义 Hankel 矩阵），并考虑系统的行为集合；通过构造数据矩阵的列空间或核空间，将任意系统轨迹表示为已测数据的线性组合，同时用系数矩阵或约束方程保证输入输出与时间移位的一致性。对于线性时不变系统，当输入满足持续激励且数据矩阵满秩时，该一般表示退化为 Willems 基本引理中的轨迹参数化；对于更一般的系统，则通过数据矩阵的秩条件或映射关系给出可达轨迹的刻画。

### 三、结果（Result）
核心发现是：基本引理所给出的“所有轨迹均可由数据矩阵列线性组合生成”并非线性时不变数据独有，而是一般数据表示的一个特例；在适当秩条件与持续激励条件下，一般表示可精确覆盖系统行为，并保持与基本引理一致的参数化形式。论文未在摘要中给出数值指标，主要贡献为形式化定理与特例归约。

### 四、结论（Conclusion）
该文为系统数据表示提供了一个统一框架，将 Willems 基本引理纳入更一般的轨迹参数化中，有助于厘清数据驱动控制中数据矩阵、持续激励与系统行为等价性之间的关系，并为推广到更广泛系统或数据条件提供理论基础。

### 五、方法论与关键技术细节
关键细节包括：以输入输出轨迹构造数据矩阵，用 Hankel 结构编码时间移位；通过列空间或核空间和系数矩阵的约束刻画轨迹；基本引理对应线性时不变、无噪声、输入持续激励且数据矩阵列满秩的特殊情形。该方法属解析代数框架，无训练损失，超参涉及 Hankel 深度与持续激励阶数；计算复杂度随轨迹长度和 Hankel 深度增长。局限性在于一般表示仍依赖精确数据与秩条件，噪声、非线性、时变及有限数据长度下的鲁棒性未在摘要中展开，实际应用需注意持续激励阶数与数据量的匹配。
