# From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation

- 区域：精读区
- 排名：9
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Ammar N. Abbas, Aayush Jain, Prashanth Viswanath, Nivesh Gadipudi, Giulia Vilone, Jim Gibbons
- 机构：Analog Devices, Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40828v1) · [PDF](https://arxiv.org/pdf/2610.40828v1)

## TLDR
In ~1,700 real-robot trials of dexterous RJ45 grasping and insertion, observation and action representation choices dominated imitation-learning success far more than optimizer or sampling choices, and offline metrics could only shortlist policies rather than replace real-robot evaluation.

## Abstract
Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion. However, real-world performance remains difficult to predict, as conventional optimization signals such as validation loss show no consistent relationship with robot success. To identify the design choices that govern real-world performance, 281 imitation-learning policies spanning seven policy families were evaluated in approximately 1,700 real-robot trials of RJ45 connector grasping and insertion using a five-fingered robotic hand. Controlled ablations showed that observation and action representations dominated conventional optimizer and sampling choices. For point-cloud policies, region-of-interest cropping, representation in the robot-base frame, and normalization within the point encoder each improved success by 70-100 percentage points. For the vision-language-action policy, absolute rather than relative action prediction improved insertion success by up to 70 percentage points. Skill decomposition, multi-view perception, and recovery demonstrations were associated with the strongest-performing systems, although their effects were not independently isolated. Of 67 offline metrics evaluated, only five measures of predicted-motion smoothness and directness reliably correlated with insertion success (r = -0.70 to -0.80), and only within a single policy family. These results identify representation choices as key determinants of real-world imitation-learning performance and show that offline metrics can shortlist policies, but cannot replace real-robot evaluation.


## 精读解读（中文）
### 一、研究动机
模仿学习策略在真实世界中的表现难以由验证损失等常规离线信号预测，尤其多指灵巧手接触丰富任务缺乏系统性设计证据；作者希望通过大规模真机消融识别决定RJ45抓取与插入成功率的观测/动作表示等设计选择，并检验离线指标能否替代真机评估。

### 二、技术方案（Method）
在Franka Research 3加Tesollo DG5F五手指平台上采集遥操作演示（30 Hz，策略10 Hz），任务分为经典运动到预设起点、学习抓取、经典搬运、学习插入四阶段；策略输入腕部RGB-D（RGB及2048点云，部分加第三方视角），输出10维末端平移3、欧拉角3和四个手关节命令（内部6D旋转时13维）。比较DP、DP3、iDP3、flow matching、ACT、等变扩散和π0.5 VLA共七类281个策略，关键消融包括ROI裁剪、相机/机器人基座坐标系、点编码器内归一化、绝对/相对动作、预测时域、优化器与采样器；用FoundationPose识别夹具，按F/G/P/I嵌套阶段和Fisher精确检验评分，并在67个离线指标上做留出验证与多检验校正/留一策略稳健性分析。

### 三、结果（Result）
约1700次真机试验显示表示选择远强于优化器和采样器：点云策略中ROI裁剪、机器人基座坐标系和点编码器内归一化分别带来70–100个百分点提升，π0.5采用绝对动作较相对动作插入提升至多70个百分点。最佳iDP3+ROI在两夹具均100%插入，匹配微调VLA而推理显存约为其1/8，并在光照、背景、场地和阳光变化下保持80–100%插入，但更紧公差插座降至0–40%。67个离线指标中仅5个预测轨迹平滑/直接性指标在单一iDP3族内与插入成功率相关（r=-0.70至-0.80），无指标追踪抓取成功率或跨策略族泛化。

### 四、结论（Conclusion）
真实机器人模仿学习的首要决定因素是观测与动作表示，而非优化器/采样器等二阶调参；接触丰富任务应分解为抓取与插入技能并结合多视角和恢复演示。离线平滑性指标只能在同一策略族内筛选插入检查点，不能替代真机评测；紧凑点云策略可在该任务上以更低内存匹敌预训练VLA。

### 五、方法论与关键技术细节
数据含中心/左夹具等五种放置的遥操作演示，抓取技能用按起始位姿簇均衡的数据、插入技能用全部回合，并加入恢复演示；观测为腕部D455 RGB 848×480与2048点云，双视角增加静态第三人称相机，动作10维、策略10 Hz。实现上比较ImageNet/R3M初始化、LoRA微调π0.5、PointNet/多阶段点编码器及扩散去噪、流匹配速度回归、ACT条件自编码器解码，训练在4×H100，最佳点云技能约69M参数、每epoch约18s、训练/推理显存约6.0/1.0GB；评分采用嵌套F/G/P/I并以Fisher检验比较单变量配对消融。局限包括多因素改动（技能分解、多视角、恢复演示）未独立隔离，离线相关性仅来自21个iDP3双夹具插入检查点且五项指标彼此高度相关，抓取失败涉及首次接触而回放观测难复现。
