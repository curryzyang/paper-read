# Coherent Moment Propagation: Epistemic Uncertainty for Pre-trained Robot Policies

- 区域：精读区
- 排名：3
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Miguel Saavedra-Ruiz, Anqi Li, Claudia D'Arpino, Alperen Degirmenci, Tucker Hermans, Fabio Ramos
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26855v1) · [PDF](https://arxiv.org/pdf/2611.26855v1)

## TLDR
The paper introduces Coherent Moment Propagation (CoMP), a test-time epistemic uncertainty estimator for flow-matching robot policies that propagates state–weight cross-covariance through the ODE solver to correct BayesDiff’s variance collapse and improve failure detection and demonstration selection.

## Abstract
Flow matching policies underpin the state-of-the-art in robot learning, with impressive results ranging from long-horizon planning to dexterous manipulation. However, they provide no measure of whether their predicted commands can be trusted, particularly in novel situations outside their training set. Epistemic uncertainty reflects uncertainty about the model's weights and quantifies this ignorance, but calculating it at inference time from a flow matching policy is not trivial. Actions are produced by an ODE solver, requiring uncertainty to be propagated through the entire integration process. BayesDiff addresses this problem for diffusion models by propagating the mean and variance of the state through the denoising chain under a last-layer Laplace posterior approximation, but it severely underestimates the epistemic uncertainty. In this paper we: i) prove that, for flow matching and diffusion ODEs, BayesDiff's total variance decays at rate $O(1/T)$ as the number of Euler steps $T$ used by the solver increases; ii) introduce Coherent Moment Propagation (CoMP), two recursions inspired by the extended and unscented Kalman filters that fix this problem by carrying the cross-covariance between state and weights; and iii) widen the last-layer posterior with observation embeddings the policy already computes, improving uncertainty estimates without retraining for CoMP and several test-time estimators alike. We demonstrate these benefits on three manipulation benchmarks with applications in failure detection and demonstration selection for fine-tuning, where CoMP corrects BayesDiff's variance collapse while matching or outperforming several uncertainty estimators.


## 精读解读（中文）
### 一、研究动机
Flow matching 策略在机器人学习中表现突出，但推理时无法判断预测动作是否可信，尤其在训练分布外的新情境中。 epistemic uncertainty 可量化模型对权重的无知，但要从 flow matching 策略的 ODE 采样过程中计算并不直接，现有 BayesDiff 对扩散模型会严重低估该不确定性。

### 二、技术方案（Method）
论文先将 flow matching/diffusion ODE 的欧拉积分视为状态转移，在最后一层 Laplace 后验近似下分析动作状态均值与方差传播，并证明 BayesDiff 的总方差随欧拉步数 T 以 O(1/T) 衰减。为此提出 CoMP：用扩展卡尔曼滤波和无迹卡尔曼滤波启发的两条递推，在每步积分中同时传播动作状态均值、方差以及状态与最后一层权重之间的交叉协方差，从而把权重不确定性正确注入最终动作。推理时以观测、采样噪声和策略 ODE 求解器为输入，输出带 epistemic uncertainty 的动作分布；同时用策略已计算的观测嵌入扩宽最后一层后验，CoMP 无需重训练即可使用。

### 三、结果（Result）
理论结果表明，BayesDiff 的方差会随欧拉步数增加而塌缩，衰减率为 O(1/T)，而 CoMP 通过保留状态-权重交叉协方差修正该问题。在三个机器人操作基准上，CoMP 在失败检测和用于微调的示范选择任务中纠正了 BayesDiff 的方差塌缩，并与多种测试时不确定性估计器相当或更优。

### 四、结论（Conclusion）
CoMP 为预训练 flow matching 机器人策略提供了一种推理时可行的 epistemic uncertainty 传播方法，能更可靠地识别不可信动作并服务于失败检测与示范筛选。利用已有观测嵌入扩宽最后一层后验是一种无需重训练的通用增强，可同时改善 CoMP 和多种测试时估计器。

### 五、方法论与关键技术细节
关键实现点包括：采用最后一层 Laplace 后验、欧拉离散 ODE 和状态-权重交叉协方差递推，分别对应 EKF/UKF 风格的两条 CoMP 递归；观测嵌入用于扩宽后验且不引入额外训练；推理需在 T 步积分中传播均值、方差和交叉协方差，计算与存储开销高于单次 ODE。评估覆盖三个操作基准及失败检测、示范选择两个下游应用；局限性是仍依赖最后一层后验、线性化/矩近似和欧拉离散，摘要未报告真实机器人或强非高斯后验下的验证。
