# RAIWAY: A Large-Wheeled Bipedal Robot with Contact-Informed Blind Locomotion

- 区域：精读区
- 排名：7
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Kyungmin Nam, Jiseong Lee, Donghyuk Choi, Jeongsoo Park, Woojin Kim, Jemin Hwangbo
- 机构：Korea Advanced Institute of Science and Technology (KAIST)
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33172v1) · [PDF](https://arxiv.org/pdf/2610.33172v1)

## TLDR
The paper presents RAIWAY, a 20-inch-wheeled bipedal robot with a contact-informed controller that distills simulated wheel–terrain multi-contact events into a latent representation inferred online from proprioception alone, enabling blind rolling locomotion over irregular and discontinuous terrain such as steep slopes, gravel, rocks, and outdoor stairs up to 15 cm.

## Abstract
We present RAIWAY, an in-house wheeled bipedal robot with 20-inch wheels, together with a contact-informed control approach for rolling locomotion across irregular and discontinuous terrain. Such locomotion is fundamentally contact-dominated, governed by local wheel--terrain interaction that is impractical to instrument directly and depends on more than terrain geometry alone. The proposed framework exploits the contact information available in simulation, distilling multi-contact events into a latent representation. At deployment, the controller infers this representation online from proprioception, requiring no contact sensing. In real-world experiments, the proposed system traverses diverse environments including steep slopes, gravel beds, studded surfaces, and rocky terrain, and demonstrates continuous ascent on the tested outdoor staircases with riser heights up to 15~cm. On our platform, the proposed controller further outperforms baselines without the contact-informed mechanism across challenging indoor and outdoor settings. The video can be found at https://youtu.be/Ch0divLg64w.


## 精读解读（中文）
### 一、研究动机
轮足机器人兼具轮式高效与腿式越障能力，但多数平台遇到地形不连续时转为踏步或抬腿，牺牲连续滚动效率；大轮径可利用更小入射角和轮胎柔顺性直接滚过中等障碍。滚动越障本质上是接触主导问题，轮-地局部接触状态无法直接密集测量，且受轮胎柔顺性和内部材料影响，显式接触建模存在明显sim-to-real差距，因此需要利用仿真中的特权接触信息学习可在部署时由本体感觉推断的表示。

### 二、技术方案（Method）
RAIWAY是6-DoF轮足双足机器人，每条腿含两个俯仰关节和一个轮关节，采用差速转向，配20英寸越野轮胎和闭孔泡沫内衬，重约28 kg、标称高1.14 m，搭载Jetson AGX Orin、IMU和关节编码器。控制器输入期望前进速度与偏航角速度，用GRU编码本体感觉历史，并由估计器预测基座线速度、高度、轮离地间隙、侧向轮速度和打滑指示等可部署量；策略以接触信息潜变量为条件，输出四个腿关节期望位置和两个轮关节期望角速度，由低层PD跟踪。训练时将仿真中每个轮的世界系原始接触位置与冲量变换到轮静态旋转不变系并归一化，经非对称去抖滤波后按轮周角度排序并补齐为每轮3个接触槽，再拼接轮级特权特征形成固定长度接触向量，经LSTM教师编码为32维潜变量，学生模块学习从本体感觉历史推断该潜变量。采用Regularized Online Adaptation联合训练教师和学生并正则化潜变量可预测性，部署时无需接触传感器或外部感知，仅用本体感觉在线推断接触信息潜变量。

### 三、结果（Result）
真实世界实验表明，RAIWAY可穿越陡坡、碎石床、钉状表面和岩石地形，并在测试的户外楼梯上实现连续上行，台阶高度最高达15 cm。与不含接触信息机制的基线相比，所提控制器在16 cm室内台阶上行和户外岩石地形穿越中取得明显更高成功率。这些结果覆盖高速连续接触变化、空间不可预测接触和周期性不连续等多种接触事件，验证了系统在代表性挑战环境中的滚动越障能力。

### 四、结论（Conclusion）
研究支持两个核心结论：大轮径使连续滚动跨越不规则和不连续地形在物理上可行，而接触信息驱动的潜变量自适应能在不依赖外部感知和接触传感的条件下提升本平台在测试环境中的越障表现。该工作将轮-地多接触事件转化为结构化特权表示并蒸馏给可部署策略，为接触主导的轮式双足运动提供了一条避免显式精确接触建模的sim-to-real路线。

### 五、方法论与关键技术细节
关键实现包括：原始接触在世界系中记录位置与冲量，变换到以轮轴为y轴、重力在轮平面投影反方向为z轴的轮静态系，x/z按轮半径、y按半圆柱长度归一化到[-1,1]；去抖滤波对新接触1个仿真子步接受、消失需连续25个子步（62.5 ms）确认，窗口依据平滑地形和5 cm台阶的99百分位接触丢失时长设定。每轮按x-z平面角度排序并补默认轮底模板至3槽，可表达底部、前下和后下同时接触，四接触以上情形很少；轮级特权特征包含轮离地间隙、轮速度和偏离理想滚动的打滑量。网络结构为GRU隐藏128、估计器和策略均为[256,128] MLP、教师LSTM隐藏8输出32维潜变量、学生为[256,128] MLP，均用LeakyReLU；腿关节PD增益Kp=50、Kd=0.5，轮关节Kp=0、Kd=2.5。局限与约束包括表示和超参针对大轮平台与接触事件设计、滤波会引入真实失去接触的短延迟、仅保留3个接触槽，且验证限于所测试室内外地形，未使用外部感知或接触传感。
