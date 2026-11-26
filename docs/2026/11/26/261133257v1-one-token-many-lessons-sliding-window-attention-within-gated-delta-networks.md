# One Token, Many Lessons: Sliding-Window Attention within Gated Delta Networks

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yuchen Song, Yangbin Chen
- 机构：Xi'an Jiaotong-Liverpool University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.33257v1) · [PDF](https://arxiv.org/pdf/2611.33257v1)

## TLDR
The paper proposes Sliding-Window Gated DeltaNet (SWGDN), which replaces short convolutions in Delta-Rule linear attention with sliding-window attention for content-dependent local mixing of queries, keys, and values—improving key–value learning-pair construction and benchmark performance while preserving the original recurrent update rules and chunkwise parallel algorithms.

## Abstract
Linear attention compresses historical context into a fixed-size recurrent state, reducing the computational and memory costs of long-sequence modeling. From the perspective of test-time regression (TTR), the state matrix can be viewed as an online-learned regression model, where keys and values serve as inputs and targets respectively, and queries are used to read from the model. From this perspective, the effectiveness of state learning depends not only on the update rule but also on how the key-value learning pairs used for state updates are constructed. While existing work has largely focused on how the state is updated and organized, we investigate how the learning pairs used for state updates are constructed. To this end, we propose Sliding-Window Gated DeltaNet (SWGDN), which replaces short convolutions in Delta-Rule linear attention with sliding-window attention to perform content-dependent local aggregation of projected queries, keys, and values. Our experiments show that SWGDN makes the key-value pairs used in consecutive updates more similar in both GDN2 and KDA. In SWGDN, carrying information from the same token across updates can help the recurrent state reinforce a previously learned association. The local mixing strategy can be incorporated into any Delta-Rule-based linear attention architecture without changing its state update equations or chunkwise parallel algorithms. We apply this strategy to two Delta-Rule variants, GDN2 and KDA, and experimental results demonstrate that SWGDN outperforms the original Delta-Rule baseline across multiple benchmarks.


## 精读解读（中文）
### 一、研究动机
线性注意力将历史上下文压缩到固定大小的循环状态中，以降低长序列建模的计算与内存开销；从测试时回归（TTR）视角看，状态矩阵是在线学习的回归模型，键和值分别作为输入与目标，查询用于读取。已有工作主要关注状态如何更新与组织，却较少研究用于状态更新的键–值学习对如何构造。作者指出，Delta-Rule 线性注意力中更新前的短卷积使用固定相对位置系数，无法根据当前局部窗口内容自适应地构造查询、键和值，因此希望在保持原始循环更新规则与分块并行算法的前提下改进线性注意力。

### 二、技术方案（Method）
SWGDN 将 GDN2/KDA 中作用于投影后 Q、K、V 的短卷积替换为伪查询驱动的滑动窗口注意力。每个头在每个分支（Q、K、V）学习形状为 G×d 的伪查询张量，每个通道组对应一个 d 维伪查询；在因果局部窗口内，三个分支都用同一组投影键作为候选进行打分，伪查询和键先经 RMSNorm 与 RoPE，再计算缩放点积并做 softmax，得到各分支、各组的内容相关混合权重。各分支用自身权重聚合本分支的投影 Q、K、V，经 SiLU 后拼接，混合后的查询用于状态读取，混合后的键和值送入骨干原有的门控 Delta 更新；状态更新方程和 chunkwise 并行算法均不变。作者在窗口大小 W=4（与原短卷积核大小一致）下实现 SWGDN2 与 SWKDA，并比较 G1、G16、G64 等不同通道组粒度。

### 三、结果（Result）
在 340M/15B 规模上，伪查询滑动窗口注意力将权重集中在少数偏移位置：SWKDA-G1 的 Q 分支偏向当前位置，K/V 分支更常选择前一位置；SWGDN2-G1 的 V 分支约有 42% 质量给前一位置。分析表明，SWGDN 使 GDN2 和 KDA 中连续更新所使用的键–值学习对在 K 与 V 表示上更相似；对单一源 token 的干预显示，跨重叠窗口携带同一 token 信息可让后续写入持续降低同一早期关联的残差，表现为近似多步学习。实验上 SWGDN 在多个基准上优于原始 Delta-Rule 基线，且 G1 的共享伪查询组已能获得大部分性能增益。

### 四、结论（Conclusion）
SWGDN 表明，除改进状态更新规则外，构造更合适的键–值学习对也是提升 Delta-Rule 线性注意力的有效方向。由于方法只改变循环更新前的局部混合，不改变状态更新方程和分块并行算法，因此可直接嫁接到任意基于 Delta-Rule 的线性注意力架构并复用现有核。内容相关的局部聚合使重要 token 能在连续窗口中反复参与学习对构造，从而强化已学关联并带来稳定性能提升。

### 五、方法论与关键技术细节
关键实现包括：窗口 W=4 与原短卷积核一致；每个头每个分支学习 G 个伪查询，G=1 时全通道共享权重，G=16/64 时按通道组细化；所有分支复用投影键打分，但各自使用独立 softmax 权重混合 Q、K 或 V；伪查询和键使用 RMSNorm 与 RoPE 以增强窗口内相对偏移敏感性；聚合后经 SiLU。分析使用 340M/15B 最终检查点、160 条 2048 token 验证序列、18 层统计，并只考虑完整窗口；相邻学习对距离在局部混合后、写门之前度量。局限性在于“多步学习”是近似解释，实际学习对、衰减和门控随时间变化，且 K/V 分支权重不一定相同；分析也集中在部分层和设定规模上。
