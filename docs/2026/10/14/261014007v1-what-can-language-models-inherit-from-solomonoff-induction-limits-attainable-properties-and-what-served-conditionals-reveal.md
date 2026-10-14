# What Can Language Models Inherit from Solomonoff Induction? Limits, Attainable Properties, and What Served Conditionals Reveal

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Luan Ozelim, Abicumaran Uthamacumaran, Hector Zenil
- 机构：King's College London, Oxford Immune Algorithmics
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.14007v1) · [PDF](https://arxiv.org/pdf/2610.14007v1)

## TLDR
This paper argues that language models cannot uniformly inherit Solomonoff induction’s universal predictive guarantees—since every computable model has cheap environments it never learns and scale yields only pointwise approximation—and recasts their success as a Kraft-inequality budget of where limited predictive competence is spent, clarifying which Solomonoff-like properties are attainable, certifiable, or should be avoided.

## Abstract
A familiar line of reasoning runs as follows: language models are flexible approximators trained under a strictly proper loss, so scale brings them closer to Solomonoff induction, and their predictive success is evidence of that approach. We apply known results from algorithmic information theory, universal prediction and Bayesian consistency. In its uniform form the conclusion holds for no computable model: each has cheap environments it never learns, and every uniformly computable family of total predictors shares one on which each member fails beyond a horizon growing with its index, so ``closer'' can hold only pointwise, one environment at a time. Nor could the offered routes certify even that: finite evaluation cannot certify agreement on rarely reached contexts, perfect corpus fit selects the corpus law as prior, and asymptotic criteria cannot see the constants that carry Solomonoff's guarantee. Our lens is the Kraft inequality read for predictors. Every model has at most the same budget of predictive success, so Solomonoff's predictor, which leaves part of it unspent, differs from a language model not in having more of it but in where it spends it; on mutually singular families this is exact, and only full-mass Bayes mixtures reach the frontier. We then discuss what is inheritable, including in-context learning as amortised Bayesian inference; what survives within a context window; which Solomonoff-like properties a deployed system should have or avoid; and what served conditionals determine. A closing table states what common practices certify and what to report. Tests are developed in a companion paper.


## 精读解读（中文）
### 一、研究动机
论文针对一种常见论证：语言模型作为灵活逼近器在严格 proper 损失下训练，规模扩大会使其逼近 Solomonoff 归纳，预测成功即为此提供证据。作者要把这个强命题拆成可检验的理论边界，区分哪些性质可继承、哪些不可继承，并说明常用评估与训练证据究竟能证明什么。

### 二、技术方案（Method）
方法上把语言模型或一般预测器形式化为对上下文给出条件分布的半测度或概率测度，以对数损失、regret、excess loss 和 Solomonoff 混合预测器为基准；再用算法信息论、通用预测与贝叶斯一致性中的已知结果（Putnam/Legg 对角化、Kraft 不等式、Bayes mixture 前沿）建立统一分析框架。关键操作是把任何预测器的累积对数损失能力视为固定预算，比较其在不同环境上的分配，并分节讨论评估、规模、数据闭包、继承性、渐近性质、部署、性质排序和测量；作者自身不做语言模型实验，数值示例由脚本生成，测试留给 companion paper。

### 三、结果（Result）
核心结论是：命题 (C) 的均匀形式对任何可计算模型都不成立，每个模型都有复杂度不高于自身的廉价环境使其永不学会；任何一致可计算的总预测器族也共享一个环境，使各成员在随索引增长的 horizon 之后失败，因此向 Solomonoff 的“更接近”只能在逐点、逐个环境意义上成立。有限评测无法认证稀有上下文上的一致性，完美拟合语料等于把语料律选为先验，渐近一致性或合并等准则看不见承载 Solomonoff 保证的常数；Kraft 透镜表明所有预测器最多拥有同样多的预测成功预算，Solomonoff 的差别在于花在哪里，且在互奇异族上只有全质量 Bayes 混合达到前沿。可继承的部分包括在声明类上用 Bayes 混合达到 Solomonoff 型保证、把 in-context learning 解释为摊销贝叶斯推断，以及在上下文窗口、部署约束和 served conditionals 中可测量的内容。

### 四、结论（Conclusion）
因此，规模、压缩效率、基准提升和元学习 regret 下降都不能 certify 语言模型在均匀意义上逼近 Solomonoff 归纳；它们至多说明在特定语料、先验、测试分布或 horizon 上的分配表现。论文主张把问题从“是否更接近”转为“在声明类上分配哪些预算、报告哪些先验与常数、部署时保留或避免哪些 Solomonoff 式性质”，并建议可信系统应具有 Solomonoff 式信念但采用非 Solomonoff 式约束。

### 五、方法论与关键技术细节
关键细节包括：对数损失以 2 为底，regret 按源期望的 KL 累积定义，Solomonoff 对任意可计算 q 的超出至多 K(q)+O(1) 位；对角环境每步损失 log V（实值条件为 log(2V/3)）而 Solomonoff 只付常数；零 regret 于语料意味着与语料律重合，仅在绝对连续源上有有限 regret，受 c 支配时至多 log c。Kraft 预算给出长度 n 下最多 2^b 个字符串累积 log-loss 低于 b 位；示例称在约 2 bits/token、16-bit 权重、每参数至少 10^3 token 时，K(q)+O(1) 可低于语料编码长度 1%。局限是讨论性论文、多数结果已知、未测量具体语言模型，结论多为理想化预测器的点态或声明类性质，渐近准则对先验和常数不敏感，链式思考、工具或检索、上下文窗口、温度、截断和 tokenisation 等部署因素需单独处理。
