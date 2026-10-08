# Bounded Autonomy and Verifiable Safety for Agentic AI Enabled Automation

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Srini Ramaswamy, Deveeshree Nayak
- 机构：DNRS.ai, University of Washington
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08815v1) · [PDF](https://arxiv.org/pdf/2610.08815v1)

## TLDR
The paper presents BRaVeS/DNRS, a bounded governance framework for agentic AI that encodes subject-matter-expert constraints as invariant anchors, monitors epistemic drift to reduce autonomy via SMARtAutonomy, and uses the Lyapunov-Bounded Consensus Framework to enforce shielded convergence or human-mediated intervention in a finite abstraction, with Monte Carlo simulations showing finite-step convergence and no safety-guard violations under stated assumptions.

## Abstract
Agentic AI-enabled automation cannot be safely deployed in high-stakes environments on probabilistic reasoning alone. A recurring risk is epistemic drift: as reasoning deepens, system behavior may move away from subject-matter-expert constraints for safe operation. This paper presents BRaVeS, a bounded reasoning and safety-governance framework termed the Defensible Next-Gen Reasoning System (DNRS). BRaVeS encodes SME-defined constraints as invariant anchors, proposes MoDA-Style (Mixture of Depths Attention) depth-aware access as a candidate mechanism for keeping these anchors visible during inference, and uses a state hierarchy (SMARtAutonomy) to reduce autonomy as epistemic risk increases. To formalize bounded recovery, we introduce the Lyapunov-Bounded Consensus Framework (LBCF), which maps continuous epistemic-risk signals into a finite K-bag abstraction and applies shielded state transitions that enforce Lyapunov-style energy descent or route the system to a human-mediated terminal state. The formal convergence result applies to the finite LBCF abstraction under fixed thresholds and feasible-shield assumptions; it does not prove safety of the full continuous neural activation space. We evaluate the framework through a discrete event Monte Carlo simulation using HAI 22.04 industrial-control-system time-series data with synthetic noise and sensor-degradation regimes. Across the tested parameter-grouping strategies and thresholds, the LBCF process achieved finite-step convergence and no safety-guard violations. These results provide simulation-based evidence that bounded governance behavior can be enforced under the stated abstraction, while motivating future work on deployed transformer implementations, live human-in-the-loop validation, and broader adversarial settings.


## 精读解读（中文）
### 一、研究动机
高风险工业控制、医疗、电网等场景中的自治式AI不能仅依赖概率推理；随着推理加深，系统可能发生认知漂移，使SME定义的安全约束在深层推理中可见性下降，进而导致无依据行动选择和自治失控。因此需要把生成式推理视为受监控轨迹，将SME约束编码为可验证的治理边界，并在认知风险升高时降低或撤销自治权。

### 二、技术方案（Method）
BRaVeS/DNRS将SME规则ℛ_SME表示为(c,τ,p,v)结构化约束元组，经对比自编码器E_CAE编码为低维不变锚点I(X0)，并通过MoDA式深度感知访问将锚点的K0,V0与当前层K_l,V_l拼接为K_mix/V_mix，使后层仍可访问SME约束。推理时计算I(X_l)与I(X0)的发散D_l、基于预测分布与不变参考分布的KL预算B_KL,l及内部假设熵H_l，合成认知风险R_l=λ_D D_l+λ_KL B_KL,l+λ_H H_l；V&V回路将争议潜变量做成Dossier并经授权把I(X0)更新为I(X0)'而不重训底座模型。风险进入模糊SMARtAutonomy挡位（Stable、Meta-Cognitive、Assisted、Regulated Rt）逐步降低权限，并由LBCF将连续风险映射为有限K-bag抽象，使用shielding强制Lyapunov式能量下降或转入人工介导终止态。评估用HAI 22.04 ICS时序数据加合成噪声与传感器退化，在固定阈值和有限K-bag假设下做120,000次离散事件蒙特卡洛仿真，测试不同参数分组策略与阈值。

### 三、结果（Result）
在所有测试的参数分组策略和阈值下，LBCF过程均实现有限步收敛且未出现安全防护违规。该结果是在离散治理抽象与仿真条件下得到的，表明该有限抽象层可执行其收敛和guard规则。形式化收敛结论仅适用于固定阈值和可行shield假设下的有限LBCF抽象，并不证明完整连续神经激活空间的安全性。

### 四、结论（Conclusion）
论文结论是：在明确假设下，BRaVeS/DNRS可将可测认知漂移与显式自治状态转换绑定，实现有界治理行为而非证明模型内在安全。其贡献分离了架构提议、形式化抽象和仿真验证三层，未来需在已部署Transformer、实时人在回路验证及更广对抗场景中检验。该方法不是AGI蓝图，也不适用于无约束、领域无关或纯探索学习。

### 五、方法论与关键技术细节
关键细节包括：SME先验约束是前提，约束元组含语义条件c_i、阈值或谓词τ_i、优先级或严重度p_i、验证权威v_i；anchor维度d_anchor远小于d_model，CAE用于降维并过滤语言噪声；发散度量含稳定项η，KL预算用经验均值与方差μ_KL,l、σ_KL,l及敏感度κ，风险权重λ_D、λ_KL、λ_H需领域校准。MoDA实现上把不变锚点作为Layer 0的KV-cache前k个静态token，路由权重w_i=σ(W_route h_{l-1}+b_route)，超过τ_route走标准块，但无论路由均执行K_mix=[K_l||K0]、V_mix=[V_l||V0]的残差旁路读取；黑盒LLM可改用检索门控、工具路由、动作抑制或外部策略守卫。LBCF在有限K-bag、固定阈值与可行shield下提供有限步收敛保证，但局限是仅仿真、未部署验证、未做实时人在回路与对抗验证，且不覆盖完整连续神经状态或生产级MoDA。
