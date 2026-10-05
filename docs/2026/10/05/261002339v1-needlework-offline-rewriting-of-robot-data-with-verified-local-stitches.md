# NEEDLEWORK: Offline Rewriting of Robot Data with Verified Local Stitches

- 区域：精读区
- 排名：2
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Juntao Ren, Yifan Hou, Shuran Song
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02339v1) · [PDF](https://arxiv.org/pdf/2610.02339v1)

## TLDR
NEEDLE is an offline robot data-augmentation method that inserts short, verified action bridges between high-dimensional recorded observations to improve policy training, raising real-robot success rates by an average of 21 percentage points over the strongest baseline.

## Abstract
Robot demonstrations may contain useful behavior even when individual episodes are inefficient or unsuccessful. Trajectory stitching offers a way to compose these behaviors into improved training data, but identifying useful connections and verifying their feasibility is difficult in high-dimensional robot data, where many prior methods rely on low-dimensional state representations. We introduce NEEDLE, an offline dataset-augmentation algorithm that addresses these challenges by adding short, verified action bridges between recorded observations in high-dimensional robot demonstrations. First, NEEDLE identifies and creates connections that bypass suboptimal detours, broaden action coverage, and augment the original dataset with failed trajectories, using only RGB images, proprioception, and episode-level outcomes, without new environment interaction or privileged object state. Next, we present a sampling technique that incorporates accepted bridges into policy training without synthesizing intermediate images or discarding the original demonstrations, allowing policies to learn alternative actions while retaining the original dataset's coverage. On real-robot tasks, NEEDLE improves success rate over the strongest baseline on each task by an average of 21 percentage points. Videos and supplementary materials are on https://needle-work.github.io/.


## 精读解读（中文）
### 一、研究动机
机器人演示数据即便单条episode效率低下或最终失败，其中仍可能包含可复用的有效行为片段，因此轨迹缝合（trajectory stitching）被视为把碎片行为组合成更优训练数据的途径。但难点在于：在高维机器人数据中如何识别真正有用的连接点，并验证这些连接在实际动力学下是否可行；已有方法大多依赖低维状态表示，难以直接推广到高维视觉观测场景。

### 二、技术方案（Method）
NEEDLE是一种离线数据增强算法，核心是在已记录的高维演示观测之间添加短的、经可行性验证的动作桥（verified action bridges）。输入仅为RGB图像、本体感知（proprioception）与episode级结果标签，不使用新的环境交互，也不使用物体真实状态等特权信息；算法先挖掘并构造可绕过次优绕行路径、扩大动作覆盖面的连接，并把失败轨迹一并纳入增强数据。随后提出一种采样技术，把被接受的桥接样本融入策略训练，既不合成中间图像，也不丢弃原始演示数据，从而让策略学到替代动作的同时保留原数据集的状态-动作覆盖。

### 三、结果（Result）
在真实机器人任务上，NEEDLE相对每个任务中最强基线平均提升21个百分点的成功率，说明仅用RGB与本体感知、无需在线交互或特权状态，也能通过离线缝合获得可用的改进数据。

### 四、结论（Conclusion）
结果表明，在高维视觉机器人数据中做离线轨迹缝合是可行的：用短的、经本地验证的动作桥连接已有观测，可在不新增环境交互、不合成图像的前提下改善策略表现，为从包含低效或失败片段的演示数据中榨取价值提供了实用方案。

### 五、方法论与关键技术细节
输入与先验约束：仅RGB图像、本体感知和episode级成败标签，不使用特权物体状态、不做新环境交互，因此增强过程完全离线。关键设计在于“局部”与“验证”：桥接片段必须足够短并经过可行性验证才被接受，以控制高维空间中的错误连接风险；采样机制在训练时混合原始演示与被接受的桥，避免合成中间图像带来的伪影，也避免丢失原数据覆盖。方法可同时利用成功与失败轨迹，通过绕过次优绕行来拓宽动作分布。局限性方面，其效果依赖桥接验证的可靠性与短程桥的假设，长距离或大位姿差异的连接可能难以验证；摘要未给出具体超参、桥长上限、采样比例与计算复杂度等实现细节，需参考原文与附录。
