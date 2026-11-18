# A Probabilistic Lateral Motion Prediction Model with Improved Response Fidelity for Vehicle-in-the-Loop Simulation

- 区域：精读区
- 排名：2
- 匹配度：5.0/10
- 来源：arxiv
- 作者：Xiangyang Ye, Chaosheng Huang, Jinwen Yang, Zhengxian Chen, Jun Li
- 机构：Tsinghua University, Jilin University, Tianjin University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21806v1) · [PDF](https://arxiv.org/pdf/2611.21806v1)

## TLDR
The paper proposes a physics-guided probabilistic lateral motion prediction model for vehicle-in-the-loop simulation that combines a 2-DOF vehicle model with recurrent residual learning, multistep rollout training, and uncertainty propagation, reducing mean lateral-position RMSE by 19.0% compared with Deep Dynamics lateral adaptation.

## Abstract
Vehicle-in-the-loop (VIL) simulation requires a lateral dynamics model that accurately reproduces vehicle responses and reliably generates horizontal lateral-position and heading commands through recursive integration. This paper presents a probabilistic lateral motion prediction model with improved response fidelity. A two-degree-of-freedom vehicle model provides the physical prior, while a recurrent neural network learns correlated residual corrections to lateral acceleration and yaw rate. To maintain prediction fidelity during recursive motion generation, multistep rollout training feeds corrected responses into subsequent states and histories and directly penalizes accumulated lateral-velocity error. A conditional Gaussian characterizes response uncertainty, which is propagated to lateral-response, position, and heading predictions through augmented-state linearization. Evaluation results demonstrate improved lateral-response and integrated-motion prediction. Compared with the Deep Dynamics lateral adaptation, the proposed model reduces mean lateral-position root-mean-square error (RMSE) from 0.596 m to 0.483 m, an improvement of 19.0%, while reducing mean lateral-velocity RMSE from 0.0469 m/s to 0.0441 m/s. These results demonstrate the effectiveness of combining physical priors, probabilistic residual learning, and multistep rollout training for response-faithful lateral motion prediction.


## 精读解读（中文）
### 一、研究动机
车辆在环仿真需要横向动力学模型不仅能准确复现横向加速度与横摆率响应，还要通过递归积分可靠生成横向位置和航向指令。现有混合模型多关注单步响应精度，预测误差在递归反馈中会通过横向加速度与横摆率的耦合不平衡累积为横向速度误差，导致自由运行轨迹漂移。因此，本文针对车辆在环仿真中响应保真与递归运动生成的一致性需求，构建概率化横向运动预测模型。

### 二、技术方案（Method）
以线性二自由度自行车模型提供物理先验，在给定转向角、纵向速度和状态历史下计算名义横向加速度与横摆率；用128单元LSTM编码10帧转向、纵向速度、横向加速度和横摆率，输出归一化残差的联合高斯分布，经重参数化得到相关修正量并更新横摆率、横向速度和历史窗口。训练采用多步rollout，将修正响应和自生成状态递归反馈，损失由条件负对数似然、加权残差均值MSE和归一化横向速度MSE组成，使用4个粒子、λμ=0.05、λvy=0.2，并以验证horizon选择checkpoint。推理时以条件均值递归积分得到横向位置与航向，并通过44维增广状态在条件均值轨迹处线性化，将响应协方差传播到横向响应、位置和航向，输出点预测及±3σ预测带。

### 三、结果（Result）
离线测试表明，多步rollout训练显著改善递归运动预测，训练horizon从1增至100时横向速度RMSE由0.2496 m/s降至0.0441 m/s，横向位置RMSE由0.934 m降至0.483 m。与Deep Dynamics横向自适应相比，所提模型将平均横向位置RMSE从0.596 m降至0.483 m，改善19.0%，同时将平均横向速度RMSE从0.0469 m/s降至0.0441 m/s；加入位姿损失后横向位置RMSE进一步降至0.452 m。消融显示去掉横向速度损失会明显恶化性能，验证了直接惩罚累积横向速度误差的必要性。

### 四、结论（Conclusion）
物理先验、概率化相关残差学习与多步rollout训练的结合，可提升车辆在环仿真中横向响应和积分运动预测的保真度。该方法在保持物理解释性的同时提供不确定性传播，适合生成横向位置与航向跟踪指令；但结论主要基于离线数据评估，仍需在闭环车辆在环平台上进一步验证。

### 五、方法论与关键技术细节
数据来自RT3000，共46条记录，其中44次换道和2次蛇形，按文件划分为33条训练、7条验证、6条测试，测试含六个机动窗口。物理先验为小角度线性二自由度模型，轮胎侧偏速度项在低速下正则化；残差为横向加速度和横摆率的加性相关修正，协方差以正标准差和有界相关系数参数化。关键超参包括训练horizon和验证horizon均为100、4个训练粒子、λμ=0.05、λvy=0.2、条件均值递归和32维增广状态协方差传播；评估指标为v_y、r、Y、φ的RMSE。局限性包括平面运动与小角度假设、固定物理参数、离线数据集规模有限，以及概率预测带仅通过线性化传播。
