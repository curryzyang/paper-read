# NeuronFuzz: Safety Neuron Guided Fuzzing for LLM Safety Evaluation

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Zhiyuan Xu, Muhammad Firhard Roslan, Joseph Gardiner, Sana Belguith, Lichao Wu
- 机构：University of Bristol
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.26222v1) · [PDF](https://arxiv.org/pdf/2608.26222v1)

## TLDR
NeuronFuzz is a white-box fuzzing framework that replaces expensive response-level feedback with continuous, prefill-time safety-neuron activations (via a differentiable SafetyOracle) to guide gradient-based mutation and efficiently discover jailbreak templates across diverse LLMs, achieving high jailbreak rates and cross-model transfer.

## Abstract
Safety evaluation is critical for assessing whether aligned Large Language Models (LLMs) remain robust against jailbreak attacks. Existing automated testing methods, however, largely rely on response-level feedback: each candidate prompt typically requires generating a target-model response to evaluate its attack effectiveness. This process is expensive and, more importantly, provides only sparse guidance on strongly aligned models, where most candidates are rejected with the same failure outcome.
  This paper presents NeuronFuzz, a white-box fuzzing framework that exploits internal safety neurons as continuous execution feedback for LLM safety evaluation. A SafetyOracle converts safety-neuron activations into a continuous safety alarm score that serves as feedback for fuzzing and can be obtained during prefill, eliminating response generation from the fuzzing loop. To construct the SafetyOracle, NeuronFuzz uses template-invariant harmful and benign inputs and stability-aware selection to identify a compact set of safety neurons whose activations capture harmful-intent recognition. Moreover, since the safety alarm score is differentiable, NeuronFuzz uses its gradients to identify safety-sensitive template positions and a masked language model to generate fluent, context-compatible mutations while preserving original harmful payload and avoiding additional optimization variables. We evaluate NeuronFuzz across 21 text and multimodal models. Across five white-box source models, it achieves a 76-100% jailbreak discovery rate, outperforming baselines by up to 48 percentage points. Its optimized templates further transfer zero-shot to open-weight and six proprietary target models, achieving average ASR and top-5 ensemble ASR (EASR) of 69.6%/92.6% and 44.1%/60.0%, respectively.


## 精读解读（中文）
### 一、研究动机
现有LLM安全测试的自动化方法大多依赖响应级反馈，每个候选提示都要生成目标模型响应才能评估，成本高且对强对齐模型反馈稀疏，导致难以区分同样被拒绝的候选。因此需要一种能在预填充阶段获得、且能提供连续信号的内部反馈来指导模糊测试。

### 二、技术方案（Method）
NeuronFuzz构建SafetyOracle作为反馈信号：首先构造模板不变的有害/良性输入对（同一模板配不同安全性载荷），在预填充阶段用前向钩子收集所有Transformer MLP块的gate和up投影激活，经最大池化后拼接成提示级表示；然后通过B次bootstrap稳定性选择，每轮拟合线性分类器并按系数绝对值保留每块sqrt(p)个神经元，筛选出选择率高、符号一致且正向主导的紧凑安全神经元集；训练轻量分类器将这些神经元激活映射为连续安全警报分数。模糊测试循环中，该分数在prefill阶段即可获得，无需生成响应；同时利用分数的梯度定位安全敏感的模板位置，用掩码语言模型生成流畅且上下文兼容的替换词，保持原有有害载荷不变，并据此迭代变异与选择候选。

### 三、结果（Result）
在21个文本和多模态模型上的评估中，NeuronFuzz在5个白盒源模型上实现76%-100%的越狱发现率，比基线最高提升48个百分点；优化后的模板零样本迁移到开源和6个专有目标模型，开源模型平均ASR/EASR为69.6%/92.6%，专有模型为44.1%/60.0%。

### 四、结论（Conclusion）
NeuronFuzz证明了将内部安全神经元作为模糊测试反馈的有效性，以预填充阶段可获得的连续信号替代昂贵稀疏的响应级反馈，显著提高了越狱模板的发现效率与迁移能力，为LLM安全评估提供了一种高效的新范式。

### 五、方法论与关键技术细节
关键细节包括：使用模板不变的有害/良性对消除模板风格干扰；神经元候选来自MLP的gate和up投影并做max-pooling；稳定性选择采用B次bootstrap，每轮保留q_l=ceil(sqrt(p_l))个最大绝对系数神经元，并要求选择率s_j与符号一致性c_j超过阈值且正系数占优；梯度引导突变仅修改模板位置，保留有害载荷；SafetyOracle在prefill阶段计算，避免了自回归解码开销。局限性在于构建SafetyOracle需要白盒访问一个源模型（或代理模型），并且超参数τ_s、τ_c需根据模型调整。
