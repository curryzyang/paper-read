# SSPE: Robust Sequential Staypoint Extraction in Degraded Trajectory Data

- 区域：精读区
- 排名：2
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Yueyang Liu, Lance Kennedy, Andreas Züfle
- 机构：Emory University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03737v1) · [PDF](https://arxiv.org/pdf/2611.03737v1)

## TLDR
The paper proposes SSPE, a robust state-driven sequential staypoint extraction method combining dynamic centroid tracking, n-step lookahead, temporal bridging, and unsupervised parameter estimation to handle noisy and sparse trajectory data, outperforming Trackintel’s sliding-window baseline in both F1-score and runtime.

## Abstract
Extracting semantically meaningful staypoints from raw trajectory streams is a foundational prerequisite for mobility analytics. However, real-world trajectory data is frequently degraded by severe spatial noise and protracted temporal dropouts. Classic threshold-based extraction methods, such as the widely adopted sliding-window algorithm, are highly sensitive to these anomalies, routinely fracturing continuous stationary episodes into disjointed fragments. To overcome this limitation, we propose the Sequential Staypoint Extraction (SSPE) algorithm. SSPE employs a resilient, state-driven architecture that replaces static spatial anchors with a dynamic centroid and introduces an $n$-step lookahead heuristic to structurally tolerate transient coordinate drift. Concurrently, it utilizes temporal bridging mechanisms to prevent artificial fragmentation during prolonged signal loss. Since optimal extraction parameters vary significantly across datasets, we further introduce a fully unsupervised, consensus-based parameter estimation framework. This framework derives baseline statistical scales directly from the raw trajectory data and identifies the optimal parameter configuration by maximizing structural agreement, thereby eliminating the reliance on annotated ground truth. We evaluate SSPE on the ExtraSensory dataset, a real-world mobility corpus with manually verified ground-truth staypoints, against the sliding-window implementation of Trackintel, one of the most widely adopted extraction baselines in the field. Empirical results demonstrate that SSPE achieves superior accuracy, yielding higher F1-scores while simultaneously improving computational efficiency over this standard.


## 精读解读（中文）
### 一、研究动机
真实轨迹常受严重空间噪声和长时间时间断采影响，传统滑动窗口等阈值方法对此高度敏感，容易把连续停留切碎并产生虚假或缺失停留点，从而破坏后续移动性分析。论文旨在提出一种能同时容忍坐标漂移和信号中断的稳健停留点提取方法，并解决无标注数据下参数难以校准的问题。

### 二、技术方案（Method）
SSPE以按时间排序的轨迹点(uid, lat, lon, t)为输入，使用锚点指针和评估指针顺序扩展候选停留序列；每个新点与候选序列的动态质心计算Haversine距离，并检查与前一保留点的时间间隔。若时间间隔超过τmax则终止扩展；若距离不超过δdist则加入序列并更新质心；若距离超限则启动n步前瞻，在未来n个点中若存在点重新落入质心邻域且累计时间间隔不超过τmax，则将当前点视为瞬态异常并跳过，否则确认离开并终止。候选序列结束后，若首末时间跨度不小于τmin，则输出停留点(uid, 质心, 首时间, 末时间)，并将锚点跳到序列末点之后，否则丢弃并前进一个点。参数校准采用无监督ABPE框架：由正时间间隔中位数得到采样间隔g，仅保留Δt≤5g的正常步长，对log10步长距离做200-bin直方图并用Otsu阈值分离静止噪声与移动，得到空间阈值ε和静止步长90分位数σ；对时间间隔做Otsu得到τOtsu并以max(τOtsu,5g)作为τbase；由跳跃后1至5步内恢复到跳跃前位置的最小恢复长度L的90分位数向上取整估计n；再围绕σ和5g构造δdist、τmax候选网格，τmin按停留概念固定，最终选择使各参数配置提取结果两两结构一致性平均最高的配置。

### 三、结果（Result）
在ExtraSensory真实移动轨迹数据上，SSPE的F1为0.7878、精确率0.7226、召回率0.8659，显著高于Trackintel滑动窗口基线的F1 0.5098、精确率0.4342、召回率0.6173；使用无监督ABPE参数估计后，SSPE达到F1 0.8107、精确率0.8854、召回率0.7476，也优于Trackintel经Hyperband调参后的F1 0.6305、精确率0.5747、召回率0.6983。论文还报告SSPE在取得更高F1的同时具有更低的运行时间。

### 四、结论（Conclusion）
SSPE通过动态质心、n步前瞻和时间桥接机制，在噪声与断采并存的退化轨迹中比传统滑动窗口更不容易碎片化连续停留，并能以无监督共识搜索替代人工标注调参。结果表明该方法在真实数据上兼顾更高准确性和更好计算效率，适合大规模移动性分析部署。

### 五、方法论与关键技术细节
评估数据为ExtraSensory，且作者手工核验了全部真值停留点；方法依赖δdist、τmin、τmax、n四个参数，ABPE用Otsu阈值、90分位数、恢复长度统计和共识最大化进行无监督选择，空间网格可细化为σ·1.25^k或粗化为固定倍数，τmax网格为5g·2^k，τmin不估计而按停留语义固定；前瞻仅检查最多n步，恢复长度估计最多检查5步，参数搜索会带来额外计算开销，且实验仅覆盖单一数据集，跨数据集泛化仍需验证。
