# Marginal Coverage Credit Reduces Redundant Exploration in Parallel State-Entropy Optimization

- 区域：精读区
- 排名：4
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Junhao Cao, Hongyi Xia, Jianian Wu, Xiaopeng Yi, Lixia Huang, Ping Guo
- 机构：Hunan Applied Technology University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27507v1) · [PDF](https://arxiv.org/pdf/2608.27507v1)

## TLDR
MCC-PGPSE improves parallel state-entropy exploration by redistributing auxiliary intrinsic rewards based on leave-one-policy-out marginal coverage credits, which reduces redundant visitation and promotes complementary state coverage across policies.

## Abstract
Policy Gradient for Parallel State Entropy maximization (PGPSE) expands state-space coverage by training independently parameterized policies in replicated copies of the same environment. However, its pooled team-entropy score measures only collective exploration and cannot identify policies that contribute non-redundant coverage. We introduce Marginal Coverage Credit for PGPSE (MCC-PGPSE), which combines leave-one-policy-out coverage with state-owner specialization to estimate policy-specific credit. MCC-PGPSE preserves PGPSE's pooled objective and redistributes non-negative auxiliary intrinsic rewards according to these credits without changing their total mass. This redistribution is designed to discourage redundant visitation and promote complementary coverage. We evaluated MCC-PGPSE in controlled environments, seven public discrete-state benchmarks, and representative Room and Maze settings from the original PGPSE protocol. Across all tested settings, MCC-PGPSE produced positive final window gains in normalized team state entropy and state support over the Entropy baseline. Controlled-task comparisons and the fixed-suite public aggregate were significant, whereas five-seed original-protocol comparisons were directionally consistent. Ablations and credit alignment controls indicate that most gains arise from leave-one-policy-out coverage rather than non-uniform weighting, mismatched credit, or neural novelty alone. These results support contribution-conditioned auxiliary reward allocation as an interpretable approach to improving complementary coverage among parallel policies in discrete state spaces.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
