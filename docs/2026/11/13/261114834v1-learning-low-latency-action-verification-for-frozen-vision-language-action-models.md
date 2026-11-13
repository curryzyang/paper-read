# Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Wen-Han Hsieh, Ken Jiankun Zheng, Chia-Chien Chen, David M. Chan, Trevor Darrell
- 机构：National Tsing Hua University, University of California, Berkeley
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14834v1) · [PDF](https://arxiv.org/pdf/2611.14834v1)

## TLDR
HDH trains a lightweight, history-conditioned action verifier from terminal outcomes of a frozen VLA’s own rollouts to rank sampled action chunks at deployment, improving manipulation success while avoiding costly large-model verification.

## Abstract
Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating alternatives with computationally expensive verifiers adds latency at each policy query. In this work, we propose HDH, a lightweight framework that uses hindsight from a frozen VLA's own deployments to improve action verification. The framework has three stages. First, we deploy the policy and collect its autonomous rollouts. We then train a compact action verifier to assign each action chunk a predicted task-success score. Finally, the frozen VLA generates action candidates, and the verifier selects the candidate with the highest score for execution. Across four LIBERO-10 tasks, HDH achieves an average success rate of 82.3\% and on three real-world manipulation tasks, HDH improves average success over the baseline policy by 22.6\%.


## 精读解读（中文）
### 一、研究动机
VLA 模型虽能生成多样动作，但单次采样可能无效，而用昂贵验证器评估候选会在每次策略查询时增加延迟。作者希望利用冻结 VLA 自身部署 rollout 的终局成败作为 hindsight 监督，学习轻量动作验证器，在不更新策略的前提下实现低延迟候选选择。

### 二、技术方案（Method）
方法分三阶段：先部署冻结的 π0.5 策略并收集自主 rollout；再把每个保留查询的当前观测、已执行动作前缀与该回合终局成败配对，用蒙特卡洛 BCEWithLogits 训练紧凑验证器预测最终任务成功概率；部署时由冻结 VLA 用独立 flow-matching 噪声采样 K=2 个动作块，验证器对每个候选前缀打分并执行最高分候选的前 H 步。验证器输入包括两路相机 SigLIP 早期特征、8 维本体状态和 H×7 动作前缀，动作 token 先做自注意力再对观测 token 做交叉注意力，经动作 token 均值池化和 128→64→1 MLP 输出失败 logit；HDH 额外用小型 GRU 将最多三个此前查询的观测、本体状态和已执行动作编码为因果历史 token。

### 三、结果（Result）
在四个 LIBERO-10 任务上，HDH 平均成功率为 82.3%，高于仅用当前观测的 HDM 的 80.3%，说明执行历史带来约 2 个百分点提升；相对冻结基线平均成功率提高约 3.5 个百分点，并优于从同一候选集随机选择，表明收益来自学习到的候选排序而非额外采样。三个真实机器人操作任务上，HDH 将平均成功率从基线的 44.7% 提升到 67.3%，即提高 22.6 个百分点。与 GPT-5、GPT-6 等大型 VLM 验证器相比，HDH 取得更高或最有竞争力的成功率，同时推理延迟显著更低；但 GPT-5 因推理较慢只使用了更少试验。

### 四、结论（Conclusion）
仅使用冻结策略自身 rollout 的终局成败作为监督，就足以训练轻量动作验证器并改善闭环操作性能。HDH 通过历史条件评分和候选排序提升冻结 VLA 的部署成功率，同时保持低推理成本，是替代大型 VLM 验证器进行实时动作选择的一种实用方案。

### 五、方法论与关键技术细节
每个任务用冻结基线策略收集 100 条 rollout，按回合划分 80 条训练和 20 条验证，并用三个训练种子分别训练 HDM 和 HDH；预测动作块长度为 10，实际执行前 H=8 步，候选数 K=2，且每个候选使用独立随机种子生成。训练目标把失败标签设为 1 减终局成功，同一回合所有保留查询共享该标签，并排除已执行长度小于 H 的查询以避免监督未执行动作。验证器约 481K 可训练参数，每个任务单独训练，评分输入不含语言提示 token，历史最多覆盖三个已完成查询且在回合间重置，推理时可复用观测编码和冻结前缀的 KV cache。局限性包括依赖稀疏终局标签、每任务单独验证器、仅评估 K=2、仿真仅四个 LIBERO-10 任务和真实仅三个任务，且 VLM 对照在输入模态与试验数量上不完全对等。
