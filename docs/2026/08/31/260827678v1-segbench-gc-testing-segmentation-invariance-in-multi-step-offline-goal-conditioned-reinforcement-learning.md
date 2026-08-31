# SegBench-GC: Testing Segmentation Invariance in Multi-Step Offline Goal-Conditioned Reinforcement Learning

- 区域：精读区
- 排名：3
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Musa Shams
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27678v1) · [PDF](https://arxiv.org/pdf/2608.27678v1)

## TLDR
SegBench-GC introduces a controlled stress test showing that in offline goal-conditioned RL, treating administrative trajectory cuts as absorbing states severely degrades multi-step learning performance, while keeping continuation-valid targets at those cuts preserves it.

## Abstract
Offline goal-conditioned reinforcement learning (GCRL) often uses trajectory structure for future-goal sampling and multi-step targets, yet logged trajectories may be partitioned for administrative reasons that do not correspond to termination. We introduce SegBench-GC, a controlled stress test of segmentation invariance that holds transitions, source trajectories, goal sampling, optimization settings, and evaluation fixed while varying only artificial backup boundaries and whether those boundaries retain continuation value. Continuation-valid targets (CVT) provide the segmentation-consistent control: reward accumulation stops at an artificial cut, but the target bootstraps from its stored successor. In a matched-count PointMaze study with 35,000 artificial cuts, three segmentation realizations, and three optimization seeds, final 50-episode-per-task success is 50.5% uncut, 39.1% with CVT, and 19.1% when the same cuts are treated as absorbing; across segmentation realizations, naive mean success ranges from 4.8% to 31.9%. An independent published n-step baseline (n=25) from the Decoupled Q-Chunking codebase shows the same failure on Puzzle-4x5: 47.2% uncut, 58.5% CVT, and 0.27% naive across three optimization seeds. A target-level diagnostic verifies the analytic target difference to numerical precision, and learned-critic diagnostics show a large optimistic shift under naive handling while CVT remains approximately aligned with the uncut critic. CVT applies standard continuation bootstrapping rather than a new Bellman rule; the contribution is the controlled benchmark, failure isolation, and cross-learner evidence that administrative segmentation can materially change multi-step offline GCRL.


## 精读解读（中文）
### 一、研究动机
离线目标条件强化学习（GCRL）常利用轨迹结构进行未来目标采样和多步目标构建，但日志轨迹可能因管理原因（如时间限制、存储限制、工作者重启）被分割，这些分割边界并不对应真实终止。将这种行政性截断误当作吸收态会移除多步目标中的延续价值，而现有研究未在固定转移、源轨迹、目标采样、优化设置和评估的条件下，隔离任意分割对离线GCRL性能的影响。因此需要一种受控的压力测试来检验分割不变性，并区分源轨迹边界与人工备份边界。

### 二、技术方案（Method）
提出SegBench-GC协议：固定转移元组、源轨迹、未来目标采样、优化设置和评估，仅改变人工备份边界（b）及其是否保留延续价值。引入延续有效目标（CVT）：在人工截断处，奖励累加停止，但目标从存储的后继状态引导（y_CVT = sum γ^i r + γ^k V(s_{t+k},g)）；朴素人工终止处理则将该延续置零（y_naive = sum γ^i r）。主要测试对象为基于IQL风格的多步GCRL学习器，使用双critic和水平索引的价值头（horizons {1,2,4,8}），actor采用固定soft mixture；对照包括单步GCIQL作为阴性对照，以及独立发布的Decoupled Q-Chunking代码库中的n步（n=25）基线。实验在PointMaze Medium Stitch上进行，每个优化种子使用三种独立分割实现，各含35,000个人工截断；在Puzzle-4x5上进行独立验证。训练100k或250k更新，评估五个固定任务的成功率，并采用配对聚合和描述性标准差。

### 三、结果（Result）
在PointMaze匹配计数研究中，未分割原始条件最终50集每任务成功率为50.5%，CVT为39.1%，朴素人工终止处理仅19.1%。朴素处理相比CVT平均成功率降低20.0个百分点，分割离散度从3.4增至13.6。三种分割实现下，朴素平均成功率范围从4.8%到31.9%，而CVT为39.6%左右。独立发布的n=25基线在Puzzle-4x5上复现相同失败：未分割47.2%，CVT 58.5%，朴素0.27%。目标级诊断确认y_naive - y_CVT = -γ^k V(s_{t+k},g)的数值残差最大3.8e-6，朴素目标在99.8%受影响槽位上向上偏移；学习critic诊断显示朴素处理下值预测平均偏移+15.54，Q预测+15.84，而CVT与原始几乎一致。阴性对照单步GCIQL完全不变。

### 四、结论（Conclusion）
SegBench-GC表明，将人工非终止截断视为吸收态会显著降低多步离线GCRL性能，并使结果对任意分割实现高度敏感；CVT作为延续一致的控制能保持大部分性能。该失败模式通过目标级和critic级机制诊断得到解释，并在独立的多步基线中复现。方法学启示是：多步离线RL应明确边界语义，并在序列边界参与目标构建时测试对良性重分割的敏感性。CVT不是新的Bellman规则，而是标准非终止截断语义的延续一致控制。

### 五、方法论与关键技术细节
关键细节包括：人工截断仅插入具有有效存储后继的非终止位置，源轨迹边界保持固定且延续有效；CVT在人工截断处保留延续引导，而朴素处理将延续置零；主要实验使用35,000个人工截断，三个分割实现（种子101,102,103）和三个优化种子（0,1,2），点迷宫目标混合为当前/未来/随机概率0.2/0.5/0.3，actor目标混合0.5/0.5；超参：三层512单元GELU、层归一化、expectile 0.9、批量1024、学习率3e-4、折扣0.99、DDPG+BC系数0.003、目标更新系数0.005；独立验证使用DQC的NS配置（policy chunk size 1, backup horizon 25, no chunk critic, mean Q aggregation, expectile distillation, quantile implicit backup, κ_b=0.7, batch size 4096, 250k updates）。局限性：CVT要求人工截断的后继属于同一连续过程，不能跨真实重置或缺失数据；实验仅三个种子，标准差为描述性而非推断性；CVT未达到完全不变性（在PointMaze上平均分割差距11.4个百分点）。
