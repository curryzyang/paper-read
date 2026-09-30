# Replication Failure and Trivial Baselines in Road-Level Crash Prediction

- 区域：精读区
- 排名：7
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Maurya Patel
- 机构：University of Westminster
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35917v1) · [PDF](https://arxiv.org/pdf/2609.35917v1)

## TLDR
This paper finds that graph neural networks for road-level crash prediction have fragile, largely non-replicable gains and are matched or beaten by a trivial cumulative-crash-count baseline when evaluation horizons are properly matched, so it recommends horizon-matched baselines and multi-seed reporting.

## Abstract
Graph neural networks are increasingly applied to road-level crash prediction, but the stability of their reported gains has received little scrutiny. We independently reconstruct the data pipeline of a recent uncertainty-aware model and evaluate eleven of its design decisions across three London boroughs under an expanding-window protocol. Four survive replication on a second borough; seven do not, and four of those reverse sign rather than attenuate. Multi-seed evaluation is decisive: one effect reverses sign between random seeds within a single borough, and the reference architecture exhibits per-borough seed spreads of up to 35.7 points against 4 points for ours. We further compare both networks against a parameter-free baseline that ranks segments by cumulative past crash count. At matched history depth our model is statistically indistinguishable from that baseline ($-0.90$ points, $p=0.61$), and the reference architecture loses to it on 18 of 18 held-out windows ($-17.37$, $p<10^{-6}$). Sweeping the baseline's lookback horizon shows it spans 22.71% to 83.94% accuracy on that variable alone, and that every published figure in this line of work is matched by the baseline at a horizon of one to five years. We argue that the apparent margin of graph networks over historical baselines in this task is substantially an artefact of the short horizons those baselines were computed over, and recommend horizon-matched baselines and multi-seed reporting as minimum practice.


## 精读解读（中文）
### 一、研究动机
近年图神经网络被广泛用于路段级碰撞预测并报告显著提升，但这些提升的稳定性与基线可比性缺乏检验。本文独立复现一个近期不确定性感知模型的数据管线，审计其设计决策在西敏、塔村、兰贝斯三区及扩展窗口协议下的可复现性，并质疑历史基线是否按相同回看期计算。

### 二、技术方案（Method）
数据使用OS Open Roads按行政区多边形端点内裁剪并做line-graph构图，目标为STATS19 2021至2024年每日路段碰撞数；35个特征包含几何与节点度、星期、7/14/30/90/365天及2/3/5年碰撞历史、伤亡类型、年平均日交通量、OpenStreetMap兴趣点密度和多重剥夺指数，长历史用稀疏碰撞表累积和矩阵计算并按训练集统计标准化。模型按时间步做图注意力，随后接GRU，解码为零膨胀Poisson头，配置为3个注意力头、1层注意力、隐藏维度16和32、残差连接；Adam学习率0.01训练200轮，无权重衰减和早停，并用split conformal做90%预测区间。评测为扩展窗口walk-forward，20天输入、14天预测、90天步长，每区6个留出窗口，覆盖2023-07-15至2024-10-07，指标AccHR@20为每日真实碰撞落入前20路段的比例在窗口内平均；所有模型结果为5个随机种子均值，按窗口和种子配对做t检验与Wilcoxon检验。

### 三、结果（Result）
11项设计决策中仅4项在第二个行政区复现，7项失败且其中4项符号反转；效应量低于约4点种子噪声带的全部失败，但两个高于噪声带的效应也失败。参考架构的种子波动远大于本文模型，每区种子跨度最高35.7点而本文约4点；与无参数累计历史碰撞数排序基线在匹配历史深度下本文模型统计不可区分，差-0.90点，p=0.61，参考架构在18/18个留出窗口输给该基线，差-17.37点，p<10^-6。基线回看期从30天到9年扫描时AccHR@20从22.71%到83.94%，跨度61.2点，且该排序在1至5年回看期即可匹配本文及参考文献的已发表数字；三区合并本文模型80.08±2.62，参考论文报告72.60，但基准表显示约8年碰撞数排序83.94、HSM经验贝叶斯83.84、封顶5年排序80.99。

### 四、结论（Conclusion）
本文认为图网络在该任务上相对历史基线的表面优势很大程度上是基线回看期过短造成的评估假象，而非建模能力差异，应至少采用与预测历史深度匹配的强基线并报告多种子结果。由于复现失败常表现为符号反转而非简单衰减，单区域单种子效应不能作为真实效应的上界或方向依据。

### 五、方法论与关键技术细节
实现关键点包括长回看历史通过稀疏碰撞列表的累积和矩阵而非滚动路段日表计算，使回看期扫描近乎计算免费；特征标准化仅用训练实例统计；统计上n=5用t(4)=2.776，正态近似约低估置信区间40%；AccHR@20对排名粒度敏感。局限包括仅三个伦敦行政区、与Gao等非完全同数据同协议，因此其发表数值映射是提示性而非受控比较；参考论文仅给三个点估计无法配对检验；标准GNN实现即使固定随机种子也非确定；训练无早停和权重衰减等设置可能影响复现。
