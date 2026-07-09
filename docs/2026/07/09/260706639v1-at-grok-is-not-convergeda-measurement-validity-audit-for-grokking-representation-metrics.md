# At-Grok Is Not Converged:A Measurement-Validity Audit for Grokking Representation Metrics

- 区域：精读区
- 排名：3
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Truong Xuan Khanh
- 机构：H&K Research Studio / Clevix LLC
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06639v1) · [PDF](https://arxiv.org/pdf/2607.06639v1)

## TLDR
This paper demonstrates that representation metrics at the grokking transition are transient and not converged, often overstating the final low-rank structure and lagging behind generalization onset, and provides a measurement-validity audit to separate these phenomena.

## Abstract
On modular arithmetic, a network's embedding keeps compressing for tens of thousands of steps after it has already generalized. Reading effective rank at the grokking transition overstates the converged value by 3-5x on an MLP, and by 1.3-1.5x on a transformer trained to convergence; on the MLP it also erases which cells compress at all. Compression lags the accuracy transition by an amount on the order of the time-to-grok, at least 10,000 steps, rather than coinciding with it. A one-variable ablation shows what sets the lag size: adding LayerNorm to an otherwise identical transformer moves the fraction of compression done by the grok step from 0.87 to 0.25, and a pre-registered control rules out scale invariance as the mechanism. We package this as an audit that separates onset from compression, flags censoring, excludes boundary cells that never fully generalize, and checks that the reference floor has plateaued, with an adversarial suite that caught a false-confidence bug in our own branch. A secondary, MLP-specific depth law linking norm budget to converged floor fails a generality test on a transformer and flips sign under free weight decay. Code and the toolkit are released.


## 精读解读（中文）
### 一、研究动机
在模算术任务中，网络嵌入在泛化后仍持续压缩数万步，但大量研究将grokking转变时的表示度量（如有效秩）直接当作收敛电路的性质，导致高估复杂度（MLP上3-5倍，transformer上1.3-1.5倍）甚至颠倒定性结论。因此需要设计审计方法判断过渡时刻的度量是否收敛，避免测量错误。

### 二、技术方案（Method）
研究以模加法、模乘法及奇偶性为任务，使用MLP和transformer（含/不含LayerNorm），以嵌入有效秩为核心度量。定义grokking时刻T_grok（测试准确率首次超过0.9）和压缩时刻T_compress（有效秩首次稳定在收敛地板附近且地板自身已平台化）。审计流程包括：分离T_grok与T_compress，标记训练不足导致的删失，排除未完全泛化的边界单元（如高norm预算的ρ=1.00单元），验证收敛地板已稳定（防止二次下降）。在clamp和自由权重衰减协议下训练至收敛，并跨norm预算扫描。单变量消融实验对比MLP、无LayerNorm的规范transformer及添加LayerNorm的transformer，量化grok步已完成压缩的比例（frac-pre）。同时设计九种场景的对抗性测试套件验证审计决策的正确性。

### 三、结果（Result）
核心发现：1) 在MLP上，at-grok有效秩高估收敛值3-5倍，且掩盖了压缩单元与非压缩单元的区别（ρ=1.05收敛秩≈12 vs ρ=1.00维持≈42，而grok步两者均≈46-48）。2) 在transformer上，at-grok有效秩高估1.3-1.5倍（嵌入和反嵌入）。3) 压缩滞后于准确率转变，滞后量约等于T_grok（≥10000步）。4) 添加LayerNorm将frac-pre从0.87（规范transformer）降至0.25，显著增大滞后。5) MLP特定的深度定律（norm预算与收敛地板Spearman -1.0）在transformer上失效（Spearman +0.14），且在自由权重衰减下符号翻转。

### 四、结论（Conclusion）
读取grokking过渡时刻的表示度量作为收敛电路的性质是不安全的：该瞬态值高估复杂度且可能颠倒顺序；压缩与泛化开始之间存在普遍滞后，其大小由归一化方案调节。提供的审计工具包（含时钟分离、删失标记、边界门控、地板稳定检查及对抗性测试）可有效避免这些测量陷阱，确保表示解读的正确性。

### 五、方法论与关键技术细节
数据：模加法、乘法、奇偶性任务，使用clamp或自由权重衰减协议。度量：嵌入矩阵的有效秩（主要）、参与比、稳定秩。架构：2层MLP（宽256）、2层transformer（嵌入维度128，4头），有无LayerNorm。训练：Adam优化器，学习率1e-3，批量512，训练步数通常为4e5（远超grokking）。关键参数：norm预算ρ（控制嵌入范数），在clamp协议下为固定值0.7-1.2。审计细节：T_grok定义为测试准确率首次>0.9；T_compress定义为首次进入收敛地板±5%且后续不反弹；地板需在最后10%训练中平台化（否则标记为删失）。边界单元：未达到完全泛化（测试准确率>0.9）或压缩度不足的单元被排除。局限性：深度定律仅在MLP+clamp协议下成立，不泛化到transformer或自由权重衰减；审计对度量选择（有效秩）和任务（模算术）的敏感性需进一步验证。
