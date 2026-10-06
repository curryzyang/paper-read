# BAT-NO: A Boundary-Condition-Aware Transformer Neural Operator for Crashworthiness Prediction of Vehicle Components

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Haoran Li, Yingxue Zhao, Haosu Zhou, Mustapha Ziane, Pierre Culiere, Tobias Pfaff, Nan Li
- 机构：Keysight Technologies, Prometheus, Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.03854v1) · [PDF](https://arxiv.org/pdf/2610.03854v1)

## TLDR
BAT-NO is a boundary-condition-aware transformer neural operator that combines recurrent mesh processing with latent-grid Fourier operator processing and hybrid local–global boundary-condition encoding to accurately predict transient displacement fields and scalar crashworthiness responses under varying geometries, loading, and support conditions.

## Abstract
High-fidelity finite-element simulations provide accurate crashworthiness predictions, but their cost limits iterative design exploration. Deep learning surrogates can reduce this cost, but many component-level models are developed under a single prescribed boundary condition, limiting generalisation to boundary variations. This work proposes a Boundary-Condition-Aware Transformer Neural Operator (BAT-NO) for autoregressive prediction of transient displacement fields and scalar crashworthiness responses under variations in geometry and boundary conditions. A B-pillar simulation framework evaluates generalisation across variations in geometry, impact position and velocity, and support stiffness. BAT-NO combines recurrent mesh processing with latent-grid Fourier operator processing. Boundary-condition information is transferred to the latent grid through a hybrid local--global mechanism. Slice-based attention models interactions among physically related regions, while direct boundary-to-grid projection preserves local spatial structure. Across the validation sets for the shape-only, shape-and-loading, and shape-loading-boundary cases, BAT-NO achieves the lowest mean final-step mean nodal Euclidean displacement error among the evaluated baselines. In the most challenging case, it reduces the mean error by 32.6% relative to the second-best model. Hyperparameter tuning reduces the validation error from 0.451 to 0.269 mm, with a comparable error of 0.267 mm on 300 unseen test simulations sampled within the investigated design space. An attention-based scalar decoder jointly predicts six response trajectories with a mean relative error of 2.46%. Most derived crashworthiness indicators have median errors below 3%. These results show that explicit local and global boundary-condition representations improve crashworthiness prediction over expanded component-level design spaces.


## 精读解读（中文）
### 一、研究动机
高保真有限元仿真能准确预测车辆部件碰撞响应，但计算成本高，限制迭代设计探索。现有组件级深度学习代理多在单一预设边界条件下开发，难以泛化到边界条件变化。实际装配结构中相邻部件或接头刚度变化会通过连接区传递，在组件层面表现为支撑、接触和载荷条件变化，因此需要显式空间化边界条件建模，同时保留局部网格保真与全局结构交互能力。

### 二、技术方案（Method）
以B柱组件瞬态碰撞为对象，将网格表示为图，节点特征包含增量位移与坐标，边特征为参考/当前构型相对向量及其范数，共8维，边界与载荷信息单独编码为节点条件特征。BAT-NO采用循环网格处理器提取局部状态与边信息，经GNO核积分式网格到规则潜网格投影后，在潜网格上执行FNO全局傅里叶算子演化，再由核式层重建回网格并解码。边界条件通过混合局部-全局机制进入潜网格：切片注意力将点软分配给物理相关切片/token并做token间自注意力以建模全局交互，直接边界到网格投影保留支撑、接触和载荷的局部空间结构。推理时自回归预测下一时刻位移场，当前几何通道由预测坐标重算，参考几何固定；注意力标量解码器从潜表示联合预测六条标量碰撞响应轨迹，并在全耦合rollout中将标量反馈至下一时间步。

### 三、结果（Result）
在shape-only、shape-and-loading、shape-loading-boundary三类验证集上，BAT-NO均取得最低的平均最终步平均节点欧氏位移误差；在最困难的shape-loading-boundary情形中，相较第二优模型平均误差降低32.6%。超参数调优将验证误差从0.451 mm降至0.269 mm，在300个设计空间内未见测试仿真上误差为0.267 mm。标量解码器联合预测六条响应轨迹的平均相对误差为2.46%，多数派生碰撞指标的误差中位数低于3%。

### 四、结论（Conclusion）
显式局部与全局边界条件表征能提升组件级碰撞代理在几何、冲击和支撑条件联合变化下的瞬态位移场与标量响应预测精度，并表明自回归场预测与工程响应量估计可在统一架构中完成，为扩展设计空间下的车辆部件碰撞代理建模提供了可行路径。

### 五、方法论与关键技术细节
数据来自B柱仿真框架，系统变化几何、冲击位置与速度、支撑刚度，用以近似装配中相邻结构传递的边界条件变化；参考几何边特征固定，当前几何边特征在自回归rollout中由预测坐标重算，每条无向边包含双向边。模型关键先验是局部网格状态与全局边界/载荷关系需分开显式表示，并通过切片注意力与直接边界到网格投影形成混合局部-全局条件注入；潜网格FNO提供全局感受野，切片注意力降低对全点注意力的网格规模依赖。摘要与预览未披露具体损失函数和完整训练超参，仅报告了超参调优效果。局限包括仅在生成数据集的有限元网格离散上评估，未验证点云或其他离散；组件级支撑刚度近似装配连接影响，泛化范围限于所研究设计空间。
