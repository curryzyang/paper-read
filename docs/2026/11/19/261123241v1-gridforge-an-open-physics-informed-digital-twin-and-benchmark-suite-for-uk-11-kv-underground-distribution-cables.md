# GridForge: An Open Physics-Informed Digital Twin and Benchmark Suite for UK 11 kV Underground Distribution Cables

- 区域：精读区
- 排名：8
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Lilliane Linnet Musoke
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23241v1) · [PDF](https://arxiv.org/pdf/2611.23241v1)

## TLDR
GridForge is an open-source, physics-informed digital twin and benchmark suite for UK 11 kV underground distribution cables that combines verified IEC thermal models, a calibrated 64-cable synthetic dataset, a fast PINN surrogate (0.148 °C RMSE), and a five-task benchmark with baselines to enable reproducible cable fault diagnosis and maintenance decision support.

## Abstract
The UK distribution-cable monitoring sector is data-rich but framework-poor: each Distribution Network Operator (DNO) collects megabytes of telemetry per asset per day, but there is no public benchmark dataset, no shared reference model, and no commonly agreed evaluation protocol for benchmarking sectoral, data-intensive models for operational decision support; notably for maintenance planning and prioritisation. We address this gap with GridForge, an open-source physics-informed digital twin and benchmark suite for fault diagnosis and prediction, integrating four building blocks: (i) a verified steady state and transient thermal model based on IEC 60287 and IEC 60853; (ii) a calibrated synthetic dataset of 64 cables (covering 320 cable-years) representing four canonical UK 11 kV thermal archetypes and four condition modes; (iii) a Physics-Informed Neural Network (PINN) surrogate that satisfies the algebraic balance defined by IEC 60287 during training and reaches an RMSE of 0.148 °C on an independent held out set against the reference analytical oracle; and (iv) a five-task benchmark suite that includes three reference baseline models (pure physics, gradient-boosted trees, and the PINN). All numerical parameters are sourced from public standards, the code is licensed under the MIT licence, and the trained PINN converges in only two minutes (as run on the computing platform in Section 10.1), enabling independent verification by DNO engineering and research practitioners. At present only the virtual-sensor task (T4) discriminates between the reference baselines; the other tasks tie or are undefined on this test split, so extending the baselines with task-specific logic is a priority future enhancement. For open validation, the dataset, test sets and models are made available at https://github.com/mlily2024/Gridforge


## 精读解读（中文）
### 一、研究动机
英国配电电缆监测领域数据丰富但框架缺失：各配电网络运营商每天采集大量遥测数据，却没有公开基准数据集、共享参考模型和统一评估协议，难以为维护规划与更换优先级提供可复现的决策支持。与此同时，11 kV 地下电缆更换成本高、故障后抢修更昂贵，且监管框架将停机惩罚与可靠性指标挂钩，因此亟需开放、物理可信且可独立验证的数字孪生与基准套件。

### 二、技术方案（Method）
GridForge 由四部分组成：首先实现并验证基于 IEC 60287 的稳态热模型、IEC 60853-2 的暂态集总热模型、同轴电场解和 Crine 介电老化动力学的物理 oracle；其次用该 oracle 生成 64 条电缆、320 电缆年、小时级遥测的合成数据集，覆盖四种英国 11 kV 热学原型和四种状态模式，并采用 SHA-256 确定性 70/15/15 划分及密封测试标签；然后训练 PINN 代理模型，输入为电流、环境温度和土壤热阻率，输出导体温度，采用四层 64 单元 tanh MLP、4 个 octave 的 Fourier 位置编码和 softplus 约束保证温度不低于环境温度，损失为 oracle 数据 MSE 与 IEC 60287 代数平衡物理残差之和，并用梯度范数平衡自适应权重，Adam 学习率 2×10^-3、批大小 256、1500 轮、4000 训练对和 800 验证对；最后在五个密封标签任务上以纯物理、梯度提升树和 PINN 三个基线按固定协议评估。

### 三、结果（Result）
PINN 在独立留出集上的导体温度预测 RMSE 为 0.148 °C，最佳验证检查点为 0.064 °C、最终轮验证 RMSE 为 0.131 °C，均显著低于预先设定的 0.5 °C 验收目标，且训练约 2 分钟即可收敛。基准套件目前只有虚拟传感器任务 T4 能区分三个参考基线，其余任务在该测试划分上打平或未定义，说明任务特定基线逻辑仍需扩展。

### 四、结论（Conclusion）
GridForge 提供了首个面向英国 11 kV 地下配电电缆的开放物理信息数字孪生与基准套件，集成了经标准验证的物理 oracle、可复现合成数据集、快速 PINN 代理和五任务密封评测协议，并以 MIT 许可和公开参数支持 DNO 与研究者独立复核。其核心价值在于把维护决策支持从私有数据和不可比方法推进到公开、物理约束、可复现的基准框架，但当前判别力有限，未来需扩展任务特定基线并扩大到约 1000 电缆年的生产规模。

### 五、方法论与关键技术细节
所有数值参数均引用公开标准（如 BS EN 60228、BS 7870、IEC 60287-2-1、Met Office 土壤气候和 IEEE 1407），不含雇主数据、NDA 数据或商业机密；数据集约 280 万样本、200 MB 未压缩 CSV，按电缆原子性划分并单独保存 failure_times.csv 密封标签。PINN 共 14,337 参数，物理损失为 IEC 60287 代数平衡残差，权重平衡采用 α=0.9、K=50、初始 w_p=10^-3，未做超参搜索；稳态求解用 5–10 步不动点迭代，典型 240 mm² XLPE 三芯电缆时间常数约 64 分钟，Crine 默认设计点为 4 MV/m、90 °C、40 年并按 Miner 规则累积损伤。局限性包括数据为合成数据、只有 T4 具判别力、基线较简单、未覆盖现场噪声与商业数据偏差，生产级规模仍属未来工作。
