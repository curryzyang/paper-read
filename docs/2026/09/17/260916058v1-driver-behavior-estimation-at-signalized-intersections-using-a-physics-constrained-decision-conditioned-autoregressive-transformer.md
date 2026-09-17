# Driver Behavior Estimation at Signalized Intersections Using a Physics-Constrained Decision-Conditioned Autoregressive Transformer

- 区域：精读区
- 排名：1
- 匹配度：5.4/10
- 来源：arxiv
- 作者：Mohammad Khoshkdahan, Pavel Laskov, Alexey Vinel
- 机构：Halmstad University, University of Liechtenstein, Karlsruhe Institute of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16058v1) · [PDF](https://arxiv.org/pdf/2609.16058v1)

## TLDR
This paper presents a high-precision real-world dataset and a two-stage physics-constrained, decision-conditioned autoregressive Transformer that predicts drivers’ stop–go decisions and longitudinal deceleration trajectories at yellow-light signalized intersections while estimating stopping comfort from a single yellow-onset snapshot.

## Abstract
Red-light violations and harsh braking at signalized intersections are major contributors to traffic accidents. This paper analyzes and predicts human driver decision-making and longitudinal trajectory behavior during traffic light signal transitions. We collected a diverse real-world dataset comprising 449 approach runs under varying speed and distance conditions. Vehicle motion was recorded using RTK-corrected GNSS with centimeter-level accuracy, and driver heart rate and multi-level comfort ratings were monitored. Spatial and temporal calibration ensured precise alignment between vehicle state and signal timing. Statistical analysis identifies required deceleration as the dominant single predictor of the stop-go decision, and heteroscedastic Gaussian modeling of peak deceleration reveals five empirical comfort ranges derived from human stopping behavior. Based on this insight, we propose a two-stage modeling framework. Stage 1 predicts the binary maneuver decision, and Stage 2 generates the longitudinal acceleration trajectory using a decision-conditioned autoregressive Transformer with physics constraints, including target-state conditioning and jerk limits. The proposed architecture outperforms baseline methods and achieves 0.49m/s^2 acceleration MAE and 0.62m distance MAE. It also estimates the future stopping-comfort level of the human driver from a single yellow-onset snapshot. Qualitative results demonstrate realistic human-like braking behavior. The dataset and source code are publicly available.


## 精读解读（中文）
### 一、研究动机
信号交叉口绿灯转黄灯阶段的决策与制动行为直接关系到红灯违规和急刹追尾等事故风险，现有研究多只预测离散停走决策或缺少高精度连续轨迹与驾驶员舒适/生理信息。论文旨在同时建模驾驶员的停走选择与纵向减速轨迹，为自适应信号配时和V2I安全舒适干预提供依据。

### 二、技术方案（Method）
研究采集30名驾驶员共449次接近运行，含185109个RTK-GNSS样本，10 Hz记录车辆位置、速度、纵向加速度，并同步测量心率与五点制动舒适度评分；信号灯由Jetson控制，通过空间投影校准纵向距离并用142 ms固定延迟加ping延迟补偿黄灯触发时刻，使黄灯起始位置误差低于30 cm。分析阶段用贝叶斯分层logistic模型估计停走决策因素，用异方差高斯建模峰值减速度并提取五类经验舒适区间；预测阶段采用两阶段框架，Stage 1输出二分类停走决策，Stage 2以该决策为条件，用自回归Transformer生成纵向加速度轨迹，并加入目标状态条件与jerk限制等物理约束，推理时仅需黄灯起始单帧快照即可生成完整停车或通过轨迹及未来舒适等级。

### 三、结果（Result）
贝叶斯分层logistic的平均边际效应显示需求减速度a_req是停走决策的主导预测因子，停车试次中黄灯起始平均a_req为1.99 m/s²，中位数1.93，标准差0.70；决策边界大致沿等a_req轮廓，较大黄灯距离阈值对应约3–4 m/s²的停走转换，较短距离则降至约2–3 m/s²。所提两阶段决策条件自回归Transformer优于基线方法，达到0.49 m/s²的加速度MAE和0.62 m的距离MAE，并能从单个黄灯起始快照估计驾驶员未来停车舒适等级，定性结果呈现类人制动行为。

### 四、结论（Conclusion）
论文证明将决策条件、自回归生成与物理约束结合，可以在信号交叉口黄灯场景中同时预测停走决策并生成真实、平滑且符合人类舒适边界的纵向减速轨迹。该框架有望用于提前识别激进停车或闯红灯风险，并支持更平滑的V2I速度引导与自适应信号控制。

### 五、方法论与关键技术细节
数据覆盖40、50、60 km/h各112次及70 km/h 56次，黄灯阈值12–79 m，含392次正常停走分析运行和少量强制停车运行以捕获高减速度；场景为同一地点、同一车辆Audi A6、白天、8天实验，包含熟悉阶段和随机纯绿灯运行以降低预期偏差。贝叶斯分层logistic含参与者随机截距u_j ~ N(0, sigma_u^2)，似然为Bernoulli；峰值减速度采用异方差高斯并导出五档舒适范围。建模关键约束包括目标状态条件与jerk限制，推理由黄灯起始单快照驱动；但可见文本未给出具体损失函数、学习率、Transformer层数等超参。局限性包括单一交叉口与车辆、白天实验、70 km/h样本较少、GNSS记录器内部延迟未知且时变导致校准残留，以及强制停车试次可能改变自然决策分布；数据集与代码已公开于GitHub。
