# ShieldVLA: Feasibility-Aware Safety Alignment for Vision-Language-Action Models

- 区域：精读区
- 排名：1
- 匹配度：5.6/10
- 来源：arxiv
- 作者：Manan Tayal, Akshay Nambi
- 机构：Microsoft Research, Indian Institute of Science (IISc)
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13231v1) · [PDF](https://arxiv.org/pdf/2609.13231v1)

## TLDR
ShieldVLA is a safety-aligned fine-tuning framework for Vision-Language-Action models that learns a model-free Hamilton-Jacobi reachability safety critic from visual observations using rubric-based VLM safety scores and uses it to gate policy optimization between reward maximization in safe regions and recovery near unsafe states, reducing cumulative safety cost by 57% on average and improving task success over SafeVLA.

## Abstract
Vision-Language-Action (VLA) models demonstrate strong generalization in robotic manipulation and navigation, but existing fine-tuning methods provide limited safety guarantees. Current approaches primarily rely on Lagrangian optimization that enforces safety through soft penalties on expected cumulative cost, often resulting in residual constraint violations or overly conservative behavior. Moreover, learning safety in visual domains is challenging due to the absence of dense per-step safety annotations. We propose ShieldVLA, a safety-aligned fine-tuning framework for VLA models based on Hamilton-Jacobi (HJ) reachability. ShieldVLA learns a model-free approximation of the HJ reachability value function directly from visual observations to estimate the safe operating region. The learned safety critic gates policy optimization by separating reward maximization within feasible regions from recovery near unsafe states, avoiding persistent reward-cost trade-offs. To enable scalable supervision in visual environments, we introduce rubric-based VLM safety scores that convert semantic safety feedback into structured critic targets without requiring manual cost labels. Across five navigation and manipulation benchmarks spanning multiple VLA backbones, ShieldVLA reduces cumulative safety cost by 57% on average and improves task success rate by +0.13 over SafeVLA.


## 精读解读（中文）
### 一、研究动机
现有VLA微调主要靠拉格朗日软惩罚对期望累计代价约束，常产生残余违规或过度保守，而且视觉域缺少密集逐步安全标注。本文要把安全从全局奖励-代价权衡转为状态相关可行性判断，在保持任务性能的同时提供更可靠的安全对齐。

### 二、技术方案（Method）
ShieldVLA用冻结VLM按结构化安全评分表把每帧观测转成连续安全裕度ell(o)，无需人工逐步代价标签；再用共享回放缓冲在线离策略训练HJ可达性安全评论家Qs_phi(o,a)，其TD目标为(1-gamma)ell(o)+gamma*done*min{ell(o), Qbar(o',a')}并配合Polyak目标网络。策略更新采用安全门控PPO：当Qs_phi(o, mean action)>delta时只优化标准PPO奖励，处于不可行区时用Lsafe=-Qs_phi(o, mean action)的确定性策略梯度把动作推向安全流形，beta_t由双升法按成本预算c_max调节。该评论家用视觉编码器加动作嵌入MLP，与VLA策略并发训练，部署时仅输出单一VLA策略，无需运行时屏蔽器。

### 三、结果（Result）
在Dubins-VL、TurtleBot-Nav、Safety-CHORES Nav、Safety-CHORES Fetch和Franka-Reach五个导航与操作基准、多个VLA主干上，ShieldVLA平均降低累计安全代价57%，任务成功率比SafeVLA提升0.13。结果说明安全门控能在可行区不施加惩罚、在危险区专门恢复，从而改善安全-性能折中。

### 四、结论（Conclusion）
基于HJ可达性的可行性感知安全对齐可避免拉格朗日方法持续奖励-代价耦合与过度保守问题，同时借助VLM评分表实现可扩展的视觉安全监督。ShieldVLA得到单个部署策略，无需额外运行时安全过滤器，在多个具身与基准上验证了有效性。其安全仍是经验性的，受评论家估计误差和VLM成本信号噪声影响。

### 五、方法论与关键技术细节
关键实现包括：用冻结VLM按碰撞风险、危险接近、机动空间等轴生成ell(o)；安全评论家独立于策略，编码器可从VLA编码器初始化并冻结或微调，MLP头输入编码特征与动作嵌入；每轮PPO在共享回放缓冲上做K步离策略TD，目标函数含Polyak平均、done指示和min备份。门控为不可微二值指示，训练时用stop-gradient作为样本掩码，仅在Qs接近delta边界时近似无偏；beta_t通过clip(beta+eta_beta*(mean cost-c_max), beta_min, beta_max)更新，仅作用于被判定不安全的转移。局限是缺乏形式化安全保证，安全集学习依赖有限数据与VLM评分质量，且门控阈值delta、单/双评论家与编码器冻结策略需按环境选择。
