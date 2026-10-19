# When is a large language model a good calibration agent? Physics-labeled prompting for budgeted engineering simulator calibration

- 区域：精读区
- 排名：2
- 匹配度：5.1/10
- 来源：arxiv
- 作者：Ruo-Qian Wang
- 机构：Rutgers University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22379v1) · [PDF](https://arxiv.org/pdf/2610.22379v1)

## TLDR
Physics-labeled LLM prompting gives a strong but transient early advantage in budgeted engineering simulator calibration, so the paper recommends using it as a warm start before handing off to a conventional optimizer, reaching target accuracy in 9 simulator runs versus 17 for Nelder–Mead.

## Abstract
Calibrating expensive engineering simulators requires tuning model parameters to match reference data, a process heavily constrained by computational costs. This study investigates whether Large Language Models (LLMs), conditioned on physical diagnostic descriptions of simulation errors, can propose informative parameter updates more efficiently than conventional derivative-free optimizers. We test this on a cylinder-wake Large-Eddy Simulation and a damped-oscillator inverse problem. Physics-labeled prompts are evaluated against four text ablations (removed, anonymized, padded, misdirected) and standard optimizers (Nelder-Mead, Bayesian optimization, CMA-ES, and random search). Results demonstrate a strong early semantic advantage: the first physics-informed LLM proposal improves the initial design in 23 of 25 trials. After five evaluations, the median calibration error is 21.9 times lower than physics-free controls. However, this advantage is transient - disappearing by fifteen evaluations - and inherent LLM decoder variability yields a 9.8-fold performance spread. To address this, we introduce a hybrid workflow that uses the LLM as a warm-start, passing accumulated evaluations to a conventional optimizer. This two-stage numerical continuation policy reaches target accuracy in just 9 simulator runs, outperforming the LLM alone (12 runs), Nelder-Mead (17 runs), and Bayesian optimization (>60 runs). Supported by sensitivity analysis validating the test cases, this hybrid physics-labeled LLM scheme proves highly effective as a calibration agent under strict evaluation budgets.


## 精读解读（中文）
### 一、研究动机
校准昂贵工程仿真器的成本主要由外层循环消耗的仿真次数决定，传统无导数优化把参数视为匿名坐标，在早期数值历史不足时难以给出方向；专家能利用物理诊断但主观、费力且难复现。本文因此检验大语言模型在接收物理诊断描述时，能否在严格评估预算下提出更有信息量的参数更新，并区分物理语义与一般提示效应的贡献。

### 二、技术方案（Method）
在圆柱尾流LES（OpenFOAM pisoFoam，校准分子黏度、Smagorinsky系数和耗散系数）及阻尼振子逆问题上，每次向LLM输入参数边界、按目标排序的前十次试验和当前运行的物理诊断文本，要求返回机器可读参数向量，越界或非法输出经裁剪/重试，不训练、不拟合、不建代理模型；与去诊断、匿名化、等长填充、误导语义四种提示消融以及Nelder-Mead、GP-BO、CMA-ES、随机搜索在同初始设计下比较，并将LLM前若干次评估作为热启动交给NM或GP-BO形成两阶段数值延续（默认交接预算B_switch=15）。物理提示重复25次、消融提示重复30次以量化解码器随机性。

### 三、结果（Result）
物理标签提示的首个提议在23/25次重复中改进了共享初始设计，消融提示仅8/30；5次评估后中位校准误差比无物理控制低21.9倍，10次后低4.7倍，15次后无差异。相同提示与初值的重复实验显示五种子中位数可相差9.8倍。两阶段延续流程报告中位9次仿真达到目标精度，优于纯LLM的12次、Nelder-Mead的17次和贝叶斯优化的>60次；对3047次求解的敏感性分析表明四个力统计量只能识别三个校准参数中的一个。

### 四、结论（Conclusion）
物理标签提示带来的是早期方向性优势，而不是收敛保证；该优势约在十次评估内衰减，并受LLM解码器变异性的显著限制。把LLM作为热启动、再由传统数值优化器接手，可将短暂的语义优势转化为紧预算下可用的校准流程。实际使用前应做参数可识别性筛查并进行多次重复，否则优化器排名可能落入噪声范围。

### 五、方法论与关键技术细节
LES目标由四个统计量归一化加权平方误差构成（阻力主频、RMS升力、平均阻力、t=250相位；权重均为1，尺度为目标值、相位用π），失败运行罚1e9，所有方法共用同一目标和初始设计；提示包含参数名、单位、边界、目标历史及当前物理差异。关键限制是LES基准为同一求解器高分辨率参考的自洽可识别性问题，并非二维LES对真实湍流的验证；物理提示仅在前约十次评估有效，B_switch=15为先验固定未调参，且LLM输出需裁剪和重试，解码器方差使少量种子比较不可靠。
