# OMP-MoE: Efficient Expert Pruning for Mixture-of-Experts LLMs via Orthogonal Matching Pursuit

- 区域：精读区
- 排名：10
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Dezhi Li, Lujun Li, Qiyuan Zhu, Hao Gu, Bei Liu, Sirui Han, Yike Guo
- 机构：The Hong Kong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31631v1) · [PDF](https://arxiv.org/pdf/2609.31631v1)

## TLDR
OMP-MoE is a training-free expert-pruning framework for Mixture-of-Experts LLMs that reformulates expert selection as sparse signal reconstruction solved by Orthogonal Matching Pursuit, adds water-filling cross-layer budget allocation and energy-based adaptive inference, and achieves superior performance retention with faster search and inference at 25–50% pruning ratios.

## Abstract
Mixture-of-Experts (MoE) models enable efficient scaling of large language models but face critical deployment challenges due to massive memory requirements. Existing pruning methods either incur prohibitive search costs or neglect the dynamic interdependencies between experts. To address these challenges, we present OMP-MoE, a novel training-free compression framework for reducing expert redundancy in MoE-based LLMs. Based on observations of expert contribution patterns, we reformulate the pruning problem as a sparse signal reconstruction task solved through Orthogonal Matching Pursuit. Specifically, our method first treats individual expert contributions as dictionary atoms and selects experts that greedily minimize reconstruction error with linear computational complexity. Then, we optimize cross-layer expert allocation through a water-filling strategy that accounts for both reconstruction quality and routing stability. Finally, we introduce OMP-MoE†, an adaptive inference mechanism that dynamically adjusts expert activation based on energy prediction. Comprehensive experiments on Qwen, DeepSeek-V2, GPT-OSS, and Mixtral MoE demonstrate consistent improvements over existing methods at 25-50% pruning ratios. For Qwen3-30B-A3B at 50% compression, we retain 93.3% of original performance, achieving 33$\times$ faster search and 1.55$\times$ inference speedup. Codes will be available after acceptance.


## 精读解读（中文）
### 一、研究动机
MoE大模型虽能稀疏激活实现高效扩展，但部署时面临巨大内存开销；现有专家合并/剪枝方法要么搜索代价过高，要么忽略专家间动态依赖。作者观察到不同层的残差衰减速率不同、专家重要性会随已选专家变化，因此需要一种训练无关、快速且能保持性能的专家剪枝框架。

### 二、技术方案（Method）
OMP-MoE将专家剪枝重写为稀疏信号重构：把每个专家加权贡献V_e视为字典原子，目标是用少量保留专家重构MoE层输出Y，系数约束为二值。方法先做一次前向统计缓存Y与V_e，再用正交匹配追踪贪心迭代选择最大化重构增益Δ_e = 2⟨R_t,V_e⟩ - ‖V_e‖_F^2的专家并更新残差；随后用注水策略跨层分配专家预算，联合优化归一化重构误差与路由稳定性风险；最后引入OMP-MoE†，基于能量预测在推理时动态跳过低能量专家。

### 三、结果（Result）
在Qwen、DeepSeek-V2、GPT-OSS和Mixtral等MoE模型上，25%至50%剪枝比例下OMP-MoE一致优于现有方法。以Qwen3-30B-A3B为例，50%压缩时仍保留93.3%原始性能，同时实现33倍更快的搜索速度和1.55倍推理加速。

### 四、结论（Conclusion）
OMP-MoE把组合搜索转化为线性复杂度的贪心稀疏重构，并通过跨层预算分配和能量感知推理，在训练无关条件下兼顾了专家剪枝的搜索效率、性能保持与部署加速，为现代MoE大模型压缩提供了可扩展方案。

### 五、方法论与关键技术细节
输入为每层展平后的B×T个token表示Y和专家贡献原子V_e；统计阶段仅需一次前向缓存，贪心阶段以Δ_e迭代选择专家，总复杂度为O(L·n·N_e·Bd)，避免组合数C(N_e,n)搜索。跨层分配使用校准集累计路由权重m_l,e并归一化，定义路由覆盖C_l(k)=Σ_t m̃_l,e_l,t与风险ψ_l(k)=-log(C_l(k)+ζ)，层代价F_l(k)=r_l(k)+λψ_l(k)，通过注水法从每层1个专家开始逐步把剩余预算加到边际代价下降最大的层。OMP-MoE†依赖能量预测动态调整专家激活；主要局限包括依赖校准统计数据、路由稳定性建模受校准集代表性影响，且方法聚焦专家保留/跳过而未做权重合并或微调。
