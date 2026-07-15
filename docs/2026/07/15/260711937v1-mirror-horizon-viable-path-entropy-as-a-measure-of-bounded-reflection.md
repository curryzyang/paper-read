# Mirror Horizon: Viable Path Entropy as a Measure of Bounded Reflection

- 区域：精读区
- 排名：3
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Tiantian Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11937v1) · [PDF](https://arxiv.org/pdf/2607.11937v1)

## TLDR
This paper introduces Viable Path Entropy (VPE) as a finite-budget measure of verified continuation capacity, demonstrating through language-model reasoning experiments that capability depends on accessible verified continuation modes under bounded reflection rather than on model parameter count.

## Abstract
Mirror Theory proposes that an intelligent system should be studied not only by what it represents, but by what coherent continuations it can sustain under repeated reflection. We make this claim operational through \emph{viable path entropy} (VPE), a finite-budget measure of verified continuation capacity. Given a mirror state, a rollout protocol, a verifier, and a mode map, VPE decomposes bounded capability into two parts: the probability of reaching a viable continuation and the diversity of verified continuation modes reached among successful rollouts. This paper restores the full theoretical scaffold behind the measure: intuition as local underdetermining constraint, taste as invariant-selecting pressure, reflection as taste-guided resolution of underdetermination, and geometry as the learned structure that makes future reflection stable. We then instantiate the theory in language-model reasoning experiments on GSM8K. Across Qwen2.5-Instruct models, 32 sampled rollouts per problem, and two reflection horizons, increasing the token budget from 96 to 160 substantially expands verified reachability, reduces zero-reachability, increases verified-mode entropy, and improves smoothed VPE. At 160 tokens, Qwen2.5-1.5B realizes the strongest mirror horizon among the tested models, even though Qwen2.5-3B has more parameters. This shows that mirror horizon is not parameter count, but accessible verified continuation capacity under a bounded reflection protocol. The result supports Mirror Theory as a measure-level account: capability is the structure of viable continuations made reachable, not merely one-shot accuracy or pass@k.


## 精读解读（中文）
### 一、研究动机
现有评估指标如loss、accuracy、pass@k将模型能力压缩为单一结果统计，忽略了内部结构差异。Mirror Theory主张智能系统应通过重复反思下能维持的连贯延续来研究，因此需要一个可操作测量有界反思下已验证延续容量的方法。

### 二、技术方案（Method）
定义可行路径熵(VPE)，给定镜面状态、rollout协议、验证器和模式映射，分解为已验证可达性概率和已验证模式多样性熵。实验在GSM8K上使用Qwen2.5-Instruct模型（0.5B、1.5B、3B），每问题32条rollout，温度0.7，top-p 0.9，比较96和160最大新token两个反射预算。验证器通过正则提取最终数字并与标准答案比较，模式映射基于长度、操作符、方程计数和推理风格分组。

### 三、结果（Result）
增加token预算从96到160显著扩大验证可达性（Qwen2.5-1.5B验证概率提升0.160，pass@32提升0.300），降低零可达性（下降0.300），提高验证模式熵（上升0.387）和平滑VPE（改善1.412 nats）。160 tokens下，Qwen2.5-1.5B在所有指标上优于0.5B和3B（3B验证概率高于0.5B但pass@32更低，模式熵远低于1.5B），证明镜面视界不依赖于参数数量。

### 四、结论（Conclusion）
结果支持Mirror Theory作为度量级解释：能力是可访问的已验证延续结构，而非一次性准确率或pass@k。镜面视界需分解为可达性和多样性，且受反射协议（预算、验证器、模式映射）调节。更大模型不一定有更大镜面视界。

### 五、方法论与关键技术细节
使用30个GSM8K问题，32条rollout，严格正则验证数字正确性（可能遗漏格式异常解）。模式映射基于启发式特征（长度、运算符、方程计数、推理风格），未使用语义聚类。VPE依赖于协议（rollout数量、token预算、验证器、模式映射），不能作为模型内在标量。局限性：简单验证器可能低估有效延续；模式映射粗粒度；采样数有限（32）。
