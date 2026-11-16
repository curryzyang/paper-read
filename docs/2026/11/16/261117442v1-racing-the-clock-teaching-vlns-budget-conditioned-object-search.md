# Racing the Clock: Teaching VLNs Budget-Conditioned Object Search

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Maitree Meher, Siming He, S. Shankar Sastry, Jitendra Malik, Claire Tomlin, Jonas Frey
- 机构：University of California, Berkeley, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17442v1) · [PDF](https://arxiv.org/pdf/2611.17442v1)

## TLDR
This paper introduces budget-conditioned object search for vision-language navigation agents and shows that supervising them with a room-level Bellman expert that plans under partial observability yields better budget-aware exploration than imitating a privileged full-map TSP/object-level expert, because effective search supervision should optimize decisions under uncertainty rather than copy routes that are optimal only with complete environment knowledge.

## Abstract
A rescue robot entering a building with thirty seconds on the clock should sprint toward the single most promising room; given ten minutes, it should instead explore a broader tour. Yet vision-language-navigation (VLN) models are typically evaluated under a fixed episode limit that the policy never observes, even though time-critical missions require behavior to adapt to the available budget. We study budget-conditioned object search: given a target category and an explicit action budget, an agent must find as many distinct target instances as possible before the budget expires. We investigate how to supervise VLNs for this task by comparing a privileged TSP expert, which plans near-optimal routes using the full map and true target locations, with a room-level Bellman expert that maximizes expected return under partial observability using high-level cross-scene semantic priors. Despite the TSP expert achieving substantially higher expert performance, its demonstrations are less effective for learning exploration: on held-out HM3D scenes, the Bellman-supervised VLN consistently outperforms the TSP-supervised VLN, with the advantage becoming more pronounced at longer budgets. At 2000 steps (500m), the Bellman-supervised VLN finds 71.4% of reachable target instances, compared with 65.5% for the TSP-supervised VLN and 44.8% for the pretrained VLN. These results highlight a distinction between optimal routing and optimal exploration: effective exploration supervision should optimize decisions under partial observability rather than imitate routes that are optimal only once the environment is fully known.


## 精读解读（中文）
### 一、研究动机
传统VLN通常在固定回合限制下评估，且策略本身看不到剩余预算，但时间敏感任务要求机器人依据可用时间在立即收集与探索远处房间之间调整行为。本文研究预算条件目标搜索：给定目标类别和显式动作预算，智能体需在预算耗尽前找到尽可能多的不同目标实例，并比较何种专家监督能最好地把预算感知搜索行为迁移给部分可观测的VLN。

### 二、技术方案（Method）
任务输入为RGB观测历史、目标类别指令和剩余预算倒计时，智能体输出基础动作，旅行、扫描与接近目标均消耗预算；实例按相机视场与距离的几何准则计为收集，无需物理拾取，奖励为每一步新收集的不同实例数。专家设计被形式化为对完整环境M的场景抽象z=φ(M)上的预算索引Bellman递推：对象级Bellman专家拥有完整地图和真实目标位置，将搜索退化为已知目标间的预算化路由/TSP式规划；房间级Bellman专家保留已观测房间连通性、门洞证据和跨场景语义先验，但不揭示未探索房间内容，在部分可观测下最大化期望回报并把未进入房间视为收益不确定、奖励延迟的搜索机会。两种专家在匹配场景、预算和记录数下蒸馏到同一Uni-NaVid学生，学生从RGB历史和语言预测基础动作，并额外与贪心frontier专家监督的VLN比较；评估时仅改变指令中的预算，并用倒计时干预和预算盲对照检验行为敏感性。

### 三、结果（Result）
尽管对象级/TSP专家自身的专家回报更高，其示范对学习探索反而更差：在留出HM3D场景上，房间级Bellman监督的VLN在每个测试预算下平均收集数最高，且优势在更长预算时更明显。在2000步（500m）预算下，房间级Bellman监督VLN找到71.4%的可达目标实例，TSP监督VLN为65.5%，预训练VLN为44.8%；仅改变声明预算即可使同一场景、同一初始位姿和确定性解码下的学习轨迹显著不同，而非简单延长同一轨迹。

### 四、结论（Conclusion）
结果表明最优路由不等于最优探索：有效探索监督应优化部分可观测下的决策，而不是模仿只有环境完全已知后才最优的路线。将剩余预算显式输入策略并提供房间级、不确定性感知的搜索示范，比全图全目标信息的路由示范更能把预算条件搜索行为迁移给视频VLN。

### 五、方法论与关键技术细节
实验在留出HM3D场景（文中为10个）上评估Uni-NaVid，测试预算包括50/150/400/800/2000步，2000步约500m；发现判定依赖相机视场和接近距离的几何准则，目标值统一为1、基础动作成本统一为1，以隔离目标优先级和成本权重影响。房间级专家仅用严格跨场景转移估计Bellman递推，门洞证据估计房间类别、跨场景先验预测发现率，未探索房间内容保持隐藏；两个Bellman学生共享架构、场景、预算、记录数和优化设置。局限性包括聚焦固定视频VLN架构与两类Bellman/贪心frontier监督，非均匀目标价值和非单位成本虽可扩展但监督优势需进一步验证，且目标是研究监督与预算使用而非替代显式地图frontier规划。
