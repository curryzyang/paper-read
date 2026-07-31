# It's Not Just More Demos: Counterfactual Action Sensitivity Coverage for Data-Efficient Robust Robot Imitation

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Giovanni D'urso, Kaushik Roy, Nicholas Lawrance, Brendan Tidd
- 机构：CSIRO
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.27261v1) · [PDF](https://arxiv.org/pdf/2607.27261v1)

## TLDR
TLDR: The paper proposes CFNBC, an offline data-selection framework that uses counterfactual action-drift sensitivity to pick a compact, response-diverse set of demonstrations for fine-tuning, enabling data-efficient repair of visuomotor imitation policies against task-preserving visual nuisances.

## Abstract
Visuomotor imitation learning has demonstrated success for manipulation tasks. However, the trained policies remain brittle to visual `nuisances', with even minor task-preserving variations such as lighting, distractions or changes in colour result in heavy degradation of the trained policy's performance. While increasing data diversity can improve robustness, it is unclear which additional demonstrations are informative for a particular trained policy. We propose Counterfactual Nuisance Behaviour Cloning (CFNBC), an offline data-selection framework for targeted robustness repair. Starting from a nominal policy trained on `clean' demonstrations, CFNBC generates paired clean and nuisance observations that preserve the expert action, then measures \emph{action drift}: the change in the policy's predicted action under a nuisance that should not alter the desired behaviour. This provides a policy-specific sensitivity signal for selecting a compact, response-diverse repair set from a larger candidate pool, without requiring rollout success labels or online policy execution. We show in MuJoCo bimanual cube transfer and SimplerEnv cube stacking that action drift correlates with nuisance-induced failure, and that response-guided repair with only $20$--$30$ selected candidates substantially outperforms matched-budget random selection while approaching the performance of much larger random repair budgets. These results support a data-centric view of robustness repair: the most useful data are not necessarily the most numerous, visually diverse, or obviously difficult, but the examples that cover fragile response modes of the current policy.


## 精读解读（中文）
### 一、研究动机
视觉运动模仿学习策略虽在标称环境下表现良好，但对光照、分心物、颜色变化等任务保持型视觉干扰十分脆弱，性能剧烈下降。仅仅增加数据多样性并不清楚哪些额外演示对特定已训练策略最有修复价值，因此需要一种离线、策略特异的针对性鲁棒修复数据选择方法。

### 二、技术方案（Method）
提出Counterfactual Nuisance Behaviour Cloning (CFNBC)离线数据选择框架。首先，从干净演示训练的标称策略出发，在相同任务状态下生成成对的干净观测与干扰观测，并保持专家动作不变；然后计算策略在归一化动作空间中的动作漂移（action drift），即干扰前后预测动作的变化，作为策略敏感性信号，并构造响应特征。接着，从候选池中通过贪心优化加权响应覆盖目标，选择覆盖多样化高漂移响应模式的紧凑修复集，而非简单选择最高漂移的冗余样本。最后，将选中的干扰观测与原始演示动作配对形成反事实修复数据，与干净演示混合进行行为克隆微调，得到修复后策略。整个过程不需要 rollout 成功标签或在线策略执行。

### 三、结果（Result）
在MuJoCo双臂立方体传递和SimplerEnv立方体堆叠任务上，标称ACT策略干净域成功率分别约为0.96和0.90，但在22种任务保持干扰条件下平均成功率降至0.30和0.32，最差条件甚至为0.00。动作漂移与干扰引起的失败强相关；仅用20到30个选出的候选样本进行响应引导修复，显著优于同等预算的随机选择，并接近更大规模随机修复预算的性能。

### 四、结论（Conclusion）
结果支持数据中心式的鲁棒修复观点：最有用的修复数据并非数量最多、视觉最多样或明显最困难的数据，而是能够覆盖当前策略脆弱响应模式的样本。CFNBC通过离线动作敏感性审计，能在无需在线交互或成功标签的情况下，高效识别并弥补特定策略的视觉脆弱性。

### 五、方法论与关键技术细节
关键细节包括：采用ACT作为基础策略；干扰空间涵盖外观、光照、分心物、局部支撑四类因素，各四个严重等级，加上六个多因素组合共22个条件；候选样本是时间子采样的响应窗口而非完整演示；响应特征使用跨时间步和动作维度的统计摘要，亲和函数衡量响应相似度；选择权重可均匀或随动作漂移增大，以优先高敏感模式；微调损失为干净BC损失加上lambda_cf加权的反事实BC损失，修复目标动作直接继承自原始演示，无需新专家标签或奖励；该方法目前仅在两个模拟任务上验证，未涉及真实世界策略，且依赖合成干扰生成的候选池质量。
