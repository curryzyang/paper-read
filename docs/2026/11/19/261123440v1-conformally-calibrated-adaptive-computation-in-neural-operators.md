# Conformally Calibrated Adaptive Computation in Neural Operators

- 区域：精读区
- 排名：4
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Abdul Qadir Ibrahim, Martin Burger, Abel Maviano Jonathan
- 机构：Deutsches Elektronen-Synchrotron DESY, University of L'Aquila
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23440v1) · [PDF](https://arxiv.org/pdf/2611.23440v1)

## TLDR
Conformal calibration can adapt Fourier modes or channel widths in neural operators to meet an error budget, but measured runtime gains are often absent and calibrated static baselines are frequently as fast or faster with better coverage, so adaptive computation should be judged by achieved coverage and end-to-end runtime against a matched static comparator.

## Abstract
Selecting less computation in a neural operator need not reduce inference time. We study this gap using conformal calibration to choose Fourier modes or channel width per input subject to a fixed error budget. A triangle-inequality envelope bounds all candidates simultaneously; a direct-score rule handles non-monotone candidate errors and, with an input-independent score, calibrates a static baseline under the same marginal guarantee. Under frozen-model and exchangeability assumptions, both rules bound the probability of issuing a prediction outside the budget and abstain when calibration is infeasible. On Burgers and Darcy flow across three training seeds, mode selection reduces active spectral support without a measurable latency reduction, because full-grid transforms and channel mixing dominate the cost. Narrowing channels does reduce Darcy forward cost, but reference-based selection must first compute the dense prediction. An input-only binary width selector avoids that pass and runs at 0.52-0.95 times dense latency; yet static widths calibrated under the same rule are often as fast or faster, and on a separately generated 1,000-example test set they generally achieve higher coverage, while the selector falls below its 90% target in more than half of the settings. Adaptive computation in neural operators should therefore be judged by achieved coverage and complete runtime against a matched static comparator.


## 精读解读（中文）
### 一、研究动机
傅里叶神经算子（FNO）对每个输入都使用相同的谱带宽与通道宽度，但不同PDE实例的复杂度差异很大，因此自然要问：某个输入究竟需要多少计算量。更关键的是，作者指出“选中更少的计算”并不等于“推理更快”，因为全网格变换与逐点通道混合等固定开销可能主导耗时。于是本文在固定误差预算下逐输入选择Fourier模态数或通道宽度，并追问这种自适应选择在计入参考pass、打分与调度的完整运行时后，是否仍优于匹配的静态基线。

### 二、技术方案（Method）
用分裂共形校准在绝对误差预算τ与风险水平δ下为每个输入选择模态数K或通道宽度w。规则一构造三角不等式包络：候选误差满足 e_K ≤ η(x,K)+e_max，其中η为候选与全模型输出的L2不一致度（部署时可算），e_max由校准集上全模型参考误差的(1−δ)共形分位数统一上界，从而一次性同时约束所有候选；规则二直接用带标签分数校准各候选误差，不假设误差随成本单调，并可用输入无关的分数退化为具有同一边际保证的静态基线，校准不可行时按约定弃权。模态候选族由训练好的FNO按前缀截断Fourier乘子得到（无需重训，全支撑下精确复现稠密前向），宽度候选族用slimmable训练与三明治规则得到{8,16,24,32}的嵌套宽度。为规避“先算稠密预测”的开销，作者另设一个仅依赖输入的二值门，用输入有限差分均值TV(x)在{8,32}之间路由，再在Burgers与Darcy（各3个训练种子）上按覆盖率与完整延迟评估。

### 三、结果（Result）
模态选择确实降低了活跃谱支撑比例，但没有带来可测量的延迟下降，因为全网格FFT与通道混合主导了Burgers和Darcy的成本；通道收窄能降低Darcy前向成本，但基于参考的宽度选择必须先算出稠密预测，因此没有净收益。纯输入二值宽度选择器全流程耗时为稠密推理的0.52–0.95倍，但在独立生成的1000例Darcy测试集上，用同一规则校准的静态宽度往往同样快甚至更快，且覆盖率普遍更高，而选择器在超过一半的设置中达不到其90%的目标覆盖率。

### 四、结论（Conclusion）
在神经算子中，逐输入自适应计算应当以实际达成的覆盖率和对匹配静态比较器的完整运行时来评判，而不能以名义稀疏度或减少的计算量来评判。在这套FNO基准上，参考pass与打分、调度开销常常抵消甚至超过自适应节省的计算，因此“少算”未必“更快”，也未必更可靠。

### 五、方法论与关键技术细节
误差预算采用固定输出网格上未归一化数组的绝对L2范数（而非相对误差），因为部署时无法获知目标范数，这使不一致度与参考误差可进入同一三角界；数据上验证集只用于选checkpoint，共形校准与评估分离（Darcy主结果为624例校准池加新生成1000例测试集），但作者明确承认打分函数与预算曾利用原测试集开发、存在复用。超参与构件包括：候选模态K∈{2,4,…,16}(Burgers)、{2,…,12}(Darcy)，谱实验τ分别为{0.02,0.03,0.05,0.10}与{0.05,0.08,0.12,0.18}，宽度实验τ∈{0.020,0.024,0.028}，宽度阶梯{8,16,24,32}，计时为RTX A6000上20次预热加100次同步重复且全流程含CPU打分、阈值传输、调度与重组。局限在于：运行时结论只适用于所测FNO与硬件，覆盖率仅在固定网格成立而非函数空间，静态对照因Bonferroni式保守处理而偏向自适应有利，且二值门与四宽度静态模型的动作空间并不对称。
