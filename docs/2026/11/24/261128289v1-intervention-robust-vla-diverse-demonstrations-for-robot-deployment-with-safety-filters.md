# Intervention-Robust VLA: Diverse Demonstrations for Robot Deployment with Safety Filters

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Tzu-Yuan Huang, Shao-Hsuan Chang, Dai-Jie Wu, Ralf Römer, Yung-Hui Li, Stefan Sosnowski, Angela P. Schoellig, Kenneth Marino, Sandra Hirche
- 机构：Technical University of Munich, Hon Hai Research Institute, University of Utah
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28289v1) · [PDF](https://arxiv.org/pdf/2611.28289v1)

## TLDR
**TLDR:** InteR-VLA improves robot safety and task success under test-time safety filters by training vision-language-action models on diverse task-completing demonstrations that broaden state coverage and mitigate intervention-induced distribution shift, achieving up to 90% Safe Success Rate in real-world experiments.

## Abstract
Vision-Language-Action models (VLAs) have shown strong potential for learning complex robotic behaviors from demonstrations. However, learning safe behavior directly from data requires extensive coverage of safety-critical situations, which is often impractical in real-world settings. Test-time safety filters provide an alternative by correcting unsafe actions during deployment, but these interventions can drive the robot into states poorly covered by the training data, thereby degrading task performance. We introduce InteR-VLA, an intervention-robust framework for VLAs that leverages diverse task-completing demonstrations to broaden task-relevant state coverage and maintain competence under safety interventions. By better aligning the training distribution with safety-filtered deployment under the same data budget, our approach mitigates intervention-induced distribution shift while preserving task performance. Real-world experiments across in-distribution and out-of-distribution settings show that InteR-VLA maintains safety, increases Safe Success Rate up to 90% from 0% for nominal policies, and consistently outperforms nominal-data training on both evaluated VLAs.


## 精读解读（中文）
### 一、研究动机
VLA通过模仿学习从示教中获取复杂机器人行为，但直接在数据中学习安全行为需要覆盖大量安全关键场景，现实采集往往不可行。测试时安全过滤器可在部署阶段修正不安全动作，但其干预会把机器人推向训练数据覆盖不足的状态，造成干预诱发的协变量偏移并降低任务成功率。路径一致的制动式干预虽能减小偏移，却在必须绕开原路径才能完成任务时过于受限，因此需要一种在安全干预下仍保持任务能力的VLA框架。

### 二、技术方案（Method）
提出InteR-VLA：在固定示教数据预算下，不重复采集标称轨迹，而是将预算分配给多种完成任务的行为模式，以扩大任务相关状态覆盖并使其更接近安全过滤后的部署分布。具体提供两类离线采集策略：无障碍的多样化完成任务示教用于拓宽任务相关覆盖；当采集时已知危险源时，使用路径阻挡障碍的多模态避障示教提供直接干预覆盖。训练仍采用VLA模仿学习，输入语言指令、相机观测与机器人本体状态，输出相对笛卡尔位移等高层动作；部署时在每个时间步用CBF安全过滤器对VLA动作做最小修正，使执行动作满足安全集约束，整个流程不需要策略rollout或针对过滤器专门调参。

### 三、结果（Result）
真实世界实验覆盖分布内和分布外设置，并在两种VLA模型上验证。结果表明InteR-VLA在保持安全的同时，将Safe Success Rate从标称策略的0%提升至最高90%，并在两个受评估VLA上持续优于仅用标称数据训练的策略。

### 四、结论（Conclusion）
安全过滤与多样化任务示教具有互补作用：过滤器在部署时提供硬安全约束，多样化示教则让VLA在过滤干预导致的状态偏移下仍具备完成任务的能力。因此在相同数据预算下，通过增加行为模式而非数据量来对齐训练分布与安全过滤部署分布，是提升VLA干预鲁棒性和实际部署安全成功率的有效途径。

### 五、方法论与关键技术细节
方法将状态定义为语言指令加观测（相机和本体感知），动作为高层相对位移；VLA常以动作块预测并按滚动时域执行前若干步。安全侧用连续可微函数h(x)定义安全集，碰撞避免可由机器人椭球近似与感知障碍间的距离构造CBF约束，过滤器算子S在满足安全约束下尽量贴近原始VLA动作；关键分析是过滤后的动作分布rho_S与示教分布rho不一致，导致未见状态。实现要点包括固定数据预算下以多样化行为模式替代重复标称示教、离线采集无需反复rollout和重训、多模态避障示教依赖采集时已知危险源，且实验主要基于两种VLA和真实世界ID/OOD设置，未给出具体损失函数与超参数细节。
