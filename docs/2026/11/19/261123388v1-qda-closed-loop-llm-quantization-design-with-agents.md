# QDA: Closed-Loop LLM Quantization Design with Agents

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Xingyang Li, Tianlang Zhao, Song Han, Ligeng Zhu
- 机构：NVIDIA, MIT
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23388v1) · [PDF](https://arxiv.org/pdf/2611.23388v1)

## TLDR
QDA is a closed-loop system in which an LLM agent automatically designs per-model and per-precision quantization recipes, using a fast KL-divergence proxy and a unified PTQ library to find recipes that outperform the strongest public baselines without adding inference overhead.

## Abstract
Post-training quantization is the standard way to serve large language models at low cost. However, the best quantization recipe differs across models and precisions. As a result, experts must redesign it for every new model, which is time-consuming and often sub-optimal. Fortunately, an LLM agent can take over this design by refining the recipe over rounds of building and evaluating candidates, so that more rounds lead to better recipes. However, evaluating one quantized reasoning model takes tens of GPU-hours, and combining methods from different codebases means porting each to the new architecture by hand. We present QDA, a system in which an agent designs the recipe for each model and precision. To make evaluation fast, QDA scores each candidate in minutes by its output KL divergence from the original model on reasoning traces that the agent never sees, and checks promising ones with long generations to catch failures such as repetition loops. To make building fast, QDA provides a library of public PTQ methods that are compatible with one another and with new model architectures. Across four reasoning models, QDA improves accuracy over the strongest public recipe by 0.9, 1.4 and 2.2 percentage points on average at W4A16, W4A8 and W3A16, using 64 GPU-hours per search. On the 320B-parameter MoE model GLM-5.3-Flash at NVFP4 W4A4, it recovers 98.3% of the FP8 model's accuracy, against 96.9% for the best vendor checkpoint. Every QDA checkpoint also runs on existing serving kernels with no inference overhead. We will release the library, the evaluator and the harness.


## 精读解读（中文）
### 一、研究动机
大语言模型（尤其是长链推理模型）部署成本高，后训练量化（PTQ）是标准降本手段，但最优量化配方会随模型和精度变化而不同，公开配方无法直接迁移，专家需为每个新模型和新精度手工设计，耗时且常非最优。现有 LLM 编码智能体可通过多轮构建与评估候选来接管配方设计，但完整评估一个量化推理模型需数十 GPU 小时，且跨代码库组合 PTQ 方法需手工移植到新架构，导致搜索难以扩展。

### 二、技术方案（Method）
QDA 将量化配方设计建模为智能体驱动的闭环“构建—评估”搜索：智能体针对给定模型和精度提出由变换、舍入方法、scale 及其调优、校准数据组成的 recipe，并调用统一 PTQ 库中 21 种可互相兼容、输入输出均为量化 checkpoint 的方法按任意顺序堆叠构建候选。为加速评估，QDA 在原始模型生成的参考推理轨迹上计算候选与原始模型下一 token 分布的 KL 散度，并缓存原始分布，使单候选评分缩短到分钟级；对高分候选再执行长文本生成检查，以捕捉重复循环等罕见失败。搜索由 harness 自动运行，并将测试基准和参考轨迹对智能体隔离，防止过拟合或污染。

### 三、结果（Result）
在四个推理模型（覆盖稠密 Transformer、线性注意力混合架构和 MoE）上，QDA 在 W4A16、W4A8、W3A16 下相对最强公开配方平均提升 0.9、1.4、2.2 个百分点，每次搜索约用 64 GPU 小时。在 320B 参数 MoE 模型 GLM-5.3-Flash 的 NVFP4 W4A4 上，单次 6.5 小时搜索恢复 FP8 模型 98.3% 的准确率，高于最佳厂商 checkpoint 的 96.9%；在相同库和预算下，QDA 比贪心搜索和 ASHA 在 W4A8/W3A16 上最多高 1.2 个百分点，且优于使用 ModelOpt 配方搜索技能的智能体 0.5–1.3 个百分点。所有 QDA checkpoint 均可直接运行在现有 serving kernel 上，无额外推理开销。

### 四、结论（Conclusion）
QDA 表明，LLM 智能体可以通过闭环配方搜索，在有限 GPU 预算下为不同模型和精度自动设计出优于强公开配方的 PTQ recipe，并生成可直接部署、无推理开销的量化 checkpoint。该工作为快速到达的新模型提供了一种可扩展的量化设计范式，降低了对手工专家配方和逐模型移植的依赖。

### 五、方法论与关键技术细节
关键实现包括：以原始模型在推理轨迹上的下一 token 分布 KL 散度作为快速代理指标，并缓存原始分布，官方称比完整评估便宜 350–990 倍；代理指标之外增加长生成验证以发现重复循环等失败，但代理指标仍可能漏检罕见失败。统一库覆盖 21 种 PTQ 方法并支持 checkpoint-to-checkpoint 堆叠，配方空间受库覆盖范围约束；测试基准与参考轨迹对智能体隐藏，以避免污染。搜索预算为每次约 64 GPU 小时，GLM-5.3-Flash 单次搜索为 6.5 小时；方法支持 W4A16、W4A8、W3A16 和 NVFP4 W4A4，并保持与现有 serving kernel 兼容。
