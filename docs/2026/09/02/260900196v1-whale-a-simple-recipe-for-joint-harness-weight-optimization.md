# WHALE: A Simple Recipe for Joint Harness-Weight Optimization

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Haechan Kim, Yoonho Lee, Gisang Lee, Chelsea Finn, Kangwook Lee
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00196v1) · [PDF](https://arxiv.org/pdf/2609.00196v1)

## TLDR
WHALE alternates between model weight fine-tuning and executable harness code search to jointly optimize both components, outperforming weight-only, harness-only, and staged baselines across search QA, math reasoning, and chess puzzle agent benchmarks.

## Abstract
Agent performance depends jointly on the model parameters and the executable harness code that manages context and control flow. Optimizing either component in isolation can leave the system bottlenecked by its frozen counterpart: weight updates can change which harness is effective, while harness updates can change which model capabilities are exposed. Existing joint-adaptation methods optimize weights and textual prompts but leave the broader harness fixed. We propose Weight-Harness Alternating LEarning (WHALE), a simple recipe that alternates two phases: updating the model under the current harness, then searching for a better harness under the updated model. We instantiate these two phases with online rejection-sampling fine-tuning and Meta-Harness, respectively. When to switch is a key design choice: to separate real improvements from noise without over-optimizing against a changing counterpart, WHALE uses either fixed phase durations or an adaptive patience rule over training signals. Using Qwen3.5-2B/4B agents across three domains (search question answering, mathematical reasoning, and chess puzzles), WHALE outperforms weight-only, harness-only, and Fast-Slow Training by 4.15-24.38 percentage points in best mean@8 accuracy. Either component can be the bottleneck: harness search matches peak weight-only accuracy with far fewer rollouts in SearchQA, but improves math accuracy only after a weight update. Small interleaved updates also outperform stagewise weight-then-harness optimization in accuracy and rollout cost. The code is available at https://github.com/krafton-ai/WHALE.


## 精读解读（中文）
### 一、研究动机
智能体的表现同时取决于模型参数与可执行的任务编排代码（harness），而单独优化其中任意一个都可能因另一方固定而受到瓶颈制约。现有的联合优化方法只同时调整权重与文本提示，却将更广泛的harness视为固定不变，难以充分挖掘系统潜能。

### 二、技术方案（Method）
提出WHALE（Weight-Harness Alternating LEarning），一种简单有效的交替学习方案。它交替执行两个阶段：先在当前harness下对模型进行在线拒绝采样微调，再在更新后的模型上利用Meta-Harness搜索更优的harness。两个阶段之间的切换策略是关键设计选择，既要用以区分真实改进与噪声，又要避免对不断变化的另一组件过度优化，因此采用固定阶段时长或基于训练信号的自适应耐心规则来决定何时切换。

### 三、结果（Result）
在Qwen3.5-2B与Qwen3.5-4B智能体上，覆盖搜索问答、数学推理与国际象棋谜题三个领域，WHALE的最佳mean@8准确率比仅优化权重、仅优化harness以及Fast-Slow Training基线高出4.15至24.38个百分点。实验还显示两个组件都可能成为瓶颈：在SearchQA中harness搜索可以用远少于权重更新的rollout达到峰值权重优化准确率，而数学准确率只有在权重更新之后才能被harness搜索进一步提升。

### 四、结论（Conclusion）
结果表明，权重与harness的联合、交替优化能显著优于单独优化和传统分阶段优化，WHALE是一种有效且简单的联合优化方案。交错的小步更新在准确率和rollout成本上都优于先权重后harness的分阶段流程，说明两者需要协同考虑。

### 五、方法论与关键技术细节
关键细节包括：权重更新阶段采用在线拒绝采样微调，利用当前模型生成样本并筛选正确或高分样本进行训练；harness搜索阶段使用Meta-Harness，在更新后的模型上搜索可执行代码形式的上下文与控制流。切换策略可选择固定阶段长度或根据验证信号的自适应耐心规则。实验使用Qwen3.5-2B与Qwen3.5-4B模型，评估指标为mean@8准确率。不同任务上harness与权重更新的收益并不对称，提示需要根据训练信号判断切换时机。
