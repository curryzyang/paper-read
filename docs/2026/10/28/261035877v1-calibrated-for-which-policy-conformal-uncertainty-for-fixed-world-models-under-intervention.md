# Calibrated for Which Policy? Conformal Uncertainty for Fixed World Models Under Intervention

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Ayush Mittal, Dhruv Gupta
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35877v1) · [PDF](https://arxiv.org/pdf/2610.35877v1)

## TLDR
The paper shows that fixed world models under policy intervention must recalibrate uncertainty to the deployment law using weighted conformal prediction with an intervention-induced density ratio, for which it derives coverage guarantees and validates them empirically under controlled policy shifts.

## Abstract
Changing a deployment policy can invalidate a world model's uncertainty while leaving the physical transition mechanism and predictor unchanged. For one-step prediction, if source and target laws share the conditional mechanism $P(Y|X)=Q(Y|X)$, then the intervention is identified by the pre-outcome change of measure $w(X)=dQ_X/dP_X$. For policy-controlled dynamics this ratio factors into state-occupancy and action-propensity terms. Weighted conformal calibration transports marginal coverage to the target law; with an estimated ratio $\hat w$, $P_Q\{Y \in C_{\hat w}(X)\} \ge 1-α-TV(Q,\hat Q) \ge 1-α-E_P|w-\hat w|$. Population log-loss regret for a source-versus-target domain classifier bounds the same ratio error. If $h$ is its clipped target posterior, $ρ$ is the target-domain prior, and $Δ(h)$ is population log-loss regret, then $E_P|w-\hat w_h| \le (1/(ργ))\sqrt{Δ(h)/2}$. An exact cancellation improves the dependence from a generic odds-map bound of order $γ^{-2}$ to $(ργ)^{-1}$. Our experiments use a released DINO-feature world model and physical Franka trajectories. Under the strongest controlled state-action shift, ordinary 90% conformal sets cover 55.0%, whereas oracle and learned-ratio calibration cover 91.0% and 90.9%. The learned surrogate remains within 0.9% total variation of the target law. Calibration is relative to the deployment law: the model can remain fixed while calibration follows the intervention. We machine-check in Lean 4 the finite-support algebraic and causal identities used in the classifier-regret argument, including its coverage-composition step.


## 精读解读（中文）
### 一、研究动机
部署策略变化会在物理转移机制和预测器不变的情况下使世界模型原有的不确定性校准失效，因为状态—动作查询分布已从采集律转向目标律。论文要解决的是固定世界模型在策略干预下如何按部署律而非采集律给出有效覆盖。

### 二、技术方案（Method）
在单步预测且源域与目标域共享条件机制 P(Y|X)=Q(Y|X) 时，用结果前密度比 w(X)=dQ_X/dP_X 识别干预；对策略控制动力学，该比值分解为状态占用比与动作倾向比。若比值未知，则用源/目标协变量训练域分类器得到后验 h，并用裁剪参数 gamma 和目标域先验 rho 构造估计比值，再做加权保形校准：保持世界模型不重训，仅用源域校准分数和测试点权重计算加权分位数。理论部分给出目标律覆盖下界 P_Q{Y in C_w(X)} >= 1-alpha-TV(Q,Qhat) >= 1-alpha-E_P|w-what|，并用分类器的总体对数损失遗憾 Delta_log(h) 控制比值误差 E_P|w-what_h| <= 1/(rho gamma) sqrt(Delta_log(h)/2)。

### 三、结果（Result）
在发布的 DINO 特征世界模型和真实 Franka 轨迹实验中，最强受控状态—动作偏移下，普通 90% 保形集仅覆盖 55.0%，而 oracle 比值校准和学习的比值校准分别达到 91.0% 与 90.9%。学习得到的替代目标分布与目标律的总变差保持在 0.9% 以内，说明估计比值足够接近 oracle 时覆盖恢复接近名义水平。

### 四、结论（Conclusion）
校准必须相对于部署策略定义：世界模型可以固定不变，而校准应随干预引起的查询分布变化而迁移。只要共享条件机制且比值可估，加权保形校准即可把源域覆盖保证输运到目标部署律，并用比值误差显式付出覆盖惩罚。

### 五、方法论与关键技术细节
关键实现是用源/目标域分类器估计结果前密度比，总体对数损失遗憾通过精确测度变换恒等式控制比值误差；裁剪下界 gamma 会影响有效样本量与总变差，从而形成覆盖与方差/稳定性的权衡。实验数据为物理 Franka 轨迹和 DINO 特征世界模型，评估的是单步预测的边际覆盖而非条件覆盖，依赖重叠/绝对连续性与共享条件机制假设。论文还在 Lean 4 中机器检查了有限支撑下的代数与因果恒等式，包括分类器遗憾论证中的覆盖复合步骤；主要局限是单步、边际覆盖、比值估计误差和裁剪带来的保守性。
