# $\mathcal{H}_\infty$ Grid-Forming Control in DC Microgrids

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Jovan Krajacic, Ognjen Stanojev, Mario Schweizer, Gabriela Hug
- 机构：ABB Corporate Research Center, ETH Zurich
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26827v1) · [PDF](https://arxiv.org/pdf/2611.26827v1)

## TLDR
The paper proposes a passivity-constrained \(\mathcal{H}_\infty\) synthesis method for DC-bus voltage control in DC microgrids that shapes converter output impedance and current-forming behavior to achieve desired grid-forming performance, validated via frequency-domain benchmarking and experiments on a four-converter DC microgrid.

## Abstract
The growing share of DC-based generation, storage and loads has increased interest in DC microgrids. As a result, DC-bus voltage regulation and stability have become active research topics, with considerable effort directed at improving the transient performance of conventional droop control. Although numerous variants of droop algorithms have been proposed, many rely on increasingly complex control structures with multiple tuning parameters and measurements, thereby increasing the commissioning burden. Moreover, stable interaction with the surrounding microgrid is not guaranteed by design. To address these issues, this paper develops a passivity-constrained $\mathcal{H}_\infty$ synthesis method for the DC-bus voltage controller. The proposed $\mathcal{H}_\infty$ controller emulates the desired grid-forming behavior of the converter by minimizing the $\mathcal{H}_\infty$ error norm between device-level performance indices and their desired values, while additionally enforcing passivity during the optimization. The novel $\mathcal{H}_\infty$ control scheme is benchmarked in the frequency domain against representative droop-based and virtual-DC-machine algorithms from the literature, while experiments on a four-converter DC microgrid corroborate the frequency-domain analysis and validate the practical applicability of the algorithm.


## 精读解读（中文）
### 一、研究动机
直流微电网中分布式电源、储能与负荷的直流化程度不断提高，使直流母线电压调节与稳定性成为研究热点。传统下垂控制虽可实现无通信的分散功率分配，但其改进方案普遍依赖多参数、多测量的复杂控制结构，调试负担大，且与周边微电网的稳定交互无法在设计阶段得到保证。现有针对直流微电网的 H∞ 设计多集中于双有源桥或负荷侧变换器，或仅以幅值要求整定固定结构下垂，既未把输出阻抗作为设计变量，也未处理无源性。

### 二、技术方案（Method）
论文提出面向 I-V 型直流母线电压控制器的无源性约束 H∞ 综合方法：保留仅用直流母线电压测量的单环 I-V 架构，但把传统静态下垂增益替换为待设计的低阶动态控制器 R_H∞，由内环 PI 电流控制器（按内模控制整定，带宽取开关频率的约七分之一以下）跟踪其电流参考并经 PWM 驱动半桥。建模上以双向 Boost 变换器的小信号平均模型为基础，给出 G_di、G_oi、G_dv 与开环输出阻抗 Z_o，并构建含串联输出阻抗 Z_out' 与并联电容导纳 Y_dc 的等效电路以推导闭环 Z_out。以既有工作定义的器件级指标——输出阻抗指标 OII 与电流形成指标 CFI——的期望频域曲线为参考，通过频域加权函数把指标与其期望值之间的 H∞ 误差范数作为目标最小化，并在优化过程中同时施加输出阻抗无源性约束，同时采用结构化/固定阶形式预先锁定控制器复杂度；最后在频域与代表性下垂及虚拟直流电机方案对比，并在四变换器直流微电网实验平台上验证。

### 三、结果（Result）
综合得到的 H∞ 控制器使闭环输出阻抗指标与电流形成指标在所关心的频段内贴合预设的期望曲线，并在设计阶段即满足输出阻抗无源性，从而保证与周边网络的稳定互联。频域基准测试表明，相较于文献中典型的下垂控制与虚拟直流电机方案，该方法在暂态性能与阻抗匹配上更具优势且无需多参数整定；四变换器直流微电网实验复现了频域分析的结论，验证了算法的实际可行性与较低的上线调试工作量。

### 四、结论（Conclusion）
将期望的构网型端子行为直接写成频域指标、并把无源性作为综合约束而非事后校验，可在保持 I-V 单环简单结构、仅需直流母线电压测量的前提下获得低阶动态控制器，实现电压支撑与电流形成兼顾的构网行为。该 H∞ 整定框架不依赖具体拓扑，可推广到其他控制结构与变换器类型，相较依赖非线性结构与大量电机类比参数的虚拟直流电机方案更易调试。

### 五、方法论与关键技术细节
关键点包括：以 Boost 变换器小信号模型为被控对象，忽略电感与开关损耗，稳态工作点由 I_o、V_in、V_dc、D 确定，电容以 C_dc 串联 r_dc 的导纳建模；性能由 OII（|OII|≤1 判为构网）与 CFI（CFI=1 为跟流、|CFI|<1 为构流）两项器件级指标刻画；目标函数为指标与期望值之间的 H∞ 误差范数加权最小化，无源性作为综合期约束以提供稳定互联的充分条件；控制器阶数与结构先验固定，输出电容视为既定而非自由设计变量，问题因此转为给定电容下可实现何种端子行为；内环 PI 带宽需显著低于开关频率并受控制带宽限制。局限性在于分析基于小信号线性化与特定 Boost 拓扑案例，无源性条件为充分非必要，且未涵盖大信号暂态与多工况鲁棒性评估。
