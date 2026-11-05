# C-GRPO: Conformal Group Relative Policy Optimization

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Arya Fayyazi, Seyedarmin Azizi, Mehdi Kamal, Massoud Pedram
- 机构：University of Southern California
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05591v1) · [PDF](https://arxiv.org/pdf/2611.05591v1)

## TLDR
C-GRPO replaces GRPO’s fixed rollout budget with calibrated conformal stopping thresholds that adaptively allocate more rollouts to hard prompts and fewer to easy ones, providing finite-sample coverage guarantees while reducing training rollouts by 49–70% without sacrificing accuracy.

## Abstract
Reasoning-oriented language model training increasingly relies on multiple on-policy rollouts, but standard Group Relative Policy Optimization (GRPO) uses a fixed group size, wasting compute on easy prompts and under-exploring hard ones. Existing adaptive-budget methods alleviate this inefficiency, yet their stopping rules are heuristic and do not provide a finite-sample calibration guarantee. We propose CGRPO, which replaces the fixed rollout budget of standard GPRO with calibrated conformal thresholds over task-specific nonconformity scores, combining Adaptive Prediction Set (APS)-style calibration for closed-form reasoning, a first-success score for execution-based code, automatic miscoverage selection, and periodic re-calibration. We prove finite-sample coverage for the resulting stopping rule and show that, under monotone policy improvement, recalibration induces a non-increasing expected training budget. Across six benchmarks spanning mathematics, graduate-level science, and code generation, CGRPO reduces mean training rollouts by 49-70% relative to fixed-budget GRPO while retaining strong fixed-budget accuracy, achieves the strongest pass@1 among evaluated static and dynamic baselines on different datasets, and transfers across model families with up to 82% rollout savings.


## 精读解读（中文）
### 一、研究动机
标准GRPO对每个提示使用固定组大小，导致简单题浪费 rollout、困难题探索不足；已有自适应预算方法多依赖启发式停止规则，缺乏随策略演化仍成立的有限样本校准保证。C-GRPO的动机是把自适应组大小构造为训练期共形校准问题，在保持准确率的同时将算力重新分配给困难样本。

### 二、技术方案（Method）
C-GRPO在固定预算网格上为每个预算k维护共形阈值，使用与训练集不相交的校准集和每个查询K_max次采样计算任务特定非一致性分数；闭式数学与科学题采用带随机化分数质量和随机打破并列的APS分数，代码执行题采用首个成功样本位置j*/k作为first-success分数。对每个k用分裂共形分位数ceil((n+1)(1-delta))计算阈值qhat_k，并加入自动miscoverage选择与周期性重校准以跟踪策略改进。训练时对每个提示从最小预算开始采样，当非一致性分数不超过对应校准阈值时停止并构造自适应组，再用该组计算GRPO相对优势并更新策略；整体无需显式约束优化，校准阈值隐式决定每步计算预算。

### 三、结果（Result）
在覆盖数学、研究生级科学和代码生成的六个基准上，C-GRPO相对固定预算GRPO将平均训练rollout减少49%至70%，同时保持强固定预算准确率。在GSM8K、HumanEval、MBPP和MATH-500上，其pass@1等于或略高于所评估的静态与动态基线，差异处于二项噪声范围内，且每个提示所需rollout最少；在Llama-3.1-8B上GSM8K无需重新调参即可达到最高82%的rollout节省。

### 四、结论（Conclusion）
C-GRPO表明共形预测可作为训练期计算控制机制，而不仅是推理后处理工具，为自适应组大小提供有限样本覆盖与错误停止控制。理论上给出每个预算下的false-stop控制、在多重性校正下自适应选择预算的同时覆盖保证，并在单调策略改进的理想条件下推出重校准使期望训练预算非增；实验上形成简单题早停、困难题保留算力的自步课程。

### 五、方法论与关键技术细节
关键实现包括独立校准集、预算网格、K_max次采样、delta选择、共形分位数有限样本校正以及定期重校准；APS的随机化分数保证连续性并带来精确边际覆盖，first-success分数在代码任务中避免因答案字符串唯一而导致APS退化。理论保证依赖样本可交换性，自适应预算的同时覆盖需多重性校正，单调策略改进下预算非增是理想化条件而非无条件结论；自动delta用于避免训练早期阈值退化。该方法不显式求解目标计算约束C，而是通过校准阈值间接控制每查询预算，实际节省幅度受校准集规模、预算网格粒度、任务验证器可靠性和策略演化漂移影响。
